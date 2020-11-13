""" Compare WebGL and SVG markers with canvas markers.

This covers all markers supported by scatter. The plots are put in tabs,
so that you can easily switch to compare positioning and appearance.

"""
import random

from bokeh.core.enums import MarkerType
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, Panel, Tabs
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.iris import flowers

source = ColumnDataSource(flowers)

u = lambda: int(random.uniform(0, 255))
n = len(source.data["petal_length"])
colors = [ "#%02x%02x%02x" % (u(), u(), u()) for i in range(0, n) ]
source.data["colors"] = colors

def make_plot(title, marker, backend):
    p = figure(title=title, plot_width=350, plot_height=350, output_backend=backend)
    getattr(p, marker)("petal_length", "petal_width", source=source, color="colors", fill_alpha=0.2, size=12)
    return p

tabs = []
for marker in MarkerType:
    p1 = make_plot(marker, marker, "canvas")
    p2 = make_plot(marker + ' SVG', marker, "svg")
    p3 = make_plot(marker + ' GL', marker, "webgl")
    tabs.append(Panel(child=row(p1, p2, p3), title=marker))

output_file("marker_compare.html", title="Compare regular, SVG, and WebGL markers")

show(Tabs(tabs=tabs))
