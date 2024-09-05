from bokeh.plotting import figure, show
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('example_data.csv')
# df = pd.read_excel('example_data.xlsx')
time = df["time"].tolist()
money = df["Money"].tolist()

plt.plot(time, money)
plt.ylabel('Money')
plt.savefig("matplotlib_example_plotting_from_csv_onto_figure.png")
plt.show()