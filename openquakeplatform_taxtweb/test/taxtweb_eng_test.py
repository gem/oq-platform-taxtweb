#!/usr/bin/env python
import unittest
import os, sys
from openquakeplatform_taxtweb.utils.taxtweb_eng import taxonomy_process

class TaxtwebEngTest(unittest.TestCase):
    pass


def make_function(func_name, taxonomy, run_slow):
    def generated(self):

        taxonomy_loc = taxonomy
        if taxonomy_loc[-1] == '/':
            taxonomy_loc = taxonomy_loc[0:-1]

        result_taxt = ["", "", taxonomy_loc[:]]
        result_err = ["", "", ""]
        
        for i in range(0, 3):
            result_taxt[i], result_err[i] = taxonomy_process(result_taxt[(i - 1) % 3], i)

            if result_err[i] is not None:
                self.assertFalse(True, result_err[i])

        for i in range(0, 3):
            if result_taxt[i] == taxonomy_loc:
                break
        else:
             self.assertEqual(result_taxt[2], taxonomy_loc)

        if run_slow:
            # temporarly disabled
            pass

    generated.__name__ = func_name
    return generated

def generator():
    data_path = os.path.join(os.path.dirname(
        sys.modules[TaxtwebEngTest.__module__].__file__), 'data')

    with open(os.path.join(data_path, 'taxonomies.txt')) as f:
        ct = 0
        r = 1
        for taxonomy in f:
            if taxonomy[0] == '#':
                r += 1
                continue
            # these numbers are dimensioned to obtain 5 minutes test, slow checks tempoarly disabled
            run_slow = (True if ct < -1 else False)
            if ct >= 600000: # check all taxonomies
                break
            taxonomy = taxonomy.strip()
            func_name = "r%04d_%s_%s_test" % (r, taxonomy.replace('.', '~'), "slow" if run_slow else "fast")
            test_func = make_function(func_name, taxonomy, run_slow)
            setattr(TaxtwebEngTest, func_name, test_func)
            ct += 1
            r += 1

generator()
