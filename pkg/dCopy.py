import pickle
from utility import path_in, path_out
from pathlib import Path

path_t2_pairs = path_in(r"output/AllT2Sequence", global_path=False)


path_t2_tse_tra_images = []
with open(path_t2_pairs, "rb") as fp:
    path_t2sequence_pairs = pickle.load(fp)
    for pair in path_t2sequence_pairs:
        if pair[1] == "t2_tse_tra":
            path_t2_tse_tra_images.append(Path(pair[0]).parent)


print(len(path_t2_tse_tra_images))



path_out_base = path_out('dataset/prostateUnique',global_path=False)
import shutil, errno


# def copyanything(src, dst):
#     try:
#         shutil.copytree(src, dst)
#     except Exception as err:
#         print(err)
#         print("SRC", src,"DST ", dst)
#         exit()
   
def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:  
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else:
            print(src,dst)

def copy_not_empty(src,dst):
    try:
           shutil.copytree(src, dst)
    except OSError as exc: 
        raise Exception("The directory isn't empty")
    
    

# for path_dir_t2 in path_t2_tse_tra_images:
#     root = path_dir_t2.parent.parent.stem
    

#     path_out = path_out_base/root / path_dir_t2.name
#     copyanything(path_dir_t2, path_out)


counter =0

for path_dir_t2 in path_t2_tse_tra_images:
    root = path_dir_t2.parent.parent.stem
    

    path_out = path_out_base/root / path_dir_t2.name
    
    try:
        copy_not_empty(path_dir_t2, path_out)
    except Exception:
        counter += 1


print("total", counter)