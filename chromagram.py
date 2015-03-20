import librosa
import matplotlib.pyplot as plt
import numpy as np
import csv

filename = '/Users/davidryan93/Documents/Northwestern, 2014-15/Winter 2015/EECS 352/Final Project/code/VCR0.16.wav'
#filename = '/Users/davidryan93/Documents/Northwestern, 2014-15/Winter 2015/EECS 352/Final Project/code/cmaj-dmin-gmaj-cmaj.wav'

y, sr = librosa.load(filename)

##============ 
## CHROMAGRAM
##============

hop_length = 256
C = librosa.feature.chromagram(y=y, sr=sr, n_fft=4096, hop_length=hop_length)

c_list = C.transpose().tolist()

with open('chromagram_full.csv', 'w') as f:
   writer = csv.writer(f, delimiter=',')
   writer.writerows(c_list) 


c_maxes = []
time_step = hop_length / float(sr)

last_bin = 0
last_bin_index = 0
for i in range(len(c_list)):
	values = c_list[i]
	x = max(values)
	x = values.index(x) + 1
	if last_bin != x:
		timestamp = time_step * i
		timestamp_diff = timestamp - (time_step * last_bin_index)
		if (timestamp_diff > 0.10):
			c_maxes.append([timestamp, x])
			last_bin = x
			last_bin_index = i


print C.transpose().shape

with open('chromagram.csv', 'w') as f:
   writer = csv.writer(f, delimiter=',')
   writer.writerows(c_maxes) 

#
#
#plt.figure(figsize=(12,4))
#librosa.display.specshow(C, sr=sr, hop_length=hop_length, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
#plt.title('Chromagram')
#plt.tight_layout()
#plt.show()
#

	


##BASICALLY JUST SERIES OF VALUES THAT ARE {"TIMESTAMP: ___", "CHROMA_BIN": ____}
#with open('chromagram.json', 'w') as outfile:
#    json.dump({''}, outfile)
