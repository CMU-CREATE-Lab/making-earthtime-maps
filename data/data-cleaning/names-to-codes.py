# Converts country names to ISO3 country codes.
# Must install pandas: pip install pandas or pip3 install pandas
# Must install coco: pip install country_converter or pip3 install country_converter

# Libraries
import pandas as pd
import country_converter as coco

def convert(inputFile, outputFile):
    df = pd.read_csv(inputFile)

    cc = coco.CountryConverter()

    # Note that the column for the country names must be called "Country Name"
    df["Country Code"] = cc.pandas_convert(series = df["Country Name"], to = "ISO3")
    
    df.to_csv(outputFile, index = False)

if __name__ == "__main__":
    # Input and output files
    # Enter file paths when prompted
    inputFile = input("Enter input file path: ")
    outputFile = input("Enter output file path: ")

    convert(inputFile, outputFile)
