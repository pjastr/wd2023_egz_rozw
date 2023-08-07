import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("gastro11.csv", sep=";", header=None).T
dane2 = dane.iloc[1:, ].copy()
dane2.columns = dane.iloc[0,]
dane2["Rok"] = pd.Series(dane2["Rok"], dtype=int)
dane2["Wartosc"] = pd.Series(dane2["Wartosc"], dtype=int)
r2007 = dane2[dane2["Rok"] == 2007]
r2009 = dane2[dane2["Rok"] == 2009]
plt.subplot(1, 2, 1)
plt.pie(r2007["Wartosc"], labels=r2007["Typy placówek"], autopct="%1.f%%")
plt.title("Dane za rok 2007")
plt.subplot(1, 2, 2)
plt.pie(r2009["Wartosc"], labels=r2007["Typy placówek"], autopct="%1.f%%")
plt.title("Dane za rok 2009")
plt.tight_layout()
plt.savefig("zad3.pdf")
plt.show()
