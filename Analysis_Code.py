import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class ContractorAnalysis:
    def __init__(self, csv_file_path):
        self.df = pd.read_csv("S:\Projects\Contractor_Segmentation_analysis\CONTRACT_DATA_ANALYSIS.csv")
        self.user_inputs = {}
        self.filtered_df = pd.DataFrame()

    def display_initial_data(self):
        print("DataFrame columns:", self.df.columns)
        print("First few rows of the DataFrame:")
        print(self.df.head())

    def get_user_inputs(self):
        self.user_inputs = {
            "Last_Project_Price": int(input("Enter Last Required Project Price in Crores: ")),
            "Cost_management": float(input("Enter Your Expected Percentage in the 4th Quarter: ")) / 100,
            "Safety_record": float(input("Enter Your Expected Percentage For Safety: ")) / 100,
            "Experience": int(input("Required Experience: ")),
            "Technical_experience": input("Technical Experience (Yes/No): "),
            "Labour_Availability": input("Labour Availability (Yes/No): "),
            "Material_Availability": input("Material Availability (Yes/No): "),
            "Equipment_Availability": input("Equipment Availability (Yes/No): "),
            "Testimonials": input("Testimonials (Good/Average): "),
            "Regional_language": input("Regional Language (Yes/No): "),
            "English_Language": input("English Language (Yes/No): "),
            "Required_Response_Time": input("Quick Response Time (Yes/No): "),
            "Recycling_Program": input("Recycling Program (Yes/No): "),
            "Standing_In_Industry": input("Standing In Industry (Yes/No): "),
            "Document_Control": input("Document Control (Yes/No): "),
            "Regional_Experience": int(input("Regional Experience, Rating Out of 10: ")),
            "Supply_Chain": input("Supply Chain, More Than 10 (Yes/No): ")
        }

    def filter_contractors(self):
        conditions = [
            (self.df['Last_Project_Price'] >= self.user_inputs['Last_Project_Price']),
            (self.df['Cost_management'] >= self.user_inputs['Cost_management']),
            (self.df['Safety_record'] >= self.user_inputs['Safety_record']),
            (self.df['Experience'] >= self.user_inputs['Experience']),
            (self.df['Technical_experience'] == self.user_inputs['Technical_experience'])
        ]

        self.filtered_df = self.df.copy()
        for condition in conditions:
            self.filtered_df = self.filtered_df[condition]

    def display_filtered_data(self):
        if not self.filtered_df.empty:
            print("Matching contractor(s) found: ")
            print(self.filtered_df)
        else:
            print("No matching contractor found.")

    def plot_comparison(self):
        if self.filtered_df.empty:
            return

        categories = [
            "Last_Project_Price", "Cost_management", "Safety_record", "Experience",
            "Technical_experience", "Labour_Availability", "Material_Availability",
            "Equipment_Availability", "Testimonials", "Regional_language",
            "English_Language", "Required_Response_Time", "Recycling_Program",
            "Standing_In_Industry", "Document_Control", "Regional_Experience",
            "Supply_Chain"
        ]

        plot_data = []

        for i, (index, row) in enumerate(self.filtered_df.iterrows()):
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
        plt.show()

def main():
    csv_file_path = 'C:/Users/Gagan Sharma/OneDrive/Desktop/CONTRACT_DATA_ANALYSIS.csv'
    analysis = ContractorAnalysis(csv_file_path)
    
    analysis.display_initial_data()
    analysis.get_user_inputs()
    analysis.filter_contractors()
    analysis.display_filtered_data()
    analysis.plot_comparison()

if __name__ == "__main__":
    main()
