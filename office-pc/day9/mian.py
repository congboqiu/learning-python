import re
from mymodule import stats_word
import json


with open('tang300.json') as f:
     text=f.read()


stats_word.stats_text(text, 100)
