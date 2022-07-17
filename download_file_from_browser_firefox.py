import os.path
import time

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import geckodriver_autoinstaller

@pytest.fixture(scope='session')
def file_remove():
    os.remove('tmp/SampleFile.jpeg')


current_dir = os.path.dirname(os.path.abspath(__file__))

options = webdriver.FirefoxOptions()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", current_dir)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

service = Service(geckodriver_autoinstaller.install())
driver = webdriver.Firefox(service=service, options=options)

browser.config.driver = driver
browser.config.hold_browser_open = True
browser.open('https://demoqa.com/upload-download')
browser.element("#downloadButton").click()
time.sleep(1)
assert os.path.getsize("tmp/sampleFile.jpeg") == 4096



