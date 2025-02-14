import streamlit as st
import pickle
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Load the trained model
with open("walmart_sales_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Walmart Sales Forecasting")
st.sidebar.header("User Input")

# Date range selection
start_date = st.sidebar.date_input("Start Date", datetime.today())
days_to_forecast = st.sidebar.slider("Days to Forecast", 1, 60, 7)
end_date = start_date + timedelta(days=days_to_forecast)

if st.sidebar.button("Predict Sales"):
    # Create a date range for prediction
    future_dates = pd.date_range(start=start_date, periods=days_to_forecast)
    future_df = pd.DataFrame({"date": future_dates})
    
    # Generate predictions (Fix: Provide appropriate input to model)
    X_future = np.arange(len(future_df)).reshape(-1, 1)  # Ensure correct shape
    predictions = model.predict(X_future)  # Pass the correct feature array
    
    # Display results
    st.subheader("Sales Forecast")
    
    # Ensure dimensions match
    result_df = pd.DataFrame({"Date": future_dates, "Predicted Sales": predictions.flatten()})
    st.write(result_df)
    
    # Plot forecast
    st.line_chart(result_df.set_index("Date"))
