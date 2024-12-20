import os
import argparse
from image_to_sound import precompute_audio_ffts

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Update the precomputed FFT library for a sample folder."
    )
    parser.add_argument(
        "--sample_folder", 
        type=str, 
        required=True, 
        help="Path to the folder containing audio sample files (.wav or .mp3)"
    )
    parser.add_argument(
        "--output_file", 
        type=str, 
        required=True, 
        help="Path to the output JSON file to save precomputed FFT data"
    )

    # Parse arguments
    args = parser.parse_args()
    sample_folder = args.sample_folder
    output_file = args.output_file

    # Check if sample folder exists
    if not os.path.exists(sample_folder):
        print(f"Error: Sample folder '{sample_folder}' does not exist.")
        return

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Run the precompute function
    print("Starting FFT precomputation...")
    precompute_audio_ffts(sample_folder, output_file)
    print("FFT library updated successfully!")

if __name__ == "__main__":
    main()
