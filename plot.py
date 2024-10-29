import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [25, 32, 34, 20, 25]

plt.title("График функции y", color='#173554', fontstyle="italic", fontweight="bold")
plt.xlabel('Ось х', color='#173554', fontweight="bold") #Подпись для оси х
plt.ylabel('Ось y', color='#173554', fontweight="bold")
ax = plt.gca()
ax.set_facecolor('#84d8d8')
plt.gcf().set_facecolor('#84d8d8')


plt.plot(x, y, color='#173554', marker='o', markersize=7)
plt.show()