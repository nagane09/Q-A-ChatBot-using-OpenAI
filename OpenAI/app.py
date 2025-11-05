import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY']=st.secrets("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACKING_V2']='true'
os.environ['LANGCHAIN_PROJECT']="Q&A ChatBot with OpenAI"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistance. Please response to user Queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm
    answer=chain.invoke({'question':question})
    return answer

##Title:-
st.title("Enchances Q&A ChatBot with OpenAI")
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your OpenAI API key: ",type="password")


llm=st.sidebar.selectbox("Select the OpenAI Model",["GPT-5","GPT-5 mini","GPT-5 nano"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

#Main Interface
st.write("Go Ahead and ask any Questions")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
elif user_input:
    st.warning("Please enter your openAI key in sidebar")
else:
    st.write("Please provide the Query")