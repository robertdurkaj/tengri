from lxml import html

# yr.no


def forecast():
    root = get_root('tests/html/yrno.html')
    print u'01:00-07:00: {0}'.format(get_temp1(root))
    print u'07:00-13:00: {0}'.format(get_temp2(root))
    print u'Wind: {0}'.format(get_wind(root))
    print u'Precipation: {0}'.format(get_precipation(root))


def get_root(path):
    tree = html.parse(path)
    return tree.getroot()


def get_temp1(root):
    table = root.find_class('yr-table')[1]
    td = table.find('.tbody/tr[1]/td[3]')
    return td.text_content().strip()


def get_temp2(root):
    table = root.find_class('yr-table')[1]
    td = table.find('.tbody/tr[2]/td[3]')
    return td.text_content().strip()


def get_wind(root):
    table = root.find_class('yr-table')[1]
    td = table.find('./tbody/tr[2]/td[5]')
    return td.text_content().strip()


def get_precipation(root):
    table = root.find_class('yr-table')[1]
    td = table.find('./tbody/tr[2]/td[4]')
    return td.text_content().strip()
