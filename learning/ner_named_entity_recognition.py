# Named Entity Recognition
# Metinde geçen isimlerin tespit edilerek sınıflandırılması işlemidir. 
# Bu işlem sonucunda, metinde geçen isimlerin (örneğin, kişi isimleri, yer isimleri) tespit edilir ve bunların ne olduğu belirlenir.

import spacy
from util import _get_nlp

nlp = _get_nlp()
# Define the text to be tokenized
text = "Ahmet, Eti şirketinin kurucusu ve eski CEO'sudur."

# Tokenize the text
doc = nlp(text)

# Named Entity Recognition (NER) işlemini gerçekleştirin
for ent in doc.ents:
    print(ent.text, ent.label_)

# Output:
# Bill Gates PERSON
# Microsoft ORG