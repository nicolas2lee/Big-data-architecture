#Spark

#### spark on kubernetes bug
* https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/issues/591
* https://github.com/kubernetes/kubernetes/issues/82131
* https://andygrove.io/2019/08/apache-spark-regressions-eks/

## build docker image

    
build spark docker image 

    ./bin/docker-image-tool.sh -r nicolas2lee -t 2.4.3_kube  build
    
    ./bin/docker-image-tool.sh -r nicolas2lee -t 2.4.3_kube  push

push to ibm cloud docker registry

    docker push <region>.io/<namespace>/spark:<tag> 

    docker push uk.icr.io/tao-lab1/spark:2.4.3

 
## spark execution in ibm cloud kubernetes

### prerequisites

#### local spark distribution
Need spark local distribution to submit spark job
#### RBAC Authorization 
creation service account & cluster role binding

    kubectl get serviceaccount

    kubectl get clusterrolebinding

    kubectl create serviceaccount spark

    kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default
 
    kubectl get serviceaccount
#### Get Oauth token 
In order to submit spark job, we need get oauth token, otherwise an unauthorised exception

    Exception in thread "main" io.fabric8.kubernetes.client.KubernetesClientException: pods "spark-pi-1570631791494-driver" is forbidden: 
    User "system:anonymous" cannot watch resource "pods" in API group "" in the namespace "default"
To get Oauth token(id-token):

    kubectl config view

#### pull docker image
in order to pull the image from ibmcloud image registry, need to configure api token or add rights for service account

    kubectl patch -n default serviceaccount/spark -p '{"imagePullSecrets":[{"name": "default-uk-icr-io"}]}'
### submission job spark
Spark options:

kubernetes endpoint url:

    --master k8s://https://c3.lon04.containers.cloud.ibm.com:23951 

spark service account

    --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark 
docker spark image
    
    --conf spark.kubernetes.container.image=uk.icr.io/tao-lab1/spark:2.4.3
account id token

    --conf spark.kubernetes.authenticate.submission.oauthToken=<id-token>
Application jar where to find

    local:///opt/spark/examples/jars/spark-examples_2.11-2.4.3.jar
    
final command

    bin/spark-submit \
        --master k8s://https://c3.lon04.containers.cloud.ibm.com:23951 \
        --deploy-mode cluster \
        --name spark-pi \
        --class org.apache.spark.examples.SparkPi \
        --conf spark.executor.instances=1 \
        --conf spark.executor.memory=512M \
        --conf spark.executor.core=256M \
        --conf spark.driver.core=256M \
        --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark  \
        --conf spark.kubernetes.container.image=uk.icr.io/tao-lab1/spark:2.4.3 \
        --conf spark.kubernetes.authenticate.submission.oauthToken=<id-token> \
        local:///opt/spark/examples/jars/spark-examples_2.11-2.4.3.jar