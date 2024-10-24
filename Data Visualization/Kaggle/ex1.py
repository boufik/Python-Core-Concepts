import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
 
 
 
# 1. Read the file and show the first 5 and 5 last rows of the dataset
spotify_filepath = "./spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
print(spotify_data.head(), end='\n\n')
print(spotify_data.tail(), end='\n\n')
 
# 2. Plot all the columns: horizontal axis is the date of the songs
plt.figure(figsize=(14,6))
plt.xlabel("Date")
plt.ylabel("Times streamed")
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
sns.lineplot(data=spotify_data)
plt.show()
 
# 3. Plot 3 columns
plt.figure(figsize=(14,6))
plt.xlabel("Date")
plt.ylabel("Times streamed")
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
plt.show()
