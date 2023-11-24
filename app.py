import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


nRows = st.number_input(
    'Number of rows', min_value=5, step=5)
nCols = st.number_input(
    'Number of cols', min_value=5, step=5)

open = [0]*nRows
for row in range(nRows):
    open[row] = [0]*nCols

open[0][0] = 1
open[1][0] = 0.5
fig = go.Figure(data=go.Heatmap(z=open, colorscale='gray',
                                hoverinfo='text', showscale=False, xgap=3, ygap=3))

st.plotly_chart(fig, use_container_width=True)

