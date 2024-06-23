import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


csv_file_path = 'S:\Projects\Contractor_Segmentation_analysis\CONTRACT_DATA_ANALYSIS.csv'
df = pd.read_csv(csv_file_path)


st.write("DataFrame columns:", df.columns)
st.write("First few rows of the DataFrame:")
st.write(df.head())

st.sidebar.header('User Inputs')
user_inputs = {
    "Last_Project_Price": st.sidebar.number_input("Enter Last Required Project Price in Crores:", min_value=0, step=1),
    "Cost_management": st.sidebar.slider("Enter Your Expected Percentage in the 4th Quarter:", 0.0, 100.0, 0.0) / 100,
    "Safety_record": st.sidebar.slider("Enter Your Expected Percentage For Safety:", 0.0, 100.0, 0.0) / 100,
    "Experience": st.sidebar.number_input("Required Experience:", min_value=0, step=1),
    "Technical_experience": st.sidebar.selectbox("Technical Experience (Yes/No):", ["Yes", "No"]),
    "Labour_Availability": st.sidebar.selectbox("Labour Availability (Yes/No):", ["Yes", "No"]),
    "Material_Availability": st.sidebar.selectbox("Material Availability (Yes/No):", ["Yes", "No"]),
    "Equipment_Availability": st.sidebar.selectbox("Equipment Availability (Yes/No):", ["Yes", "No"]),
    "Testimonials": st.sidebar.selectbox("Testimonials (Good/Average):", ["Good", "Average"]),
    "Regional_language": st.sidebar.selectbox("Regional Language (Yes/No):", ["Yes", "No"]),
    "English_Language": st.sidebar.selectbox("English Language (Yes/No):", ["Yes", "No"]),
    "Required_Response_Time": st.sidebar.selectbox("Quick Response Time (Yes/No):", ["Yes", "No"]),
    "Recycling_Program": st.sidebar.selectbox("Recycling Program (Yes/No):", ["Yes", "No"]),
    "Standing_In_Industry": st.sidebar.selectbox("Standing In Industry (Yes/No):", ["Yes", "No"]),
    "Document_Control": st.sidebar.selectbox("Document Control (Yes/No):", ["Yes", "No"]),
    "Regional_Experience": st.sidebar.slider("Regional Experience, Rating Out of 10:", 0, 10, 0),
    "Supply_Chain": st.sidebar.selectbox("Supply Chain, More Than 10 (Yes/No):", ["Yes", "No"])
}

st.write("User inputs:")
st.write(user_inputs)

filtered_df = df[
    (df['Last_Project_Price'] >= user_inputs['Last_Project_Price']) &
    (df['Cost_management'] >= user_inputs['Cost_management']) &
    (df['Safety_record'] >= user_inputs['Safety_record']) &
    (df['Experience'] >= user_inputs['Experience']) &
    (df['Technical_experience'] == user_inputs['Technical_experience']) &
    (df['Labour_Availability'] == user_inputs['Labour_Availability']) &
    (df['Material_Availability'] == user_inputs['Material_Availability']) &
    (df['Equipment_Availability'] == user_inputs['Equipment_Availability']) &
    (df['Testimonials'] == user_inputs['Testimonials']) &
    (df['Regional_language'] == user_inputs['Regional_language']) &
    (df['English_Language'] == user_inputs['English_Language']) &
    (df['Required_Response_Time'] == user_inputs['Required_Response_Time']) &
    (df['Recycling_Program'] == user_inputs['Recycling_Program']) &
    (df['Standing_In_Industry'] == user_inputs['Standing_In_Industry']) &
    (df['Document_Control'] == user_inputs['Document_Control']) &
    (df['Regional_Experience'] >= user_inputs['Regional_Experience']) &
    (df['Supply_Chain'] == user_inputs['Supply_Chain'])
]

st.write("Filtered DataFrame:")
st.write(filtered_df)

if not filtered_df.empty:
    st.write("Matching contractor(s) found:")
    st.write(filtered_df)

    categories = [
        "Last_Project_Price", "Cost_management", "Safety_record", "Experience",
        "Technical_experience", "Labour_Availability", "Material_Availability",
        "Equipment_Availability", "Testimonials", "Regional_language",
        "English_Language", "Required_Response_Time", "Recycling_Program",
        "Standing_In_Industry", "Document_Control", "Regional_Experience",
        "Supply_Chain"
    ]

    plot_data = []

    for i, (index, row) in enumerate(filtered_df.iterrows()):
        Contractor_name = row['Contractor_name']
        df_values = [
            ("Last_Project_Price", float(row['Last_Project_Price']), Contractor_name),
            ("Cost_management", float(row['Cost_management']) * 100, Contractor_name),
            ("Safety_record", float(row['Safety_record']) * 100, Contractor_name),
            ("Experience", float(row['Experience']), Contractor_name),
            ("Technical_experience", 1 if row['Technical_experience'] == 'Yes' else 0, Contractor_name),
            ("Labour_Availability", 1 if row['Labour_Availability'] == 'Yes' else 0, Contractor_name),
            ("Material_Availability", 1 if row['Material_Availability'] == 'Yes' else 0, Contractor_name),
            ("Equipment_Availability", 1 if row['Equipment_Availability'] == 'Yes' else 0, Contractor_name),
            ("Testimonials", 1 if row['Testimonials'] == 'Good' else 0, Contractor_name),
            ("Regional_language", 1 if row['Regional_language'] == 'Yes' else 0, Contractor_name),
            ("English_Language", 1 if row['English_Language'] == 'Yes' else 0, Contractor_name),
            ("Required_Response_Time", 1 if row['Required_Response_Time'] == 'Yes' else 0, Contractor_name),
            ("Recycling_Program", 1 if row['Recycling_Program'] == 'Yes' else 0, Contractor_name),
            ("Standing_In_Industry", 1 if row['Standing_In_Industry'] == 'Yes' else 0, Contractor_name),
            ("Document_Control", 1 if row['Document_Control'] == 'Yes' else 0, Contractor_name),
            ("Regional_Experience", float(row['Regional_Experience']), Contractor_name),
            ("Supply_Chain", 1 if row['Supply_Chain'] == 'Yes' else 0, Contractor_name)
        ]
        plot_data.extend(df_values)

    plot_df = pd.DataFrame(plot_data, columns=["Category", "Value", "Contractor"])

    plt.figure(figsize=(12, 10))
    sns.barplot(data=plot_df, y="Category", x="Value", hue="Contractor", dodge=True)
    plt.title("Comparison of Matching Contractors")
    st.pyplot(plt)
else:
    st.write("No matching contractor found.")