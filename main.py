#   pip: inflect googletrans==3.1.0a0
#   ?? замена чисел в тексте
#   выбор языка

import inflect
from googletrans import Translator

translator=Translator()
p = inflect.engine()

def zmn(x):
    if int(x)!=10:
        y=(p.number_to_words(x))
        ts=translator.translate(str(y), src='en', dest='ru')
        output=ts.text
    else:
        output='ДЕСЯТЬ'
    return output.replace(',', '').upper()

print('Введите число:')
x=input()
print(zmn(x))