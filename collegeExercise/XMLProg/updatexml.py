'''
    UpdateXml File
'''
import xml.etree.cElementTree as xml

def updateXml(filename):
    #Start  with root element
    tree = xml.ElementTree(file=filename)
    root = tree.getroot()

    for salary in root.iter("salary"):
        salary.text = "1000"
    tree = xml.ElementTree(root)
    with open (filename,"wb") as fh:
        tree.write(fh)

updateXml("test.xml")