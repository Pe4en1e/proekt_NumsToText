#   pip: inflect googletrans==3.1.0a0
#   попробуй api яндекса
#   ?? замена чисел в тексте
#   компиляция в exe / граф интерфейс??
#   выбор языка

import inflect
from googletrans import Translator

translator=Translator()
p = inflect.engine()

print('Введите число:')
x=input() # принимаем число
y=(p.number_to_words(x)) # преобразовываем в текст
ts=translator.translate(str(y), src= 'en', dest= 'ru') # переводим на русский
output=ts.text # берем итоговую строку
print(output.replace(',', ''))

def zmn(x): 
    y=(p.number_to_words(x))
    ts=translator.translate(str(y), src='en', dest='ru')
    output=ts.text
    return output.replace(',', '')

print('Введите число:')
x2=input()
print(zmn(x2))