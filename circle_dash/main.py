from random import random
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import figure, curdoc

num_circles = 10

# LOAD YOUR DATA
x = [random()*70 for i in range(num_circles)]
y = [random()*70 for i in range(num_circles)]

# GENERATE YOUR PLOTS
p = figure(x_range = (0, 100), y_range = (0, 100))
r = p.circle(x, y, size=5)

# HANDLE CALLBACKS ... user interactions offered in widgets
ds = r.data_source

def add_circle():
    new_data = {}
    new_data['x'] = ds.data['x'] + [random()*70]
    new_data['y'] = ds.data['y'] + [random()*70]

    ds.data = new_data

# CREATE INTERACTIVE WIDGETS
b = Button(label = 'Add circle')
b.on_click(add_circle)

# FORMAT/CREATE THE DOCUMENT TO RENDER
curdoc().add_root(column(b, p))


