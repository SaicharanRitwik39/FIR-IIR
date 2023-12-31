# FIR-IIR-FFT

This repository contains the codes for FIR, IIR filters in MATLAB, Python and their implementation in Verilog. I have also tried to generalize this process of filtering by attempting to build a streamlit web application wherein the user can input any signal and the application will parse the input and apply the required filter automatically. The code for the Web App is in the file Code.py and has not been hosted yet (incomplete as of now).

# WEB APP
<img src = "Screenshot 2023-07-24 163945.png">

* FIR (Finite Impulse Response) Filter: In signal processing, a finite impulse response (FIR) filter is a filter whose impulse response (or response to any finite length input) is of finite duration, because it settles to zero in finite time. (Source: Wikipedia). The FIR Folder has all the code for a simple 4 Tap filter implemented in Python, MATLAB and Verilog.
A FIR filter output, 'y' can be defined by the following equation:
$$y[n] = \sum_{i=0}^{N} b[i] \cdot x[n-i]$$
Here, 'y' is the filter output, 'x' is the input signal and 'b' are the filter coefficients. 'N' is the filter order. The higher the value of N is, the more complex the filter will be.

* IIR (Infinite Impulse Response) Filter:
* FFT (Fast Fourier Transform): 
