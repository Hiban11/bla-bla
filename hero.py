import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
file_path = 'D:/OYAA/Tubidy.li_-Maroon-5-Sugar-_Official-Music-Video_.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(file_path, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print ('Wait')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
hero = 'D:/OYAA/Hero - Mariah Carey.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(hero, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('Hero')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
best_4_you = 'D:/OYAA/Maroon 5 - Best 4 You (Lyrics)_fj6TNbK5dLM.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(best_4_you, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('best 4 you')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
girl = 'D:/OYAA/Maroon 5 - Girls Like You (Lyrics) ft. Cardi B.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(girl, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('girl like you')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
hel = 'D:/OYAA/Maroon 5, Julia Michaels - Help Me Out (Lyrics _ Lyric Video) (1).wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(hel, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('help me out')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
come = 'D:/OYAA/y2mate.com - Nirvana  Come As You Are Official Music Video.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(come, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('come as you are')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
drain = 'D:/OYAA/y2mate.com - Nirvana  Drain You Audio.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(drain, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('drain you')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
smelss = 'D:/OYAA/y2mate.com - Nirvana  Smells Like Teen Spirit Official Music Video.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(smelss, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('smells like teen spirit')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
okee = 'D:/OYAA/y2mate.com - Nirvana  Something In The Way Audio.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(okee, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('something in the way')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")

import librosa
import numpy as np

# Tentukan path file audio yang ingin digunakan
oke = 'D:/OYAA/y2mate.com - Nirvana  You Know Youre Right LP Version.wav'# Ganti dengan path file audio yang sesuai

# Baca file audio menggunakan Librosa
audio, sr = librosa.load(oke, sr=None, mono=True)

# Ekstraksi fitur-fitur audio dasar
tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
zcr = librosa.feature.zero_crossing_rate(audio)

# Tampilkan hasil ekstraksi fitur
print('you know you right')
print(f"Tempo: {tempo}")
print(f"Chroma STFT: {np.mean(chroma_stft)}")
print(f"Spectral Centroid: {np.mean(spec_cent)}")
print(f"Spectral Bandwidth: {np.mean(spec_bw)}")
print(f"Spectral Rolloff: {np.mean(rolloff)}")
print(f"Zero Crossing Rate: {np.mean(zcr)}")




