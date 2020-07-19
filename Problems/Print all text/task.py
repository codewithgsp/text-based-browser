from lxml import etree
#  xml_str = '<root><elem1>I am elem1</elem1><elem2>I am elem2</elem2><elem3>I am elem3</elem3></root>'

root = etree.fromstring(input())

for num in range(len(root)):
    print(root[num].text)