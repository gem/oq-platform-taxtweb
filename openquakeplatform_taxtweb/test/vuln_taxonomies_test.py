#!/usr/bin/env python
import unittest
import os, sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

from openquakeplatform.test import pla

class VulnTaxonomiesTest(unittest.TestCase):
    pass

def make_function(func_name, taxonomy):
    def generated(self):
        pla.get('/taxtweb/%s' % taxonomy)
        resulte_tag = pla.xpath_finduniq("//input[@id='resultE']", times=20)

        pla.waituntil_js(3, "gem_pageloaded == true;")

        if resulte_tag.get_attribute("value") != taxonomy:
            print "\nA:[%s]\nB:[%s]\n" % (taxonomy, resulte_tag.get_attribute("value"))
        self.assertEqual(resulte_tag.get_attribute("value"), taxonomy)
            
        # resulte_tag.click()   # Positions the cursor at the end of the string        
        # resulte_tag.sendKeys(Keys.BACK_SPACE)
        
        #exp_filename = os.path.join(exp_path,
        #                        "example_%d.%s" % (tab_id * 100 + example['exa_id'],
        #                       example['sfx']))
        #        with codecs.open(exp_filename, 'r', 'utf-8') as exp_file:
        #    expected = exp_file.read()

        #ret = ret_tag.get_attribute("value")
        #if ret is None:
        #    ret = ret_tag.get_attribute('innerHTML')
        #self.assertEqual(ret, expected)

    generated.__name__ = func_name
    return generated

def generator():
    data_path = os.path.join(os.path.dirname(
        sys.modules[VulnTaxonomiesTest.__module__].__file__), 'data')
    
    with open(os.path.join(data_path, 'taxonomies.txt')) as f:
        ct = 0
        for taxonomy in f:
            if taxonomy[0] == '#':
                continue
            if ct == 1000:
                break
            taxonomy = taxonomy.strip()
            func_name = "%s_test" % taxonomy
            test_func = make_function(func_name, taxonomy)
            setattr(VulnTaxonomiesTest, func_name, test_func)
            ct += 1

generator()
