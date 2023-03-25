import random

miasta_list = ['Warszawa', 'Kraków', 'Wrocław', 'Łódź', 'Poznań', 'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin',
               'Białystok']
miasta_list = random.sample(miasta_list, len(miasta_list))

for i in range(0, len(miasta_list)):
    if i < len(miasta_list) - 1:
        print(miasta_list[i], end=' -> ')
    else:
        print(miasta_list[i])
