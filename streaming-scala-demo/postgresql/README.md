psql 'host=dbaas905.hyperp-dbaas.cloud.ibm.com port=28022 sslmode=verify-full sslrootcert=/Users/xinrui/tao/ibmcloud_projects/streaming-scala-demo/postgresql/cert/cert.pem user=admin password=<password>'


\COPY student FROM '/Users/xinrui/tao/ibmcloud_projects/streaming-scala-demo/postgresql/sqlloader/data.csv' WITH (FORMAT csv);
 
 
