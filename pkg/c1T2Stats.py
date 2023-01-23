import pickle

from utility import path_in


def find_unique_values(path_pickle):

    t2_lst = []
    with open(path_pickle, "rb") as fp:
        path_sequence_t2_pairs = pickle.load(fp)
        t2_lst = [t2[1] for t2 in path_sequence_t2_pairs]

    t2set = set(t2_lst)

    return t2set


path_pickle_sequence_t2_pairs = path_in(r"output/AllT2Sequence", global_path=False)
unique_values_t2 = find_unique_values(path_pickle_sequence_t2_pairs)
print(unique_values_t2)

unique_values_t2 = {
    "t2_tse_tra_Grappa3",
    "t2_tse_sag_320_p2",
    "t2_localizer_prostate",
    "t2_tse_cor",
    "t2_tse_tra_S5_ND",
    "t2_loc tra",
    "t2_tse_tra_exacte_copy_diffusie",
    "t2_tse_sag",
    "t2_tse_tra",
    "t2_loc sag",
    "t2_localizer",
    "t2_localizer_sag",
    "t2_tse_sag_S3_ND",
    "t2_tse_tra_320_p2",
    "t2_tse_cor_320_p2",
}

