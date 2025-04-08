mport cv2
from PIL import Image

# Load an image
image = cv2.imread('C:\\Users\\CSE\\Desktop\\image.jpg')

# Print image properties
print("Image Height:", image.shape[0])  # Height
print("Image Width:", image.shape[1])  # Width
print("Number of Channels:", image.shape[2])  # Channels (e.g., 3 for BGR, 1 for grayscale)
print("Image Size (in Pixels):", image.size)  # Total number of pixels
print("Image Data Type:", image.dtype)  # Data type of image (e.g., uint8)
# Open an image using Pillow
image = Image.open('C:\\Users\\CSE\\Desktop\\image.jpg')

# Get the format of the image (e.g., 'JPEG', 'PNG', etc.)
print("Image Format:", image.format)
