from lxml import etree

# xml_str = '<a attr="123"><b>hello</b><c/></a>'
# xml_str = '<root a1="aba" a2="caba"/>'
root = etree.fromstring(input())
attr = input()

print(root.get(attr) if attr in root.keys() else None)
