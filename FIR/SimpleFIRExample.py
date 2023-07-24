def fir_filter(signal, coefficients):
    """
    Applies a Finite Impulse Response (FIR) filter to the input signal.

    Parameters:
        signal (list): The input signal to be filtered.
        coefficients (list): The FIR filter coefficients.

    Returns:
        list: The filtered output signal.
    """

    # Ensure that the signal and coefficients have compatible lengths.
    if len(signal) < len(coefficients):
        raise ValueError("Signal length must be greater than or equal to coefficients length.")

    # Initialize the filtered output.
    output_signal = [0.0] * len(signal)

    # Apply the FIR filter.
    for i in range(len(signal)):
        for j in range(len(coefficients)):
            if i - j >= 0:
                output_signal[i] += signal[i - j] * coefficients[j]

    return output_signal

# Define the input signal and FIR filter coefficients.
input_signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_coefficients = [0.1, 0.2, 0.3, 0.4]

# Apply the FIR filter.
filtered_signal = fir_filter(input_signal, filter_coefficients)

# Print the filtered output.
print(filtered_signal)
