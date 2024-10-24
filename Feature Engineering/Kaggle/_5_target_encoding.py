# 0a. Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
from category_encoders import MEstimateEncoder
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor

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
warnings.filterwarnings('ignore')



# 1. AUXILIARY FUNCTIONS
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



# 2. Basics - Inspect the categorical columns
df = pd.read_csv("../input/fe-course-data/ames.csv")
print(df.select_dtypes(["object"]).nunique())
print(df["SaleType"].value_counts())



# 3. Target encoding - Split the dataset to AVOID OVERFITTING
# 3a. Encoding split
X_encode = df.sample(frac=0.20, random_state=0)
y_encode = X_encode.pop("SalePrice")
# 3b. Training split
X_pretrain = df.drop(X_encode.index)
y_train = X_pretrain.pop("SalePrice")



# 4. MEstimatorEncoder
# 4a. Create the encoder
from category_encoders import MEstimateEncoder
features = ["Neighborhood", "SaleType"]
encoder = MEstimateEncoder(cols=features, m=5)
# 4b. Fit the encoder on the encoding split
encoder.fit(X_encode, y_encode)
# 4c. Encode the training split
X_train = encoder.transform(X_pretrain, y_train)



# 5. See how the encoded feature compares to the target
encoder_cols = encoder.cols
print(encoder_cols)
plt.figure(dpi=90)
ax = sns.distplot(y_train, kde=True, hist=False)
ax = sns.distplot(X_train[feature], color='r', ax=ax, hist=True, kde=False, norm_hist=True)
ax.set_xlabel("SalePrice")



# 6. Compare scores
X = df.copy()
y = X.pop("SalePrice")
score_base = score_dataset(X, y)
score_new = score_dataset(X_train, y_train)
print(f"Baseline Score: {score_base:.4f} RMSLE")
# All categorical cols were label-encoded because of score_dataset function
print(f"Score with Encoding: {score_new:.4f} RMSLE")
# All categorical cols were label-encoded because of score_dataset function, but 2 of them ("SaleType" and "Neighborhood" were
# target-encoded, even in a smaller proportion of the dataset, but this yields a better result in our performance metric



# 7. Non-sense feature allegedly results in a better RMSLE, but this because of OVERFITTING (we did not split the dataset)
# 7A. We can try 0, 1, 5, 50
m = 0
X = df.copy()
y = X.pop('SalePrice')
# 7b. Create an UNINFORMATIVE feature
X["Count"] = range(len(X))
X["Count"][1] = 0  # actually need one duplicate value to circumvent error-checking in MEstimateEncoder
# 7c. Fit and transform on the same dataset
encoder = MEstimateEncoder(cols="Count", m=m)
X = encoder.fit_transform(X, y)
score =  score_dataset(X, y)
print(f"Score: {score:.4f} RMSLE")

plt.figure(dpi=90)
ax = sns.distplot(y, kde=True, hist=False)
ax = sns.distplot(X["Count"], color='r', ax=ax, hist=True, kde=False, norm_hist=True)
ax.set_xlabel("SalePrice");
