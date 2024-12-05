 # structure of daily_batch_jobs folder
1. prepare your table with onetime execution in spark, log it with ${etl_id}_ddl.sql
2. write your logic with ${etl_id}.sql.
3. use ${home}/scrpts/submit_offline_jobs.sh script to summbit daily batch jobs.
