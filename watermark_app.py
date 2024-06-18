# Import built-in and third-party libraries

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageFont, ImageDraw

# Function to add watermark

def add_watermark(file_path, watermark_text, save_path):
    original_image = Image.open(file_path).convert("RGBA")
    image_width, image_height = original_image.size

    # Create a transparent overlay image for the watermark
    overlay_image = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

    # Load a font for the watermark
    font_size = int(image_height / 20)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Enable drawing on the transparent overlay
    draw = ImageDraw.Draw(overlay_image)

    # Calculate the watermark width and height
    watermark_width = font.getlength(watermark_text)
    ascent, descent = font.getmetrics()
    watermark_height = ascent + descent

    # Calculate the position for the watermark
    x = image_width - watermark_width - 10
    y = image_height - watermark_height - 10

    # Add watermark to the transparent overlay
    draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)

    # Combine the original image with the transparent overlay image
    watermarked_image = Image.alpha_composite(original_image, overlay_image)

    # Save the watermarked image
    watermarked_image.convert("RGB").save(save_path)

# Function to upload image

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])

    if file_path:
        watermark_text = watermark_entry.get()

        if watermark_text:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])

            if save_path:
                try:
                    add_watermark(file_path, watermark_text, save_path)
                    messagebox.showinfo("Success", "Watermark added successfully!")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter the watermark text.")

# Create the main window

root = tk.Tk()
root.title("Watermark Adder")

# Create and place the widgets

tk.Label(root, text="Watermark Text:").pack(pady=10)

watermark_entry = tk.Entry(root, width=50)
watermark_entry.pack(pady=10)

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)

# Run the main loop

root.mainloop()