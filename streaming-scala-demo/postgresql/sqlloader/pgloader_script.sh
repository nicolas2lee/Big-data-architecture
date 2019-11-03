pgloader -v  \
         --type csv                                   \
         --field "id,name,email"                  \
         --with truncate                              \
         --with "fields terminated by ','"            \
         ./data.csv                   \
         'host=dbaas905.hyperp-dbaas.cloud.ibm.com port=28022 sslmode=verify-full sslrootcert=/Users/xinrui/tao/ibmcloud_projects/streaming-scala-demo/postgresql/cert/cert.pem user=admin password=<should-replace-by-password>'

