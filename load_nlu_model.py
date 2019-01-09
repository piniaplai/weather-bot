from __future__ import unicode_literals
from rasa_nlu.model import Metadata, Interpreter
import pprint
interpreter = Interpreter.load('models/nlu/default/current/') # loads model
raw = interpreter.parse("What is Israel") # parses provided input and gives intent classification
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(raw)
