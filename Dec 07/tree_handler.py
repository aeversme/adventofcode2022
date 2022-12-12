from class_handler import Directory


def define_directories(tree_list):
    directories = []
    for i in tree_list:
        if i[1] == 'cd' and i[2] != '..':
            new_dir = Directory(i[2])
            directories.append(new_dir)
    return directories


def populate_directories(tree_list):
    # directories = define_directories(tree_list)
    dir_list = []
    working_dir = None
    for i in tree_list:
        if i[1] == 'ls':
            continue
        print(f'pwd: {working_dir}')
        if i[1] == 'cd':
            print('Change directory command found...')
            if i[2] != '..':
                if dir_list:
                    for j in dir_list:
                        if j.name == i[2]:
                            working_dir = j
                            print(f'   Directory found in list, moving into {working_dir.name}')
                else:
                    working_dir = Directory(i[2])
                    print(f'   Not a match, creating and moving into new directory {working_dir.name}')
                    dir_list.append(working_dir)
            else:
                print(f'   Moving up one directory to {working_dir.parent_directory}...')
                working_dir = working_dir.parent_directory
        elif i[0] == 'dir':
            new_dir = None
            found = False
            print(f'   New directory in tree: {i[1]}')
            for k in dir_list:
                if k.name == i[1]:
                    new_dir = k
                    print(f'   Directory found: new_dir = {new_dir.name}')
                    found = True
                    continue
                else:
                    print(f'   Not a match')
                    new_dir = Directory(i[1])
            working_dir.child_directories.append(new_dir)
            print(f'      {new_dir.name} is a child of {working_dir.name}')
            new_dir.parent_directory = working_dir
            print(f'      {working_dir.name} is the parent of {new_dir.name}')
            if found:
                dir_list[dir_list.index(new_dir)] = new_dir
                print(f'         Directory {new_dir.name} modified')
            else:
                dir_list.append(new_dir)
                print(f'         Directory added to list: {new_dir.name}')
        else:
            print(f'   File found: {i[1]}, size {i[0]}')
            working_dir.files.append(i)
            working_dir.size += int(i[0])
    return dir_list


def add_to_parent_size(directory):
    print(f'Current dir: {directory.name}')
    if directory.child_directories:
        print(f'   {directory.name} has {len(directory.child_directories)} child directories')
        for child in directory.child_directories:
            if not child.added_to_parent:
                add_to_parent_size(child)
                directory.size += child.size
                child.added_to_parent = True
    return directory
