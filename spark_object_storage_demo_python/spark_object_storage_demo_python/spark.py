from pyspark.sql import SparkSession

def get_spark():
    return (SparkSession.builder
                .master("local")
                .appName("spark_object_storage_demo_python")
                .getOrCreate())