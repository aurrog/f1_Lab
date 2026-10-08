import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('notebooks/data.csv')

fig, ax = plt.subplots()
sc = ax.scatter(df['x'], df['y'], c=df['speed'], cmap='viridis')
fig.colorbar(sc, label='speed')

plt.show()