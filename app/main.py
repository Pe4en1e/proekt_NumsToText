#   pip: inflect googletrans==3.1.0a0

import inflect
from googletrans import Translator

translator = Translator()
p = inflect.engine()

def zmn(x, y):
    rtxt = (p.number_to_words(x))
    prerts = rtxt + ' ruble'
    rts = translator.translate(str(prerts), src='en', dest='ru')
    rubles = rts.text

    if int(y) < 99:
        ktxt = (p.number_to_words(y))
        prekts = ktxt + ' kopek'
        kts = translator.translate(str(prekts), src='en', dest='ru')
        kopek = kts.text
    else:
        return 'Копеек не может быть больше 99'

    return rubles.replace(',', '').upper() + ' ' + kopek.replace(',', '').upper()


print('Введите рубли:')
x = input()
print('Введите копейки:')
y = input()
print(zmn(x, y))

