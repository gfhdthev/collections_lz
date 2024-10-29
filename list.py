input_data = open('input.txt', 'r')
data = input_data.read()

n = int(data)
list = []
list.append(0) #добавлем первый ноль
list.append(1) #добавлем первую единицу

s1 = 0
s2 = 1
k = 0 #количество элементов больше медианного значения

for i in range(1, n-1):

    if i%2 == 0: #если i четное, то мы обноляем s1
        s1 = s1+s2
    elif i%2 == 1: #если i нечетное, то мы обноляем s2(чередуем после каждого числа)
        s2 = s1+s2

    list.append(s1+s2)

i = 0

for i in range(0, len(list)): 
    if list[i] % 2 == 0: #проверяем на четность
        list[i] = list[i] * 2 #если четное, то умножаем на 2

    else:
        list[i] = list[i] ** 2 #если нечетное, то возводим в квадрат

i = 0

minim = min(list) #минмимальный элемент
maxim = max(list) #максимальный элемент
lenl = len(list) #длина списка

arifm = sum(list)/len(list) #медианное значение

for i in range(0, len(list)):
    if int(list[i]) > arifm:
        k += 1 #проверяем, сколько чисел бедет больше мидианного значения

output = open('output.txt', 'w')
output.write(str('min - ') + str(minim) + str('\nmax - ') + str(maxim) + str('\nlen - ') + str(lenl) + str('\n> median - ') + str(k))

input_data.close()
output.close()