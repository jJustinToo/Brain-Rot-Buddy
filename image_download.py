import os
import shutil
import time
from bing_image_downloader import downloader

def download_image(query):
    # Set the output directory to 'images'
    output_dir = 'temp/images'
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Download the image into a 'query' subfolder
    downloader.download(query, limit=1, output_dir=output_dir, adult_filter_off=False, force_replace=False, timeout=60)
    
    # Move and rename the image from the 'query' subfolder to the main 'images' folder
    query_folder = os.path.join(output_dir, query)
    
    if os.path.exists(query_folder):
        for filename in os.listdir(query_folder):
            file_path = os.path.join(query_folder, filename)
            
            # Create a unique filename based on the query and current timestamp
            new_filename = f"{query}.jpg"
            new_file_path = os.path.join(output_dir, new_filename)
            
            shutil.move(file_path, new_file_path)  # Move and rename file
            
        # Remove the now empty 'query' folder
        os.rmdir(query_folder)
    
    print(f"Downloaded and saved image for '{query}' as '{new_filename}' in the '{output_dir}' directory.")