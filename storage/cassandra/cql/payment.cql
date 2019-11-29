#CREATE KEYSPACE test_demo
#WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
#/
CREATE TABLE tablename(
                        id int PRIMARYKEY,
                        amount string
)