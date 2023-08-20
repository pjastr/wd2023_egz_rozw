import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
x1 = [27.2, 8.8, 28.1, 21.1, 14.9]
e1 = [0, 0.1, 0, 0, 0]
l1 = ["A", "B", "C", "D", "E"]
c1 = ["gray", "bisque", "gold", "tomato", "khaki"]
plt.pie(x1, explode=e1, colors=c1, startangle=15, shadow=True, labels=l1, autopct="%1.1f%%")
plt.title("Tytuł 1")
plt.subplot(2, 1, 2)
x2 = [25.7, 21.2, 13.4, 12.8, 26.8]
c2 = ["turquoise", "orange", "goldenrod", "green", "orangered"]
plt.pie(x2, explode=e1, colors=c2, startangle=15, shadow=True, labels=l1, autopct="%1.1f%%")
plt.title("Tytuł 2")
plt.tight_layout()
plt.savefig("zad1.svg")
plt.show()
