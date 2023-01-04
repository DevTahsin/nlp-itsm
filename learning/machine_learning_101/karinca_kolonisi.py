# Karınca Kolonisi Algoritması (Ant Colony Optimization Algorithm - ACO) bir optimizasyon algoritmasıdır. Bu algoritma, problemlerin çözümünde yararlanılır ve çözüm için en uygun yolu bulmaya çalışır. Algoritma, birkaç adımda çalışır:

# İlk olarak, problem alanında birkaç tane "köprü" kurulur. 
# Bu "köprüler" problem alanındaki yol güzergâhlarını temsil eder.
# Daha sonra, bu "köprüler" arasında gezinen birkaç tane "karınca" yaratılır.
# Bu "karıncalar", problem alanında gezinir ve hangi yolun daha uygun olduğunu belirlerler.
# Karıncalar gezdikçe, yol üzerinde "köprüler" arasında yer alan "ödeme duvarı" (pheromone trail) bırakırlar. 
# Bu "ödeme duvarı" diğer karıncaların yolun hangi bölümlerinin daha uygun olduğunu anlamasına yardımcı olur.
# Bu işlem tekrarlandıkça, diğer karıncalar en uygun yolu takip etmeye başlar. 
# Bu süreç devam ettikçe, en uygun yol bulunur ve problem çözülmüş olur.

#Örneğin, bir şirketin birkaç farklı üretim tesisinden birinde üretilen bir ürünün diğer tesislere dağıtımı için en uygun rotayı bulmaya çalışalım. 
# Bu durumda, her bir üretim tesisi bir "köprü" olacak ve "karıncalar" rotaları keşfederken, rotalar üzerinde "ödeme duvarı" bırakacak. 
# Bu süreç devam ettikçe, en uygun rota belirlenir ve ürünlerin dağıtımı için en uygun yol bulunmuş olur.

# Bu örnekte, "ödeme duvarı" maliyetleri temsil edebilir. 
# Örneğin, bir rotada maliyetler daha düşükse, o rota diğer rotalara göre daha uygun olacaktır ve diğer karıncalar bu rotayı tercih edecektir. 
# Bu sayede, en uygun rota belirlenmiş olur.

import random

# Örnek bir hedef fonksiyonu
def target_function(path, distances):
  total_distance = 0
  for i in range(len(path) - 1):
    total_distance += distances[path[i]][path[i+1]]
  return total_distance

# Karınca koloni algoritmasını içeren bir fonksiyon oluştur
def ant_colony_optimization(num_ants, num_iterations, cities, distances, initial_feromones):
  # Başlangıç koşullarını ayarla
  ants = []
  for i in range(num_ants):
    path = [initial_cities[i]]
    visited_cities = {initial_cities[i]: True}
    for _ in range(len(cities) - 1):
      next_city = choose_next_city(path[-1], visited_cities, cities, distances, initial_feromones)
      path.append(next_city)
      visited_cities[next_city] = True
    ants.append(path)
  best_ant = min(ants, key=lambda ant: target_function(ant, distances))
  
  # İterasyonları çalıştır
  for _ in range(num_iterations):
    # Tüm karıncaların hareketlerini simüle et
    for i in range(num_ants):
      path = [initial_cities[i]]
      visited_cities = {initial_cities[i]: True}
      for _ in range(len(cities) - 1):
        next_city = choose_next_city(path[-1], visited_cities, cities, distances, initial_feromones)
        path.append(next_city)
        visited_cities[next_city] = True
      ants[i] = path
    
    # En iyi karıncayı bul
    best_ant = min(ants, key=lambda ant: target_function(ant, distances))
    
    # Yol feremon değerlerini güncelle
    for i in range(len(best_ant) - 1):
      initial_feromones[best_ant[i]][best_ant[i+1]] *= 1.1
      initial_feromones[best_ant[i+1]][best_ant[i]] *= 1.1
  
  # Sonuçları döndür
  return best_ant

# Bir karıncanın hangi şehre gideceğini belirleyen fonksiyon
def choose_next_city(current_city, visited_cities, cities, distances, feromones):
  next_city = None
  max_product = 0
  for city in cities:
    if city not in visited_cities:
      product = feromones[current_city][city] * (1.0 / distances[current_city][city])
      if product > max_product:
        max_product = product
        next_city = city
  return next_city

# Karınca sayısı N=3 olmak üzere, aşağıdaki şehir turu kombinasyonel optimizasyon problemini (en kısa mesafe) Karınca Koloni Opt. ile toplam 3 iterasyonda çözümleyiniz.
num_ants = 3
num_iterations = 3

# Şehirlerin listesi
cities = ['A', 'B', 'C', 'D']

# Şehirler arası mesafeler
distances = {
  'A': {'B': 3, 'C': 7, 'D': 9},
  'B': {'C': 5},
  'C': {'D': 10}
}

# Başlangıçta yol feremon değerleri
initial_feromones = {
  'A': {'B': 0.23, 'C': 0.41, 'D': 0.34},
  'B': {'C': 0.33},
  'C': {'D': 0.51}
}

# Karınca başlangıç şehirleri
initial_cities = ['B', 'C', 'A']

# Karınca koloni algoritmasını çalıştır
best_path = ant_colony_optimization(num_ants, num_iterations, cities, distances, initial_feromones)

# En kısa yolu ekrana yazdır
print(best_path)
