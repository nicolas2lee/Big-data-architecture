#Spark

## build docker image
    ./bin/docker-image-tool.sh -r <repo> -t my-tag build
    ./bin/docker-image-tool.sh -r <repo> -t my-tag push
    
    ./bin/docker-image-tool.sh -r nicolas2lee -t 2.4.3  build
    ./bin/docker-image-tool.sh -r nicolas2lee -t 2.4.3  push
 
## spark execution in kubernetes

Command template

    bin/spark-submit \
        --master k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port> \
        --deploy-mode cluster \
        --name spark-pi \
        --class org.apache.spark.examples.SparkPi \
        --conf spark.executor.instances=5 \
        --conf spark.kubernetes.container.image=<spark-image> \
        local:///path/to/examples.jar   
    
To get kubernetes master ip addr & port 

    kubectl cluster-info
To configure your spark job jar, this path is the path of your jar in all pods

    local:///path/to/examples.jar 
    
Also should configure service account in kubernetes, otherwise some error messages will appear:

    Caused by: io.fabric8.kubernetes.client.KubernetesClientException: 
    Failure executing: GET at: https://kubernetes.default.svc/api/v1/namespaces/default/pods/spark-pi-1559473692540-driver. 
    Message: Forbidden!Configured service account doesn't have access. Service account may have been revoked. 
    pods "spark-pi-1559473692540-driver" is forbidden: User "system:serviceaccount:default:default" cannot get pods in the namespace "default"      
Check service account and clusterrolebinding:
    
    kubectl get serviceaccount
    
    kubectl get clusterrolebinding
    
    kubectl create serviceaccount spark
    
    kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default
     
    kubectl get serviceaccount
    
Command:
        
    bin/spark-submit \
        --master k8s://https://192.168.99.100:8443 \
        --deploy-mode cluster \
        --name spark-pi \
        --class org.apache.spark.examples.SparkPi \
        --conf spark.executor.instances=1 \
        --conf spark.executor.memory=512M \
        --conf spark.executor.core=256M \
        --conf spark.driver.core=256M \
        --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark  \
        --conf spark.kubernetes.container.image=nicolas2lee/spark:2.4.3 \
        local:///opt/spark/examples/jars/spark-examples_2.11-2.4.3.jar

Memory & CPU issue

By default, the spark job takes 1g RAM & 1 cpu, so if you run locally, should be attention with number of instances

The minimum memory of each executor node should be 450M

Executor memory 134217728 must be at least 471859200        

    minikube start --memory 2048 --cpus 4  