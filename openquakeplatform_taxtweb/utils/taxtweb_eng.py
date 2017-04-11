#!/usr/bin/env python
from utils.taxtweb_maps import *
from utils.taxtweb_head import *

from collections import OrderedDict

class TaxtSel(object):    
    def __init__(self, items=[], selected=-1, disabled=False, change_cb=None):
        '''
        items => list of 1 element dicts
        selected => int identifing current selected item
        '''
        self.items = items
        self.selected = selected
        self.disabled = disabled
        self.change_cb = change_cb

    def empty(self):
        self.items = []
        self.selected = -1

    def disabled(self, disabled=None):
        if disabled == None:
            return self.disabled
        else:
            self.disabled = disabled
        
    def items(self, items=None):
        '''
        items => list of 1 element dicts
        selected => int identifing current selected item
        '''
        if items == None:
            items = []
        else:
            self.items = items[:]

    def selected(self, selected=-1):
        self.selected = selected
        if self.change_cb:
            self.change_cb()
        

class TaxtBool(object):
    def __init__(self, val=False, change_cb=None):
        self.val = val
        self.change_cb = change_cb

    def val(self, val=None):
        if val == None:
            return self.val
        else:
            self.val = val
            if self.change_cb:
                self.change_cb()
            return self.val

class TaxtRadioItem(object):
    def __init__(self, val=None, checked=False, radio=None, change_cb=None):
        self.val = val
        self.checked = checked
        self.change_cb = change_cb
        self.radio = radio

    def val(self, val=None):
        if val != None:
            self.val = val

        return self.val

    def check(self, is_checked=False):
        if is_checked == True:
            if self.radio != None:
                for item in self.radio.items:
                    item.check(False)
        self.checked = is_checked

        return self.checked


class TaxtRadio(object):
    def __init__(self, items=[]):
        self.items = items[:]
        for item in items:
            item.radio = self

    def item_add(self, item):
        self.items.append(item)
        item.radio = self



        

class TaxtStr(object):
    def __init__(self, val=None, change_cb=None):
        self.val = val
        self.change_cb = change_cb

    def val(self, val=None):
        if val == None:
            return self.val
        else:
            self.val = val
            if self.change_cb:
                self.change_cb()
            return self.val


def taxt_Direction1RB1Click(taxt_radioitem):
    pass

def taxt_Direction1RB2Click(taxt_radioitem):
    pass

def taxt_Direction2RB1Click(taxt_radioitem):
    pass

def taxt_Direction2RB3Click(taxt_radioitem):
    pass


class Taxonomy(object):
    def __init__(self):
        # dropdown
        self.MaterialCB11 = TaxtSel()
        self.MaterialCB21 = TaxtSel()
        self.MaterialCB31 = TaxtSel()
        self.MaterialCB41 = TaxtSel()
        self.SystemCB11 = TaxtSel()
        self.SystemCB21 = TaxtSel()
        self.MaterialCB12 = TaxtSel()
        self.MaterialCB22 = TaxtSel()
        self.MaterialCB32 = TaxtSel()
        self.MaterialCB42 = TaxtSel()
        self.SystemCB12 = TaxtSel()
        self.SystemCB22 = TaxtSel()
        self.HeightCB1 = TaxtSel()
        self.HeightCB2 = TaxtSel()
        self.HeightCB3 = TaxtSel()
        self.HeightCB4 = TaxtSel()
        self.DateCB1 = TaxtSel()
        self.OccupancyCB1 = TaxtSel()
        self.OccupancyCB2 = TaxtSel()
        self.PositionCB = TaxtSel()
        self.PlanShapeCB = TaxtSel()
        self.RegularityCB1 = TaxtSel()
        self.RegularityCB2 = TaxtSel()
        self.RegularityCB4 = TaxtSel()
        self.RegularityCB3 = TaxtSel()
        self.RegularityCB5 = TaxtSel()
        self.WallsCB = TaxtSel()
        self.RoofCB1 = TaxtSel()
        self.RoofCB2 = TaxtSel()
        self.RoofCB3 = TaxtSel()
        self.RoofCB5 = TaxtSel()
        self.RoofCB4 = TaxtSel()
        self.FloorCB1 = TaxtSel()
        self.FloorCB2 = TaxtSel()
        self.FloorCB3 = TaxtSel()
        self.FoundationsCB = TaxtSel()
        self.OutTypeCB = TaxtSel()

        # boolean
        self.DirectionCB = TaxtBool()

        # radio
        self.Direction1RB1 = TaxtRadioItem(val="false", change_cb=taxt_Direction1RB1Click)
        self.Direction1RB2 = TaxtRadioItem(val="true", change_cb=taxt_Direction1RB2Click)
        self._Direction1R = TaxtRadio(items=[self.Direction1RB1, self.Direction1RB2])
        self.Direction1RB1.check(True)
        
        self.Direction2RB1 = TaxtRadioItem(val="unspec", change_cb=taxt_Direction2RB1Click)
        self.Direction2RB3 = TaxtRadioItem(val="spec", change_cb=taxt_Direction2RB3Click)
        self._Direction2R = TaxtRadio(items=[self.Direction2RB1, self.Direction2RB3])
        self.Direction2RB1.check(True)

        # strings
        self.noStoreysE11 = TaxtStr()
        self.noStoreysE12 = TaxtStr()
        self.noStoreysE21 = TaxtStr()
        self.noStoreysE22 = TaxtStr()
        self.noStoreysE31 = TaxtStr()
        self.noStoreysE32 = TaxtStr()
        self.noStoreysE41 = TaxtStr()
        self.DateE1 = TaxtStr()
        self.DateE2 = TaxtStr()
        self.resultE = TaxtStr()


if __name__ == '__main__':
    taxonomy = Taxonomy()
    print taxonomy
