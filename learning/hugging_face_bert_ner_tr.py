# Named Entity Recognition
# Metinde geçen isimlerin tespit edilerek sınıflandırılması işlemidir. 
# Bu işlem sonucunda, metinde geçen isimlerin (örneğin, kişi isimleri, yer isimleri) tespit edilir ve bunların ne olduğu belirlenir.

from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

model_checkpoint = "akdeniz27/bert-base-turkish-cased-ner"
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

output = ner_pipeline("Ahmet, Eti şirketinin kurucusu ve eski CEO'sudur.")

print(output)   