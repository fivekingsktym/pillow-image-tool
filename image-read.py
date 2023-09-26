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

    # case-1
    # image_data = BytesIO(response.content).read()
    # image_data = len(image_data)
    # print(f"File Size (bytes) is: {image_data}")

    # case-1
    # check the image_size file_size in bytes
    image_size = len(response.content)
    print(f"File Size (bytes) is: {image_size}")
    
else:
    print("Failed to fetch the image from the URL")
