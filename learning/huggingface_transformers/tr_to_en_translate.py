from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
def translate(text):
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-tr-en")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-tr-en")
    batch = tokenizer([text], return_tensors="pt",max_length=512, truncation=True)
    generated_ids = model.generate(**batch)
    outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return outputs
