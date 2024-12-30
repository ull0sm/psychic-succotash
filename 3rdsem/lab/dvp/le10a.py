import plotly.express as px
import pandas as pd

data = {
    "date":["jan 2020","feb 2020","mar 2020","apr 2020","may 2020","jun 2020","jul 2020"],
    "value":[10, 15, 13, 17, 14, 18, 20]
}

df = pd.DataFrame(data)

fig = px.line(df,x = "date",y="value")
fig.show()