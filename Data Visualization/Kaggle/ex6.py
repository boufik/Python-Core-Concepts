import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns


# 1. Read the dataset
spotify_filepath = "../input/spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# 2. Set the desired style. Choices are: "white", "whitegrid", "dark", "darkgrid", "ticks"
sns.set_style("darkgrid")
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
