import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY']=st.secrets.get("LANGCHAIN_API_KEY", "")
os.environ['LANGCHAIN_TRACKING_V2']='true'
os.environ['LANGCHAIN_PROJECT']="Q&A ChatBot with Ollama"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistance. Please response to user Queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):
    llm=Ollama(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm
    answer=chain.invoke({'question':question})
    return answer

##Title:-
st.title("Enchances Q&A ChatBot with OpenAI")
st.sidebar.title("Settings")


llm=st.sidebar.selectbox("Select the OpenAI Model",["gemma3","qwen2:1.5b"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

#Main Interface
st.write("Go Ahead and ask any Questions")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the Query")
