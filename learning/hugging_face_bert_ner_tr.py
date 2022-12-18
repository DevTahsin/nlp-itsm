# Named Entity Recognition
# Metinde geçen isimlerin tespit edilerek sınıflandırılması işlemidir. 
# Bu işlem sonucunda, metinde geçen isimlerin (örneğin, kişi isimleri, yer isimleri) tespit edilir ve bunların ne olduğu belirlenir.

from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

model_checkpoint = "akdeniz27/bert-base-turkish-cased-ner"
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

output = ner_pipeline("Çekilen Excel’de Tarih kısımları tarih olarak değil, genel olarak gözüküyor. Ama sonrasında genelden tarihe çektiğimizde bile genel olarak kalmaya devam ediyor. Excel’den çıkarttığımız raporlarda da bu bize sorun çıkartıyor. Mümkünse Excel çekildiğinde tarih başlıklarının altında gelen verilerin tarih olarak gelmesi konusunda yardımcı olabilir misiniz? Bu konuyu İbrahim beye teams üzerinden göstermiştim.")

print(output)