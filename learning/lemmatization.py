# Lemmatization
# Metnin kelimelerini köklerine indirgeme işlemidir.

#Bu örnekte, öncelikle spaCy kütüphanesinin Türkçe dil modelini yüklüyoruz. 
# Daha sonra, lemmatization işlemini gerçekleştirmek istediğimiz metin parçasını tanımlıyoruz. 
# Ardından, nlp fonksiyonunu kullanarak metni tokenlere ayırıyoruz ve daha sonra bu tokenler için lemma değerlerini elde ediyoruz. 
# Bu örnekte, metin parçası tokenlere ayrılmış ve her bir token için lemma değeri elde edilmiştir.

# Not: Lemmatization işleminde, kelimenin gramer dilbilgisi (yani, fiil mi, isim mi, sıfat mı vs.) göz önünde bulundurulur ve bu dilbilgisine göre kelime köküne indirgenir. 
# Örneğin, "yürümek" fiil olduğu için "yürümek" kelimesinin kökü "yürümek" olurken, "istemek" isim olduğu için "istemek" kelimesinin kökü "istemek" olacaktır.

import spacy
from util import _get_nlp

nlp = _get_nlp()

# Define the text to be lemmatized
text = "Gidiyorum buralardan."

# Tokenize the text
doc = nlp(text)

# Lemmatize the text
lemmas = [token.lemma_ for token in doc]

# Print the lemmas
print(lemmas)

# Output:
# ['yürümek', 'istemek', '.']