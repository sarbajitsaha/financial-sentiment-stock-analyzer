import os
import subprocess

def download_dataset(dataset_slug, output_dir):
    """Download and unzip a Kaggle dataset."""
    os.makedirs(output_dir, exist_ok=True)
    command = f"kaggle datasets download -d {dataset_slug} -p {output_dir} --unzip"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Downloaded {dataset_slug} to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {dataset_slug}: {e}")
        print("Ensure Kaggle API is set up: https://www.kaggle.com/docs/api")

if __name__ == "__main__":
    # Download news dataset
    download_dataset("hkapoor/indian-financial-news-articles-20032020", "data/raw/news")
    
    # Download stock dataset
    download_dataset("rohanrao/nifty50-stock-market-data", "data/raw/stocks")
