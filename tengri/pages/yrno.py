SITE = 'yr.no'
PARENT = './/*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[2]/tbody'
ELEMENTS = (
    ('Temp (01:00-07:00)',  '/tr[1]/td[3]'),
    ('Temp (07:00-13:00)',  '/tr[2]/td[3]'),
    ('Wind',                '/tr[2]/td[5]'),
    ('Precipation',         '/tr[2]/td[4]'),
)
TEST_FILE = 'tests/html/yrno.html'
