SITE = 'meteoblue.com'
TEST_FILE = 'tests/html/meteoblue.html'

_day_div = './/div[@id="day2"]'
LINES = (
    ('',            './/div[@id="header"]/div/div[1]/h1'),
    ('',            './/div[@class="location_description"]'),
    ('',            _day_div + '//div[@class="tab_day_long"]'),
    ('Max temp',    _day_div + '//div[@class="tab_temp_max"]'),
    ('Min temp',    _day_div + '//div[@class="tab_temp_min"]'),
    ('Wind',        _day_div + '//div[@class="wind"]'),
    ('Precipation', _day_div + '//div[@class="tab_precip"]'),
)
