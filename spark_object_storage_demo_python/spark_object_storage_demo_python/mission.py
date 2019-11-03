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

    Y_train = transaction_train_df_raw['isFraud']
    X_train = transaction_train_df_raw.drop('isFraud', axis=1)  # 506691



    num_test = 0.20
    X_all = transaction_train_df_raw.drop('isFraud', axis=1)
    Y_all = transaction_train_df_raw['isFraud']
    X_train, X_test, Y_train, Y_test = train_test_split(X_all, Y_all, test_size=num_test)



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

    X_train_after_processing = preprocessor_pipeline.fit_transform(X_train)

    model = RandomForestClassifier(n_estimators=100, random_state=0)
    my_pipeline = Pipeline(steps=[('preprocessor', preprocessor_pipeline), ('model', model)])

    # Preprocessing of training data, fit model
    # my_pipeline.fit(X_train, Y_train)
    my_pipeline.fit(X_train, Y_train)

    # Preprocessing of validation data, get predictions
    preds = my_pipeline.predict(X_test)
    #ibm_cos.get_data()
    # conf = SparkConf().set("spark.jars", "/path-to-jar/spark-streaming-kafka-0-8-assembly_2.11-2.2.1.jar")
    # sc = SparkContext(conf=conf)
    # hconf = sc._jsc.hadoopConfiguration()
    # hconf.set("fs.cos.impl", "com.ibm.stocator.fs.ObjectStoreFileSystem")
    #
    # hconf.set("fs.stocator.scheme.list", "cos")
    # hconf.set("fs.stocator.cos.impl", "com.ibm.stocator.fs.cos.COSAPIClient")
    # hconf.set("fs.stocator.cos.scheme", "cos")
    #
    # hconf.set("fs.cos.service.endpoint", "http://s3.eu.cloud-object-storage.appdomain.cloud")
    # hconf.set("fs.cos.service.access.key","5a82b5387e164d2695c537e9bc0ff628")
    # hconf.set("fs.cos.service.secret.key","dd499706946be78e4a981b36183773b1de0d61078545b5de")
    # train_transaction = sc.textFile("cos://zt-fraud-detection.service/ieee-fraud-detection/train_transaction.csv")
    # train_transaction.foreach(print)

