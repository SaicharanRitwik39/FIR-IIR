import math
import sympy
import requests
import numpy as np
import pandas as pd
import streamlit as st
import scipy.signal as signal
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
from scipy.signal import kaiserord, lfilter, firwin, freqz, firwin2


#Function used for calling the Lottie files. Lines 14-19.
@st.cache_resource
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()


#Page configuration settings. Lines 23-26.
st.set_page_config(
    page_title = 'FIR-IIR-FFT',
    page_icon = '💹'
)


#TITLE and Lottie animation code. Lines 30-38.
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
     'Choose amongst the following methods:',
     ('FIR Filter', 'IIR Filter', 'FFT Algorithm'))
    
    
#FIR Filter Code. Lines 48-60.
if(options == 'FIR Filter'):
    st.title("FIR Filter")
    
    st.write("***")
    
    with st.expander("FILTER TYPE"):
         typeoffilter = st.radio(
              'Choose the type of Filter:',
         ('hamming', 'boxcar', 'triang', 'nuttall', 'hann', 'blackman', 'bartlett'))
    
    numtaps = st.number_input("Enter the length of the filter:", value = 3)
    cutoff = st.number_input("Enter the cutoff frequency:", value = 0.1)
    passzero = st.selectbox(
    'Choose True for Low Pass Filter, False for High Pass Filter',
    (True, False))
    
    st.subheader("Signal Processing:")
    st.write("Enter the input signal as a sine function of 't'. For example: 2 * np.sin(2 * np.pi * 5 * t)")
    input_function = st.text_area("Enter the sine function:", "2 * np.sin(2 * np.pi * 5 * t)")
    
    # Time vector for the input signal
    t = np.linspace(0, 1, 1000)
    
    input_signal = eval(input_function)
    
    #input_signal_str = st.text_area("Enter the input signal (comma-separated values):", "1, 2, 3, 4, 5")
    #input_signal = np.fromstring(input_signal_str, dtype=float, sep=',')
    
    window = typeoffilter
    firfiltertaps = signal.firwin(numtaps, cutoff, window=window, pass_zero=passzero)
    
    st.write("***")
    
    with st.expander("RESULTS"):
         st.write("***")
         
         st.subheader("FIR Filter Coefficients")
         firfiltercoeffradio = st.radio(
             'Do you want to see the coefficients?',
             ('Show', 'Don\'t show'), horizontal = True)
         if(firfiltercoeffradio == "Show"):   
            st.write(firfiltertaps)
         
         st.write("***")
            
         firfilterinputsignal = st.radio(
             'Do you want to see the input signal?',
             ('Show', 'Don\'t show'), horizontal = True)
         if(firfilterinputsignal == "Show"):
            st.write(input_signal) 
            
         st.write("***")   
            
         output_signal = signal.lfilter(firfiltertaps, 1, input_signal)   
         firfilteroutputsignal = st.radio(
             'Do you want to see the output signal?',
             ('Show', 'Don\'t show'), horizontal = True)
         if(firfilteroutputsignal == "Show"):
            st.write(output_signal) 
            
         st.write("***")   
    
    

    # Plot signals
    st.subheader("Signal Plots:")
    fig, ax = plt.subplots()
    ax.plot(input_signal, label='Input Signal')
    ax.plot(output_signal, label='Output Signal')
    ax.legend()
    st.pyplot(fig)


#https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html    
