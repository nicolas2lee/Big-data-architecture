# Big-data-architecture
It is a big data architecture verification project

#Docker
The basic docker image is openjdk-11.0.1

remove all docker containers & images

    docker rm $(docker ps -a -q)
    
    ocker rmi $(docker images -q)
    
## docker useful commands
Docker provides a single command that will clean up any resources — images, containers, volumes, and networks — that are dangling (not associated with a container):

    docker system prune
    
#Kubernetes
## how to deploy a pre defined action
    kubectl create -f filename.yaml
or

    kubectl apply -f filename.yaml
    
## how to expose service
https://gardener.cloud/050-tutorials/content/howto/service-access/

## how to get access to container

    kubectl exec -it kafka-server-cluster-1 bash

