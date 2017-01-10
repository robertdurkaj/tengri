from lxml import html

# mountain-forecast.com


LABELS = ('Summary', 'High temp', 'Low temp', 'Wind', 'Rain', 'Snow')
PREFIX = './/*[@id="forecast-cont"]/table'
XPATHS = ('/tr[8]/td[4]',             # Summary
          '/tr[11]/td[4]/span',       # High temp
          '/tr[12]/td[4]/span',       # Low temp
          '/tr[7]/td[4]/div/span',    # Wind
          '/tr[9]/td[4]/b/span',      # Rain
          '/tr[10]/td[4]/b/span', )   # Snow


root = None


def forecast():
    load_html('tests/html/mountain-forecast.html')
    for label in LABELS:
        value = get_value(label)
        print u'{0}: {1}'.format(label, value)


def load_html(path):
    global root
    if root is None:
        tree = html.parse(path)
        root = tree.getroot()
    return root


def get_value(label):
    if root is None:
        return ''  # TODO raise exception

    i = LABELS.index(label)
    xpath = PREFIX + XPATHS[i]

    element = root.find(xpath)
    if element is None:
        return ''

    return element.text_content().strip()
