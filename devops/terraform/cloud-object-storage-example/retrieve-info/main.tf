data "ibm_resource_group" "cos_group" {
  name = "Default"
}

data "ibm_resource_instance" "cos_instance" {
  name              = "streaming-demo-cos"
  resource_group_id = "${data.ibm_resource_group.cos_group.id}"
  service           = "cloud-object-storage"
}

data "ibm_cos_bucket" "standard-ams03" {
  bucket_name = "test-i-am-a-test-bucket"
  resource_instance_id = "${data.ibm_resource_instance.cos_instance.id}"
  bucket_type = "cross_region_location"
  bucket_region = "eu"
}

output "bucket_private_endpoint" {
  value = "${data.ibm_cos_bucket.standard-ams03.s3_endpoint_private}"
}