from PIL import Image
import numpy as np
import os
import json
import librosa
import wave
from scipy.spatial.distance import euclidean, cosine
from scipy.interpolate import interp1d

def precompute_audio_ffts(sample_folder, output_file):
	fft_library = {}
	for filename in os.listdir(sample_folder):
		if filename.endswith('.wav') or filename.endswith('.mp3'):
			file_path = os.path.join(sample_folder, filename)
			y, sr = librosa.load(file_path, sr=8000, mono=True)
			fft_result = np.abs(np.fft.fft(y))
			fft_result = resample_fft(fft_result)
			fft_result = normalize_fft(fft_result)
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

def compute_fft(slice):
	fft = np.fft.fft2(slice)
	fft_magnitude = np.abs(np.fft.fftshift(fft))

	# return 1D fft for comparison with audio fft
	return fft_magnitude.flatten()

def normalize_fft(fft):
	magnitude = np.abs(fft)
	return magnitude / np.max(magnitude)

def assemble_audio(sample_folder, sample_list, output_path):
    # Open the output wave file
    with wave.open(output_path, 'wb') as output_wave:
        for i, sample in enumerate(sample_list):
            sample_path = os.path.join(sample_folder, sample)
            
            # Read each sample
            with wave.open(sample_path, 'rb') as sample_wave:
                # Set output params using the first sample
                if i == 0:
                    output_wave.setparams(sample_wave.getparams())
                
                # Read and write audio frames
                frames = sample_wave.readframes(sample_wave.getnframes())
                output_wave.writeframes(frames)

def resample_fft(fft_data, target_length=8000):
    """
    Resample FFT data to a target length.
    
    Parameters:
        fft_data (numpy array): Input FFT data to be resampled.
        target_length (int): The desired length of the output.
        
    Returns:
        numpy array: Resampled FFT data.
    """
    x_original = np.linspace(0, 1, len(fft_data))  # Original FFT indices
    x_resampled = np.linspace(0, 1, target_length)  # Target FFT indices
    interpolator = interp1d(x_original, fft_data, kind='linear')
    return interpolator(x_resampled)



def find_sound(slice_fft, sample_library, type="min"):
	selected_similarity = -float('inf') if type == "max" else float('inf')
	selected_sound = None

	for sample_name, sample_fft in sample_library.items():

		similarity = compute_similarity(slice_fft, sample_fft, "cos")


		if type == 'max' and similarity > selected_similarity:
			selected_sound = sample_name
			selected_similarity = similarity
		elif type == 'min'and similarity < selected_similarity:
			selected_sound = sample_name
			selected_similarity = similarity
	
	return selected_sound


def compute_similarity(image_fft, sound_fft, type="cos"):
	
	if type == "cos":
		return cosine_similarity(image_fft, sound_fft)
	elif type == "euclidean":
		return euclidian_similarity(image_fft, sound_fft)
	else:
		return  cosine_similarity(image_fft, sound_fft)


def cosine_similarity(image_fft, sound_fft):
	similarity = 1 - cosine(image_fft, sound_fft)
	return similarity

def euclidian_similarity(image_fft, sound_fft):
	similarity = 1 / (1 + euclidean(image_fft, sound_fft))
	return similarity


# returns image_fft, sound_fft padded to same length
def pad_ffts(image_fft, sound_fft):
	if len(image_fft) > len(sound_fft):

		return image_fft, np.pad(sound_fft, (0, len(image_fft) - len(sound_fft)), mode='constant')
	
	elif len(image_fft) < sound_fft:
		return np.pad(image_fft, (0, len(sound_fft) - len(image_fft)), mode='constant'), sound_fft

	return image_fft, sound_fft

def prepare_fft(fft):
	return normalize_fft(resample_fft(compute_fft(fft)))


def image_to_sound(image):
	samples = load_sample_library("./samples.json")
	slices = slice_image(image)
	sounds = [None] * len(slices)

	for i in range(len(slices)):
		image_fft = prepare_fft(slices[i])
		sounds[i] = find_sound(image_fft, samples)
	
	print(sounds)

	assemble_audio('./samples', sounds, "./output.mp3")
