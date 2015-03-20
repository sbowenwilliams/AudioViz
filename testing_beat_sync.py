import librosa
import matplotlib.pyplot as plt
import numpy as np
import csv

filename = '/Users/davidryan93/Documents/Northwestern, 2014-15/Winter 2015/EECS 352/Final Project/code/Thunderclap_test.wav'
#filename = '/Users/davidryan93/Documents/Northwestern, 2014-15/Winter 2015/EECS 352/Final Project/code/cmaj-dmin-gmaj-cmaj.wav'

y, sr = librosa.load(filename)

hop_length = 64
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length)

C = librosa.feature.chromagram(y=y, sr=sr, n_fft=4096, hop_length=hop_length)

C_sync = librosa.feature.sync(C, beats, aggregate=np.median)

plt.figure(figsize=(12,6))

plt.subplot(2, 1, 1)
librosa.display.specshow(C, sr=sr, hop_length=64, y_axis='chroma', vmin=0.0, vmax=1.0)
plt.title('Chroma')
plt.colorbar()

plt.subplot(2, 1, 2)
librosa.display.specshow(C_sync, y_axis='chroma', vmin=0.0, vmax=1.0)

beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=64)
librosa.display.time_ticks(beat_times)

plt.title('Beat-synchronous Chroma (median aggregation)')

plt.colorbar()
plt.tight_layout()

plt.show()
