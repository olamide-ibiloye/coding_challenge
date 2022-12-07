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

    for row in csv_list:
        key, *values = row
        csv_dict[key] = [value for value in values]

    return csv_dict


def merger(paths: list):
    # saving dictionaries to a list
    files = [csv_to_dict(path) for path in paths]

    # using first file as the starting file
    merged_file = files[0]
    other_files = files[1:]

    for file in other_files:
        for id, column in file.items():
            for value in column:
                merged_file[id].append(value)

        # taking care of any missing values
        # replacing with 'NA'
        for id, column in merged_file.items():
            if id not in file.keys():
                merged_file[id].append('NA')

    return merged_file


def main(file_name: str):
    merged_file = merger(all_file_paths)
    merged_file_list = []

    # creating a list comprising of id and other columns
    for key, value in merged_file.items():
        row = [key]
        row.extend(value)
        merged_file_list.append(row)

    # exporting final file
    with open(f'{file_name}.csv', 'w') as f:
        for line in merged_file_list:
            f.write("%s\n" % ','.join(line))


if __name__ == "__main__":
    try:
        # starting program
        print("Welcome to the file merge program\n")

        # getting number of files to be merged
        number_of_files = int(input("How many files would you like to merge?:\n"))
        # no merging if file number is less than 2
        if number_of_files < 2:
            raise Exception("Sorry, you need at least 2 files to merge")

        all_file_paths = []
        for num in range(number_of_files):
            # naming files to start from 1 not 0 hence num+1
            file_path = input(f"Enter the path for file {num + 1}:\n")
            # confirm the path to ensure file exists
            if not os.path.exists(file_path):
                raise FileNotFoundError("Please put in a valid file path")

            all_file_paths.append(file_path)

        target_file_name = input("Enter a name for your file:\n")
        
        print("\nMerging!")

        main(target_file_name)

        print("\nDone!")
    
    except Exception as e:
        print(e)