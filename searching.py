import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)
        hod = data.keys()
        for dat in hod:
            if dat == field:
                value = data[field]
                return value
            return None

    return data(field)


def linear_search(field, searched_number):
    dict = {"index": "", "count": ""}
    positions = []
    count = 0
    for idx, idy in enumerate(field):
        if idy == searched_number:
            count = count + 1
            positions.append(idx)
        else:
            pass
    dict["count"] = count
    dict["index"] = positions

    return dict

def main():
    searched_number = 0
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    
print(main())

if __name__ == '__main__':
    main()