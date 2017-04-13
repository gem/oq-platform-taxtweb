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
        self._items = items[:]
        self._selected = selected
        self._disabled = disabled
        self._change_cb = change_cb

    def empty(self):
        self._items = []
        self._selected = -1

    def disabled(self, disabled=None):
        if disabled == None:
            return self._disabled
        else:
            self._disabled = disabled

    def items(self, items=None):
        '''
        items => list of 1 element dicts
        selected => int identifing current selected item
        '''
        if items == None:
            return self._items
        else:
            self._items = items[:]

    def selected(self, selected=-1):
        if selected != -1:
            self._selected = selected
            if self._change_cb:
                self._change_cb(self)

        return self._selected


class TaxtBool(object):
    def __init__(self, val=False, change_cb=None):
        self._val = val
        self._change_cb = change_cb

    def val(self, val=None):
        if val == None:
            return self._val
        else:
            self._val = val
            if self._change_cb:
                self._change_cb(self)
            return self._val

class TaxtRadioItem(object):
    def __init__(self, val=None, checked=False, radio=None, change_cb=None):
        self._val = val
        self._checked = checked
        self._change_cb = change_cb
        self._radio = radio

    def radio(self, radio=None):
        if (radio == None):
            return self._radio
        else:
            self._radio = radio

    def val(self, val=None):
        if val != None:
            self._val = val
            if self._change_cb:
                self._change_cb(self)

        return self._val

    def checked(self, is_checked=False):
        if is_checked == True:
            if self._radio != None:
                for item in self._radio._items:
                    item.checked(False)
        self._checked = is_checked

        return self._checked


class TaxtRadio(object):
    def __init__(self, items=[]):
        self._items = items[:]
        for item in items:
            item.radio(self)

    def item_add(self, item):
        self.items.append(item)
        item.radio(self)


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
                self.change_cb(self)
            return self.val


def taxt_Direction1RB1Click(taxt_radioitem):
    pass

def taxt_Direction1RB2Click(taxt_radioitem):
    pass

def taxt_Direction2RB1Click(taxt_radioitem):
    pass

def taxt_Direction2RB3Click(taxt_radioitem):
    pass

def taxt_OutTypeCBSelect(obj):
    pass

def taxt_SetDirection2(obj):
    pass

def taxt_MaterialCB11Select(obj):
    pass

def taxt_MaterialCB21Select(obj):
    pass

def taxt_MaterialCB31Select(obj):
    pass

def taxt_MaterialCB41Select(obj):
    pass

def taxt_SystemCB11Select(obj):
    pass

def taxt_SystemCB21Select(obj):
    pass

def taxt_MaterialCB12Select(obj):
    pass

def taxt_MaterialCB22Select(obj):
    pass

def taxt_MaterialCB32Select(obj):
    pass

def taxt_MaterialCB42Select(obj):
    pass

def taxt_SystemCB12Select(obj):
    pass

def taxt_SystemCB22Select(obj):
    pass

def taxt_HeightCB1Select(obj):
    pass

def taxt_HeightCB1Select(obj):
    pass

def taxt_HeightCB1Select(obj):
    pass

def taxt_HeightCB2Select(obj):
    pass

def taxt_HeightCB2Select(obj):
    pass

def taxt_HeightCB2Select(obj):
    pass

def taxt_HeightCB3Select(obj):
    pass

def taxt_HeightCB3Select(obj):
    pass

def taxt_HeightCB3Select(obj):
    pass

def taxt_HeightCB4Select(obj):
    pass

def taxt_HeightCB4Select(obj):
    pass

def taxt_DateCB1Select(obj):
    pass

def taxt_DateE1Change(obj):
    pass

def taxt_DateE2Change(obj):
    pass

def taxt_OccupancyCB1Select(obj):
    pass

def taxt_OccupancyCB2Select(obj):
    pass

def taxt_PositionCBSelect(obj):
    pass

def taxt_PlanShapeCBSelect(obj):
    pass

def taxt_RegularityCB1Select(obj):
    pass

def taxt_RegularityCB2Select(obj):
    pass

def taxt_RegularityCB3Select(obj):
    pass

def taxt_RegularityCB4Select(obj):
    pass

def taxt_RegularityCB5Select(obj):
    pass

def taxt_WallsCBSelect(obj):
    pass

def taxt_RoofCB1Select(obj):
    pass

def taxt_RoofCB2Select(obj):
    pass

def taxt_RoofCB3Select(obj):
    pass

def taxt_RoofCB4Select(obj):
    pass

def taxt_RoofCB5Select(obj):
    pass

def taxt_FoundationsCBSelect(obj):
    pass

def taxt_FloorCB1Select(obj):
    pass

def taxt_FloorCB2Select(obj):
    pass

