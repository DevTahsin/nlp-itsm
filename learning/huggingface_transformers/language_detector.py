import torch
from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification

tokenizer = XLMRobertaTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")

model = XLMRobertaForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")


def detect_language(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)

    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    return model.config.id2label[predicted_class_id]