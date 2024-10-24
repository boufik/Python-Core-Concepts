import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
 
# 0. Read the data
my_filepath = "/kaggle/input/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"
my_data = pd.read_csv(my_filepath, index_col="page_id")
print(my_data.head())
print(my_data.shape)
 
# 1. KDE: Distribution of appearances
print("Average appearances in original data =", my_data["APPEARANCES"].mean(), end='\n\n')
sns.kdeplot(data=my_data, x="APPEARANCES", fill=True)
plt.title("Original Data: Heroes appearances density function")
plt.show()
 
# 2. KDE while filtering: Keep the rows, where APPEARANCES <= 50 ---> A new dataframe is created
new_data = my_data[my_data["APPEARANCES"] <= 50]
print("Average appearances in filtered data =", new_data["APPEARANCES"].mean(), end='\n\n')
sns.kdeplot(data=new_data, x="APPEARANCES", fill=True)
plt.title("Filtered data: Heroes appearances density function")
plt.show()
 
# 3. Joint plot: 2D-KDE
sns.jointplot(data=my_data, x="YEAR", y="APPEARANCES", kind="kde")
# plt.title("2D-KDE: Year vs Appearances")
plt.show()
sns.jointplot(data=my_data, x="YEAR", y="APPEARANCES", kind="hist")
# plt.title("2D-HIST: Year vs Appearances")
plt.show()
 
# 4. Scatter plot to reveal the relation between year, appearances and ID
sns.scatterplot(x=my_data['YEAR'], y=my_data['APPEARANCES'])
plt.title("Relation between: year and appearances")
plt.show()
sns.scatterplot(x=my_data['YEAR'], y=my_data['APPEARANCES'], hue=my_data['ID'])
plt.title("Relation between: year, appearances and ID")
plt.show()
 
df1 = my_data[my_data['ID'] == 'Secret Identity']
df2 = my_data[my_data['ID'] == 'Public Identity']
df3 = my_data[my_data['ID'] == 'Identity Unknown']
SUM1 = df1.shape[0]
SUM2 = df2.shape[0]
SUM3 = df3.shape[0]
SUM = my_data.shape[0]
print("Heroes with Secret Identity  = {}/{}".format(SUM1, SUM))
print("Heroes with Public Identity  = {}/{}".format(SUM2, SUM))
print("Heroes with Identity Unknown = {}/{}".format(SUM3, SUM))
