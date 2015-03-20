import librosa
import matplotlib.pyplot as plt
import numpy as np
import csv

def getBeats():
	filename = 'VCR_background.wav'

	y, sr = librosa.load(filename)

	##==============
	## BEAT TRACKER
	##==============

	hop_length = 64
	tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length)

	print 'Estimated tempo: %0.2f beats per minute' % tempo

	## 4. Convert the frame indices of beat events into timestamps
	beat_times = librosa.frames_to_time(beat_frames, sr=sr, hop_length=hop_length)

	return beat_times

x = getBeats()
print x