#!/usr/bin/env python
# encoding: utf-8

import pymysql
import pandas as pd


host = '116.63.131.185'
port = 6033
user = 'geektime'
password = 'python3'
conn = pymysql.connect(host=host, port=port, user=user, password=password, db='geektime', charset='utf8')
cur = conn.cursor()


def query(cursor, q):
    cursor.execute(q)
    print(cursor.fetchall())


# select * from table

# query(cur, 'select * from table1')

df1 = pd.read_csv('./table1.csv')
df2 = pd.read_csv('./table2.csv')

# select * from table limit 10

# query(cur, 'select * from table1 limit 10')

output = df1.head(10)


# select id from table

# query(cur, 'select id from table1')

output = df1['ID']


# select count(id) from table

# query(cur, 'select count(id) from table1')

output = df1['ID'].count()


# select * from table where id<1000 and age>30

# query(cur, 'select * from table1 where id<1000 and age>30')

output = df1[(df1['ID'] < 1000) & (df1['age'] > 30)]


# select id, count(distinct order_id) from table1 group by id

# query(cur, 'select age, count(distinct order_id) from table1 group by age')

output = df1.drop_duplicates(['order_id']).groupby('age').aggregate({'order_id': 'count'})


# select * from table1 t1 inner join table2 t2 on t1.id = t2.id

# query(cur, 'select * from table1 t1 inner join table2 t2 on t1.id=t2.id')

output = pd.merge(df1, df2, on='ID')


# select * from table1 union select * from table2

# query(cur, 'select * from table1 union select * from table2')

output = pd.concat([df1, df2])


# delete from table1 where id = 10

print(df1.head(10))
df = df1.drop(df1[df1['ID'] == 10].index)
print(df.head(10))


# alter table table1 DROP column column_name;

print(df1.head())
df = df1.drop(columns=['order_id'], axis=1)
print(df.head())

cur.close()
conn.close()

