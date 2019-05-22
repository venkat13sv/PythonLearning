import xml.etree.ElementTree as ET
tree=ET.parse('xmlfile.xml')
root=tree.getroot()
print(root.tag)
for country in root.iter('country'):
    print("Country ={0}".format(country.attrib['name']))
for country in root.findall('country'):
    print(country.attrib['name'])
for country in root:
    for child in country:
        print(child.tag,child.attrib)
