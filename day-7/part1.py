class Item:
    def __init__(self, name: str):
        self.name = name

    def size(self) -> int:
        pass

    def has_content(self) -> bool:
        pass


class File(Item):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    def size(self) -> int:
        return self._size

    def has_content(self) -> bool:
        return False

    def __str__(self):
        return self.name


class Folder(Item):
    def __init__(self, name: str, parent):
        super().__init__(name)
        self.contents = []
        self.parent = parent

    def size(self) -> int:
        return sum([content.size() for content in self.contents])

    def has_content(self) -> bool:
        return True

    def __str__(self):
        return self.name + ': ' + str([str(f) for f in self.contents])


with open('day-7/input.txt', 'r') as source:
    lines = source.read().splitlines()

    root: Folder = Folder('/', None)
    current: Folder = root

    def add_dir(line):
        [_, name] = line.split(' ')
        current.contents.append(Folder(name, current))

    def add_file(line):
        [size, name] = line.split(' ')
        current.contents.append(File(name, int(size)))

    def change_directory(line, current):
        [_1, _2, name] = line.split(' ')
        if name == '/':
            return root
        if name == '..':
            return current.parent
        return next(folder for folder in current.contents if folder.name == name)

    found = []

    def find_of_size(folder, desired_size) -> None:
        if folder.has_content():
            for content in folder.contents:
                find_of_size(content, desired_size)

            if folder is not root and folder.size() < desired_size:
                found.append(folder)

    for line in lines:
        if line.startswith('$'):
            if line.startswith('$ cd'):
                current = change_directory(line, current)
        elif line.startswith('dir'):
            add_dir(line)
        else:
            add_file(line)

    find_of_size(root, 100000)

    print(sum([f.size() for f in found]))
