import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
print("Setup Complete")


# 1. Read the data
ign_filepath = "../input/ign_scores.csv"
ign_data = pd.read_csv(ign_filepath, index_col="Platform")
print(list(ign_data.columns))
print(ign_data.head())
print(ign_data.describe())

print(ign_data)
# What is the highest average score received by PC games, for any genre?
high_score = 7.759930
# On the PS Vita platform, which genre has the lowest average score? Put your answer in single quotes
worst_genre = 'Simulation'

# 2. Bar Chart and Heatmap
# Bar chart showing average score for racing games by platform
sns.barplot(x=ign_data.index, y=ign_data['Racing'])
sns.heatmap(data=ign_data, annot=True)
