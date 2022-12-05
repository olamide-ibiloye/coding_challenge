import os
import sys

csv_file = ["data/Xsmall Files/file1.csv",
            "data/Xsmall Files/file2.csv",
            "data/Xsmall Files/file3.csv"]


def csv_to_dict(csv):
    with open(csv) as f:
        csv_list = []
        csv_dict = {}

        for r in f.readlines():
            entry = [val.strip('", \n') for val in r.split(",")]
            csv_list.append(entry)

    (_, *header), *data = csv_list

    for row in data:
        key, *values = row
        csv_dict[key] = {key: value for key, value in zip(header, values)}

    return csv_dict


def main(paths: list):
    #######

    files = [csv_to_dict(path) for path in paths]
    output_file = files[0]

    return output_file

    #####
    

if __name__ == "__main__":
    print("Welcome to the file merge program\n")

    numberOfFiles = int(input("How many files would you like to merge?:\n"))
    allFilePaths = []

    for num in range(numberOfFiles):
        filePath = input(f"Enter the path for file {num + 1}:\n")
        allFilePaths.append(filePath)

    print("\nMerging!")

    print(main(allFilePaths))

    print("\nDone!")