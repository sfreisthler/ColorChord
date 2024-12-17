from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def slice_image(image_path, num_slices = 10):
	image = Image.open(image_path).convert('L')

	width, height = image.size
	slice_width = width // num_slices

	slices = []

	for i in range(num_slices):
		box = (i * slice_width, 0, (i + 1) * slice_width, height)
		slice_img = image.crop(box)
		slices.append(np.array(slice_img))
		
	return slices

def display_image(image):
	plt.imshow(image, cmap='gray')
	plt.axis('off')
	plt.show()

def compute_fft(slice):
	fft = np.fft.fft2(slice)
	fft_magnitude = np.abs(np.fft.fftshift(fft))

	# return 1D fft for comparison with audio fft
	return fft_magnitude.flatten()

