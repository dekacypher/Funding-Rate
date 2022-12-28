import pytesseract
from PIL import Image
import os
import glob
# folder path
dir_path = '/Users/aishahalane/Screenshots'





count = -1
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)

files = glob.glob(os.path.join(dir_path, '*'))

# Sort the list of files by their modification time using the os.path.getmtime function:
files.sort(key=os.path.getmtime)

# Get the path of the latest file by taking the last element of the sorted list:
latest_file = files[-1]

# Open the image file

image = Image.open(latest_file)

# Extract the text from the image using OCR
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)