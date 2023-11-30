import streamlit as st
import pandas as pd
import numpy as np
from PercolationStats import PercolationStats
import plot_utils
import streamlit.components.v1 as components
import json

st.set_page_config(page_title='Monte Carlo Simulation', layout='wide')
st.title(plot_utils.titles[1])
# create an empty dataframe to append runs
if "data" not in st.session_state:
    data = pd.DataFrame(columns=plot_utils.data_columns)
    st.session_state['data'] = data


def new_filename():
    st.session_state['filename'] = plot_utils.pick_random_file()


if "filename" not in st.session_state:
    new_filename()


@st.cache_data
def run_new_simulation(nrows, ncols, trials):
    pstats = PercolationStats(nrows, ncols, trials)
    pstats.run_simulation()
    df_new = pd.DataFrame([[nrows, ncols, trials,
                            pstats.mean(),
                            pstats.stddev(),
                            pstats.confidenceLo(),
                            pstats.confidenceHi()
                            ]], columns=plot_utils.data_columns)
    st.session_state.data = pd.concat(
        [st.session_state.data, df_new], axis=0)


col1, col2 = st.columns((3, 3))
with col1:
    st.write(plot_utils.titles[2])
    pick = st.button(label="Pick a random file")
    if pick:
        new_filename()
        st.write("{}".format(st.session_state['filename']))
        st.plotly_chart(plot_utils.create_heatmap(
            st.session_state['filename']), use_container_width=True)
with col2:
    st.write(plot_utils.titles[3])
    st.latex(plot_utils.equations[1])
    st.write(plot_utils.titles[4])
    st.latex(plot_utils.equations[2])
    st.latex(plot_utils.equations[3])


nRows = st.number_input(
    'Number of rows', min_value=5, step=5)
nCols = st.number_input(
    'Number of cols', min_value=5, step=5)
nTrials = st.number_input(
    'Number of trials', min_value=30, step=10)
add = st.button(label="Add simulation")
if add:
    run_new_simulation(nRows, nCols, nTrials)
    st.dataframe(st.session_state.data)


st.header("The references")
st.markdown(""" <a href="https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php">Princeton Algorithms I-Assigment 1</a> """,
            unsafe_allow_html=True)
st.header("Source code")

'''
    [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/YagmurGULEC/MonteCarloSimulationWithStreamlit) 

'''
st.markdown("<br>", unsafe_allow_html=True)
