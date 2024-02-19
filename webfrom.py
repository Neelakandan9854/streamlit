import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Simulated IoT data
def generate_iot_data(num_samples=1400):
    timestamp = pd.date_range(start='2024-01-01', periods=num_samples, freq='H')
    temperature = np.random.normal(loc=25, scale=5, size=num_samples)
    humidity = np.random.normal(loc=50, scale=10, size=num_samples)
    data = pd.DataFrame({'Timestamp': timestamp, 'Temperature': temperature, 'Humidity': humidity})
    return data

# Main function
def main():
    st.title("IoT Data Dashboard")
    
    # Generate some example data
    iot_data = generate_iot_data()
    
    # Display the raw data
    st.subheader("Raw Data")
    st.write(iot_data)
    
    # Line chart for temperature
    st.subheader("Temperature Trend")
    fig_temp = px.line(iot_data, x='Timestamp', y='Temperature', title='Temperature Trend')
    st.plotly_chart(fig_temp)
    
    # Line chart for humidity
    st.subheader("Humidity Trend")
    fig_humidity = px.line(iot_data, x='Timestamp', y='Humidity', title='Humidity Trend')
    st.plotly_chart(fig_humidity)

# Run the main function
if __name__ == "__main__":
    main()
