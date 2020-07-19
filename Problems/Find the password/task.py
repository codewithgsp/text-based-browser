from lxml import etree
# xml_str = '<profile><account login="login" password="secret"/></profile>'
xml_str = '''
<result>
  <webpage link="hyperskill.com"></webpage>
  <users>
    <!-- Random comment -->
    <user id="239" password="qwerty"><info email="a@a.a"/></user>
  </users>
</result>
'''


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    etree.dump(root)

    print(root.keys())

    if root.get('password'):
        return root.get('password')


    # check password in root
    if not root.get('password'):
        # check password in the child elements
        for num in range(len(root)):
            if len(root[num]) > 0:
                find_password(etree.tostring(root[num]))
            else:
                if 'password' in root[num].keys():
                    return root[num].get('password')
    else:
        return root.get('password')


print(find_password(xml_str))