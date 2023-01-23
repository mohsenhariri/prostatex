import pickle

from utility import path_in


def t2_stats(path_pickle):

    t2 = {}
    with open(path_pickle, "rb") as fp:
        path_sequence_t2_pairs = pickle.load(fp)
        for pair in path_sequence_t2_pairs:
            if pair[1] in t2.keys():
                t2[pair[1]] += 1
            else:
                t2[pair[1]] = 1
    return t2



path_pickle_sequence_t2_pairs = path_in(r"output/AllT2Sequence", global_path=False)
unique_values_t2 = t2_stats(path_pickle_sequence_t2_pairs)
print(unique_values_t2)

