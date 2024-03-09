import duckdb


def unite(data_path: str = "../data/db.duckdb"):
    conn = duckdb.connect(data_path)

    conn.execute("""
            create or replace table events as
            select * from '../data/*.csv'
            """)

    conn.execute("""
            copy events to '../data/events.parquet'
            """)

    conn.close()


if __name__ == "__main__":
    unite()
