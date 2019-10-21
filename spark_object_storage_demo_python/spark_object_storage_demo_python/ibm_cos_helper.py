from ibm_botocore.client import Config, ClientError
import ibm_boto3
from ibm_s3transfer.aspera.manager import AsperaTransferManager, AsperaConfig

#https://cloud.ibm.com/docs/services/cloud-object-storage/libraries?topic=cloud-object-storage-python#using-python
def get_item(cos, bucket_name, item_name):
    print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
    try:
        file = cos.Object(bucket_name, item_name).get()
        print("File Contents: {0}".format(file["Body"].read()))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))

def get_buckets(cos):
    print("Retrieving list of buckets")
    try:
        buckets = cos.buckets.all()
        for bucket in buckets:
            print("Bucket Name: {0}".format(bucket.name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))

def get_data():
    COS_ENDPOINT = "https://s3.eu.cloud-object-storage.appdomain.cloud"  # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
    COS_API_KEY_ID = "phWenEzTBmpBfuluOeGpVZ2vJD6J6YOtwvPdKtYWFZ2-"  # eg "W00YiRnLW4a3fTjMB-oiB-2ySfTrFBIQQWanc--P3byk"
    COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
    COS_RESOURCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/22a5864ba3754cf0a274ba36ea94a358:72601e19-4b09-4f8c-8bf5-757c0c2eddfb::"  # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003abfb5d29761c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"
    cos = ibm_boto3.resource("s3",
                             ibm_api_key_id=COS_API_KEY_ID,
                             ibm_service_instance_id=COS_RESOURCE_CRN,
                             ibm_auth_endpoint=COS_AUTH_ENDPOINT,
                             config=Config(signature_version="oauth"),
                             endpoint_url=COS_ENDPOINT
                             )
    BUCKET_NAME = "zt-fraud-detection"
    FILE_PREFIX= "resource"
    train_identity = "ieee-fraud-detection/train_identity.csv"
    train_transaction = "ieee-fraud-detection/train_transaction.csv"
    test_identity = "ieee-fraud-detection/test_identity.csv"
    test_transaction = "ieee-fraud-detection/test_transaction.csv"
    ms_transfer_config = AsperaConfig(multi_session="all",
                                      target_rate_mbps=2500,
                                      multi_session_threshold_mb=100)
    transfer_manager = AsperaTransferManager(client=cos, config=ms_transfer_config)

    transfer_manager.download(BUCKET_NAME, train_identity, "{}/{}".format(FILE_PREFIX, train_identity))
    transfer_manager.download(BUCKET_NAME, train_transaction, "{}/{}".format(FILE_PREFIX, train_transaction))
    transfer_manager.download(BUCKET_NAME, test_identity, "{}/{}".format(FILE_PREFIX, test_identity))
    transfer_manager.download(BUCKET_NAME, test_transaction, "{}/{}".format(FILE_PREFIX, test_transaction))