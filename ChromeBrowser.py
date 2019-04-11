# -*- coding: utf-8 -*-
import time
import win32api

import win32con
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from urllib import request
import pyautogui
# selenium 模拟浏览器自动化测试
from selenium.webdriver.common.keys import Keys


class ChromeBrowser:
    choptions = Options()
    browser = None
    man_img_src = ''

    def __init__(self):
        self.choptions.add_argument("--no-sandbox")
        # self.choptions.add_argument("--disable-dev-shm-usage")
        # self.choptions.add_argument("--headless")
        # self.choptions.add_argument('blink-settings=imagesEnabled=false')
        # self.choptions.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(options=self.choptions)

        # self.browser = webdriver.PhantomJS(executable_path='E:\\phantomjs-2.1.1-windows\\bin')

    def init_chrome(self):
        self.browser.get("https://www.mzitu.com/56056")
        man_img = self.browser.find_element_by_xpath("//div[@class='main-image']/p/a/img")
        self.man_img_src = man_img.get_attribute("src")

    def save_pics(self, path='E:\\tmp'):
        if not os.path.exists(path):
            os.makedirs(path)
        selfheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = request.Request(self.man_img_src, headers=selfheaders)
        data = request.urlopen(req, timeout=30).read()
        img_f = open(path + "temp.jpg", 'wb')
        img_f.write(data)
        img_f.close()

    def open_pic(self):
        # script = "function download(src){var $a = document.createElement('a');$a.setAttribute('href', src);$a.setAttribute('download', '');var evObj = document.createEvent('MouseEvents');evObj.initMouseEvent( 'click', true, true, window, 0, 0, 0, 0, 0, false, false, true, false, 0, null);$a.dispatchEvent(evObj);};"
        # self.browser.execute_script(script + " download(arguments[0])", self.man_img_src)
        img_tag = self.browser.find_element_by_xpath("//div[@class='main-image']/p/a/img")
        actions = ActionChains(self.browser)
        actions.move_to_element(img_tag).context_click(img_tag).perform()
        pyautogui.typewrite(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter', 'enter'])
        time.sleep(1.5)
        actions.send_keys(Keys.ENTER).perform()
        pyautogui.typewrite(['enter'])

        print(self.browser.page_source)
        # self.browser.get_screenshot_as_file("E:\\tmp\\mig.png")


if __name__ == '__main__':
    chr_browser = ChromeBrowser()
    chr_browser.init_chrome()
    chr_browser.open_pic()
    # chr_browser.browser.close()



