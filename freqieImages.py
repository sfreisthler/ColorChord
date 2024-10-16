import os
from PIL import Image

# source image
image_path = "static/cat.png"
img = Image.open(image_path)

# define number of slices
num_slices = 10
img_width, img_height = img.size


slice_width = img_width // num_slices

slices = []


# generate slices
for i in range(num_slices):
	left = i * slice_width
	right = left + slice_width if i < num_slices - 1 else img_width
	slice_img = img.crop((left, 0, right, img_height))
	slice_img.save(os.path.join("static", f"slice_{i}.png"))
	slices.append(slice_img)

