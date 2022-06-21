import io
import docx2txt
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
set(stopwords.words('english'))
import pandas as pd
import base64 
import time
from resume_reader import read_word_resume
from resume_score import get_resume_score
from jd_cleaner import clean_job_decsription
from keyword_counter import counter

import streamlit as st

st.set_page_config(
     page_title="ATS Resume Scanner",
     page_icon="logo.png",
     layout="wide",
 )


def home():
    st.title('ATS Scanner')

    title_alignment="""
    <style>
    .css-10trblm {
        text-align: center
        }
    .stButton
    {
        text-align:center;
    }
    .stButton .css-1q8dd3e
    {
        padding: 0.75rem 2.75rem;
        background-color: #40ff00;
        color: black;
        font-weight: bold;
    }
    .streamlit-expanderHeader
    {
        color: #40ff00;
    }
    </style>
    """
    st.markdown(title_alignment, unsafe_allow_html=True)
    st.subheader('A free to use Job Description Matcher!!!')
    
    st.header('Upload Your Resume In Docx Format')
    docx_file = st.file_uploader('',type=['docx'])
    with st.expander("Click to view Resume"):
        if docx_file is not None:
            raw_text = docx2txt.process(docx_file)
            st.write(raw_text)
    
    st.header('Enter Job Description')
    title = st.text_area('')
    
    if st.button("Compare Job to Resume"):
        if docx_file is not None and title is not None:
            
            #progress bar
            with st.spinner('Reading Docx Resume'):
                time.sleep(3)
            resume = read_word_resume(docx_file)

            with st.spinner('Reading Job Description'):
                time.sleep(3)
            clean_jd = clean_job_decsription(title)

            with st.spinner('Calculating Count of Keywords'):
                time.sleep(3)

            data = counter(clean_jd)
            _,b,_ = st.columns([3,6,3])
            expander = b.expander("Click to view top keywords")
            
            expander.header('Top KeyWords')
            expander.table(data[:15])    

            # # create_word_cloud(clean_jd)
            with st.spinner('Getting Resume Match Score'):
                time.sleep(3)
            text = [resume, title] 
            # ## Get a Match score
            b.write(get_resume_score(text))


if __name__ == '__main__':
    home()