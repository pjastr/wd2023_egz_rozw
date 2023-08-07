import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("mieszkania11.xlsx")
ind = data[data["Formy budownictwa"] == "indywidualne"]
sp = data[data["Formy budownictwa"] == "spółdzielcze"]
kom = data[data["Formy budownictwa"] == "komunalne"]

years = ind["Rok"]
plt.bar(years, ind["Wartość"], label="indywidualne", color="pink")
plt.bar(years, sp["Wartość"], label="spółdzielcze", bottom=ind["Wartość"], color="violet")
bottom3 = np.array(ind["Wartość"]) + np.array(sp["Wartość"])
plt.bar(years, kom["Wartość"], label="komunalne", bottom=bottom3, color="brown")
plt.xticks(years)
plt.annotate("max", xy=(2017, 71000), arrowprops=dict(facecolor='black'), xytext=(2016.5, 65000))
plt.title("Wykres danych o mieszkaniach")
plt.legend()
plt.savefig("zad2.jpg")
plt.show()
