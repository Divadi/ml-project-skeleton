import shutil
import os

# Zips path, stores in tmp, returns path to zipped file.
def zip_path(path):
    folder_name = os.path.basename(path)
    parent_name = os.path.dirname(path)

    tmp = '/tmp'
    os.makedirs(tmp, exist_ok=True)
    return shutil.make_archive(os.path.join(tmp, folder_name), 'zip', parent_name, folder_name)