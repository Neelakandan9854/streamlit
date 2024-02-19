import streamlit as st
import pandas as pd

def create_iceberg_table(data):
    # Calculate the total number of rows
    total_rows = data.shape[0]
    
    # Calculate the number of rows to display above the iceberg
    above_iceberg = int(total_rows * 0.8)
    
    # Create the dataframe for the iceberg table
    iceberg_data = pd.DataFrame({
        'Rank': range(1, total_rows + 1)
    })
    
    # Add columns from the original data
    for column in data.columns:
        iceberg_data[column] = data[column].values

    # Add 'Above Iceberg' column
    iceberg_data['Above Iceberg'] = ['Yes' if i < above_iceberg else 'No' for i in range(total_rows)]
    
    return iceberg_data

def main():
    st.title('Iceberg Table')
    
    # Allow users to upload a file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the uploaded file
        data = pd.read_csv(uploaded_file)
        
        # Create the iceberg table
        iceberg_data = create_iceberg_table(data)
        
        # Display the iceberg table using Streamlit
        st.write(iceberg_data)
        
        # Allow user to specify local path to save the iceberg table
        save_path = st.text_input("Enter local path to save the iceberg table (e.g., iceberg_table.parquet):")
        
        if st.button("Save Iceberg Table") and save_path:
            try:
                # Save the iceberg table to the specified path as Parquet file
                iceberg_data.to_parquet(save_path, index=False)
                st.success(f"Iceberg table saved to {save_path}")
            except Exception as e:
                st.error(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    main()
