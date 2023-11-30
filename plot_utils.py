import os
import random
import glob
from run_test_percolation import test_run_percolation
import numpy as np
import plotly.graph_objects as go


data_columns = ['nRows', 'nCols', 'Trials', 'Mean', 'Std Dev',
                'Confidence Low Interval', 'Confidence High Interval']

empty_dict = dict.fromkeys(data_columns)
data_dict = dict(colorscale='gray', showscale=False, xgap=3, ygap=3)
layout_dict = dict(xaxis_title='Bottom', font=dict(size=20))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(BASE_DIR, 'test_data/percolation/')
titles = {
    1: """
Estimate the value of percolation threshold via Monte Carlo Simulation
""",
    2: """Percolation theory helps describe 
         phenomena where connectivity occurs through a medium. 
         This medium is a random system comprised of n-by-m grid of sites
         and connections between sites. 
         The network can represent a porous material, a network of pipes,
          a social network, or even a computer network. 
         That is why it has applications in various fields, including physics, 
         mathematics, material science, and computer science. 
         To illustrate, the simulation below shows the open sites. 
         The interactive simulation is created to illustrate 
         the open but not full (gray), full(white) and closed sites(black). A site is considered full when there is a connection to at least one of the top sites. 
         The system percolates one of the bottom sites are connected to the top . """,
    3: """The heatmap representation is only one trial. 
         However if sufficiently large number of computations(at least 30) 
         T is performed, the percolation threshold is computed averaging 
         of the fraction of sites opened when the system with n-by-m grid sites is percolated.


     """,
    4: """
To calculate the standard deviation, the following is used. Also, 95 percent confidence interval for the percolation threshold is achieved as follows.
"""
}


equations = {
    1: r'''
   \bar{x}=\frac{x_1+x_2+...+x_T}{T}
    ''',
    2: r'''
   s^2=\frac{(x_1-\bar{x})^2+(x_2-\bar{x})^2+...+(x_T-\bar{x})^2}{T-1}
    ''',
    3: r'''
   \bar{x}\pm \frac{1.96s}{\sqrt{T}}
    '''
}


def pick_random_file():
    t = os.path.join(test_dir, '*.txt')
    filename = random.choice(glob.glob(t))
    return filename


def create_heatmap(test_file):

    p = test_run_percolation(test_file)
    open = np.flip(np.array(p.isOpen)+np.array(p.getIsFull()))
    data = go.Heatmap(z=open, **data_dict)
    title = None
    if p.percolates():
        title = "Percolates"
    else:
        title = "Does not percolate"
    fig = go.Figure(data=data, layout=dict(layout_dict, title=title))
    return fig


