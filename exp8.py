from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend, LegendItem, Title , Span

output_file("line_graph_with_annotations.png")

x = [1,2,3,4,5]
y1 = [2,5,7,2,8]
y2 = [1,4,5,3,6]

p = figure(title = "Line graph with annotations and legends",x_axis_label = "x-axis",y_axis_label= "y-axis")

line1 = p.line(x,y1,line_width=2,color="blue",legend_label = "line 1")
line2 = p.line(x,y2,line_width=2,color="red",legend_label = "line 2")

annotation = Span(location = 3, dimension = "width", line_color= "black",line_width = 8)

p.add_layout(annotation)

legend = Legend(items = [LegendItem(label = "line 1",renderers = [line1]),LegendItem(label = "line 2",renderers = [line2])])
p.add_layout(legend)
show(p)