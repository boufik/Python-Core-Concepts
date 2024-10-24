import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns


# 1. Read the file
cancer_filepath = "../input/cancer.csv"
cancer_data = pd.read_csv(cancer_filepath, index_col="Id")
print(cancer_data.head())

# In the first five rows of the data, what is the largest value for 'Perimeter (mean)'?
max_perim = 87.46
# What is the value for 'Radius (mean)' for the tumor with Id 8510824?
mean_radius = 9.504

# 2. Histogram containing the 2 values of the class (class="Diagnosis")
sns.histplot(data=cancer_data, x="Area (mean)", hue="Diagnosis")

# 3. KDE plot containing the 2 values of the class (class="Diagnosis")
sns.kdeplot(data=cancer_data, x="Radius (worst)", hue="Diagnosis")

# 4. 2D-KDE plot (jointplot) containing the 2 values of the class (class="Diagnosis")
sns.jointplot(data=cancer_data, x="Radius (worst)", y="Area (mean)")
sns.jointplot(data=cancer_data, x="Radius (worst)", y="Area (mean)", kind="hist")
sns.jointplot(data=cancer_data, x="Radius (worst)", y="Area (mean)", kind="kde")
