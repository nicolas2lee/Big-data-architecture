# docker
    docker build -t nicolas2lee/hadoop:hadoop_3_1_2_hive_3_1_1 .

# java issues:
current work version in hive: jdk <= jdk1.8 

#hive

    export HADOOP_HOME=/opt/hadoop-3.1.2
    
    export HIVE_HOME=/opt/apache-hive-3.1.1-bin

    $HIVE_HOME/bin/schematool -dbType derby -initSchema

    $HIVE_HOME/bin/hiveserver2

    $HIVE_HOME/bin/beeline -u jdbc:hive2://localhost:10000
    
    
    curl -s 'http://localhost:50111/templeton/v1/ddl/database/default/table/pokets?user.name=ctdean'
    