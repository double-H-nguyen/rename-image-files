import datetime
import os

root = os.path.join('..', 'food')
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        source_name = os.path.join(directory, name)
        timestamp = os.path.getmtime(source_name) # os.getmtime returns a timestamp in ticks, which is not easily readable. It must be converted to a standard datetime string first.
        modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':', '.')
        target_name = os.path.join(directory, f'{modified_date}_{name}')

        print(f'Renaming: {source_name} to: {target_name}')

        os.rename(source_name, target_name)