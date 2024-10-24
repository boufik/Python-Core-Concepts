import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
print("Setup Complete")
 
"""
# Set up code checking
import os
if not os.path.exists("../input/museum_visitors.csv"):
    os.symlink("../input/data-for-datavis/museum_visitors.csv", "../input/museum_visitors.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex2 import *
print("Setup Complete")
"""
 
 
 
# 1. Read the CSV file
museum_filepath = "../input/museum_visitors.csv"
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)
museum_data.tail()
# How many visitors did the Chinese American Museum receive in July 2018?
ca_museum_jul18 = 2620
# How many more visitors did Avila Adobe receive than the Firehouse Museum?
avila_oct18 = 19280 - 4622
 
 
# 2. Show the lineplots for all the museums and for only 1 museum after that
sns.lineplot(data=museum_data)
sns.lineplot(data=museum_data['Avila Adobe'], label="Avila Adobe")
