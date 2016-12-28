from lxml import html

# yr.no


def forecast():
    root = get_root('tests/html/yrno.html')
    print u'Max temp: {0}'.format(get_max_temp(root))
    print u'Min temp: {0}'.format(get_min_temp(root))
    print u'Wind: {0}'.format(get_wind(root))
    print u'Precipation: {0}'.format(get_precipation(root))


def get_root(path):
    tree = html.parse(path)
    return tree.getroot()


def get_max_temp(root):
    table = root.find_class('yr-table')[1]
    td = table.find('.tbody/tr[2]/td[3]')
    return td.text_content().strip()


def get_min_temp(root):
    table = root.find_class('yr-table')[1]
    td = table.find('.tbody/tr[1]/td[3]')
    return td.text_content().strip()


def get_wind(root):
    table = root.find_class('yr-table')[1]
    td = table.find('./tbody/tr[2]/td[5]')
    return td.text_content().strip()


def get_precipation(root):
    table = root.find_class('yr-table')[1]
    td = table.find('./tbody/tr[2]/td[4]')
    return td.text_content().strip()
