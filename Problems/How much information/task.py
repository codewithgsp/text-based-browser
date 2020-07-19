from lxml import etree

# xml_str = '<a attr="123"><b>hello</b><c/></a>'
# xml_str = '<root a1="aba" a2="caba"/>'
root = etree.fromstring(input())

num_of_child_elements = len(root)
count_root_attributes = len(root.keys())
print(num_of_child_elements, count_root_attributes)