'''
    Create Xml File
'''
import xml.etree.cElementTree as xml

def createXml(filename):
    #Start  with root element
    root = xml.Element("users")
    child1 = xml.Element("child1")
    root.append(child1)

    userid1 = xml.SubElement(child1,"id")
    userid1.text = "124"

    Username1 = xml.SubElement(child1,"name")
    Username1.text = "John"
    tree = xml.ElementTree(root)
    with open(filename,"wb") as fn:
        tree.write(fn)

createXml("test.xml")