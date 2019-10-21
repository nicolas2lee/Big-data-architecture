import pyspark.sql.functions as F
from pyspark import SparkConf, SparkContext

import spark_object_storage_demo_python.ibm_cos_helper as ibm_cos
from ibm_s3transfer.aspera.manager import AsperaTransferManager, AsperaConfig


def with_life_goal(df):
    return df.withColumn("life_goal", F.lit("escape!"))



if __name__ == '__main__':

    ibm_cos.get_data()
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

