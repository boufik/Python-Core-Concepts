# 0. Basics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor

# Set Matplotlib defaults
plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=14,
    titlepad=10,
)



# 1. AUXILIARY FUNCTION ---->
# Input1 = every dataframe "X" to be trained (it may contain categorical cols, but they will be encoded with .factorize()
# Input2 = every Series (1-column dataframe) that acts as a target
# Input3 = the regressor model (default model = XGBRegressor)

def score_dataset(X, y, model=XGBRegressor()):
    # Label encoding for categoricals
    for colname in X.select_dtypes(["category", "object"]):
        X[colname], _ = X[colname].factorize()
    # Metric for Housing competition is RMSLE (Root Mean Squared Log Error)
    score = cross_val_score(
        model, X, y, cv=5, scoring="neg_mean_squared_log_error",
    )
    score = -1 * score.mean()
    score = np.sqrt(score)
    return score



# 2. Prepare data - Evaluate performance
df = pd.read_csv("../input/fe-course-data/ames.csv")
X = df.copy()
y = X.pop("SalePrice")
print(score_dataset(X, y))



# 3. 5D kmeans algorithm ----> Create a Feature of Cluster Labels ----> New "Cluster" column

# 3a. Select the 5 features to be clustered
features = ["LotArea", "TotalBsmtSF", "FirstFlrSF", "SecondFlrSF", "GrLivArea"]
# 3b. Standardize them
X_scaled = X[features]                                  # The new temporary dataframe contains only these 5 columns-features
X_scaled = (X_scaled - X_scaled.mean(axis=0)) / X_scaled.std(axis=0)    # mean, std are methods applied to a whole dataframe
# 3c. Create and apply the kmeans algorithm
kmeans = KMeans(n_clusters=10, n_init=10, random_state=0)
X["Cluster"] = kmeans.fit_predict(X_scaled)								# A 1-column dataframe (Series) with column name = "Cluster"
X["Cluster"] = X["Cluster"].astype("category")
print(X[features + ["Cluster"]].head(8))
print(score_dataset(X, y))



# 4. Create relplots to see better the relation between the 5 features and the target
X2 = X.copy()                                   # Since X2 is a copy of X, then X2 dataframe contains "Cluster", but not "SalePrice"
X2["Cluster"] = X2.Cluster.astype("category")
X2["SalePrice"] = y								# Merge the target column
sns.relplot(
    x="value", y="SalePrice", hue="Cluster", col="variable",
    height=4, aspect=1, facet_kws={'sharex': False}, col_wrap=3,
    data=X2.melt(
        value_vars=features, id_vars=["SalePrice", "Cluster"],
    ),
);



# 5. Cluster-Distance Features: The k-means algorithm offers an alternative way of creating features. Instead of labelling each feature
# with the nearest cluster centroid, it can measure the distance from a point to all the centroids and return those distances as
# features. We use "fit_transform" to do so, not "fit_predict" method

kmeans = KMeans(n_clusters=10, n_init=10, random_state=0)
X_cd = kmeans.fit_transform(X_scaled)							  # A 10-column dataframe with elements = distances from centroids
centroid_cols = [f"Centroid_{i}" for i in range(X_cd.shape[1])]
X_cd = pd.DataFrame(X_cd, columns=centroid_cols)
X = X.join(X_cd)
print(X[features + centroid_cols].head(8))
print(score_dataset(X, y))
