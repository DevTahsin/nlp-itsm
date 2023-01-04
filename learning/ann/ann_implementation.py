import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# veriyi çek
dataset = pd.read_csv('Churn_Modelling.csv')

# gereksiz kolonları sil
# bağımsız değişkenler X e
# bağımlı değişken y e
    X = pd.DataFrame(dataset.iloc[:, 3:13].values)
    y = dataset.iloc[:, 13].values

# text verileri daha rahat işlemek için kategori labella
# örneğin cinsiyet alanı 1 ve 0 olarak
# ülke alanı [0,0],[0,1][1,0] gibi coğrafik olarak işaretlenir
# [0 0] means- France.
# [0 1] means Spain
# [1 0] means Germany
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X_2 = LabelEncoder()
X.loc[:, 2] = labelencoder_X_2.fit_transform(X.iloc[:, 2])
labelencoder_X_1 = LabelEncoder()
X.loc[:, 1] = labelencoder_X_1.fit_transform(X.iloc[:, 1])
ct = ColumnTransformer([("Country", OneHotEncoder(), [1])], remainder = 'passthrough')

labelencoder_X_1 = LabelEncoder()
X.loc[:, 1] = labelencoder_X_1.fit_transform(X.iloc[:, 1])
X = ct.fit_transform(X)
X = X[:, 1:]

# makine öğrenmesi modeli yaparken, elimizdeki verileri training sette eğitmemiz gerekiyor.
# modelimizin performansını ölçmek içinse test set kullanıcaz.
# test sete verimizin %20 sini ayırıyoruz. test_size a 0.2 değerini bu yüzden verdik.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# feature scaling
# veri setimizde görüldüğü üzere verilerimizin birbirine göre farklı ölçeklerde olduğunu görüyoruz.
# özellikle balance ve estimated_salary, bu durum hesap işlemlerimizi daha uzun sürede yapmamıza neden oluyor.
# feature scaling bize verilerimizi belirli bir ölçekte normalize etmemizi sağlıyor.
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# keras kütüphanesini kullanarak yapay sinir ağı oluşturacağız.
import keras
from keras.models import Sequential
from keras.layers import Dense

# yapay sinir ağı oluştur
# Sequential classı yapay sinir ağlarını(sıralı katman) oluşturmak için kullanılır
classifier = Sequential()

# giriş katmanı ve ilk gizli katmanı oluştur
# Dense tensorflow da en sık kullanılan classdır. Dense ANN ye tam bağlı bir katman eklememizi sağlar.
# add metodu ile katmanı ekliyoruz.
# output_dim = 6, gizli katmandaki nöron sayısını temsil eder. burada 6 dememizin çok bir anlamı yok
# activation = 'relu' ise gizli katmanın aktivasyon fonksiyonunu temsil eder. relu fonksiyonu gizli katmanın aktivasyon fonksiyonu olarak kullanılır.
# input_dim = 11 ise girdideki bağımsız değişkenlerimizi temsil eder. 
classifier.add(Dense(6, 'relu', input_dim = 11))    

# ikinci gizli katmanı oluştur
classifier.add(Dense(6, 'relu'))

# çıkış katmanı oluştur
# aktivasyon fonksiyonu sigmoid
classifier.add(Dense(1,   'sigmoid'))

# yapay sinir ağı derle
# adam stochastic gradient descent algoritmasını kullanır.
# optimizer eğitim boyunca ağırlıkları günceller ve kaybı azaltır.
# binary prediction yapmak istediğimiz için loss u binary_crossentropy olarak belirledik.
# metrics = ['accuracy'] ile doğruluk metrikleri kullanacağımızı belirttik.
classifier.compile('adam', 'binary_crossentropy', ['accuracy'])

# yapay sinir ağı eğit
classifier.fit(X_train, y_train, 10, 100)

# eğitilmiş veriye göre tahmin yap
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# confusion matrix ve accuracy score hesapla
# confusion matrix kullanmamızın sebebi tahminlerimizin doğruluğunu ölçmek için daha iyi bir gösterim sağlamasıdır.
# 0 ve 1 arasında bir doğruluk payı döner
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test,y_pred)

