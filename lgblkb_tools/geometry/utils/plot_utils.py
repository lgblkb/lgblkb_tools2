import pandas as pd
import matplotlib.pyplot as plt
import shapely.geometry as shg
from matplotlib.collections import PatchCollection


def plot_polygon(polygon: shg.Polygon, label=None, ax=None, name='', **kwargs):
    if ax is None:
        plot = plt.plot
    else:
        plot = ax.plot
    default_opts = dict(lw=3)
    if label is None:
        labeler = lambda l: dict(default_opts, label=l)
    else:
        labeler = lambda l: dict(default_opts, label='{} {}'.format(label, l))
    plotter = lambda linestring, _label: plot(*linestring.xy, **dict(labeler(_label), **kwargs))
    plotter(polygon.exterior, 'exterior')
    if name:
        x, y = polygon.exterior.xy
        target_point_index = list(x).index(min(x))

        plt.text(x[target_point_index], y[target_point_index], s=name)
    for i, p_i in enumerate(polygon.interiors):
        plotter(p_i, 'interior {}'.format(i))


def plot_patches(polygons, ax=None, c=None, **kwargs):
    if ax is None: ax = plt.gca()
    if isinstance(polygons, pd.Series):
        pcol = PatchCollection(polygons.map(lambda p: shg.Polygon(p.exterior)), **kwargs)
    else:
        poly_objs = [shg.Polygon(x.exterior) for x in polygons]
        pcol = PatchCollection(poly_objs, **kwargs)
    if c: pcol.set_color(c)
    ax.add_collection(pcol)
