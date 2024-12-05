CREATE TABLE target.user_info (
    user_id INT,
    user_name STRING,
    gender STRING,
    regester_dt DATE
)
USING PARQUET
PARTITIONED BY (regester_dt);