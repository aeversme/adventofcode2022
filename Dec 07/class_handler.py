class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent_directory = None
        self.child_directories = []
        self.files = []
        self.added_to_parent = False

    def __repr__(self):
        parent = None
        if self.parent_directory is not None:
            parent = self.parent_directory.name
        return f'Dir {self.name}: size {self.size}; parent = {parent}; ' \
               f'{len(self.child_directories)} child dirs; {len(self.files)} files'
