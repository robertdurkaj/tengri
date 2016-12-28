from lxml import html

# meteoblue.com
# //div[@id="day2"]//div[@class="tab_temp_max"]
# //div[@id="day2"]//div[@class="tab_temp_min"]
# //div[@id="day2"]//div[@class="wind"]
# //div[@id="day2"]//div[@class="tab_precip"]


def forecast():
    # tree = html.parse('meteoblue.html')
    # print tree
    # print tree.getroot()

    # day2 = tree.getroot().get_element_by_id('day2')
    # print html.tostring(day2)
    # print day2.text_content()

    root = get_root('tests/html/meteoblue.html')
    print u'Max temp: {0}'.format(get_max_temp(root))
    print u'Min temp: {0}'.format(get_min_temp(root))
    print u'Wind: {0}'.format(get_wind(root))
    print u'Precipation: {0}'.format(get_precipation(root))


def get_root(path):
    tree = html.parse(path)
    return tree.getroot()


def get_max_temp(root):
    day2 = root.get_element_by_id('day2')
    div = day2.find_class('tab_temp_max')[0]
    return div.text_content().strip()


def get_min_temp(root):
    day2 = root.get_element_by_id('day2')
    div = day2.xpath('.//div[@class="tab_temp_min"]')[0]
    return div.text_content().strip()


def get_wind(root):
    day2 = root.get_element_by_id('day2')
    div = day2.find_class('wind')[0]
    return div.text_content().strip()


def get_precipation(root):
    day2 = root.get_element_by_id('day2')
    div = day2.find('.//div[@class="tab_precip"]')
    return div.text_content().strip()
