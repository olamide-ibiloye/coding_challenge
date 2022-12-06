csv_file = ["data/Small Files/file1.csv",
            "data/Small Files/file2.csv",
            "data/Small Files/file3.csv"]


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
    files = [csv_to_dict(path) for path in paths]
    merged_file = files[0]
    other_files = files[1:]

    for file in other_files:
        for id, column in file.items():
            for key, value in column.items():
                merged_file[id][key] = value

    return merged_file
    

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