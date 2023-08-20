import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel("ceny31.xlsx")
jablka = data[data["Rodzaje towarów i usług"] == "jabłka - za 1kg"]
cytryny = data[data["Rodzaje towarów i usług"] == "cytryny - za 1 kg"]
miesiace = jablka["Miesiące"]
x = np.arange(0, 12)
plt.plot(x, jablka["Wartosc"], label="Jabłka", linestyle="--", linewidth=2)
plt.plot(x, cytryny["Wartosc"], label="Cytryny", linestyle="-.", linewidth=3)
plt.legend()
plt.xticks(x, miesiace, rotation=45)
plt.title("Dane za 2016 rok")
plt.ylabel("Ceny w zł")
plt.tight_layout()
plt.savefig("zad2.webp")
plt.show()
