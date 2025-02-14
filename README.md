# Walmart Sales Forecasting - Streamlit App

## Overview

This project is a **Walmart Sales Forecasting** web application built using **Streamlit** and a trained machine learning model. The app allows users to predict future sales based on user-inputted date ranges. The model was trained in **Google Colab** and deployed using Streamlit.

## Features

- Predict future sales for up to **60 days**.
- User-friendly interface with date selection.
- Visualize the forecasted sales using an interactive line chart.
- Built with **Streamlit** for easy deployment.
- Model trained in **Google Colab** and integrated into the Streamlit app.

## Dataset

The dataset used for training the model is included in the project folder. It contains historical sales data, which was preprocessed and used to train the machine learning model.

## Project Structure


├── data_analysis_streamlit/  # Project Folder
│   ├── walmart_sales_model.pkl  # Trained Model
│   ├── Walmart_Store_sales.csv  # Dataset Used for Training
│   ├── app.py  # Streamlit Application

## Installation & Setup

### 1. Clone the Repository

git clone https://github.com/shifakouser8618/data_analysis_streamlit.git
cd data_analysis_streamlit

### 2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Streamlit App
streamlit run app.py

After running this command, open the provided **local URL** in your browser.

## Model Training (Google Colab)

- The machine learning model was trained in **Google Colab** using **time series analysis techniques**.
- The trained model (`walmart_sales_model.pkl`) was exported and integrated into the Streamlit app.
- The Colab notebook containing the full training process is included in the project folder.

## Future Improvements

- Enhance the model for better accuracy.
- Add more features like seasonality detection.
- Deploy the app using **Streamlit Sharing** or **Docker**.

## Contributions

Feel free to fork the repository and submit pull requests if you have any improvements or suggestions!

## License

This project is open-source and available under the MIT License.


**Developed by Shifa Kouser.**

