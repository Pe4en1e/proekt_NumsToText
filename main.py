#   pip: inflect googletrans==3.1.0a0
#   попробуй api яндекса
#   ?? замена чисел в тексте
#   компиляция в exe / граф интерфейс??
#   выбор языка

import inflect
from googletrans import Translator

translator=Translator()
p = inflect.engine()

def zmn(x):
    
    y=(p.number_to_words(x))
    ts=translator.translate(str(y), src='en', dest='ru')
    output=ts.text
    return output.replace(',', '').upper()

print('Введите число:')
x=input()
if x=='10':
    print('ДЕСЯТЬ')
else:
    print(zmn(x))