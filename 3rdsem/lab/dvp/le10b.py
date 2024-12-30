import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Latitude': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
    'Longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740],
    'Population': [8419000, 3980400, 2716000, 2328000, 1690000]
}
df = pd.DataFrame(data)

# Create a map plot
fig = px.scatter_map(df, lat="Latitude", lon="Longitude", size="Population")

fig.show()