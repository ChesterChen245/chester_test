create table user_info (
    user_id as int,
    user_name as string,
    gender as string,
    regester_dt as date
)
using parquet
partition by (regester_dt)
;