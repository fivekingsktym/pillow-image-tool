# # Open the image using Pillow
image_data = Image.open(blog_data.thumbnail_img)
# Get the width and height of the image
height, width = image_data.size
print(f"Width: {width}, Height: {height} ###########################################")

# case-1
database_image = blog_data.thumbnail_img.read()
form_image = thumbnail_img.read()
# Get the size of the image data in bytes
database_image_bytes = len(database_image)
form_image_bytes = len(form_image)
print(f"File Size (bytes) of database_image is: {database_image_bytes} ***************************************8")
print(f"File Size (bytes) of form_image is: {form_image_bytes} ***************************************8")
Close the file objects
blog_data.thumbnail_img.close()
thumbnail_img.close()

# case-2
try:
    database_image = Image.open(blog_data.thumbnail_img)
    form_image = Image.open(thumbnail_img)

    database_image_bytes = len(database_image.tobytes())
    form_image_bytes = len(form_image.tobytes())

    print(f"File Size (bytes) of database_image is: {database_image_bytes} #########################")
    print(f"File Size (bytes) of form_image is: {form_image_bytes} #########################")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the images if they were opened successfully
    if 'database_image' in locals():
        database_image.close()
        print('database_image closed..............................')
    if 'form_image' in locals():
        form_image.close()
        print('form_image closed..............................')

# case-3
# Open the database image
with Image.open(blog_data.thumbnail_img.path) as database_image:
    database_image_bytes = len(database_image.tobytes())

# Open the form image
with Image.open(thumbnail_img) as form_image:
    form_image_bytes = len(form_image.tobytes())

# print(f"File Size (bytes) of database_image is: {len(blog_data.thumbnail_img)} #########################")
print(f"File Size (bytes) of database_image is: {database_image_bytes} #########################")
print(f"File Size (bytes) of form_image is: {form_image_bytes} #########################")


        