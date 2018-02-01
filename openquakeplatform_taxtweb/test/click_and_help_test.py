#!/usr/bin/env python
import unittest
from openquake.moon import platform_get
from selenium.webdriver.common.keys import Keys


class VulnTaxonomiesTest(unittest.TestCase):
    @staticmethod
    def setup_class():
        pla = platform_get()
        pla.get('/taxtweb')
        try:
            dontshow_tag = pla.xpath_finduniq(
                "//div[@id='taxtweb_splash']//input[@name='dontshowmeagain']",
                times=10)
            pla.wait_visibility(dontshow_tag)
            dontshow_tag.click()
            close_tag = pla.xpath_finduniq(
                "//div[@id='taxtweb_splash']//button[@name='close_btn']")
            close_tag.click()
        except:
            pass

    def click_and_help_simple_test(self):
        pla = platform_get()

        first_tab_tag = pla.xpath_finduniq(
            "//li[span[normalize-space(text()) = 'Structural System']]")
        first_tab_tag.click()

        click_and_help_tag = pla.xpath_finduniq(
            "//li[@id='id_help_form']")
        click_and_help_tag.click()

        simple_help = pla.xpath_finduniq(
            "//li[span[normalize-space(text()) = 'Direction X']]")
        simple_help.click()

        pla.select_window_by_name(".*Direction X.*", timeout=5.0,
                                  is_regex=True)
        pla.window_close()
        pla.select_main_window()

    def click_and_help_complex_test(self):
        pla = platform_get()

        third_tab_tag = pla.xpath_finduniq(
            "//li[span[normalize-space(text()) = 'Exterior Attributes']]")
        third_tab_tag.click()

        click_and_help_tag = pla.xpath_finduniq(
            "//li[@id='id_help_form']")
        click_and_help_tag.click()

        select_tag = pla.xpath_finduniq(
            "//select[@id='PositionCB']")
        # select_tag.click()
        select_tag.send_keys(Keys.ENTER)

        item_tag = pla.xpath_finduniq(
            "//div[@id='gem_help_select']/span[normalize-space(text()) = "
            "'Adjoining building(s) on two sides']")

        item_tag.click()

        pla.select_window_by_name(".*Adjoining buildings on two sides.*",
                                  timeout=5.0, is_regex=True)
        pla.window_close()
        pla.select_main_window()
