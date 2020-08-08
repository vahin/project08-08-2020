import pandas as pd
import plotly.express as px

data = pd.read_csv("covidCases.csv")

x = px.scatter(data, x="date", y="cases", color="country")
x.show()
y = px.histogram(data, x="date", y="cases", color="country")
y.show()
