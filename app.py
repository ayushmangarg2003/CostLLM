import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def get_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

# Application Below

st.set_page_config("CostLLM")
st.header("Cost Predictor")

prod_desc = st.text_input("Enter Product Description")
complexity = st.selectbox('What is complexity of Project?', ('Low', 'Medium', 'High'))
team_size = st.number_input("Enter Team Size")
experience = st.selectbox('What is Team Experience?', ('Beginner', 'Intermediate', 'Expert'))
llm_used = st.selectbox('Which LLM is being Used', ('Gemini-Pro','Gemini-Vision-Pro','GPT3.5', 'GPT4', 'Llama2'))

submit = st.button("Get Estimate")

input_prompt= f"""
You are an expert project manager and you have a great experience with LLMs, your new job is to predict the cost and time required for building a new product with the following details
        - Product Description = {prod_desc}
        - Project complexity = {complexity}
        - Team Size = {team_size}
        - Team Experience = {experience}
        - LLM to be used in product = {llm_used}

        You have to return Estimated Cost in Rupees and Estimated Time in Hours in format 
        Cost : 
        </br>
        Time :
"""

if submit:
    response = get_response(input_prompt)
    st.write(response)


