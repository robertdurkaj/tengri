SITE = 'mountain-forecast.com'
PARENT = './/div[@id="forecast-cont"]/table'
ELEMENTS = (
    ('Summary',     '/tr[8]/td[4]'),
    ('High temp',   '/tr[11]/td[4]/span'),
    ('Low temp',    '/tr[12]/td[4]/span'),
    ('Wind',        '/tr[7]/td[4]/div/span'),
    ('Rain',        '/tr[9]/td[4]/b/span'),
    ('Snow',        '/tr[10]/td[4]/b/span'),
)
TEST_FILE = 'tests/html/mountain-forecast.html'
