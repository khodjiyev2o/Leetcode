class PhyloTree:
    def __init__(self, name):
        self.name = name
        self.left_child = None
        self.right_child = None
        self.similarity_values = {}


    def __str__(self):
        if self.is_leaf():
            return self.name
        else:
            return "({}, {})".format(str(self.left_child), str(self.right_child))


    def is_leaf(self):
        return self.left_child is None and self.right_child is None


def read_fasta_file(filename):
        organisms = {}
        with open(filename) as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                if lines[i].startswith(">"):
                    name = lines[i][1:].split()[0]
                    genome_sequence = ""
                    i += 1
                    while i < len(lines) and not lines[i].startswith(">") and lines[i].strip():
                        genome_sequence += lines[i].strip()
                        i += 1
                    organisms[name] = genome_sequence
                else:
                    i += 1
        return organisms


def create_ngram_sets(organisms, n):
        ngram_sets = {}
        for name, genome_sequence in organisms.items():
            ngram_sets[name] = set()
            for i in range(len(genome_sequence) - n + 1):
                ngram_sets[name].add(genome_sequence[i:i + n])
        return ngram_sets


def compute_similarity(ngram_sets):
        similarity_values = {}
        for name1, ngrams1 in ngram_sets.items():
            for name2, ngrams2 in ngram_sets.items():
                if name1 != name2:
                    similarity_values[(name1, name2)] = len(ngrams1.intersection(ngrams2)) / len(ngrams1.union(ngrams2))
        return similarity_values


def find_min_similarity(similarity_values):
        min_similarity = float('inf')
        min_pair = None
        for pair, similarity in similarity_values.items():
            if similarity < min_similarity:
                min_similarity = similarity
                min_pair = pair
        return min_pair


def create_tree(similarity_values):
        trees = {}
        for pair in similarity_values:
            name1, name2 = pair
            if name1 not in trees:
                trees[name1] = PhyloTree(name1)
            if name2 not in trees:
                trees[name2] = PhyloTree(name2)
            trees[name1].similarity_values[name2] = similarity_values[pair]
            trees[name2].similarity_values[name1] = similarity_values[pair]
        while len(trees) > 1:
            name1, name2 = find_min_similarity(similarity_values)
            new_name = "{}_{}".format(name1, name2)
            new_tree = PhyloTree(new_name)
            new_tree.left_child = trees.pop(name1)
            new_tree.right_child = trees.pop(name2)
            for name in trees:
                if name == name1 or name == name2:
                    continue
                new_similarity_value = (trees[name].similarity_values[name1] * len(
                    trees[name].left_child.similarity_values) + trees[name].similarity_values[name2] * len(
                    trees[name].right_child.similarity_values)) / (len(trees[name].left_child.similarity_values) + len(
                    trees[name].right_child.similarity_values))
                new_tree.similarity_values[name] = new_similarity_value
                trees[name].similarity_values[new_name] = new_similarity_value
            trees[new_name] = new_tree
        return trees.popitem()[1]


class PhyloTree:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def is_leaf(self):
        return not self.children

    def is_root(self):
        return not hasattr(self, 'parent')

    def add_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_descendants(self):
        descendants = []
        for child in self.children:
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants


# Testing PhyloTree class and its methods
def test_phylo_tree():
    # create tree
    try:
        A = PhyloTree('A')
        B = PhyloTree('B')
        C = PhyloTree('C')
        D = PhyloTree('D')
        E = PhyloTree('E')

        # test add_child()
        A.add_child(B)
        A.add_child(C)
        B.add_child(D)
        C.add_child(E)

        assert A.get_children() == [B, C]
        assert B.get_children() == [D]
        assert C.get_children() == [E]

        # test is_leaf() and is_root()
        assert A.is_root() is True
        assert D.is_leaf() is True
        assert E.is_leaf() is True
        assert B.is_root() is True

        # test add_parent() and get_parent()
        C.add_parent(A)
        assert C.get_parent() == A

        # test get_descendants()
        assert A.get_descendants() == [B, D, C, E]
        assert B.get_descendants() == [D]
        assert C.get_descendants() == [E]
        assert D.get_descendants() == []
        assert E.get_descendants() == []
        print("All tests passed!")
    except AssertionError:
        print("Tests failed")


test_phylo_tree()
