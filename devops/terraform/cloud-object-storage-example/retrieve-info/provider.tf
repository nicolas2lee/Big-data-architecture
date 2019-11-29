variable "ibmcloud_api_key" {
  default  = "<api-key>"
}

provider "ibm" {
  ibmcloud_api_key   = "${var.ibmcloud_api_key}"
  generation         = 1
  region             = "us-south"
}


