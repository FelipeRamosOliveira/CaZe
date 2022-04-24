import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


class Preprocessor:
    def __init__(self, df):
        self.__df = df

    def transformer(self):
        X = self.__df

        categoric = [cname for cname in X.columns if X[cname].nunique(
        ) < 50 and X[cname].dtype == "object"]
        numerical = [cname for cname in X.columns if X[cname].dtype in [
            'int64', 'float64']]

        numerical_transformer = SimpleImputer(strategy='constant')
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False))])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, numerical),
                ('cat', categorical_transformer, categoric)])

        return(preprocessor)


class SelectModel:

    def __init__(self, models, X, y, seed, preprocessor):
        self._preprocessor = preprocessor
        self._models = models
        self._seed = seed
        self._X = X
        self._y = y

    def guess_best(self):

        models_names = []
        models_algor = []
        r_square_mean = []
        r_square_stdv = []

        k_fold = KFold(n_splits=10, shuffle=True, random_state=self._seed)

        for model in self._models.items():

            pipe = Pipeline(
                steps=[('preprocessor', self._preprocessor), ('model', model[1])])

            scores = cross_val_score(
                pipe, self._X, self._y, cv=k_fold, scoring="r2")

            models_names.append(model[0])
            models_algor.append(model[1])

            r_square_mean.append(scores.mean())
            r_square_stdv.append(scores.std())

        r_square_mean = np.array(r_square_mean, dtype=np.float)
        r_square_stdv = np.array(r_square_stdv, dtype=np.float)

        return {"model": models_names, 'r_square_mean': r_square_mean, "r_square_stdv": r_square_stdv, "models_algor": models_algor}
