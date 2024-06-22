import pandas as pd

csv_file_path = 'C:/Users/Gagan Sharma/OneDrive/Desktop/CONTRACT_DATA_ANALYSIS.csv'
df = pd.read_csv(csv_file_path)

# print(df.head(5))

user_inputs = { 
    "Last_Project_Price": int(input("Enter Last Required Project Price in Crores: ")),
    "Cost_management": float(input("Enter Your Expected Percentage in the 4th Quater: ")) / 100,
    "Safety_record": float(input("Enter Your Expected Percentage For Safety: ")) / 100,
    "Experience": int(input("Required Experience: ")),
    "Technical_experience": input("Technical Experience (Yes/No): "),
    "Labour_Availability": input("Labour Availability (Yes/No): "),
    "Material_Availability": input("Material Availability (Yes/No): "),
    "Equipment_Availability": input("Equipment Availability (Yes/No): "),
    "Testimonials": input("Testimonials Good/Average: "),
    "Regional_language": input("Regional Language (Yes/No): "),
    "English_Language": input("English Language (Yes/No): "),
    "Required_Response_Time": input("Quick Response Time (Yes/No): "),
    "Recycling_Program": input("Recycling Program (Yes/No): "),
    "Standing_In_Industry": input("Standing In Industry (Yes/No): "),
    "Document_Control": input("Document Control (Yes/No): "),
    "Regional_Experience": float(input("Regional Experience, Rating Out of 10: ")),
    "Supply_Chain": input("Supply Chain, More Than 10 (Yes/No): ")
}

# print(user_inputs)

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

if not filtered_df.empty:
    print("Matching contractor(s) found:")
    print(filtered_df)
else:
    print("No matching contractor found.")
