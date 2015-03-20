import librosa
import matplotlib.pyplot as plt
import numpy as np
import json

def getChromaAmps():
	filename = 'audiofiles/VCR.mp3'

	y, sr = librosa.load(filename)

	## CHROMAGRAM
	print "finding chromagram..."
	hop_length = 1024.0
	n_fft = 4096.0
	C = librosa.feature.chromagram(y=y, sr=sr, n_fft=n_fft, hop_length=hop_length)
	c_list = C.transpose().tolist()

	## AMPLITUDE
	print "finding amplitude..."
	S       = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length)) ** 2
	log_S   = librosa.core.logamplitude(S, ref_power=np.median)
	a_list = log_S.transpose().tolist()

	data = []
	time_step = hop_length / float(sr)
	num_steps = len(c_list)

	print "making output..."
	for i in range(num_steps):
		#chroma
		chroma_values = c_list[i]
		chroma_max = max(chroma_values)
		chroma = chroma_values.index(chroma_max) + 1
		
		#amplitude
		amplitude_avg = sum(a_list[i])
		amplitude = round(amplitude_avg/len(a_list[i]), 0)
		
		#timestamp
		timestamp = time_step * i	
		data.append([timestamp, chroma, amplitude])

	#possibly normalize the amplitudes

	return data