#!/bin/bash

# usage: bash submit_jobs.sh $etl_id

# get input params
PARAM_COUNT=$#

# if the params correct
if [ $PARAM_COUNT -eq 1 ]; then
    echo "got etl_id"
else
    echo "input params error, usage: bash submit_jobs.sh $etl_id"
    exit 101
fi

# prepare variables
etl_id=$1
home_folder='/Users/chester/Desktop/test/chester_test/'

# spark commit
spark-sql -f '${home_folder}/${etl_id}.sql'

# run docker image
docker build -t spark-sql-example
docker run --rm spark-sql-example

docker exec -i spark-container spark-sql -f /batch_sql/example_job.sql
