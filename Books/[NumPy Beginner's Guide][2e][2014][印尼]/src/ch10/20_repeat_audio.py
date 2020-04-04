from scipy.io import wavfile
import matplotlib.pyplot as plt
# import urllib2
import urllib.request
import numpy as np
import sys

# response = urllib2.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
response = urllib.request.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
print(response.info())

WAV_FILE = 'smashingbaby.wav'
filehandle = open(WAV_FILE, 'wb')
filehandle.write(response.read())
filehandle.close()

sample_rate, data = wavfile.read(WAV_FILE)
print("Data type", data.dtype, "Shape", data.shape)

plt.subplot(2, 1, 1)
plt.title("Original" )
plt.plot(data)

plt.subplot(2, 1, 2)

# 重复音频片段
try:
    N = int(sys.argv[1])
except IndexError as e:
    N = 4
repeated = np.tile(data, N)

# 绘制音频数据
plt.title("Repeated")
plt.plot(repeated)
wavfile.write("repeated_yababy.wav", sample_rate, repeated)

plt.show ()
