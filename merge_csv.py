csv_file = ["data/Small Files/file1.csv",
            "data/Small Files/file2.csv",
            "data/Small Files/file3.csv"]

csv_file_2 = ["data/Large Files/file1.csv",
              "data/Large Files/file2.csv",
              "data/Large Files/file3.csv"]


def csv_to_dict(csv):
    with open(csv) as f:
        csv_list = []

        for r in f.readlines():
            entry = [val.strip('", \n') for val in r.split(",")]
            csv_list.append(entry)

    csv_dict = {}
    (_, *header), *data = csv_list

    for row in data:
        key, *values = row
        csv_dict[key] = {key: value for key, value in zip(header, values)}

    return csv_dict


def merger(paths: list):
    files = [csv_to_dict(path) for path in paths]
    merged_file = files[0]
    other_files = files[1:]

    for file in other_files:
        for id, column in file.items():
            for key, value in column.items():
                merged_file[id][key] = value

    return merged_file


def main():
    merged_file = merger(allFilePaths)

    header = ['id']
    first_entry = list(merged_file.values())[-1]
    header.extend(list(first_entry.keys()))

    merged_file_list = [header]

    for key, value in merged_file.items():
        entry = [key]
        other_entries = [value for key, value in value.items()]
        entry.extend(other_entries)

        merged_file_list.append(entry)

    with open('merged_file.csv', 'w') as f:
        for line in merged_file_list:
            f.write("%s\n" % ','.join(line))


if __name__ == "__main__":
    print("Welcome to the file merge program\n")

    numberOfFiles = int(input("How many files would you like to merge?:\n"))
    allFilePaths = []

    for num in range(numberOfFiles):
        filePath = input(f"Enter the path for file {num + 1}:\n")
        allFilePaths.append(filePath)

    print("\nMerging!")

    main()

    print("\nDone!")
