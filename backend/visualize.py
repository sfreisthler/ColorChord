import matplotlib.pyplot as plt
import numpy as np

def display_image(image):
	plt.imshow(image, cmap='gray')
	plt.axis('off')
	plt.show()

def display_fft(fft_data, sample_rate=None, is_2d=False, title="FFT Visualization"):
    """
    Visualizes FFT data (1D or 2D).
    
    Parameters:
        fft_data (numpy array): The FFT data to visualize.
        sample_rate (int, optional): The sample rate of the signal (used for 1D FFTs).
        is_2d (bool): Set to True for 2D FFT visualization (e.g., image FFT).
        title (str): Title of the plot.
    """
    if is_2d:
        # 2D FFT Visualization (Magnitude Spectrum)
        fft_magnitude = np.log(1 + np.abs(fft_data))  # Log scale for better visualization
        plt.figure(figsize=(8, 6))
        plt.imshow(np.fft.fftshift(fft_magnitude), cmap='gray', extent=(-1, 1, -1, 1))
        plt.colorbar(label='Magnitude (log scale)')
        plt.title(title)
        plt.xlabel('Normalized Frequency (u)')
        plt.ylabel('Normalized Frequency (v)')
        plt.show()
    else:
        # 1D FFT Visualization
        fft_magnitude = np.abs(fft_data)  # Magnitude of FFT
        frequencies = np.fft.fftfreq(len(fft_data), 1/sample_rate) if sample_rate else np.arange(len(fft_data))
        
        # Only plot positive frequencies
        half = len(fft_magnitude) // 2
        frequencies = frequencies[:half]
        fft_magnitude = fft_magnitude[:half]
        
        plt.figure(figsize=(10, 6))
        plt.plot(frequencies, fft_magnitude, color='blue')
        plt.title(title)
        plt.xlabel('Frequency (Hz)' if sample_rate else 'Frequency Bin')
        plt.ylabel('Magnitude')
        plt.grid()
        plt.show()