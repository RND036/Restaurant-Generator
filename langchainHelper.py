from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from dotenv import load_dotenv
import os

load_dotenv()

groqapi_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0.7,api_key=groqapi_key)


def generate_resturant_name_and_item(cuisine):
    # chain1:restturant Name 
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food.suggest only one  fancy name for this dont want any explanations "
    )

    name_chain = LLMChain(llm=llm,prompt=prompt_template_name,output_key="resturant_name")

    # chain2:menu items
    prompt_template_item = PromptTemplate(
        input_variables=['resturant_name'],
        template="""suggest some menu items for {resturant_name},return it as a comma separated string  just give menu items dont want any explanations"""
    )

    food_item_chain = LLMChain(llm=llm,prompt=prompt_template_item,output_key="menu_items")


    # creating sequestial chain 
    chain = SequentialChain(
        chains=[name_chain,food_item_chain],
        input_variables=['cuisine'],
        output_variables = ['resturant_name','menu_items']
       
    )
    response = chain({'cuisine':cuisine})

    return response
