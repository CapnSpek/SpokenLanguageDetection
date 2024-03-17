# Script to reduce the size of the huge training dataset to 1/3rd of the original size.

import os
import concurrent.futures
import random

folder_path = './dataset/train/train'
files = os.listdir(folder_path)

def delete(files_to_remove):
    """
    Deletes the specified files from the folder_path in a multi threaded way

    Args:
        files_to_remove (list): A list of file names to be deleted.

    Returns:
        None
    """
    def delete_file(file_name):
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(delete_file, files_to_remove)

def find_and_delete_files(language):
    """
    Find and delete files that have a specific language prefix.

    Args:
        language (str): The language prefix to filter the files.

    Returns:
        None
    """
    # Filter and store the formatted names of files in the set
    file_set_prefix = set()
    for file_name in files:
        if file_name.startswith(f'{language}_'):
            file_set_prefix.add(file_name.split('.')[0])
    # Select 2/3rd of the files randomly
    num = len(file_set_prefix) * 2 // 3
    files_to_remove_prefix = random.sample(list(file_set_prefix), num)  # Convert set to list
    files_to_remove = []
    for file_name in files:
        if file_name.split('.')[0] in files_to_remove_prefix:
            files_to_remove.append(file_name)
    delete(files_to_remove)
    

if __name__ == '__main__':
    find_and_delete_files("de")
    find_and_delete_files("en")
    find_and_delete_files("es")