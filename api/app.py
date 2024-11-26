from fastapi import FastAPI
import kaggle
import os

app = FastAPI()

# Set your Kaggle API credentials
os.environ['KAGGLE_USERNAME'] = 'your_kaggle_username'
os.environ['KAGGLE_KEY'] = 'your_kaggle_key'

@app.get("/download-dataset")
def download_dataset():
    dataset = 'dataset-owner/dataset-name'  # Replace with the actual dataset path on Kaggle
    kaggle.api.dataset_download_files(dataset, path='.', unzip=True)
    return {"message": "Dataset downloaded successfully"}

# To run the app, use the command: uvicorn app:app --reload