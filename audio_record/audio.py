import pyaudio
import wave

# 設定擷取音訊的參數
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5  # 設定擷取的時間長度

# 初始化PyAudio
audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    output=False, frames_per_buffer=CHUNK)

print("擷取音訊中...")

frames = []

# 擷取音訊數據
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("擷取完成！")

# 停止音訊流
stream.stop_stream()
stream.close()
audio.terminate()

# 將擷取到的音訊保存為WAV文件
with wave.open("output.wav", "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))