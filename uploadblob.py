
import os, uuid
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# Generate concatenated tables
salaries = pd.read_csv('salary_download.csv')
savings = pd.read_csv('savings_download.csv')
salariesandsavings = salaries.join(savings['Savings'], on='id')
salariesandsavings = salariesandsavings[['id','Salary','Savings']]
salariesandsavings.to_csv('salariesandsavings_radomirfabian.csv',sep=',',index=False)

# Get the connection string from Shared Access Signature
connect_str = "BlobEndpoint=https://bdacademy.blob.core.windows.net/?sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2022-08-31T15:33:52Z&st=2022-08-09T07:33:52Z&spr=https&sig=66NHfW%2FPPySH9IfpsX0pMj%2Fymjdh2xJVPFf3o9Rw4vA%3D"
container_name = "ready"
local_file_name = "salariesandsavings_radomirfabian.csv"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

with open(local_file_name, "rb") as file:
	blob_client.upload_blob(file)
