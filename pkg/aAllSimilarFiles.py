import os
import pickle

from utility import path_in, path_out


def find_files(path, filetype):
    """_summary_

    Args:
        path (_type_): _description_
        filetype (_type_): _description_

    Returns:
        _type_: _description_
    """
    files_path = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                files_path.append(os.path.join(root, file))
    return files_path


def find_first_file(path, filetype):
    """_summary_

    Args:
        path (_type_): _description_
        filetype (_type_): _description_

    Returns:
        _type_: _description_
    """
    files_path = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                files_path.append(os.path.join(root, file))
                break

    return files_path


def save_add_dcm(name: str):
    """_summary_

    Args:
        name (str): _description_
    """

    path_dataset = path_in(r"manifest-A3Y4AE4o5818678569166032044/PROSTATEx")

    path_files = find_files(path_dataset, ".dcm")
    # path_files = find_first_file(path_dataset, ".dcm")

    print("Number of files: ", len(path_files))
    path_save_result = path_out(r"output") / name

    with open(path_save_result, "wb") as fp:
        pickle.dump(path_files, fp)


save_add_dcm("FirstDicoms")  # 18321
# save_add_dcm("AllDicoms") # 309251
