import os

def csv_to_dict(csv_path: str):
    # opening file and converting to list
    with open(csv_path) as f:
        csv_list = []

        for r in f.readlines():
            entry = [val.strip('", \n') for val in r.split(",")]
            csv_list.append(entry)

    # creating a dictionary from the list using first column (id) as key
    csv_dict = {}
    (_, *header), *data = csv_list

    for row in data:
        key, *values = row
        csv_dict[key] = {key: value for key, value in zip(header, values)}

    return csv_dict


def merger(paths: list):
    # saving dictionaries to a list
    files = [csv_to_dict(path) for path in paths]

    # using first file as the starting file
    merged_file = files[0]
    other_files = files[1:]

    for file in other_files:
        for id, column in file.items():
            for key, value in column.items():
                merged_file[id].update({key: value})

    return merged_file


def main(file_name: str):
    merged_file = merger(all_file_paths)

    # creating file header for csv
    # saving first column as id
    header = ['id']
    sample_entry = list(merged_file.values())[-1]
    header.extend(list(sample_entry.keys()))

    # adding header as the row in the list
    merged_file_list = [header]

    for key, value in merged_file.items():
        entry = [key]
        other_entries = [value for key, value in value.items()]
        entry.extend(other_entries)

        merged_file_list.append(entry)

    # exporting final file
    with open(f'{file_name}.csv', 'w') as f:
        for line in merged_file_list:
            f.write("%s\n" % ','.join(line))



if __name__ == "__main__":
    try:
        # starting program
        print("Welcome to the file merge program\n")

        # getting number of files to be merged
        # no merging if file number is less than 2
        number_of_files = int(input("How many files would you like to merge?:\n"))
        if number_of_files <= 1:
            raise Exception("Sorry, you need at least 2 files to merge")

        all_file_paths = []
        for num in range(number_of_files):
            # confirm the path to ensure file exists
            file_path = input(f"Enter the path for file {num + 1}:\n")
            if not os.path.exists(file_path):
                raise FileNotFoundError("Sorry, recheck the file path")

            all_file_paths.append(file_path)

        target_file_name = input("Enter a name for your file:\n")
        
        print("\nMerging!")

        main(target_file_name)

        print("\nDone!")
    
    except Exception as e:
        print(e)