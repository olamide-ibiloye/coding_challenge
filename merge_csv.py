import os

def csv_to_dict(csv_path: str):
    # opening file and reading into a list
    with open(csv_path) as f:
        csv_list = [[val.strip() for val in r.split(",")]
                    for r in f.readlines()]

    (_, *header), *data = csv_list

    # creating dictionary as it is the most effective way to hold the data
    # dictionary prevents duplicate entries, since ids and column names are unique
    # using the first column (id) as key 
    csv_dict = {}
    for row in data:
        key, *values = row
        csv_dict[key] = {key: value for key, value in zip(header, values)}

    return csv_dict


def merger(paths: list):
    # converting all paths to dictionary using csv_to_dict function
    # effectively managed using list
    files = [csv_to_dict(path) for path in paths]

    # using first file as the starting file
    # in other words, implementing left join
    merged_file = files[0]
    other_files = files[1:]

    # getting column names
    columns = list(merged_file.values())[0]

    # iterating through file_2 onward
    for file in other_files:
        # columns in the current file
        cols = list(file.values())[0]
        # updating number of columns
        columns.update(cols)
        for id, row in file.items():
            for key, value in row.items():
                # if id already exists in the current merged file then update
                if id in merged_file.keys():
                    merged_file[id].update([(key, value)])
                else:
                    # for new ids, creating a new entry for it
                    # creating 'NAs' to fill blanks
                    # by tracking the number of columns already in existence
                    merged_file[id] = {key: 'NA' for key in columns.keys()}
                    merged_file[id].update([(key, value)])

        # taking care of any missing values
        # tracking ids with no record in the current file
        # filling with 'NA'
        for id in merged_file.keys():
            if id not in file.keys():
                merged_file[id].update([(key, 'NA')])

    return merged_file


def main(file_name: str):
    # saving the final merged file
    merged_file = merger(all_file_paths)
    # building header with the first as the id
    # getting other column names and adding to header
    header = ['id']
    first_key = list(merged_file.keys())[0]
    first_key_value = merged_file[first_key]
    header.extend(first_key_value.keys())
    # final merged file in list format starts with the header
    merged_file_list = [header]

    # creating a list comprising of id and other columns
    for key, value in merged_file.items():
        row = [key]
        row.extend(value.values())
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