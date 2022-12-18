# makale özet
# makale özetleme için kullanılan yöntem
# 1- makale token parçalara ayrılır (tokenization)
# 2- token parçaları özellikleri belirlenir (POS tagging)
# 3- token parçalarında anahtar kelimeler belirlenir


import spacy
from spacy.lang.tr.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
from util import _get_nlp

nlp = _get_nlp()

text = """Merhaba ,

SR Onay Bekleyen kaytılarda onay bekleniyor aşamasında kayıtlar kapatılabilmektedir. Onay bekleniyor aşamasında kaydın kapatılmaması için çalışma yapılmasını  rica ediyoruz.

Aynı kayıtlarda kapatıldığında ise kayıt tekrar aktif oluyor.  sorunu çözümünü rica ediyoruz."""


doc = nlp(text)

keyword = []
stopwords = list(STOP_WORDS)
pos_tag = ["PROPN", "ADJ", "NOUN", "VERB"]
for token in doc:
    if(token.text in stopwords or token.text in punctuation):
        continue
    if(token.tag_ in pos_tag):
        keyword.append(token.text)

freq_word = Counter(keyword)
# print(freq_word.most_common(5))

max_freq = Counter(keyword).most_common(1)[0][1]
for word in freq_word.keys():
    freq_word[word] = (freq_word[word]/max_freq)
# print(freq_word.most_common(5))

sent_strength={}
for sent in doc.sents:
    for word in sent:
        if word.text in freq_word.keys():
            if sent in sent_strength.keys():
                sent_strength[sent]+=freq_word[word.text]
            else:
                sent_strength[sent]=freq_word[word.text]
# print(sent_strength)

summarized_sentences = nlargest(3, sent_strength, key=sent_strength.get)
# print(summarized_sentences)

# print(type(summarized_sentences[0]))

final_sentences = [ w.text for w in summarized_sentences ]
summary = ' '.join(final_sentences)
print(summary)

# gensim summarization
# print(summarize(doc))
