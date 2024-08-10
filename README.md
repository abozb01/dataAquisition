# dataAquisition
# Data Acquisition Pipeline

## Overview

This Python script automates the process of acquiring, cleaning, and storing data for analytics purposes. It downloads data from an FTP server, cleans it, and stores it in a SQLite database, making it ready for analysis such as training and predictions.

## Workflow

1. **Download Data**:
   - Connect to an FTP server and download CSV files from a specified remote directory to a local directory.

2. **Load Data**:
   - Load the downloaded CSV files into Pandas DataFrames for easy manipulation and analysis.

3. **Clean Data**:
   - Clean the data by dropping rows with missing values and converting date columns to `datetime` objects.

4. **Store Data**:
   - Store the cleaned data in a SQLite database named `analytics_data.db`, making it ready for analytics operations.

5. **Pipeline Setup**:
   - The entire process, from downloading to storing data, is managed by the `data_acquisition_pipeline` function.

## Usage

### FTP Setup
- **ftp_server**: Replace with the actual FTP server address.
- **username**: Provide the FTP server username.
- **password**: Provide the FTP server password.
- **remote_dir**: Specify the path to the remote directory where the CSV files are located.

### Local Directory
- **local_dir**: Specify the local directory where the downloaded files will be saved. The directory will be created automatically if it doesn't exist.

### Data Cleaning
- The script currently drops any rows with missing values and converts date columns to `datetime` objects. Modify the `clean_data` function to implement additional data cleaning steps based on your needs.

### Database Storage
- The cleaned data is stored in a SQLite database named `analytics_data.db`. Replace this with another database solution (e.g., MySQL, PostgreSQL) if needed by modifying the `store_data` function.

## Running the Script

To execute the data acquisition pipeline, run the following command in your terminal:

```bash
python data_acquisition.py
