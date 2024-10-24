# 0. Imports
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns




# **********************************************************************************************
# **********************************************************************************************
# 1. Show trends and changes over time (lineplot) - There is usually a column named "Date"
# **********************************************************************************************
# **********************************************************************************************

# 1.1. Lineplot = Show for all the hotels (first plot) and then for only 1 (second plot)
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)
sns.lineplot(data=museum_data)
sns.lineplot(data=museum_data['Avila Adobe'], label="Avila Adobe")




# **********************************************************************************************
# **********************************************************************************************
# 2. Show Distribution (histplot, kdeplot, jointplot)
# **********************************************************************************************
# **********************************************************************************************

# 2.1. Histplot = Histogram (with or without 'hue' argument)
cancer_data = pd.read_csv(cancer_filepath, index_col="Id")
sns.histplot(data=cancer_data, x="Area (mean)", hue="Diagnosis")

# 2.2. Kdeplot = Smoothed Histogram (with or without 'hue' argument)
cancer_data = pd.read_csv(cancer_filepath, index_col="Id")
sns.kdeplot(data=cancer_data, x="Radius (worst)", hue="Diagnosis")

# 2.3. Jointplot = 2D-KDE plot or 2D-HIST plot (with or without 'kind' argument)
cancer_data = pd.read_csv(cancer_filepath, index_col="Id")
sns.jointplot(data=cancer_data, x="Radius (worst)", y="Area (mean)")
sns.jointplot(data=cancer_data, x="Radius (worst)", y="Area (mean)", kind="hist")
sns.jointplot(data=cancer_data, x="Radius (worst)", y="Area (mean)", kind="kde")




# **********************************************************************************************
# **********************************************************************************************
# 3. Show comparison (barplot, heatmap)
# **********************************************************************************************
# **********************************************************************************************

# 3.1. Barplot = Bar diagram
ign_data = pd.read_csv(ign_filepath, index_col="Platform")
sns.barplot(x=ign_data.index, y=ign_data['Racing'])

# 3.2. Heatmap = Color-coded tiles (with 'annot=True', numbers in tiles are visible)
# ALL THE NUMBERS IN DATAFRAME MUST ARE THE SAME THING: EX: DELAY FOR AIRLINE COMPANY
# EX: ROW1 = 1 (Jan), ROW2 = 2 (Feb), ....
# EX: COL1 = A (AEGEAN), COL2 = B (RYANAIR), ....
# ALL THE NUMBERS ARE DELAYS
ign_data = pd.read_csv(ign_filepath, index_col="Platform")
sns.heatmap(data=ign_data, annot=True)




# **********************************************************************************************
# **********************************************************************************************
# 4. Show relation between 2 or 3 variables (scatterplot, regplot, swarmplot, lmplot)
# **********************************************************************************************
# **********************************************************************************************

# 4.1. Scatterplot - Relation between 2 variables: BOTH CONTINUOUS
candy_data = pd.read_csv(candy_filepath, index_col="id")
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

# 4.2. Regplot - Relation and regression line between 2 variables: BOTH CONTINUOUS
candy_data = pd.read_csv(candy_filepath, index_col="id")
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

# 4.3. Swarmplot - Relation between 2 variables: 1 CONTINUOUS + 1 CATEGORICAL
candy_data = pd.read_csv(candy_filepath, index_col="id")
sns.swarmplot(x=candy_data["chocolate"], y=candy_data["winpercent"])

# 4.4. Scatterplot - Relation between 3 variables: 2 CONTINUOUS + 1 CATEGORICAL (in 'hue' argument)
candy_data = pd.read_csv(candy_filepath, index_col="id")
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])

# 4.5. Lmplot - Relation and regression line between 3 variables: 2 CONTINUOUS + 1 CATEGORICAL (in 'hue' argument)
candy_data = pd.read_csv(candy_filepath, index_col="id")
sns.lmplot(data=candy_data, x="pricepercent", y="winpercent", hue="chocolate")
