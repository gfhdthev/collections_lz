#name:adres
book = {'Ilya':'Minsk', 'Arseniy':'Mogilev', 'Bob':'Moskow'}

while True:
    a = input('Введите, что вы хотите сделать (просмотр/изменение/удаление): ')

    if a == 'просмотр':
        print(book)

    elif a == 'изменение':
        print('Вот имена записанных людей:')
        for key in book:
            print(key)

        b = input('Введите пользователя, чьи данные нужно изменить: ')
        print('Вот адрес данного персонажа: ', book[b])
        c = input('Введите, какой адрес установить: ')

        book[b] = c
        

    elif a == 'удаление':
        print('Вот имена записанных людей:')
        for key in book:
            print(key)

        b = input('Введите пользователя, чьи данные нужно удалить: ')

        del book[b]

    else:
        break

