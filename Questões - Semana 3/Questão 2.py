
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


carros = pd.read_csv('mt_cars.csv')  # Importa a planilha
print(carros)

print(carros.describe())

sns.heatmap(carros.corr(), cmap = "YlGnBu", annot = True)  # Mapa de calor
carros.plot.scatter('wt', 'mpg')
carros.plot.scatter('hp', 'cyl')

plt.show()
