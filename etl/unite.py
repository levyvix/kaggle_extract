import duckdb

conn = duckdb.connect("../data/db.duckdb")


conn.execute("""
           create or replace table events as
           select * from '../data/*.csv'
           """)

conn.execute("""
           copy events to '../data/events.parquet'
           """)

conn.close()
