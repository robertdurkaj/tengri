SITE = 'meteoblue.com'
PARENT = './/div[@id="day2"]'
ELEMENTS = (
    ('Max temp',     '//div[@class="tab_temp_max"]'),
    ('Min temp',     '//div[@class="tab_temp_min"]'),
    ('Wind',         '//div[@class="wind"]'),
    ('Precipation',  '//div[@class="tab_precip"]'),
)
TEST_FILE = 'tests/html/meteoblue.html'
