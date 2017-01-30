SITE = 'yr.no'

_day_table = './/*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[2]'
LINES = (
    ('',                './/*[@id="ctl00_ctl00_contentBody"]/div[1]/h1/span'),
    ('',                    _day_table + '/caption'),
    ('Temp (01:00-07:00)',  _day_table + '/tbody/tr[1]/td[3]'),
    ('Temp (07:00-13:00)',  _day_table + '/tbody/tr[2]/td[3]'),
    ('Wind',                _day_table + '/tbody/tr[2]/td[5]'),
    ('Precipation',         _day_table + '/tbody/tr[2]/td[4]'),
)
