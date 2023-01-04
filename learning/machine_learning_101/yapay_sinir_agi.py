# Yapay sinir ağları (YSA), bir türevi olan yapay öğrenme yöntemlerine ait bir algoritmadır. 
# Bu algoritmalar sayesinde bilgisayarlar, verilen örnekler üzerinden öğrenmeyi amaçlar. 
# Öğrendiklerini yeni veri setleriyle test etmeyi ve bu verileri kullanarak tahminlerde bulunmayı hedefler.

# YSA'lerin temel yapısı, gerçek sinir ağlarından esinlenerek tasarlandı. 
# Bu yapı, bir girdi katmanı, birkaç gizli katman ve bir çıktı katmanından oluşur. 
# Girdi katmanı, ağa verilen verileri temsil eder. 
# Gizli katmanlar ise, girdi katmanından geçen verileri işleyen ve çıktı katmanına iletilen katmanlardır. 
# Çıktı katmanı ise, ağın öğrendiği bilgileri kullanarak verilen girdilere ilişkin tahminleri yapar.

# YSA'ler, öğrendiklerini ağırlık değerleri olarak saklarlar. 
# Bu değerler, ağın girdi verilerine verdiği önem derecesini belirtir. 
# Örneğin, bir resim tanıma uygulamasında, ağın gözünde daha önemli olan nesnelerin resimlerinde bulunan özellikler, daha yüksek ağırlık değerlerine sahip olacaktır.

# YSA'ler, verilen örnekler üzerinden öğrendiklerini, öğrenme algoritmalarını kullanarak güncellerler. 
# Bu algoritmalar, ağın tahminlerinin doğruluğunu ölçer ve ağırlık değerlerini bu doğruluğa göre günceller. 
# Bu sayede, ağ öğrendiklerini daha da geliştirir ve daha doğru tahminler yapmaya başlar.

# YSA'ler, çok çeşitli uygulamalarda kullanılabilir. 
# Örneğin, makine öğrenimi algoritmalarının çoğu, YSÖ temelli algoritmalardır. 
# Ayrıca, ses ve görüntü tanıma, metin çevirisi, makine öğrenimi gibi birçok alanda da kullanılırlar.
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def mean_squared_error(y_pred, y):
    return 0.5 * (y_pred - y)**2

def mean_squared_error_derivative(y_pred, y):
    return y_pred - y

# Örnek veri oluşturma
X = np.array([[0.87, 0.51], [2.10, 1.24], [1.11, 2.90]])
y = np.array([1.63, 2.11, 2.30])

# Ağırlıkları ve bias değerlerini rastgele oluşturma
weights_1 = np.random.uniform(size=(2, 2))
weights_2 = np.random.uniform(size=(2, 1))
bias_1 = np.random.uniform(size=(1, 2))
bias_2 = np.random.uniform(size=(1, 1))

# Öğrenme oranı
learning_rate = 0.001

# Eğitim döngüsü
for epoch in range(1):
    for i in range(len(X)):
        x, y = X[i], y[i]
        
        # İleri yayılım
        z_1 = np.dot(x, weights_1) + bias_1
        a_1 = sigmoid(z_1)
        z_2 = np.dot(a_1, weights_2) + bias_2
        a_2 = z_2
        
        # Geri besleme
        error = mean_squared_error(a_2, y)
        delta_2 = mean_squared_error_derivative(a_2, y)
        delta_1 = np.dot(delta_2, weights_2.T) * sigmoid_derivative(a_1)
        
        print(a_1)
        print(delta_2)
        print(x)
        print(delta_1)
        # Ağırlıkları güncelleme
        weights_2 -= learning_rate * np.dot(a_1.T, delta_2)
        weights_1 -= learning_rate * np.dot(x.T, delta_1)
        bias_2 -= learning_rate * delta_2
        bias_1 -= learning_rate * delta_1
