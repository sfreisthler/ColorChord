import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Step 1: Read the wav file
sample_rate, data = wavfile.read('piano.wav')

# Step 2: If stereo, select one channel (optional, depending on the wav file)
if len(data.shape) > 1:
    data = data[:, 0]  # Use only the first channel

# Step 3: Compute the Fourier Transform
N = len(data)  # Number of samples
fft_result = np.fft.fft(data)  # Compute FFT
frequencies = np.fft.fftfreq(N, 1/sample_rate)  # Get corresponding frequencies

# Step 4: Plot the results
plt.figure(figsize=(10, 6))

# Plot only the positive frequencies
plt.plot(frequencies[:N//2], np.abs(fft_result)[:N//2])
plt.title('Fourier Transform of the Audio Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()