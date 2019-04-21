#!/usr/bin/env bash

file_prefix=$1
login_user=dbadmin
host=192.168.56.92
db_user=dbadmin
db_name=VMart
db_password=password

# VM及びVerticaが立ち上がっていることを前提とする

echo "unique: Start"
time python uniqueByRow.py ${file_prefix}.csv ./${file_prefix}_unique.csv
wait
echo "unique: End"

echo "normalize: Start"
time python normalize.py ./${file_prefix}_unique.csv ./${file_prefix}_unique_normalized.csv
wait
echo "normalize: End"

echo "scp to Vertica server: Start"
scp ${file_prefix}_unique_normalized.csv ${login_user}@${host}:/tmp/
wait
echo "scp to Vertica server: End"

echo "create table: Start"
vsql -h ${host} -U ${db_user} -d ${db_name} -w ${db_password} -c "create schema if not exists investigation;"
wait
vsql -h ${host} -U ${db_user} -d ${db_name} -w ${db_password} -c "drop table if exists investigation CASCADE;"
wait
vsql -h ${host} -U ${db_user} -d ${db_name} -w ${db_password} -c "create table investigation.measured_urls (account_id int, url varchar(8) not null) direct order by url asc partition by substr(url, 5, 1);"
wait
echo "create table: End"

echo "import data: Start"
vsql -h ${host} -U ${db_user} -d ${db_name} -w ${db_password} -i -c "copy investigation.measured_urls from '/tmp/${file_prefix}_unique_normalized.csv' delimiter ',' direct;"
wait
echo "import data: End"

echo "exec query: Start"
ssh ${login_user}@${host} "vsql -h ${host} -U ${db_user} -d ${db_name} -w ${db_password} -iA -F',' -c \"with duplication as (select url, count(*) as dup from investigation.measured_urls group by url) select * from duplication where dup >= 2 order by dup desc;\" > /tmp/${file_prefix}_result.csv"
wait
echo "exec query: End"

echo "download result: Start"
scp ${login_user}@${host}:/tmp/${file_prefix}_result.csv ./
echo "download result: End"

echo "clean data, table, csv: Start"
vsql -h ${host} -U ${db_user} -d ${db_name} -w ${db_password} -c "drop table if exists investigation.measured_urls CASCADE;"
wait
vsql -h ${host} -U ${db_user} -d ${db_name} -w ${db_password} -c "drop schema investigation RESTRICT"
wait
ssh ${login_user}@${host} "rm /tmp/${file_prefix}_unique_normalized.csv /tmp/${file_prefix}_result.csv;"
wait
echo "clean data, table, csv: End"
