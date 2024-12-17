from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import json
import librosa

def precompute_audio_ffts(sample_folder, output_file):
	fft_library = {}
	for filename in os.listdir(sample_folder):
		if filename.endswith('.wav') or filename.endswith('.mp3'):
			file_path = os.path.join(sample_folder, filename)
			y, sr = librosa.load(file_path, sr=8000, mono=True)
			fft_result = np.abs(np.fft.fft(y))
			fft_library[filename] = fft_result.tolist()
			print(f"{filename} processed")

	with open(output_file, 'w') as json_file:
		json.dump(fft_library, json_file)

	print(f"FFT data saved to {output_file}")

def load_sample_library(json_file):
	with open(json_file, 'r') as f:
		fft_library = json.load(f)
	return {k: np.array(v) for k, v in fft_library.items()}

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

