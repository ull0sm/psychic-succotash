import plotly.express as px

size = [10,20,30,40,50]
x = [1,2,3,4,5]
y = [5,6,7,8,9]
z = [9,3,5,0,1]

fig = px.scatter_3d(x=x,y=y,z=z,size=size)
fig.show()