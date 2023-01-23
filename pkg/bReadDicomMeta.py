import pickle

import pydicom
from utility import PathType, path_in, path_out


def save_meta(path_pickle: PathType) -> None:
    """_summary_

    Args:
        path_pickle (PathType): _description_
    """
    path_meta_pair = []
    path_meta_pair_errs = []

    with open(path_pickle, "rb") as fp:
        path_imgs_lst: list = pickle.load(fp)
        for i, path_img in enumerate(path_imgs_lst):
            print("Iteration: ", i)
            try:
                inf = pydicom.dcmread(path_img)
                path_meta_pair.append([path_img, inf])

            except Exception as err:
                print(err)
                path_meta_pair_errs.append([path_img, str(err)])

    path_save_path_meta = path_out(r"output") / "AllMeta"
    with open(path_save_path_meta, "wb") as fp:
        pickle.dump(path_meta_pair, fp)

    if path_meta_pair_errs:
        path_save_path_meta_errs = path_out(r"output") / "ErrorMeta"
        with open(path_save_path_meta_errs, "wb") as fp:  # Pickling
            pickle.dump(path_meta_pair_errs, fp)
    else:
        print("All images have been read successfully.")


def save_sequence(path_pickle):

    path_sequence_pair = []
    path_sequence_pair_errs = []
    path_sequence_pair_t2 = []

    with open(path_pickle, "rb") as fp:
        path_imgs_lst: list = pickle.load(fp)
        for i, path_img in enumerate(path_imgs_lst):
            print("Iteration: ", i)
            try:
                inf = pydicom.dcmread(path_img)
                series_description = inf.SeriesDescription
                path_sequence_pair.append([path_img, series_description])

                if "t2" in series_description.lower():
                    path_sequence_pair_t2.append([path_img, series_description])

            except Exception as err:
                print(err)
                path_sequence_pair_errs.append([path_img, str(err)])

        path_save_path_sequence = path_out(r"output") / "AllSequence"
        with open(path_save_path_sequence, "wb") as fp:
            pickle.dump(path_sequence_pair, fp)

        path_save_path_sequence_t2 = path_out(r"output") / "AllT2Sequence"
        with open(path_save_path_sequence_t2, "wb") as fp:
            pickle.dump(path_sequence_pair_t2, fp)
            print("Number of T2 images: ", len(path_sequence_pair_t2))

        if path_sequence_pair_errs:
            path_save_path_sequence_errs = path_out(r"output") / "ErrorSequence"
            with open(path_save_path_sequence_errs, "wb") as fp:  # Pickling
                pickle.dump(path_sequence_pair_errs, fp)
        else:
            print("All images have been read successfully.")


path_pickle_first = path_in(r"output/FirstDicoms", global_path=False)
# save_meta(path_pickle_first)
save_sequence(path_pickle_first)
