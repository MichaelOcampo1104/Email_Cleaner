#THIS CODE IS WORKING PLEASE CHECK EXCELL FILE IN PROPER FORMATING IN CASE RECIEVED SOME OUTPUT ERROR

import pandas as pd
import re

def clean_email_body(text):
    """
    Function to remove email addresses and headers from the email body.
    """
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove common headers like "From:", "To:", "CC:", etc.
    headers_to_remove = ["From:", "To:", "CC:", "BCC:", "Subject:", "Date:", "Reply-To:", "Sent:", "Attachments:"]
    for header in headers_to_remove:
        text = re.sub(f"{header}.*", '', text)
        
    return text.strip()

if __name__ == "__main__":
    # Define the path to the original CSV file
    file_path = '230918_P103_Mails.csv'
    
    # Load the CSV into a DataFrame
    df = pd.read_csv(file_path, encoding='ISO-8859-1', low_memory=False)

    
    # Check the first few entries of the 'Body' column before cleaning
    print("Before cleaning:")
    print(df['Body'].head())
    
    # Handle NaN or float entries by converting them to empty strings
    df['Body'] = df['Body'].fillna('')
    
    # Apply the cleaning function to the 'Body' column
    df['Cleaned_Body'] = df['Body'].apply(lambda x: clean_email_body(str(x)))
    
    # Check the first few entries of the 'Cleaned_Body' column after cleaning
    print("After cleaning:")
    print(df['Cleaned_Body'].head())
    
    # Define the path where you want to save the cleaned CSV file
    cleaned_file_path = r'230918_P103_Mail_Clean.csv'
    
    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(cleaned_file_path, index=False)
    
    #this code is working
    

