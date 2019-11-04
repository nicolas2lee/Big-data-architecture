import pyspark.sql.functions as F

#import spark_object_storage_demo_python.ibm_cos_helper as ibm_cos
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import category_encoders as ce
from sklearn_pandas import DataFrameMapper

def with_life_goal(df):
    return df.withColumn("life_goal", F.lit("escape!"))


if __name__ == '__main__':

    FILE_PREFIX = "../resource/ieee-fraud-detection"

    train_identity = "train_identity.csv"
    train_transaction = "train_transaction.csv"
    test_identity = "test_identity.csv"
    test_transaction = "test_transaction.csv"

    identity_train_df = pd.read_csv("{}/{}".format(FILE_PREFIX, train_identity))
    transaction_train_df_raw = pd.read_csv("{}/{}".format(FILE_PREFIX, train_transaction))

    identity_test_df = pd.read_csv("{}/{}".format(FILE_PREFIX, test_identity))
    X_final = pd.read_csv("{}/{}".format(FILE_PREFIX, test_transaction))
    print("===============finish file loading=================")
    Y_train = transaction_train_df_raw['isFraud']
    X_train = transaction_train_df_raw.drop('isFraud', axis=1)  # 506691

    # num_test = 0.20
    # X_all = transaction_train_df_raw.drop('isFraud', axis=1)
    # Y_all = transaction_train_df_raw['isFraud']
    # X_train, X_test, Y_train, Y_test = train_test_split(X_all, Y_all, test_size=num_test)

    # Preprocessing for numerical data
    numerical_transformer = SimpleImputer(strategy='mean')
    # Preprocessing for categorical data
    # to implment addr2, divide into 2 categories, then one hot enconding
    onehot_categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', ce.OneHotEncoder())
    ])

    binary_categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('binary', ce.BinaryEncoder(drop_invariant=False))
    ])

    ordinary_categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('ordinary', ce.OrdinalEncoder())
    ])

    # Bundle preprocessing for numerical and categorical data
    preprocessor_pipeline = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, ['TransactionDT', 'TransactionAmt', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'D1', 'D4', 'D10', 'D15']),
            ('onehot_cat', onehot_categorical_transformer, ['ProductCD', 'card4', 'M6']),
            #         ('onehot_cat', onehot_categorical_transformer, ['ProductCD', 'card4', 'card6', 'M6']),
            #        binary encoder did not work, should re implement
            #        ('binary_cat', binary_categorical_transformer, ['card3', 'card5', 'addr1', 'addr2']),
            ('binary_cat', binary_categorical_transformer, ['P_emaildomain']),
            ('ordinary_cat', ordinary_categorical_transformer, ['card1', 'card2'])

        ])

    # dataFrameMapper = DataFrameMapper([
    #         (['TransactionDT', 'TransactionAmt', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'D1', 'D4', 'D10', 'D15'], numerical_transformer),
    #         (['ProductCD', 'card4', 'M6'], onehot_categorical_transformer),
    #         #         ('onehot_cat', onehot_categorical_transformer, ['ProductCD', 'card4', 'card6', 'M6']),
    #         #        binary encoder did not work, should re implement
    #         #        ('binary_cat', binary_categorical_transformer, ['card3', 'card5', 'addr1', 'addr2']),
    #         (['P_emaildomain'], binary_categorical_transformer ),
    #         (['card1', 'card2'], ordinary_categorical_transformer)
    #     ]
    # )
    X_train_after_processing = preprocessor_pipeline.fit_transform(X_train)
    model = RandomForestClassifier(n_estimators=100, random_state=0)
    #my_pipeline = Pipeline(steps=[('preprocessor', preprocessor_pipeline), ('model', model)])

    # Preprocessing of training data, fit model
    # my_pipeline.fit(X_train, Y_train)
    #my_pipeline.fit(X_train, Y_train)

    from sklearn2pmml.pipeline import PMMLPipeline

    pipeline = PMMLPipeline([
        #("preprocessing", dataFrameMapper),
        ("classifier", model)
    ])
    pipeline.fit(X_train_after_processing, Y_train)

    from sklearn2pmml import sklearn2pmml

    sklearn2pmml(pipeline, "model.pmml", with_repr=True)

    # Preprocessing of validation data, get predictions
    #preds = my_pipeline.predict(X_test)