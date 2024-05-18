from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
import cv2
import librosa
import numpy as np
from pydub import AudioSegment
import time
from django.views.decorators.csrf import ensure_csrf_cookie
import cv2
import base64

highest_prediction = None
emotion_picture = []
emotion_sound = []
emotions = ['Angry','disgust','Fearful', 'Happy', 'Neutral', 'Sad', 'Surprised']
# Create your views here.

def home(request):

    return render(request,"base.html")


@csrf_exempt
def upload_audio(request):
        save_audio(request)
        makePrediction('D:/yapayzekafinaluygulama/')
        
          # Ses dosyasını kaydetme işlemi
        return JsonResponse({'message': 'Ses kaydedildi ve işlendi.'})
   

def save_audio(request):
    try:
        os.remove('D:/yapayzekafinaluygulama/temp_audio.wav')
    except:
         pass
    audio_file = request
    # Ses dosyasını diskte belirtilen bir konuma kaydetme
    with open(os.path.join('D:/yapayzekafinaluygulama/', 'temp_audio.wav'), 'wb+') as destination:
        for chunk in audio_file:
            destination.write(chunk)

def upload_image(request):
    
        image = request.POST['image']

        image_data = base64.b64decode(image.split(',')[1])
        # Resmi bir dosyaya kaydet
        with open('D:/yapayzekafinaluygulama/uploaded_image.png', 'wb') as f:
            f.write(image_data)

        # Kaydedilen resmi oku
        image_path = 'D:/yapayzekafinaluygulama/uploaded_image.png'
        image_data = cv2.imread(image_path)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Yüzleri bul
        faces = face_cascade.detectMultiScale(image_data, scaleFactor=1.1, minNeighbors=5, minSize=(48, 48))

        if len(faces) > 0:
            # İlk yüzü al
            x, y, w, h = faces[0]

            # Yüzü kes
            face_image = image_data[y:y+h, x:x+w]

            # Grayscale'e dönüştür
            grayscale_face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
            resized_image = cv2.resize(grayscale_face_image, (48, 48))
            input_data = np.expand_dims(resized_image, axis=0)
            input_data = np.expand_dims(input_data, axis=-1)
            # Grayscale yüzü kaydet
            grayscale_face_path = 'D:/yapayzekafinaluygulama/uploaded_face_grayscale.png'
            cv2.imwrite(grayscale_face_path, grayscale_face_image)

            model = load_model('D:/yapayzekafinaluygulama/face83p.keras')
          
            result = model.predict(input_data)
            global emotion_picture
            emotion_picture = result

            
            
            
            return JsonResponse({'message': 'Yüz başarıyla bulundu ve kesildi.'})
        else:
            return JsonResponse({'message': 'Yüz bulunamadı.'})
    
    
   

def makePrediction(audio_path):
     mfccs = load_data(audio_path)
     model = load_model('D:/yapayzekafinaluygulama/sesmodeli2.keras')
     
     result = model.predict(mfccs)
     global emotion_sound
     emotion_sound = result

     return result



def load_data(data_path):
    data = []
    for filename in os.listdir(data_path):
        if filename.endswith('.wav'):
                filepath = os.path.join(data_path, filename)
                feature = extract_feature(filepath)
                data.append(feature)

    return np.array(data)

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


def getCalculatedResult(request):
    req = request.POST['req']
    print(req)
    np.set_printoptions(precision=20)
    print(emotion_sound)
    print(emotion_picture)
    wanted = emotions.index(req)

    sound = emotion_sound[0,[wanted]]
    picture = emotion_picture[0,[wanted]]
    result = (sound + picture)/2
    print(result)
    return JsonResponse({"message":str(result[0])})
