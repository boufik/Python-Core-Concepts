# 0a. Import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import mutual_info_regression

# 0b. Set Matplotlib defaults
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



# 1. AUXILIARY FUNCTIONS
def make_mi_scores(X, y):

    X = X.copy()
    for colname in X.select_dtypes(["object", "category"]):
        X[colname], _ = X[colname].factorize()
	# All discrete features should now have integer dtypes
    discrete_features = [pd.api.types.is_integer_dtype(t) for t in X.dtypes]

    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features, random_state=0)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores


def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")




# 2. Load data and make some "rel" plots inline
df = pd.read_csv("../input/fe-course-data/ames.csv")
features = ["YearBuilt", "MoSold", "ScreenPorch"]
sns.relplot(
    x="value", y="SalePrice", col="variable", data=df.melt(id_vars="SalePrice", value_vars=features), facet_kws=dict(sharex=False),
);
# sns.relplot(data=df, x="YearBuilt", y="SalePrice")
# plt.show()



# 3. Discover the MI scores
X = df.copy()
y = X.pop('SalePrice')
mi_scores = make_mi_scores(X, y)
print(mi_scores.head(10))
print(mi_scores.tail(10))
plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores.head(10))
plot_mi_scores(mi_scores.tail(10))




# 4. An "outsider" feature named "BldgType" - with not a high value of MI - seems to interact well and have some type
# of relation with a variable ("GrLivArea") that is very high in MI scores

sns.catplot(x="BldgType", y="SalePrice", data=df, kind="boxen");


feature = "GrLivArea"
sns.lmplot(
    x=feature, y="SalePrice", hue="BldgType", col="BldgType",
    data=df, scatter_kws={"edgecolor": 'w'}, col_wrap=3, height=4,
);


feature = "MoSold"
sns.lmplot(
    x=feature, y="SalePrice", hue="BldgType", col="BldgType",
    data=df, scatter_kws={"edgecolor": 'w'}, col_wrap=3, height=4,
);
