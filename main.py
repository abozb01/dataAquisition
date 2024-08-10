import os
import ftplib
import pandas as pd
import sqlite3
from datetime import datetime

# Step 1: Connect to the FTP server and download the data

def download_data(ftp_server, username, password, remote_dir, local_dir):
    ftp = ftplib.FTP(ftp_server)
    ftp.login(username, password)
    ftp.cwd(remote_dir)

    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    filenames = ftp.nlst()
    for filename in filenames:
        local_file = os.path.join(local_dir, filename)
        with open(local_file, 'wb') as f:
            ftp.retrbinary('RETR ' + filename, f.write)
    ftp.quit()
    print("Data downloaded successfully.")

# Step 2: Load the data into Pandas DataFrame

def load_data(local_dir):
    data_frames = []
    for filename in os.listdir(local_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(local_dir, filename)
            df = pd.read_csv(file_path)
            data_frames.append(df)
    combined_df = pd.concat(data_frames, ignore_index=True)
    print("Data loaded into DataFrame.")
    return combined_df

# Step 3: Clean the data

def clean_data(df):
    # Example: Drop rows with missing values and convert date columns to datetime objects
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    print("Data cleaned.")
    return df

# Step 4: Store the data in a SQLite database

def store_data(df, db_name='analytics_data.db'):
    conn = sqlite3.connect(db_name)
    df.to_sql('analytics_data', conn, if_exists='replace', index=False)
    conn.close()
    print("Data stored in SQLite database.")

# Step 5: Set up the entire process

def data_acquisition_pipeline():
    # FTP server details
    ftp_server = 'ftp.example.com'
    username = 'your_username'
    password = 'your_password'
    remote_dir = '/data/source/'
    local_dir = './data/'

    # Download, load, clean, and store data
    download_data(ftp_server, username, password, remote_dir, local_dir)
    df = load_data(local_dir)
    cleaned_df = clean_data(df)
    store_data(cleaned_df)

    print("Data acquisition pipeline completed.")

# Run the data acquisition pipeline
if __name__ == '__main__':
    data_acquisition_pipeline()
