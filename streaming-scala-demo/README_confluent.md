./bin/zookeeper-server-start ./etc/kafka/zookeeper.properties 

 ./bin/kafka-server-start ./etc/kafka/server.properties


 ./bin/schema-registry-start ./etc/schema-registry/schema-registry.properties
 
 
 
 ./bin/kafka-topics --zookeeper localhost:2181 --create --topic test \
    --partitions 1 --replication-factor 1
    
./bin/control-center-start ./etc/confluent-control-center/control-center.properties
