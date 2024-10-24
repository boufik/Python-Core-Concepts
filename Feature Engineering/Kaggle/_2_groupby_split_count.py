# 0a. Import
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor



# 1. AUXILIARY FUNCTIONS
def score_dataset(X, y, model=XGBRegressor()):
    # 1a. Label encoding for categoricals
    for colname in X.select_dtypes(["category", "object"]):
        X[colname], _ = X[colname].factorize()
    # 1b. Metric for Housing competition is RMSLE (Root Mean Squared Log Error)
    score = cross_val_score(
        model, X, y, cv=5, scoring="neg_mean_squared_log_error",
    )
    score = -1 * score.mean()
    score = np.sqrt(score)
    return score


# 2. Prepare data
df = pd.read_csv("../input/fe-course-data/ames.csv")
X = df.copy()
y = X.pop("SalePrice")


# 3. Create 3 new features
X_1 = pd.DataFrame()
X_1["LivLotRatio"] = X["GrLivArea"] / X["LotArea"]
X_1["Spaciousness"] = (X["FirstFlrSF"] + X["SecondFlrSF"]) / X["TotRmsAbvGrd"]
X_1["TotalOutsideSF"] = X["WoodDeckSF"] + X["OpenPorchSF"] + X["EnclosedPorch"] + X["Threeseasonporch"] + X["ScreenPorch"]



# 4. One hot encoding
# 4a. One-hot encode the column named "BldgType" ---> Use `prefix="Bldg"` in `get_dummies` ---> New columns will be named "Bldg.....", # where "...." stands for the categorical value
X_2 = pd.get_dummies(df.BldgType, prefix="Bldg")
print(X_2.head(5), '\n\n')
# 4b. Multiply by "GrLivArea" (row-by-row)
X_2 = X_2.mul(df.GrLivArea, axis=0)            # Data type of "X_2" = pandas.Series, so that I can perform the multiplication X_2.mul # # ("mul" is a pd.Series method)
print(X_2.head(5))



# 5. Count how many kinds of outdoor areas are greater than 0.0
X_3 = pd.DataFrame()
X_3["PorchTypes"] = X[["WoodDeckSF", "OpenPorchSF", "EnclosedPorch", "Threeseasonporch", "ScreenPorch"]].gt(0.0).sum(axis=1)
print(X[["WoodDeckSF", "OpenPorchSF", "EnclosedPorch", "Threeseasonporch", "ScreenPorch"]].head(5))
print(X_3.head(5))



# 6. Breaking down a categorical feature by splitting
print(df.MSSubClass.unique())
X_4 = pd.DataFrame()
X_4["MSClass"] = X["MSSubClass"].str.split("_", n=1, expand=True)[0]



# 7. Grouped Transform
X_5 = pd.DataFrame()
X_5["MedNhbdArea"] = X.groupby("Neighborhood")["GrLivArea"].transform("median")



# 8. Join new datasets in the original one and compare the performances
X_new = X.join([X_1, X_2, X_3, X_4, X_5])
print(score_dataset(X, y))
print(score_dataset(X_new, y))
