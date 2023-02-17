in_file = open('evolution.in')
out_file = open('evolution.out', 'w')


class Node:
    existing_values = set()  # evolutions already in the tree

    def __init__(self, values):
        self.values = values
        Node.existing_values |= values
        self.parent = None
        self.children = []

    def create_node_between(self, child, traits):
        # Creates a node between self and child with specified traits
        # child must be in self.children
        self.children.remove(child)
        new_node = Node(traits)
        self.add_child(new_node)
        new_node.add_child(child)
        return new_node

    def add_child(self, child):
        # Adds a child to self
        self.children.append(child)
        child.parent = self
        child.values -= self.values

    def add(self, traits):
        # Attempts to add a population with certain traits to the tree
        # Returns True if successful, False if the tree isn't proper anymore
        if not traits:  # Already exists
            return True
        for child in self.children:
            if traits >= child.values:  # Continue down a certain branch
                traits = traits - child.values
                return child.add(traits)
            elif child.values > traits:  # Add node between links
                self.create_node_between(child, traits)
                return True
            elif child.values & traits:  # Create branch between link
                new_node = self.create_node_between(child, child.values & traits)
                new_node.add_child(Node(traits - self.values))
                return True
        if traits & Node.existing_values:  # Duplicates exist
            return False
        self.children.append(Node(traits))  # End branch
        return True


in_file.readline()  # Ignore first line

root = Node(set())
for line in in_file:
    _, *cow = line.split()
    res = root.add(set(cow))  # Add to tree
    if not res:
        print("no", file=out_file)  # Not proper
        break
else:
    print("yes", file=out_file)  # Proper
