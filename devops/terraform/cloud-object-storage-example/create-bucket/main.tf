data "ibm_resource_group" "cos_group" {
  name = "Default"
}

resource "ibm_resource_instance" "cos_instance" {
  name              = "streaming-demo-cos"
  resource_group_id = "${data.ibm_resource_group.cos_group.id}"
  service           = "cloud-object-storage"
  plan              = "lite"
  location          = "global"
}

resource "ibm_cos_bucket" "standard-my-custom-demo-bucket" {
  bucket_name = "zt-a-standard-my-custom-demo-bucket"
  resource_instance_id = "${ibm_resource_instance.cos_instance.id}"
  #bucket_type = "cross_region_location"
  cross_region_location = "eu"
  storage_class = "standard"
}

resource "ibm_cos_bucket" "standard-my-custom-demo-bucket2" {
  bucket_name = "zt-a-standard-my-custom-demo-bucket2"
  resource_instance_id = "${ibm_resource_instance.cos_instance.id}"
  #bucket_type = "cross_region_location"
  cross_region_location = "eu"
  storage_class = "standard"
}

resource "ibm_resource_key" "cos_service_credential" {
  name = "cos_service_credential"
  role = "Writer"
  resource_instance_id = "${ibm_resource_instance.cos_instance.id}"

  parameters = {
    "HMAC" = true
  }
}