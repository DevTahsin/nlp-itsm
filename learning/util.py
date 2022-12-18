# Tokenizasyon (Tokenization)
# Bir metin parçasını kelimelerine ayırma

from importlib.util import find_spec
from pathlib import Path
import spacy
from nlptr import sbd
from nlptr.tokenizer import Tokenizer

def _get_nlp():
    nlp = spacy.load(Path(find_spec("nlpturk_model").origin).parent)  # Load Turkish language model provided by spacyturk
    nlp.tokenizer = Tokenizer(nlp)
    return nlp 