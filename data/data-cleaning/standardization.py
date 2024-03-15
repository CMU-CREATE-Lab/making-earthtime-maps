## Overview
# Takes a .csv file as input
# Computes the z-scores of quantitative values by row and column
# Ouputs a .csv file with z-scores

## Notes
# Input file must have quantitative values

# Libraries
import pandas as pd
from scipy.stats import zscore

# Returns the start index of the quantitative columns and values
def getIndex(df):
    count = 0

    numCols = df.shape[1]

    for i in range(numCols):
        type = str(df.iloc[:, i].dtype)
        print(type)
        
        if (type != "int64" and type != "float64"):
            count += 1
    
    return count

# Calculates and writes z-scores to a new .csv file
def convert(inputFile, outputFile, n):
    df = pd.read_csv(inputFile)

    # Data cleaning
    # Moves the non-numeric columns to the front of the frame
    qualitativeCols = df.select_dtypes(exclude = "number")
    dfClean = pd.concat([qualitativeCols, df.drop(columns = qualitativeCols)], axis = 1)

    index = getIndex(dfClean)

    labels = dfClean.iloc[:, :index]
    values = dfClean.iloc[:, index:]

    zScores = values.apply(zscore, axis = n, nan_policy = "omit")

    outputFrame = pd.concat([labels, zScores], axis = 1)

    outputFrame.to_csv(outputFile, index = False)

if __name__ == "__main__":
    inputFile = input("Enter input file path: ")
    direction = input("Standardize by row, column, or both (R for row, C for column, B for both): ")

    # Selections of by row, column, or both
    if direction == "R":
        rowFile = input("Enter output file path for row: ")
        convert(inputFile, rowFile, 1)
    elif direction == "C":
        colFile = input("Enter output file path for column: ")
        convert(inputFile, colFile, 0)
    elif direction == "B":
        rowFile = input("Enter output file path for row: ")
        colFile = input("Enter output file path for column: ")
        convert(inputFile, rowFile, 1)
        convert(inputFile, colFile, 0)
    else:
        print("Invalid Input Error")
