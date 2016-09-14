#!/usr/bin/env python
import unittest
import os, sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

from openquakeplatform.test import pla

class VulnTaxonomiesTest(unittest.TestCase):
    pass

def tag_and_val_get(xpath, times):
    resulte_tag = pla.xpath_finduniq(xpath, times=times)
    resulte_val = resulte_tag.get_attribute("value")
    return (resulte_tag, resulte_val)


def make_function(func_name, taxonomy, run_slow):
    def generated(self):
        sys.stderr.write("START: ");
        taxonomy_loc = taxonomy
        if taxonomy_loc[-1] == '/':
            taxonomy_loc = taxonomy_loc[0:-1]

        pla.get('/taxtweb/%s' % taxonomy_loc)
        pla.waituntil_js(3, "gem_pageloaded == true;")

        typeoftax_tag, typeoftax_val = tag_and_val_get("//select[@id='OutTypeCB']", 20)
        typeoftax_sel = Select(typeoftax_tag)
        for i in range(0,3):
            typeoftax_sel.select_by_index(i)
            resulte_tag, resulte_val = tag_and_val_get("//input[@id='resultE']", 20)
            if resulte_val == taxonomy_loc:
                break
        else:
             self.assertEqual(resulte_val, taxonomy_loc)

        if run_slow:
            sys.stderr.write("RUN SLOW START\n")
            resulte_tag.click()   # Positions the cursor at the end of the string
            if len(resulte_val) > 0 and resulte_val[-1] == '/':
                resulte_tag.send_keys(Keys.BACK_SPACE)
                resulte_tag, resulte_val = tag_and_val_get("//input[@id='resultE']", 20)

            cur = resulte_val
            while len(cur) > 0:
                last = cur[-1]
                resulte_tag.send_keys(Keys.BACK_SPACE)
                # sys.stderr.write("BS");
                resulte_tag, resulte_val = tag_and_val_get("//input[@id='resultE']", 20)
                resulte_bgcol = resulte_tag.value_of_css_property('background-color')
                self.assertNotEqual(resulte_bgcol, "rgba(255, 223, 191, 1)")

                if last is "/":
                    # check integrity
                    virtual_tag, virtual_val = tag_and_val_get("//input[@id='resultE_virt']", 20)

                    self.assertEqual(resulte_bgcol, "rgba(191, 255, 191, 1)")
                    self.assertEqual(resulte_val, virtual_val)

                if resulte_val == "":
                    break

    generated.__name__ = func_name
    return generated

def generator():
    data_path = os.path.join(os.path.dirname(
        sys.modules[VulnTaxonomiesTest.__module__].__file__), 'data')

    with open(os.path.join(data_path, 'taxonomies.txt')) as f:
        ct = 0
        r = 1
        for taxonomy in f:
            if taxonomy[0] == '#':
                r += 1
                continue
            run_slow = False
            # these numbers are dimensioned to obtain 5 minutes test
            if ct < 25:
                run_slow = True
            if ct >= 60:
                break
            taxonomy = taxonomy.strip()
            func_name = "r%04d_%s_test" % (r, taxonomy)
            test_func = make_function(func_name, taxonomy, run_slow)
            setattr(VulnTaxonomiesTest, func_name, test_func)
            ct += 1
            r += 1

generator()