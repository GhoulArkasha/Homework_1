string_1 = "Не знаю, как там в Лондоне, я не был. Может там собака - друг человека. " \
    "А у нас управдомом - друг человека."

print('Шаг1 - Количество символов - {}'.format(len(string_1)))
print(f'Шаг2 - Развернутая строка - {string_1[::-1]}')
print(f'Шаг3 - Все слова с большой буквы -  {string_1.title()}')
print(f'Шаг4 - Все слова с маленькой буквы - {string_1.lower()}')
print(f'Шаг5 - Число вхождений "нд" в строку - {string_1.count("нд")}')
print(f'Шаг5 - Число вхождений "ам" в строку - {string_1.count("ам")}')
print(f'Шаг5 - Число вхождений "о" в строку - {string_1.count("о")}')
print(f'Шаг6 - Исходная строка - {string_1}')