def taxt_FloorCB3Select(obj):
    pass

class Taxonomy(object):
    def __init__(self):
        # dropdown
        self.MaterialCB11 = TaxtSel(change_cb=taxt_MaterialCB11Select)
        self.MaterialCB21 = TaxtSel(change_cb=taxt_MaterialCB21Select)
        self.MaterialCB31 = TaxtSel(change_cb=taxt_MaterialCB31Select)
        self.MaterialCB41 = TaxtSel(change_cb=taxt_MaterialCB41Select)
        self.SystemCB11 = TaxtSel(change_cb=taxt_SystemCB11Select)
        self.SystemCB21 = TaxtSel(change_cb=taxt_SystemCB21Select)
        self.MaterialCB12 = TaxtSel(change_cb=taxt_MaterialCB12Select)
        self.MaterialCB22 = TaxtSel(change_cb=taxt_MaterialCB22Select)
        self.MaterialCB32 = TaxtSel(change_cb=taxt_MaterialCB32Select)
        self.MaterialCB42 = TaxtSel(change_cb=taxt_MaterialCB42Select)
        self.SystemCB12 = TaxtSel(change_cb=taxt_SystemCB12Select)
        self.SystemCB22 = TaxtSel(change_cb=taxt_SystemCB22Select)
        self.HeightCB1 = TaxtSel(change_cb=taxt_HeightCB1Select)
        self.HeightCB2 = TaxtSel(change_cb=taxt_HeightCB2Select)
        self.HeightCB3 = TaxtSel(change_cb=taxt_HeightCB3Select)
        self.HeightCB4 = TaxtSel(change_cb=taxt_HeightCB4Select)
        self.DateCB1 = TaxtSel(change_cb=taxt_DateCB1Select)
        self.OccupancyCB1 = TaxtSel(change_cb=taxt_OccupancyCB1Select)
        self.OccupancyCB2 = TaxtSel(change_cb=taxt_OccupancyCB2Select)
        self.PositionCB = TaxtSel(change_cb=taxt_PositionCBSelect)
        self.PlanShapeCB = TaxtSel(change_cb=taxt_PlanShapeCBSelect)
        self.RegularityCB1 = TaxtSel(change_cb=taxt_RegularityCB1Select)
        self.RegularityCB2 = TaxtSel(change_cb=taxt_RegularityCB2Select)
        self.RegularityCB4 = TaxtSel(change_cb=taxt_RegularityCB3Select)
        self.RegularityCB3 = TaxtSel(change_cb=taxt_RegularityCB4Select)
        self.RegularityCB5 = TaxtSel(change_cb=taxt_RegularityCB5Select)
        self.WallsCB = TaxtSel(change_cb=taxt_WallsCBSelect)
        self.RoofCB1 = TaxtSel(change_cb=taxt_RoofCB1Select)
        self.RoofCB2 = TaxtSel(change_cb=taxt_RoofCB2Select)
        self.RoofCB3 = TaxtSel(change_cb=taxt_RoofCB3Select)
        self.RoofCB4 = TaxtSel(change_cb=taxt_RoofCB4Select)
        self.RoofCB5 = TaxtSel(change_cb=taxt_RoofCB5Select)
        self.FloorCB1 = TaxtSel(change_cb=taxt_FloorCB1Select)
        self.FloorCB2 = TaxtSel(change_cb=taxt_FloorCB2Select)
        self.FloorCB3 = TaxtSel(change_cb=taxt_FloorCB3Select)
        self.FoundationsCB = TaxtSel(change_cb=taxt_FoundationsCBSelect)
        self.OutTypeCB = TaxtSel(change_cb=taxt_OutTypeCBSelect)

        # boolean
        self.DirectionCB = TaxtBool(change_cb=taxt_SetDirection2)

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
        self.noStoreysE11 = TaxtStr(change_cb=taxt_HeightCB1Select)
        self.noStoreysE12 = TaxtStr(change_cb=taxt_HeightCB1Select)
        self.noStoreysE21 = TaxtStr(change_cb=taxt_HeightCB2Select)
        self.noStoreysE22 = TaxtStr(change_cb=taxt_HeightCB2Select)
        self.noStoreysE31 = TaxtStr(change_cb=taxt_HeightCB3Select)
        self.noStoreysE32 = TaxtStr(change_cb=taxt_HeightCB3Select)
        self.noStoreysE41 = TaxtStr(change_cb=taxt_HeightCB4Select)
        self.DateE1 = TaxtStr(change_cb=taxt_DateE1Change)
        self.DateE2 = TaxtStr(change_cb=taxt_DateE2Change)
        self.resultE = TaxtStr()


if __name__ == '__main__':
    taxonomy = Taxonomy()
    print taxonomy
