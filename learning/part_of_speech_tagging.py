# Part of speech tagging POS
# cümle öğelerini dil bilgisi kurallarına göre etiketleme işlemidir.
# ADJ: Sıfat
# ADP: Edat
# ADV: Zarf
# AUX: Fiil
# CONJ: Bağlaç
# DET: Belirteç
# INTJ: Seslenme
# NOUN: İsim
# NUM: Sayı
# PART: Dilbilgisi
# PRON: Zamir
# PROPN: Özel isim
# PUNCT: Noktalama işareti
# SCONJ: Bağlaç
# SYM: Sembol
# VERB: Fiil

import spacy
from util import _get_nlp

nlp = _get_nlp()
# Define the text to be tokenized
text = "Ahmet, Eti şirketinin kurucusu ve eski CEO'sudur."

# Tokenize the text
doc = nlp(text)

# Print the tokens
for token in doc:
    print(token.text, token.tag_)

# Output:
# Bu
# cümleyi
# kelimelere
# ayırmak
# istiyorum
# .