import pymysql

connection = pymysql.connect("localhost","root","","demo")
cursor=connection.cursor();
DB_table_name ="Nihar";
sql_query="CREATE TABLE " + DB_table_name + """
                        (ID INT NOT NULL AUTO_INCREMENT,
                         ENROLLMENT varchar(100) NOT NULL,
                         NAME VARCHAR(50) NOT NULL,
                         DATE VARCHAR(20) NOT NULL,
                         TIME VARCHAR(20) NOT NULL,
                             PRIMARY KEY (ID)
                             );
                        """;
try:
	cursor.execute(sql_query);
	data=cursor.fetchone();
	print("DTA:%s"%data);


except Exception as e:
	print("Hello:",e);

connection.close();