from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

def zero_shot_classification(text, candidate_labels):
    return classifier(text, candidate_labels)

