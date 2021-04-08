import pandas as pd
import wave
import numpy as np
# 将音频写入csv文件
def read_to_write(data,name):
    data = pd.DataFrame(data)
    # index = [1]则只写入一行
    print(data)
    renovation = data
    print(renovation)
    renovation.to_csv(name,index = False ,sep= ',',header=None)
    return renovation

# 读取音频文件，并保存成数组（一维向量）的形式
def read_wav(path):
    f = wave.open(path, "rb")
    # 打开音频文件
    params = f.getparams()
    # 获取wav音频的信息
    nchannels, sampwidth, framerate, nframes = params[:4]
    # 获取音频的通道数，宽度，采样频率，声音数据
    str_data = f.readframes(nframes)
    # 将声音数据提取存放再str_data中
    f.close()
    # 关闭音频文件
    wave_data = np.frombuffer(str_data, dtype=np.short)
    # 将读取的wav文件存入wave_data,存入的格式为16进制
    wave_data_list = list(wave_data)
    # 将wave_data中的数据转换成一维向量数组的形式
    wave_data = np.delete(wave_data, wave_data_list[len(wave_data_list)-1])
    # 删除从wave_data_list[]开始的数
    wave_data = wave_data.astype(np.float32, order='C') / 32768.0
    return wave_data

path = r"D:\gongyong\csdn\Heaven.wav"
wav = read_wav(path)
print(wav)
read_to_write(wav,'audio1.csv')