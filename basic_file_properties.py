import os
import time

file_path = "20160712_174018.jpg"

print(f"File: {file_path}")
print(f"Last Accessed Time: {time.ctime(os.path.getatime(file_path))}")
print(f"Last Modified Time: {time.ctime(os.path.getmtime(file_path))}")
print(f"Last Created Time: {time.ctime(os.path.getctime(file_path))}")
print(f"File Size: {round(os.path.getsize(file_path) / 1024**2, 2)} MB")

# root = os.path.join('..', 'image-renaming-test')
# for directory, subdir_list, file_list in os.walk(root):
#     for name in file_list:
#         source_name = os.path.join(directory, name)
#         print(source_name)