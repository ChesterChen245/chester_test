#!/bin/bash

# usage: bash submit_jobs.sh $etl_id

# get input params
PARAM_COUNT=$#

# if the params correct
if [ $PARAM_COUNT -eq 2 ]; then
    echo "got etl_id"
else
    echo "input params error, usage: $0 <job_type> <$etl_id>  "
    exit 101
fi

# prepare variables
job_type=$1
etl_id=$2

# check job_type
if [[ "$job_type" != "streaming" && "$job_type" != "batch" ]]; then
    echo "error, job_type must be 'streaming' or 'batch'。"
    exit 102
fi

home_folder='/Users/chester/Desktop/test/chester_test/src/'


if [[ $job_type == "batch" ]]; then
    container_folder='batch_jobs/batch_sql/'
    exe_file='${home_folder}batch_jobs/batch_sql/${etl_id}.sql'
    container_folder='${container_folder}${etl_id}.sql'

    # batch job commit
    docker cp ${exe_file} 'spark-container:${container_folder}' && \
    docker exec -it spark-container spark-sql -f ${container_folder}

elif [[ $job_type == "streaming" ]]; then
    container_folder='streaming_jobs/'
    exe_file='${home_folder}streaming_jobs/${etl_id}.py'
    container_folder='${container_folder}${etl_id}.py'

    # streaming job commit
    docker cp ${exe_file} 'spark-container:${container_folder}' && \
    docker exec -it spark-container spark-sql -f ${container_folder}    
fi


