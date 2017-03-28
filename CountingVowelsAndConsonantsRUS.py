# CountingVowelsAndConsonantsRU.py
# by Prometheus111
#подсчёт гласных и согласных букв во введённом тексте
#запрос на ввод и перевод введённых букв в нижний регистр
i = input('Введите текст: \n').lower()
#гласные и согласные буквы для русской версии кода
g = ['а','е','ё','и','о','у','э','ю','я']
s = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ','ь','ъ']
#вывод количества
print('Количество гласных: ', len([1 for x in list(i) if x in g]))
print('Количество согласных: ', len([1 for x in list(i) if x in s]))
# Enjoy learning new things! Prometheus111 helps you with your studying!
# https://github.com/Prometheus111 
