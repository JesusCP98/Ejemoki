import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go # Liberia para graficar datos


def funcion():
 x = np.arange(0,10,0.1)
 y = x*np.cos(x)
 fig2 = go.Figure()
 fig2.add_trace(go.Scatter(x=x, y=y, mode='markers'))

 return fig2


 
