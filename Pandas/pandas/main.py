import pandas as pd
from websockets.cli import print_during_input

if __name__ == '__main__':

    # Dataframe (table)
    product_df = pd.DataFrame(
        {
            "id": ["SKU-1", "SKU-2", "SKU-3", "SKU-4", "SKU-5"],
            "name": ["shoes", "pants", "shirts", "sweaters", "designer-jacket"],
            "price": [760, 520, 450, 550, 4500],
            "currency": ["SEK", "SEK", "SEK", "SEK", "SEK"],

        }
    )

    print(product_df) #might take some time (first run)

    # Helper methods / Utility Methods (pandas)
    print(product_df["price"].max())    # Highest Value
    print(product_df["price"].min())    # Medium Value
    print(product_df["price"].mean())   # Mean of Total
    print(product_df["price"].median()) # Median of Total

    print(product_df.describe())        # Statistics of Numerical data

    print(product_df["price"].sort_values()) # Sorting algorithm == Quicksort

    # to_* (export files) - skapar en csv-fil
    product_df.to_csv("products.csv", index=False) # Path = Project Folder



    ################# DIRTY DATAFRAME - to clean #################
    dirty_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", "Sku-3", "sku_4", "SKU5 "],
            "name": [" Shoes", "pants ", "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", " 450", "550 ", " 4500"],
            "currency": [" sek", "SEK ", "Sek", "sek ", " SEK"],
        }
    )

    # dirty_df.id = [cleaned string]
    # dirty_df["id"].strip() # This won't properly replace values in Series (columns)
    dirty_df["id"] = dirty_df["id"].str.strip() # remove Whitespaces (start/end of string)
    dirty_df["id"] = dirty_df["id"].str.upper() #  ALL CAPS
    dirty_df["id"] = dirty_df["id"].str.replace(" ", "").str.replace("_", "-") # Replace String Content

    ## EDGE CASES ##
    # SKU5 <-- which EXCLUDES '-', Danger zone, because transformation isn't adding symbols...
    # SKU_4 <-- Technical Danger zone, what if multiple -- exists?

    dirty_df["price"] = dirty_df["price"].str.strip()
    dirty_df["price"] = dirty_df["price"].astype(float) # Casts: Current-datatype -> Float

    dirty_df["name"] = dirty_df["name"].str.strip()
    dirty_df["name"] = dirty_df["name"].str.title() # Makes first letter CAPS
    dirty_df["name"] = dirty_df["name"].str.replace(r"\s+", " ", regex = True) # regex, value, bool

    print(dirty_df.values)


    ############ MISSING DATA DATAFRAME ##############

    missing_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", None, "sku_4", "SKU5 "],
            "name": [" Shoes", None, "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", None, "550 ", " 4500"],
            "currency": [" sek", "SEK ", "Sek", None, " SEK"],
        }
    )

    print(missing_df.isna()) # pandas tool for identifying TRUE missing values

    missing_df["id_missing"] = missing_df["id"].isna()
    print(missing_df)

"""    Variant - men inte att rekomendera med större mängder data att loopa
mdf_values = ["id", "name", "price", "currency"]
    for mdf in mdf_values:
        missing_df[mdf + "-missing"] = missing_df[mdf].isna()

    print(missing_df) """