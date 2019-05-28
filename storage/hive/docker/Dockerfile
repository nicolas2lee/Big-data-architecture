FROM nicolas2lee/hadoop
ENV HADOOP_VERSION 3.1.2
ENV HIVE_VERSION 3.1.1


RUN wget http://miroir.univ-lorraine.fr/apache/hive/hive-"$HIVE_VERSION"/apache-hive-"$HIVE_VERSION"-bin.tar.gz
RUN tar -xzvf apache-hive-"$HIVE_VERSION"-bin.tar.gz --directory /opt
RUN rm apache-hive-"$HIVE_VERSION"-bin.tar.gz
RUN export HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION

CMD /opt/hadoop-$HADOOP_VERSION/bin/hdfs datanode


RUN export HADOOP_HOME=/opt/hadoop-3.1.2