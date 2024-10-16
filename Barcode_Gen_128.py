"""
Barcode 128 Code Generator Script
Author: Pedro Garza-Ramos
Date: October 2024
Description:
    This script generates 128-Barcodes based on user input and saves them as an image file.

Dependencies:
    - os (folder creation)
    - barcode (barcode generation; need install)
    - pillow (for image processing; need install)
    (for barcode and pillow use: 'pip install python-barcode pillow'


"""


import os
import barcode
from barcode.writer import ImageWriter


def generate_barcode(data, barcode_type='code128', output_folder='Barcode_Folder_Storage'):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create a Barcode object
    code = barcode.get_barcode_class(barcode_type)

    # Set the data and create the barcode
    code_instance = code(data, writer=ImageWriter())

    # Save the barcode to an image file in the specified folder
    filename = f"{output_folder}/{data}_{barcode_type}"
    code_instance.save(filename)

    print(f"Barcode saved as {filename}")

# Main loop for generating barcodes
while True:
    data_to_encode = input("Value to barcode (Type 'quit' to exit): ")

    if not data_to_encode:
        print("Please enter a value.")
        continue
    elif data_to_encode.lower() == 'quit':
        print("Exiting the program.")
        break

    generate_barcode(data_to_encode, barcode_type='code128', output_folder='Barcode_Folder_Storage')

# Barcodes stored in 'Barcode_Folder_Storage' folder in same directory

