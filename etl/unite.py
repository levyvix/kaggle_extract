import duckdb

duckdb.connect("../data/db.duckdb")


duckdb.sql("""
           create or replace table events as
           select * from '../data/*.csv'
           """)

duckdb.sql("""
           copy events to '../data/events.parquet'
           """)
