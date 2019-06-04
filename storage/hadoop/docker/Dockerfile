FROM openjdk:8-jdk-stretch
ENV HADOOP_VERSION 3.1.2
RUN wget http://apache.mediamirrors.org/hadoop/common/hadoop-"$HADOOP_VERSION"/hadoop-"$HADOOP_VERSION".tar.gz
RUN tar -xzvf hadoop-"$HADOOP_VERSION".tar.gz --directory /opt
RUN rm hadoop-"$HADOOP_VERSION".tar.gz

ADD ./conf /opt/hadoop-$HADOOP_VERSION/etc/hadoop
#ADD ./namenode_run.sh /opt/namenode_run.sh
#RUN chmod 777 /opt/namenode_run.sh

CMD /opt/hadoop-$HADOOP_VERSION/bin/hdfs datanode



