from image_to_sound import slice_image, display_image, precompute_audio_ffts, load_sample_library

def main():

	precompute_audio_ffts('./samples', 'samples.json')
	samples = load_sample_library('./samples.json')
	
	test_path = '../static/cat.png'

	slices = slice_image(test_path)

if __name__=='__main__':
	main()