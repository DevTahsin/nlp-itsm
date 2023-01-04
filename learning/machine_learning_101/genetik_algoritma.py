# Genetik Algoritmalar, yapay zeka ve bilgisayar bilimlerinde bir optimizasyon tekniğidir. 
# Bu teknik, bir problemin çözümünü bulmak için bir nesil yaratır ve bu neslin üyelerini (özellikle çözümleri) birbirleriyle çaprazlarlar ve rasgele değişiklikler uygularlar. 
# Bu süreç, birkaç nesil boyunca tekrarlanır ve her nesil için bir "fitness" (uygunluk) fonksiyonu kullanılarak en uygun çözümler seçilir. 
# Bu yöntem, biyolojik evrimin esaslarına dayanır ve genetik algoritmaların adını da verir.

# Bu yöntem, birçok farklı tür problemin çözümünde kullanılabilir, ancak en sık kullanılan alanları makine öğrenimi ve tasarım otomatizasyonudur. 
# Örneğin, bir makine öğrenimi modelinin hiperparametrelerini otomatik olarak ayarlamak için genetik algoritmalar kullanılabilir. 
# Aynı şekilde, bir tasarım optimizasyonu için de kullanılabilir, örneğin bir hava taşıyıcısının performansını optimize etmek için.

# Genetik Algoritmalar, diğer optimizasyon yöntemlerine göre daha yavaş çalışsa da, genellikle daha iyi çözümler bulabilirler. 
# Bunun nedeni, diğer yöntemlerin sınırlı bir arama alanına odaklanırken, genetik algoritmalar tüm arama alanını tarar ve en iyi çözümleri bulmaya çalışır. 
# Ayrıca, genetik algoritmalar, çok boyutlu problemler için daha uygun bir seçenek olabilir, çünkü diğer yöntemlerin performansı genellikle bu tür problemlerle doğru orantılı değildir.

# Örnek bir soru üzerinden ele alacak olursak.
# Genetik Algoritma kullanarak, N = 4 (parçacık) yardımıyla, it. = 3 (iterasyon) kapsamında, f(x,y) = 2x + y
# fonksiyonunu 'minimize' ediniz.
# Soruya ek olarak verilenler:
# Her parçacık / birey 4 bitten oluşacaktır. En az 1 en çok 15 değeri alabilirler. 
# Çaprazlama için en iyi 2 parçacık / bireyin bitlerini en sağdan bir ve en soldan bir bit olacak şekilde çaprazlayınız. 
# Mutasyonu her değişken için farklı bir parçacığın / bireyin, herhangi bir bite uygulayınız.

import random

# Özelikler:
# N: Parçacık sayısı
# it: Iterasyon sayısı
# l: Parçacık uzunluğu
# min_val: En düşük değer
# max_val: En yüksek değer
# f: Fonksiyon (x,y)

N = 4
it = 3
l = 4
min_val = 1
max_val = 15

# Fonksiyon (f(x,y) = 2x + y)
def f(x,y):
    return 2*x + y

# Birinci nesil için parçacıkları oluştur
particles = []
for i in range(N):
    particle = []
    for j in range(l):
        particle.append(random.randint(min_val, max_val))
    particles.append(particle)
print("Birinci Nesil Parçacıkları:", particles)

# Birinci nesil için "fitness" (uygunluk) puanlarını hesapla
scores = []
for particle in particles:
    scores.append(f(particle[0], particle[1]))
print("Birinci Nesil Uygunluk Puanları:", scores)

# Birinci nesil için en uygun parçacıkları seç
best_particles = []
for i in range(N):
    best_particles.append(particles[scores.index(min(scores))])
    scores[scores.index(min(scores))] = float("inf")
print("Birinci Nesil En Uygun Parçacıklar:", best_particles)

# Iterasyonları gerçekleştir
for k in range(it):
    # İkinci nesil için parçacıkları oluştur (çaprazlama)
    particles = []
    for i in range(N):
        particle = []
        for j in range(l):
            if j < 2:
                particle.append(best_particles[i][j])
            else:
                particle.append(best_particles[(i+1) % N][j])
        particles.append(particle)
    print("İkinci Nesil Parçacıkları:", particles)

    # İkinci nesil için "fitness" (uygunluk) puanlarını hesapla
    scores = []
    for particle in particles:
        scores.append(f(particle[0], particle[1]))
    print("İkinci Nesil Uygunluk Puanları:", scores)

    # İkinci nesil için en uygun parçacıkları seç
    best_particles = []
    for i in range(N):
        best_particles.append(particles[scores.index(min(scores))])
        scores[scores.index(min(scores))] = float("inf")
    print("İkinci Nesil En Uygun Parçacıklar:", best_particles)

    # İkinci nesil için parçacıkları mutasyona uğrat
    for i in range(N):
        r = random.randint(0, l-1)
        best_particles[i][r] = random.randint(min_val, max_val)
    print("İkinci Nesil Mutasyon Uygulanmış Parçacıklar:", best_particles)

# En uygun parçacıkları göster
print("En Uygun Parçacıklar:", best_particles)

