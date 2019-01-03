from xml.etree import ElementTree
tree = ElementTree.parse("test.xml")
root = tree.getroot()


children = list(root)
for child in children:
    ElementTree.dump(child)