from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", api_key=st.secrets['api_key'], temperature=0)


st.title("Detailed Summary Generator & its Summary")

template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic'] 
)

template2 = PromptTemplate(
    template='write five line summary about this {text}',
    input_variables=['text'] 
)

topic = st.text_input("Enter your topic")
parser = StrOutputParser()

if st.button('Enter'):
    # Step 1: Generate detailed report
    detailed_report = (template1 | model | parser).invoke({"topic": topic})
    
    # Step 2: Generate 5-line summary from the detailed report
    summary = (template2 | model | parser).invoke({"text": detailed_report})
    
    # Display both
    st.subheader("Detailed Report")
    st.write(detailed_report)

    st.subheader("5-line Summary")
    st.write(summary)
