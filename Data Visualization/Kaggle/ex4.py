import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns


# 1. Read the dataset
candy_filepath = "../input/candy.csv"
candy_data = pd.read_csv(candy_filepath, index_col="id")
print(candy_data.head())

# Which candy was more popular with survey respondents: '3 Musketeers' or 'Almond Joy'? 
more_popular = '3 Musketeers'
# Which candy has higher sugar content: 'Air Heads' or 'Baby Ruth'?
more_sugar = 'Air Heads'

# 2. Sugar vs Win ----> Scatter and regression line plot
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

# 3. Sugar vs Win vs Chocolate ----> Scatter and regression line plot (lmplot)
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])
sns.lmplot(data=candy_data, x="pricepercent", y="winpercent", hue="chocolate")

# 4. Chocolate vs Win
sns.swarmplot(x=candy_data["chocolate"], y=candy_data["winpercent"])
