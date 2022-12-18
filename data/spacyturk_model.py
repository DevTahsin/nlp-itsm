import sys
from spacy import util

cmd = [sys.executable, "-m", "pip", "install"] + ["https://github.com/nlpturk/nlpturk/releases/download/v0.0.2/nlpturk_model-0.0.2-py3-none-any.whl"]


util.run_command(cmd)