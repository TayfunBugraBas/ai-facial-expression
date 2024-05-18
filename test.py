import os
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
import cv2
import librosa
import numpy as np
from pydub import AudioSegment
import time



def extract_feature(file_path, n_mfcc=40, max_len=174):
    audio_data, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=n_mfcc)
    pad_width = max_len - mfccs.shape[1]
    if pad_width > 0:
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfccs = mfccs[:, :max_len]
    #print(mfccs)
    return mfccs


result = extract_feature('D:/yapayzekafinal/ses/angry_05/03-01-05-01-01-01-01.wav')