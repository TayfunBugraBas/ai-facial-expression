PROJENİN BAŞKA DAĞITIMDA 
ÇALIŞTIRILMASI
1.	Adım 
Bilgisayarınızda projenin ses dosyalarını algılayabilmesi adına FFMPEG yüklü olması gerekmektedir.
FFMPEG yüklenişi için örnek video şu şekildedir:
https://www.youtube.com/watch?v=YgkmBMGrles
2.	Adım
Gerekli Python kütüphanelerini kurunuz Proje içerisinde Python 3.11.7 versiyonu kullanılmıştır.
Kütüphanelerin versiyonları şu şekildedir:
Tensorflow: 2.16.1
Keras: 3.2.1
Django: 5.0.6
Librosa: 0.10.2
Numpy: 1.26.4
Pandas: 2.1.4
Pydub: 0.25.1
Opencv-Python: 4.9.0.80
Resampy 0.4.3
Bunlar yapılan uygulamanın çalışması için gereken minimum uygulamalar ve kütüphanelerdir. <strong><b style="color:red;">Anaconda Navigator</b></strong> kullanmanız önerilir. Paket olarak çoğu kütüphaneyi yükleyip problemsiz çalıştırabilirsiniz. Paket yüklemesi sonrası Kerneli sıfırlayın. 
3.	Adım Projeyi Başlatma
Projeyi başlatmak için  terminal içerisinde cd aigusesser yazıp enter tuşuna bastıktan sonar aigusesser dosyasına girin 
“python manage.py runserver” yazıp projeyi başlatabilirsiniz. Projenin düzgün çalışabilmesi amacıyla Views.py dosyası içerisinde geçici resim ve görüntünün tutulduğu dosya yollarını bilgisayarınıza göre düzeltmeyi unutmayın. Aynı zamanda bu işlemi yapay zeka modellerinin yükleneceği klasör yolu için yapmayı unutmayın. 
	
	Proje Windows ortamında çalışmaktadır başka bir platform üzerinde denenmemiştir, 
