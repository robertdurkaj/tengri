SITE = 'mountain-forecast.com'

_day_table = './/div[@id="forecast-cont"]/table'
LINES = (
    ('',            './/ul[@id="breadcrumbs"]'),
    ('',            './/ul[@class="elev"]/li[@class="active"]'),
    ('',            _day_table + '/tr[3]/td[2]'),
    ('Summary',     _day_table + '/tr[8]/td[4]'),
    ('High temp',   _day_table + '/tr[11]/td[4]/span'),
    ('Low temp',    _day_table + '/tr[12]/td[4]/span'),
    ('Wind',        _day_table + '/tr[7]/td[4]/div/span'),
    ('Rain',        _day_table + '/tr[9]/td[4]/b/span'),
    ('Snow',        _day_table + '/tr[10]/td[4]/b/span'),
)
