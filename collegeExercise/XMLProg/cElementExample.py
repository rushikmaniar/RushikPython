import xml.etree.cElementTree as xml
def parseXml(filename):
    tree = xml.ElementTree(file=filename)
    root = tree.getroot()

    print("-"*40)
    print("Iterating using getchildern()")
    print("-"*40)

#    users = root.getchildren()
    users = list(root)
    for user in users:
        #user_children = user.getchildren()
        user_children = list(user)
        for user_child in user_children:
            print(user_child.tag + " = " + user_child.text)

parseXml("test.xml")