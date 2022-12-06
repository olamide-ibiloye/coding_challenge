csv_file = ["data/Small Files/file1.csv_path",
            "data/Small Files/file2.csv_path",
            "data/Small Files/file3.csv_path"]

csv_file_2 = ["data/Large Files/file1.csv_path",
              "data/Large Files/file2.csv_path",
              "data/Large Files/file3.csv_path"]


def csv_to_dict(csv_path: str):
    with open(csv_path) as f:
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


def main(file_name: str):
    merged_file = merger(all_file_paths)

    header = ['id']
    first_entry = list(merged_file.values())[-1]
    header.extend(list(first_entry.keys()))

    merged_file_list = [header]

    for key, value in merged_file.items():
        entry = [key]
        other_entries = [value for key, value in value.items()]
        entry.extend(other_entries)

        merged_file_list.append(entry)

    with open(f'{file_name}.csv_path', 'w') as f:
        for line in merged_file_list:
            f.write("%s\n" % ','.join(line))


if __name__ == "__main__":
    print("Welcome to the file merge program\n")

    number_of_files = int(input("How many files would you like to merge?:\n"))
    all_file_paths = []

    for num in range(number_of_files):
        file_path = input(f"Enter the path for file {num + 1}:\n")
        all_file_paths.append(file_path)

    target_file_name = input("Enter a name for your file:\n")

    print("\nMerging!")

    main(target_file_name)

    print("\nDone!")