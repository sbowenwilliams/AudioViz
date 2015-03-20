import librosa
import matplotlib.pyplot as plt
import numpy as np
import csv
import json

#filename = '/Users/davidryan93/Documents/Northwestern, 2014-15/Winter 2015/EECS 352/Final Project/code/Thunderclap.mp3'
filename = '/Users/davidryan93/Documents/Northwestern, 2014-15/Winter 2015/EECS 352/Final Project/code/VCR0.16.wav'

y, sr = librosa.load(filename)

##=================
## AMPLITUDE, DUDE
##=================

#perceptual weighting

S       = np.abs(librosa.stft(y, n_fft=4096, hop_length=256.0)) ** 2
log_S   = librosa.core.logamplitude(S, ref_power=np.median)


log_S_transposed = log_S.transpose().tolist()

S_avg = []
S_max = []
S_sum = []
print log_S.transpose().shape
print "getting"

for i in range(len(log_S_transposed)):
	avg = sum(log_S_transposed[i])
	S_avg.append(avg/len(log_S_transposed[i]))
	S_sum.append(avg)
	S_max.append(max(log_S_transposed[i]))

print "done"

print sorted(S_avg)

#with open('amplitude.csv', 'w') as f:
#   writer = csv.writer(f, delimiter=',')
#   writer.writerows(S_avg) 
#
#plt.figure(figsize=(12,4))
#librosa.display.specshow(log_S, sr=sr, cmap='gray_r', x_axis='time')
#plt.title('Amplitude')
#plt.tight_layout()
#plt.show()
