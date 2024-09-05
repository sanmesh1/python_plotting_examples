from bokeh.plotting import figure, show
import pandas as pd

df = pd.read_csv('example_data.csv')
# df = pd.read_excel('example_data.xlsx')
time = df["time"].tolist()
money = df["Money"].tolist()

p = figure(title="Money over time",
           x_axis_label = "time", y_axis_label="Money")

p.line(time, money, legend_label="line1", line_width=2)

show(p)