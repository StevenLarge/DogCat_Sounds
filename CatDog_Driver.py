#Python analysis script for cat vs dog sounds (.wav files)
#
#Steven Large
#January 20th 2018

import scipy.io.wavfile as sciwav
import matplotlib.pyplot as plt
import matplotlib as mpl
import prettyplotlib as ppl

import scipy.signal 													#scipy.signal.periodogram(DATA) gives PSD

#Import example data

Cat_rate,Cat_data = scipy.io.wavfile.read('cats_dogs/cat_100.wav')
Dog_rate,Dog_data = scipy.io.wavfile.read('cats_dogs/dog_100.wav')

plt.plot(Cat_data)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Cat Meow')
plt.savefig('Cat_Sample.png')
plt.close()

plt.plot(Dog_data)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Dog Barking')
plt.savefig('Dog_Sample.png')
plt.close()



