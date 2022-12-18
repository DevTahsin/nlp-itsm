# Tokenizasyon (Tokenization)
# Bir metin parçasını kelimelerine ayırma

import spacy
from util import _get_nlp

nlp = _get_nlp()
# Define the text to be tokenized
text = "Bu cümleyi kelimelere ayırmak istiyorum."

# Tokenize the text
doc = nlp(text)

# Print the tokens
for token in doc:
    print(token.text)

# Output:
# Bu
# cümleyi
# kelimelere
# ayırmak
# istiyorum
# .