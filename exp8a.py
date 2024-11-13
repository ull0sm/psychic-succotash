from bokeh.plotting import figure, output_file, show

graph = figure (title = "Bokeh line graph")

x = [1,2,3,4,5]
y = [5,4,3,2,1]

graph.line(x,y)
show(graph)