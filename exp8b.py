from bokeh.plotting import figure, output_file, show

graph = figure (title = "Bokeh bar graph")


x = [1,2,3,4,5]
y = [1,2,3,4,5]

graph.vbar(x,top = y, width = 0.2)
show(graph)