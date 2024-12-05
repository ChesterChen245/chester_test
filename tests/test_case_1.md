# insert test data
```sql
insert into target.user_info values (1,'zhangsan','male',date('2024-01-01'));
insert into target.user_info values(2,'zhaosi','male',date('2024-01-01'));
insert into target.user_info values(3,'wangwu','male',date('2024-01-02'));
insert into target.user_info values(4,'liliu','female',date('2024-01-02'));
```

# run the test batch
```shell
bash /Users/chester/Desktop/test/chester_test/scripts/submit_offline_jobs.sh example_job
```