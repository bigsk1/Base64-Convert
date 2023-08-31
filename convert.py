import os
import base64
from PIL import Image

def image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except Exception as e:
        print(f"Error converting {image_path} to Base64: {e}")
        return None

def resize_and_convert(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            img = img.resize((250, 160), Image.LANCZOS)
            img.save(output_path, "webp")
    except Exception as e:
        print(f"Error resizing and converting {image_path}: {e}")

def main():
    image_dir = "images"
    valid_extensions = [".webp", ".jpg", ".jpeg", ".png"]

    for filename in os.listdir(image_dir):
        if any(filename.endswith(ext) for ext in valid_extensions):
            full_path = os.path.join(image_dir, filename)

            # Resize and convert the image to WebP
            webp_filename = os.path.splitext(filename)[0] + "_converted.webp"
            webp_path = os.path.join(image_dir, webp_filename)
            resize_and_convert(full_path, webp_path)

            print(f"Resized and converted {filename} to WebP and saved as {webp_filename}")

            # Convert the WebP image to Base64
            base64_string = image_to_base64(webp_path)
            if base64_string:
                txt_filename = os.path.splitext(filename)[0] + ".txt"
                txt_path = os.path.join(image_dir, txt_filename)

                with open(txt_path, "w") as txt_file:
                    txt_file.write(base64_string)

                print(f"Converted {webp_filename} to Base64 and saved as {txt_filename}")

if __name__ == "__main__":
    main()
