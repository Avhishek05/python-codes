class Node:
    name = "abhishek"
    def change_name(self , newname):
        self.name = newname
abhi = Node()
print abhi.name
abhi.change_name("kuldeep")
print abhi.name
