import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv

#Allows us to configure the name of the page
st.set_page_config(page_title="Resume AI Critiquer", page_icon="📃", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get an AI-powered feedback tailored to your needs!")