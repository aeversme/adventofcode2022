from class_handler import Directory


def populate_directories(tree_list):
    dir_list = []
    working_dir = None
    for i in tree_list:
        if i[1] == 'ls' or i[0] == 'dir':
            continue
        # print(f'   pwd: {working_dir}')
        if i[1] == 'cd':
            # print('Change directory command found...')
            if i[2] != '..':
                parent_dir = None
                if dir_list:
                    parent_dir = working_dir
                working_dir = Directory(i[2])
                # print(f'   Creating and moving into new directory {working_dir.name}')
                working_dir.parent_directory = parent_dir
                if parent_dir:
                    working_dir.parent_directory.child_directories.append(working_dir)
                dir_list.append(working_dir)
            else:
                # print(f'   Moving up one directory to {working_dir.parent_directory}...')
                working_dir = working_dir.parent_directory
        else:
            # print(f'      File found: {i[1]}, size {i[0]}')
            working_dir.files.append(i)
            working_dir.size += int(i[0])
    return dir_list


def add_to_parent_size(directory):
    # print(f'Current dir: {directory.name}')
    if directory.child_directories:
        # print(f'   {directory.name} has {len(directory.child_directories)} child directories')
        for child in directory.child_directories:
            if not child.added_to_parent:
                add_to_parent_size(child)
                directory.size += child.size
                child.added_to_parent = True
    return directory
