from PIL import Image
import requests
from io import BytesIO

# URL of the image
image_url = 'https://img.freepik.com/premium-photo/cat-waves-with-his-paw-as-if-he-says_937306-462.jpg'

# Fetch the image from the URL
response = requests.get(image_url)

# Check if the request was successful
if response.status_code == 200:
    # Open the image from the response content
    with Image.open(BytesIO(response.content)) as image_data:
        # check the image_data file_size in bytes
        image_data_bytes = len(image_data.tobytes())
    
    print(f"File Size (bytes) is: {image_data_bytes}")
    
else:
    print("Failed to fetch the image from the URL")
