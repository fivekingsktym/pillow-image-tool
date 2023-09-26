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
    image_data = Image.open(BytesIO(response.content))
    
    # Get the size of the image
    # image_height_width = image_data.size
    height , width = image_data.size
    
    print(f"Width: {width}, Height: {height}")
    
else:
    print("Failed to fetch the image from the URL")
