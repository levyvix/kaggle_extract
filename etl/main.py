from extract import extract
from unite import unite_pl

if __name__ == "__main__":
    extract(
        "mkechinov/ecommerce-events-history-in-cosmetics-shop",
        "../data/",
    )

    unite_pl("../data/")
