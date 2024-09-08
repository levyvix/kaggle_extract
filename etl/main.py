from extract import extract, clean_data
from unite import unite_pl


def main():
    extract(
        "unanimad/corona-virus-brazil",
        "../data/",
    )

    clean_data("../data/")

    unite_pl(
        "../data/",
    )

    


if __name__ == "__main__":
    main()