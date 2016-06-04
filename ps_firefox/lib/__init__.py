# coding: utf-8

import codecs
from selenium import webdriver


class ff_automation():

    def __init__(self):
        self.driver = webdriver.Firefox()

    def start_firefox(self, url):
        self.driver.get(url)

    def stop_firefox(self):
        self.driver.close()

    def get_title(self):
        title = self.driver.title
        return title

    def get_content_by_tag_name(self, tag_name):
        content_list = []
        element_list = self.driver.find_elements_by_tag_name(tag_name)

        for element in element_list:
            content = element.text.replace('\n', '')
            content_list.append(content)

        return content_list

    def set_content(self, path, value):
        with codecs.open(path, 'w', encoding='utf-8') as file:
            file.write(value + '\n')

    def add_content(self, path, value):
        with codecs.open(path, 'a', encoding='utf-8') as file:
            file.write(value + '\n')
