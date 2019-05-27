#Kafka
## launch producer & consumer in kubernetes

    bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test
    
    bin/kafka-topics.sh --list --zookeeper zookeeper:2181
    
    bin/kafka-console-producer.sh --broker-list kafka-server-cluster-0:9092,kafka-server-cluster-1:9092 --topic test
    
    bin/kafka-console-consumer.sh  --bootstrap-server kafka-server-cluster-0:9092 --topic test --from-beginning

## launch producer & consumer externally

    bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test
    
    bin/kafka-topics.sh --list --zookeeper zookeeper:2181
    
    bin/kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic test

## communicate with kafka deployed in kubernetes externally 

https://argus-sec.com/external-communication-with-apache-kafka-deployed-in-kubernetes-cluster/
    
In kubernetes with cluster ip

    bin/kafka-console-producer.sh --broker-list kafka-server-cluster-0:9092 --topic test
            
    bin/kafka-console-consumer.sh  --bootstrap-server kafka-server-cluster-1:9092 --topic test --from-beginning

    bin/kafka-console-producer.sh --broker-list 192.168.99.100:32321 --topic test
        
    bin/kafka-console-consumer.sh  --bootstrap-server 192.168.99.100:32321 --topic test --from-beginning
    
    bin/kafka-console-consumer.sh  --bootstrap-server 192.168.99.100:32321 --topic test --from-beginning
