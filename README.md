# Image Watermarking Application
## Description
This is a simple desktop application built with Python that allows users to upload images and add a custom watermark. The application uses the `tkinter` library for the graphical user interface and the `Pillow` (PIL) library for image processing.

## Features
- Upload images in various formats (JPG, JPEG, PNG, BMP, GIF).
- Add custom text as a watermark.
- Save the watermarked image in JPG or PNG format.

## Requirements
- Python 3.x
- Pillow library

## Installation
1. **Clone the repository:**
```
cd image-watermarking-app
git clone https://github.com/your-username/image-watermarking-app.git
```

2. **Install the required libraries:**
```
pip install Pillow
```

## Usage
1. **Run the application:**
```
python watermark_app.py
```

2. **Using the application:**
- Enter the watermark text in the provided text field.
- Click the "Upload Image" button to select an image.
- Choose the location and filename to save the watermarked image.
- The application will process the image and save it with the watermark.