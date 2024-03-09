from extract import extract
from unite import unite

if __name__ == "__main__":
    extract(
        "mkechinov/ecommerce-events-history-in-cosmetics-shop",
        "../data/",
    )

    unite("../data/db.duckdb")
