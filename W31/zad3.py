import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = pd.read_excel("samochody31.xlsx", header=None).T
dane.columns = ["Rodzaj", "Rok", "Wartość"]
dane["Rok"] = pd.Series(dane["Rok"], dtype=int)
dane["Wartość"] = pd.Series(dane["Wartość"], dtype=int)
r17 = dane[dane["Rok"] == 2017]
r18 = dane[dane["Rok"] == 2018]
y = np.arange(0, 6)
yp = r17["Rodzaj"]
x1 = r17["Wartość"]
x2 = r18["Wartość"]
plt.barh(y - 0.165, x1, label="2017", height=0.33)
plt.barh(y + 0.165, x2, label="2018", height=0.33)
plt.legend()
plt.xticks(np.arange(0, 2.5, 0.5) * 10e6, np.arange(0, 2.5, 0.5))
plt.xlabel("Wartość w mln")
plt.yticks(y, yp, rotation=45)
plt.title("Dane o samochodach")
plt.tight_layout()
plt.savefig("zad3.png")
plt.show()
