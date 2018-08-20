from lib.tree.Node import Node


class DirTree:

    def __init__(self, root=Node("/")):
        if isinstance(root, Node):
            self.root = root
        elif isinstance(root, str):
            self.root = Node(root)
        self.root.set_access(True)


    def add(self, node_path=None):
        if node_path is None:
            return
<<<<<<< HEAD
        if node_path in ["", "/"]:
=======
        if node_path in ["","/"]:
>>>>>>> b8a386b4b7a35f549d9671c8934a5617f5f70ffa
            return self.root
        path_split = ""
        if isinstance(node_path, str):
            path_split = self.__url_filter(node_path)
            path_split = path_split.split("/")

        if path_split is None or path_split[0] == "":
            return
        parent = self.root
        for node_name in range(len(path_split)):
            parent = parent.add_child(path_split[node_name])
            if parent is None:
                break

        return parent
<<<<<<< HEAD
=======

>>>>>>> b8a386b4b7a35f549d9671c8934a5617f5f70ffa


    def __url_filter(self, url):
        offset = url.find("#")
        url = url[:offset if offset != -1 else None]
        offset = url.find("?")
        url = url[:offset if offset != -1 else None]
        return self.__drop(url)


    def __drop(self, url, char='/'):
        url = url[len(self.root.name):]
        try:
            if url[0] == char:
                url = url[1:]
            if url[-1] == char:
                url = url[:-1]
        except Exception:
            pass
        return url


    def get_node(self, path):
        path_split = ""
        if isinstance(path, str):
            path_split = self.__url_filter(path)
            path_split = path_split.split("/")
            if path_split[0] == "":
                return self.root
        try:

            parent = self.root
            for node_name in path_split:
                if parent.is_leaf():
                    break
                parent = parent.children.get(node_name)

        except KeyError:
            raise KeyError("Node isn't exit.(Path:%s)" % path)
        return parent


    def print_tree(self):
        self.__print(self.root)


    def __print(self, node, depth=0):
        if node.is_root():
            print(" +--", node.name)
        pre_str = " │   " * (depth + 1)
        for c in node.children:
            print(pre_str + " +--", c.name, c.status)
            self.__print(c, depth + 1)


    # Depth-first walk
    def enum_tree(self):
        return iter(self.root)


    @property
    def num_of_nodes(self):
        num = 0
        for node in self.enum_tree():
            num += 1
        return num


    @staticmethod
    def last_range(iterable):
        it = iter(iterable)
        last = next(it)
        for val in it:
            yield last, False
            last = val
        yield last, True


if __name__ == '__main__':
    pass
