package tao

import org.apache.spark.{SparkConf, SparkContext}

object Application {


  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("testApp").setMaster("local[*]")
    var sc = new SparkContext(conf)

    var hconf = sc.hadoopConfiguration
    hconf.set("fs.cos.impl", "com.ibm.stocator.fs.ObjectStoreFileSystem")

    hconf.set("fs.stocator.scheme.list", "cos")
    hconf.set("fs.stocator.cos.impl", "com.ibm.stocator.fs.cos.COSAPIClient")
    hconf.set("fs.stocator.cos.scheme", "cos")

    hconf.set("fs.cos.service.endpoint", "http://s3.eu.cloud-object-storage.appdomain.cloud")
    hconf.set("fs.cos.service.access.key","5a82b5387e164d2695c537e9bc0ff628")
    hconf.set("fs.cos.service.secret.key","dd499706946be78e4a981b36183773b1de0d61078545b5de")
    val rdd =sc.textFile("cos://zt-fraud-detection.service/sample_submission.csv")
    rdd.collect.foreach(println)
  }
}





