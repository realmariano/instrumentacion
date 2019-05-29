from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
input_data = read("output.wav")
audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio)#(audio[0:1024])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("output Wav")
# display the plot
plt.show()
