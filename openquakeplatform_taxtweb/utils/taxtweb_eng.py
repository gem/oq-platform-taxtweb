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
    def __init__(self, full):
        if full:
            self.OutTypeCB = TaxtSel(['Full',
                                      'Omit Unknown',
                                      'Short'],
                                     change_cb=taxt_OutTypeCBSelect)
            self.OutTypeCB.selected(2)

        self.DirectionCB = TaxtBool(val=True, change_cb=taxt_SetDirection2)

        self.Direction1RB1 = TaxtRadioItem(val="false", change_cb=taxt_Direction1RB1Click)
        self.Direction1RB2 = TaxtRadioItem(val="true", change_cb=taxt_Direction1RB2Click)
        self._Direction1R = TaxtRadio(items=[self.Direction1RB1, self.Direction1RB2])
        self.Direction1RB1.checked(True)

        self.Direction2RB1 = TaxtRadioItem(val="unspec", change_cb=taxt_Direction2RB1Click)
        self.Direction2RB3 = TaxtRadioItem(val="spec", change_cb=taxt_Direction2RB3Click)
        self._Direction2R = TaxtRadio(items=[self.Direction2RB1, self.Direction2RB3])
        self.Direction2RB1.checked(True)

        self.MaterialCB11 = TaxtSel(['Unknown Material',
                                     'Concrete, unknown reinforcement',
                                     'Concrete, unreinforced',
                                     'Concrete, reinforced',
                                     'Concrete, composite with steel section',
                                     'Steel',
                                     'Metal (except steel)',
                                     'Masonry, unknown reinforcement',
                                     'Masonry, unreinforced',
                                     'Masonry, confined',
                                     'Masonry, reinforced',
                                     'Earth, unknown reinforcement',
                                     'Earth, unreinforced',
                                     'Earth, reinforced',
                                     'Wood',
                                     'Other material'], change_cb=taxt_MaterialCB11Select)
        self.MaterialCB21 = TaxtSel(change_cb=taxt_MaterialCB21Select)
        self.MaterialCB31 = TaxtSel(change_cb=taxt_MaterialCB31Select)
        self.MaterialCB41 = TaxtSel(change_cb=taxt_MaterialCB41Select)
        self.SystemCB11 = TaxtSel(change_cb=taxt_SystemCB11Select)
        self.SystemCB21 = TaxtSel(change_cb=taxt_SystemCB21Select)

        self.MaterialCB12 = TaxtSel(['Unknown Material',
                                     'Concrete, unknown reinforcement',
                                     'Concrete, unreinforced',
                                     'Concrete, reinforced',
                                     'Concrete, composite with steel section',
                                     'Steel',
                                     'Metal (except steel)',
                                     'Masonry, unknown reinforcement',
                                     'Masonry, unreinforced',
                                     'Masonry, confined',
                                     'Masonry, reinforced',
                                     'Earth, unknown reinforcement',
                                     'Earth, unreinforced',
                                     'Earth, reinforced',
                                     'Wood',
                                     'Other material'], change_cb=taxt_MaterialCB12Select)
        self.MaterialCB22 = TaxtSel(change_cb=taxt_MaterialCB22Select)
        self.MaterialCB32 = TaxtSel(change_cb=taxt_MaterialCB32Select)
        self.MaterialCB42 = TaxtSel(change_cb=taxt_MaterialCB42Select)
        self.SystemCB12 = TaxtSel(change_cb=taxt_SystemCB12Select)
        self.SystemCB22 = TaxtSel(change_cb=taxt_SystemCB22Select)

        self.HeightCB1 = TaxtSel(['Unknown number of storeys',
                                  'Range of the number of storeys',
                                  'Exact number of storeys',
                                  'Approximate number of storeys'],
                                 selected=0, change_cb=taxt_HeightCB1Select)
        self.noStoreysE11 = TaxtStr(change_cb=taxt_HeightCB1Select)
        self.noStoreysE12 = TaxtStr(change_cb=taxt_HeightCB1Select)



        self.HeightCB2 = TaxtSel(['Unknown number of storeys',
                                  'Range of the number of storeys',
                                  'Exact number of storeys',
                                  'Approximate number of storeys'],
                                 selected=0, change_cb=taxt_HeightCB2Select)
        self.noStoreysE21 = TaxtStr(change_cb=taxt_HeightCB2Select)
        self.noStoreysE22 = TaxtStr(change_cb=taxt_HeightCB2Select)

        self.HeightCB3 = TaxtSel(['Height above grade unknown',
                                  'Range of height above grade',
                                  'Exact height above grade',
                                  'Approximate height above grade'],
                                 selected=0, change_cb=taxt_HeightCB3Select)
        self.noStoreysE31 = TaxtStr(change_cb=taxt_HeightCB3Select)
        self.noStoreysE32 = TaxtStr(change_cb=taxt_HeightCB3Select)

        self.HeightCB4 = TaxtSel(['Unknown slope',
                                  'Slope of the ground'],
                                  selected=0, change_cb=taxt_HeightCB4Select)
        self.noStoreysE41 = TaxtStr(change_cb=taxt_HeightCB4Select)

        self.DateCB1 = TaxtSel(['Year unknown',
                                'Exact date of construction or retrofit',
                                'Bounds for the date of construction or retrofit',
                                'Latest possible date of construction or retrofit',
                                'Approximate date of construction or retrofit'],
                               selected=0, change_cb=taxt_DateCB1Select)
        self.DateE1 = TaxtStr(change_cb=taxt_DateE1Change)
        self.DateE2 = TaxtStr(change_cb=taxt_DateE2Change)

        self.OccupancyCB1 = TaxtSel(['Unknown occupancy type',
                                     'Residential',
                                     'Commercial and public',
                                     'Mixed use',
                                     'Industrial',
                                     'Agriculture',
                                     'Assembly',
                                     'Government',
                                     'Education',
                                     'Other occupancy type'],
                                    selected=0, change_cb=taxt_OccupancyCB1Select)
        self.OccupancyCB2 = TaxtSel(change_cb=taxt_OccupancyCB2Select)

        self.PositionCB = TaxtSel(['Unknown building position',
                                   'Detached building',
                                   'Adjoining building(s) on one side',
                                   'Adjoining building(s) on two sides',
                                   'Adjoining building(s) on three sides'],
                                  selected=0, change_cb=taxt_PositionCBSelect)

        self.PlanShapeCB = TaxtSel(['Unknown plan shape',
                                    'Square, solid',
                                    'Square, with an opening in plan',
                                    'Rectangular, solid',
                                    'Rectangular, with an opening in plan',
                                    'L-shape',
                                    'Curved, solid (e.g. circular, eliptical, ovoid)',
                                    'Curved, with an opening in plan',
                                    'Triangular, solid',
                                    'Triangular, with an opening in plan',
                                    'E-shape',
                                    'H-shape',
                                    'S-shape',
                                    'T-shape',
                                    'U- or C-shape',
                                    'X-shape',
                                    'Y-shape',
                                    'Polygonal, solid',
                                    'Polygonal, with an opening in plan',
                                    'Irregular plan shape'],
                                   selected=0, change_cb=taxt_PlanShapeCBSelect)

        self.RegularityCB1 = TaxtSel(['Unknown structural irregularity',
                                      'Regular structure',
                                      'Irregular structure'],
                                     selected=0, change_cb=taxt_RegularityCB1Select)
        self.RegularityCB2 = TaxtSel(change_cb=taxt_RegularityCB2Select)
        self.RegularityCB4 = TaxtSel(change_cb=taxt_RegularityCB3Select)
        self.RegularityCB3 = TaxtSel(change_cb=taxt_RegularityCB4Select)
        self.RegularityCB5 = TaxtSel(change_cb=taxt_RegularityCB5Select)

        self.WallsCB = TaxtSel(['Unknown material of exterior walls',
                                'Concrete exterior walls',
                                'Glass exterior walls',
                                'Earthen exterior walls',
                                'Masonry exterior walls',
                                'Metal exterior walls',
                                'Vegetative exterior walls',
                                'Wooden exterior walls',
                                'Stucco finish on light framing for exterior walls',
                                'Plastic/vinyl exterior walls, various',
                                'Cement-based boards for exterior walls',
                                'Material of exterior walls, other'],
                               selected=0, change_cb=taxt_WallsCBSelect)

        self.RoofCB1 = TaxtSel(['Unknown roof shape',
                                'Flat',
                                'Pitched with gable ends',
                                'Pitched and hipped',
                                'Pitched with dormers',
                                'Monopitch',
                                'Sawtooth',
                                'Curved',
                                'Complex regular',
                                'Complex irregular',
                                'Roof shape, other'],
                               selected=0, change_cb=taxt_RoofCB1Select)
        self.RoofCB2 = TaxtSel(['Unknown roof covering',
                                'Concrete roof, no covering',
                                'Clay or concrete tile roof covering',
                                'Fibre cement or metal tile covering',
                                'Membrane roof covering',
                                'Slate roof covering',
                                'Stone slab roof covering',
                                'Metal or asbestos sheet covering',
                                'Wooden or asphalt shingle covering',
                                'Vegetative roof covering',
                                'Earthen roof covering',
                                'Solar panelled roofs',
                                'Tensile membrane or fabric roof',
                                'Roof covering, other'],
                               selected=0, change_cb=taxt_RoofCB2Select)

        self.RoofCB3 = TaxtSel(['Roof material, unknown',
                                'Masonry roof',
                                'Earthen roof',
                                'Concrete roof',
                                'Metal roof',
                                'Wooden roof',
                                'Fabric roof',
                                'Roof material,other'],
                               selected=0, change_cb=taxt_RoofCB3Select)

        self.RoofCB4 = TaxtSel(change_cb=taxt_RoofCB4Select)
        self.RoofCB5 = TaxtSel(['Roof-wall diaphragm connection unknown',
                                'Roof-wall diaphragm connection not provided',
                                'Roof-wall diaphragm connection present',
                                'Roof tie-down unknown',
                                'Roof tie-down not provided',
                                'Roof tie-down present'],
                               selected=0, change_cb=taxt_RoofCB5Select)

        self.FoundationsCB = TaxtSel(['Unknown foundation system',
                                      'Shallow foundation, with lateral capacity',
                                      'Shallow foundation, with no lateral capacity',
                                      'Deep foundation, with lateral capacity',
                                      'Deep foundation, with no lateral capacity',
                                      'Foundation, other'],
                                     selected=0, change_cb=taxt_FoundationsCBSelect)

        self.FloorCB1 = TaxtSel(['Floor material, unknown',
                                 'No elevated or suspended floor material (single-storey)',
                                 'Masonry floor',
                                 'Earthen floor',
                                 'Concrete floor',
                                 'Metal floor',
                                 'Wooden floor',
                                 'Floor material, other'],
                                selected=0, change_cb=taxt_FloorCB1Select)
        self.FloorCB2 = TaxtSel(change_cb=taxt_FloorCB2Select)
        self.FloorCB3 = TaxtSel(['Floor-wall diaphragm connection, unknown',
                                 'Floor-wall diaphragm connection not provided',
                                 'Floor-wall diaphragm connection present'],
                                selected=0, change_cb=taxt_FloorCB3Select)

        self.resultE = TaxtStr()


if __name__ == '__main__':
    taxonomy = Taxonomy(True)
    print taxonomy
