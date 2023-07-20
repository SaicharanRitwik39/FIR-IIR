import math
import sympy
import requests
import numpy as np
import pandas as pd
import streamlit as st
import scipy.signal as signal
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie


#Function used for calling the Lottie files. Lines 13-18.
@st.cache_resource
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()


#Page configuration settings. Lines 22-25.
st.set_page_config(
    page_title = 'FIR-IIR-FFT',
    page_icon = '💹'
)


#TITLE and Lottie animation code. Lines 29-37.
col1, col2 = st.columns([2,1])
with col1:
     st.title("DIGITAL FILTERS") 
     st.write("This app will help with the implementation of FIR, IIR filters and Fast Fourier Transforms.")  
with col2:
     url1 = "https://lottie.host/a728c96a-1d21-4d2d-a11b-8bc62de85517/b5Qt36Db10.json"
     res1_json = load_lottieurl(url1)
     st_lottie(res1_json)
st.write("***")     


#SIDEBAR information Lines 41-44.
with st.sidebar:
    options = st.selectbox(
     'Choose amongst the following numerical methods:',
     ('FIR Filter', 'IIR Filter', 'FFT Algorithm'))
    
    
#FIR Filter Code.
if(options == 'FIR Filter'):
    st.title("FIR Filter")
    
    with st.expander("Filter Type"):
        typeoffilter = st.radio(
             'Choose the type of Filter:',
        ('nuttall', 'hamming', 'hann', 'blackman', 'bartlett'))
    
    numtaps = st.number_input("Enter the length of the filter:", value = 3)
    cutoff = st.number_input("Enter the cutoff frequency:", value = 0.1)
    passzero = st.selectbox(
    'Choose True for Low Pass Filterm False fir High Pass Filter',
    ('True', 'False'))
    
#signal.firwin

    
