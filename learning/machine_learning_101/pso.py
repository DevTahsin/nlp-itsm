#Parçacık Sürü Optimizasyonu (Particle Swarm Optimization, PSO) bir yapay zeka yöntemidir ve bir hedef fonksiyonun üzerinde arama yapmayı amaçlar. 
# Bu yöntem, bir parçacık sürüsünün simüle edilmesiyle çalışır ve bu sürüdeki parçacıklar, hedef fonksiyonun bir çözümünü bulmaya çalışırlar. 
# Bu parçacıklar, önceki adımlarından ders alarak hedefe doğru hareket ederler ve zamanla daha iyi çözümler bulmayı amaçlar.

# PSO, genellikle diğer optimizasyon yöntemlerine göre daha az sayıda adım ile çözüm bulmayı başarır ve ayrıca bir "global optimum" (en iyi çözüm) bulmayı amaçlar, diğer yöntemler ise "local optimum" (yerel en iyi çözüm) bulmayı hedefler. 
# Ancak, bu yöntem genellikle diğer yöntemlerden daha az doğruluğa sahiptir ve daha az güvenilir sonuçlar verebilir.

# PSO, özellikle çok değişkenli fonksiyonların çözümünde kullanılır ve genellikle diğer optimizasyon yöntemlerine göre daha hızlıdır. 
# Örneğin, bir makine öğrenimi modelinin parametrelerinin ayarlanmasında kullanılabilir.

# aşağıdaki PSO sorusunu python ile implemente edelim.

# Parçacık Sürü Optimizasyonu ile N = 3 (parçacık) yardımıyla, it. = 3 (iterasyon) kapsamında, f(x,y) = (2+x)-3y fonksiyonunu 'maksimize' ediniz.
# [ Önemli: 
# Her parçacık için velocity (v) başlangıç değerlerini rastgele veriniz. 
# Rastgele değerler (0, 1) açık aralığından elde edilecektir. 
# Bulunan - kullanılan değerlerde virgülden sonra 2 basamak hassaslık kullanıp, 0,5 ve üstü değerleri yukarı, 0,49 ve aşağı değerleri aşağı yuvarlayınız.] 
import random

# c1 ve c2, parçacık sürü optimizasyonu (PSO) yönteminde kullanılan sabitlerdir. 
# Bu sabitler, parçacıkların hareketlerini yönetmek için kullanılır ve genellikle PSO yönteminin performansını etkiler.
# c1, bireysel en iyi değere (pbest) olan etkisini belirler. 
# Örneğin, yüksek bir c1 değeri, bireysel en iyi değere olan etkisini artıracak ve parçacıkların pbest değerine olan yakınlaşmasını sağlayacaktır.
# c2, sürünün en iyi değere (gbest) olan etkisini belirler. 
# Örneğin, yüksek bir c2 değeri, gbest değere olan etkisini artıracak ve parçacıkların gbest değerine olan yakınlaşmasını sağlayacaktır
c1 , c2 = 1, 1
gbest = 0
# fonksiyonumuz
def f(x, y):
  return (2 + x) - 3 * y

# Parçacık sürüsü oluşturun
particles = [{'x': 0, 'y': 0, 'v': 0, 'pbest': 0} for _ in range(3)]

# Başlangıç değerlerini atayın
for particle in particles:
  particle['x'] = random.uniform(-10, 10)
  particle['y'] = random.uniform(-10, 10)
  particle['v'] = round(random.uniform(0, 1), 2)
  if particle['v'] >= 0.5:
    particle['v'] = round(particle['v'], 0)
  else:
    particle['v'] = round(particle['v'], 0)

# Iterasyonları gerçekleştirin
for _ in range(3):
  # Her bir parçacık için fonksiyon değerini hesaplayın
  for particle in particles:
    particle['f'] = f(particle['x'], particle['y'])

  # Parçacık sürüsünü güncelleyin
  for particle in particles:
    # Bireysel en iyi değeri ve sürünün en iyi değerini güncelleyin
    if particle['f'] > particle['pbest']:
      particle['pbest'] = particle['f']
    if particle['f'] > gbest:
      gbest = particle['f']
      
    # Yeniden velocity değerini hesaplayın ve güncelleyin
    particle['v'] = particle['v'] + c1 * random.random() * (particle['pbest'] - particle['x']) + c2 * random.random() * (gbest - particle['x'])
    particle['v'] = round(particle['v'], 2)
    if particle['v'] >= 0.5:
      particle['v'] = round(particle['v'], 0)
    else:
      particle['v'] = round(particle['v'], 0)
      
    # Yeniden konum değerini hesaplayın ve güncelleyin
    particle['x'] = particle['x'] + particle['v']
    particle['y'] = particle['y'] + particle['v']


# En iyi değeri yazdırın
print(gbest)
