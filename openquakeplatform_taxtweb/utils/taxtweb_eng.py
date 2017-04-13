#!/usr/bin/env python
from utils.taxtweb_maps import *
from utils.taxtweb_head import *

taxonomy = None

class TaxtSel(object):
    def __init__(self, name, items=[], val=-1, disabled=False, change_cb=None):
        '''
        items => list of 1 element dicts
        val => int identifing current val item
        '''
        self._name = name
        self._items = items[:]
        if items:
            if val == -1:
                self._val = 0
            else:
                self._val = val
        else:
            self._val = val

        self._disabled = disabled
        self._first_disabled = False
        self._change_cb = change_cb

    def empty(self):
        self._items = []
        self._val = -1

    def disabled(self, disabled=None):
        if disabled == None:
            return self._disabled
        else:
            self._disabled = disabled

    def first_disabled(self, first_disabled=None):
        if first_disabled != None:
            self._first_disabled = first_disabled

        return self._first_disabled

    def items(self, items=None, val=0):
        '''
        items => list of 1 element dicts
        val => int identifing current val item
        '''
        if items == None:
            return self._items
        else:
            self._items = items[:]

        self.val(val)

    def val(self, val=-1):
        # print "%s VAL HERE: %d" % (self._name, val)
        if val != -1:
            if val == 0 and self._first_disabled == True:
                raise ValueError
            self._val = val
            if self._change_cb:
                self._change_cb(self)

        return self._val

    def __str__(self):
        ret = "  %s (Sel)\n" % self._name
        if self._items:
            for k, v in enumerate(self._items):
                if k == self._val:
                    ret += "    %02d) * [%s]\n" % (k, v)
        #        else:
        #           ret += "    %02d)   [%s]\n" % (k, v)
        else:
            ret += "    - no elements -\n"

        return ret


class TaxtBool(object):
    def __init__(self, name, val=False, change_cb=None):
        self._name = name
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

    def __str__(self):
        return "  %s (Bool)\n    %s\n" % (self._name, "True" if self._val else "False")


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
    def __init__(self, val=None, change_cb=None, disabled=None):
        self._val = val
        self._change_cb = change_cb
        self._disabled = disabled

    def val(self, val=None):
        if val == None:
            return self._val
        else:
            self._val = val
            if self._change_cb:
                self._change_cb(self)
            return self._val

    def disabled(self, disabled=None):
        if disabled == None:
            return self._disabled
        else:
            self._disabled = disabled


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

def taxt_HeightCB2Select(obj):
    pass

def taxt_HeightCB3Select(obj):
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
    def __init__(self, name, full):
        self._name = name
        if full:
            self.OutTypeCB = TaxtSel('OutTypeCB', ['Full',
                                      'Omit Unknown',
                                      'Short'],
                                     change_cb=taxt_OutTypeCBSelect)
            self.OutTypeCB.val(2)

        self.DirectionCB = TaxtBool("DirectionCB", val=True, change_cb=taxt_SetDirection2)

        self.Direction1RB1 = TaxtRadioItem(val="false", change_cb=taxt_Direction1RB1Click)
        self.Direction1RB2 = TaxtRadioItem(val="true", change_cb=taxt_Direction1RB2Click)
        self._Direction1R = TaxtRadio(items=[self.Direction1RB1, self.Direction1RB2])
        self.Direction1RB1.checked(True)

        self.Direction2RB1 = TaxtRadioItem(val="unspec", change_cb=taxt_Direction2RB1Click)
        self.Direction2RB3 = TaxtRadioItem(val="spec", change_cb=taxt_Direction2RB3Click)
        self._Direction2R = TaxtRadio(items=[self.Direction2RB1, self.Direction2RB3])
        self.Direction2RB1.checked(True)

        self.MaterialCB11 = TaxtSel('MaterialCB11',
                                    ['Unknown Material',
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
                                     'Other material'], val=0, change_cb=taxt_MaterialCB11Select)
        self.MaterialCB21 = TaxtSel('MaterialCB21', change_cb=taxt_MaterialCB21Select)
        self.MaterialCB31 = TaxtSel('MaterialCB31', change_cb=taxt_MaterialCB31Select)
        self.MaterialCB41 = TaxtSel('MaterialCB41', change_cb=taxt_MaterialCB41Select)
        self.SystemCB11 = TaxtSel('SystemCB11', change_cb=taxt_SystemCB11Select)
        self.SystemCB21 = TaxtSel('SystemCB21', change_cb=taxt_SystemCB21Select)

        self.MaterialCB12 = TaxtSel('MaterialCB12', ['Unknown Material',
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
        self.MaterialCB22 = TaxtSel('MaterialCB22', change_cb=taxt_MaterialCB22Select)
        self.MaterialCB32 = TaxtSel('MaterialCB32', change_cb=taxt_MaterialCB32Select)
        self.MaterialCB42 = TaxtSel('MaterialCB42', change_cb=taxt_MaterialCB42Select)
        self.SystemCB12 = TaxtSel('SystemCB12', change_cb=taxt_SystemCB12Select)
        self.SystemCB22 = TaxtSel('SystemCB22', change_cb=taxt_SystemCB22Select)

        self.HeightCB1 = TaxtSel('HeightCB1', ['Unknown number of storeys',
                                  'Range of the number of storeys',
                                  'Exact number of storeys',
                                  'Approximate number of storeys'],
                                 val=0, change_cb=taxt_HeightCB1Select)
        self.noStoreysE11 = TaxtStr(change_cb=taxt_HeightCB1Select)
        self.noStoreysE12 = TaxtStr(change_cb=taxt_HeightCB1Select)



        self.HeightCB2 = TaxtSel('HeightCB2', ['Unknown number of storeys',
                                  'Range of the number of storeys',
                                  'Exact number of storeys',
                                  'Approximate number of storeys'],
                                 val=0, change_cb=taxt_HeightCB2Select)
        self.noStoreysE21 = TaxtStr(change_cb=taxt_HeightCB2Select)
        self.noStoreysE22 = TaxtStr(change_cb=taxt_HeightCB2Select)

        self.HeightCB3 = TaxtSel('HeightCB3', ['Height above grade unknown',
                                  'Range of height above grade',
                                  'Exact height above grade',
                                  'Approximate height above grade'],
                                 val=0, change_cb=taxt_HeightCB3Select)
        self.noStoreysE31 = TaxtStr(change_cb=taxt_HeightCB3Select)
        self.noStoreysE32 = TaxtStr(change_cb=taxt_HeightCB3Select)

        self.HeightCB4 = TaxtSel('HeightCB4', ['Unknown slope',
                                  'Slope of the ground'],
                                  val=0, change_cb=taxt_HeightCB4Select)
        self.noStoreysE41 = TaxtStr(change_cb=taxt_HeightCB4Select)

        self.DateCB1 = TaxtSel('DateCB1', ['Year unknown',
                                'Exact date of construction or retrofit',
                                'Bounds for the date of construction or retrofit',
                                'Latest possible date of construction or retrofit',
                                'Approximate date of construction or retrofit'],
                               val=0, change_cb=taxt_DateCB1Select)
        self.DateE1 = TaxtStr(change_cb=taxt_DateE1Change)
        self.DateE2 = TaxtStr(change_cb=taxt_DateE2Change)

        self.OccupancyCB1 = TaxtSel('OccupancyCB1', ['Unknown occupancy type',
                                     'Residential',
                                     'Commercial and public',
                                     'Mixed use',
                                     'Industrial',
                                     'Agriculture',
                                     'Assembly',
                                     'Government',
                                     'Education',
                                     'Other occupancy type'],
                                    val=0, change_cb=taxt_OccupancyCB1Select)
        self.OccupancyCB2 = TaxtSel('OccupancyCB2', change_cb=taxt_OccupancyCB2Select)

        self.PositionCB = TaxtSel('PositionCB', ['Unknown building position',
                                   'Detached building',
                                   'Adjoining building(s) on one side',
                                   'Adjoining building(s) on two sides',
                                   'Adjoining building(s) on three sides'],
                                  val=0, change_cb=taxt_PositionCBSelect)

        self.PlanShapeCB = TaxtSel('PlanShapeCB', ['Unknown plan shape',
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
                                   val=0, change_cb=taxt_PlanShapeCBSelect)

        self.RegularityCB1 = TaxtSel('RegularityCB1', ['Unknown structural irregularity',
                                      'Regular structure',
                                      'Irregular structure'],
                                     val=0, change_cb=taxt_RegularityCB1Select)
        self.RegularityCB2 = TaxtSel('RegularityCB2', change_cb=taxt_RegularityCB2Select)
        self.RegularityCB4 = TaxtSel('RegularityCB4', change_cb=taxt_RegularityCB3Select)
        self.RegularityCB3 = TaxtSel('RegularityCB3', change_cb=taxt_RegularityCB4Select)
        self.RegularityCB5 = TaxtSel('RegularityCB5', change_cb=taxt_RegularityCB5Select)

        self.WallsCB = TaxtSel('WallsCB', ['Unknown material of exterior walls',
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
                               val=0, change_cb=taxt_WallsCBSelect)

        self.RoofCB1 = TaxtSel('RoofCB1', ['Unknown roof shape',
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
                               val=0, change_cb=taxt_RoofCB1Select)
        self.RoofCB2 = TaxtSel('RoofCB2', ['Unknown roof covering',
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
                               val=0, change_cb=taxt_RoofCB2Select)

        self.RoofCB3 = TaxtSel('RoofCB3', ['Roof material, unknown',
                                'Masonry roof',
                                'Earthen roof',
                                'Concrete roof',
                                'Metal roof',
                                'Wooden roof',
                                'Fabric roof',
                                'Roof material,other'],
                               val=0, change_cb=taxt_RoofCB3Select)

        self.RoofCB4 = TaxtSel('RoofCB4', change_cb=taxt_RoofCB4Select)
        self.RoofCB5 = TaxtSel('RoofCB5', ['Roof-wall diaphragm connection unknown',
                                'Roof-wall diaphragm connection not provided',
                                'Roof-wall diaphragm connection present',
                                'Roof tie-down unknown',
                                'Roof tie-down not provided',
                                'Roof tie-down present'],
                               val=0, change_cb=taxt_RoofCB5Select)

        self.FoundationsCB = TaxtSel('FoundationsCB', ['Unknown foundation system',
                                      'Shallow foundation, with lateral capacity',
                                      'Shallow foundation, with no lateral capacity',
                                      'Deep foundation, with lateral capacity',
                                      'Deep foundation, with no lateral capacity',
                                      'Foundation, other'],
                                     val=0, change_cb=taxt_FoundationsCBSelect)

        self.FloorCB1 = TaxtSel('FloorCB1', ['Floor material, unknown',
                                 'No elevated or suspended floor material (single-storey)',
                                 'Masonry floor',
                                 'Earthen floor',
                                 'Concrete floor',
                                 'Metal floor',
                                 'Wooden floor',
                                 'Floor material, other'],
                                val=0, change_cb=taxt_FloorCB1Select)
        self.FloorCB2 = TaxtSel('FloorCB2', change_cb=taxt_FloorCB2Select)
        self.FloorCB3 = TaxtSel('FloorCB3', ['Floor-wall diaphragm connection, unknown',
                                 'Floor-wall diaphragm connection not provided',
                                 'Floor-wall diaphragm connection present'],
                                val=0, change_cb=taxt_FloorCB3Select)

        self.resultE = TaxtStr()

        self.taxt_ValidateMaterial1()
        self.taxt_ValidateMaterial2()
        self.taxt_ValidateRoof()
        self.taxt_ValidateFloor()
        self.taxt_ValidateHeight()
        self.taxt_ValidateDate()

    def __str__(self):
        ret = "%s (Taxonomy)\n" % self._name
        ret += self.OutTypeCB.__str__()
        ret += self.DirectionCB.__str__()
        ret += self.MaterialCB11.__str__()
        ret += self.MaterialCB21.__str__()
        ret += self.MaterialCB31.__str__()
        ret += self.MaterialCB41.__str__()
        ret += self.SystemCB11.__str__()
        ret += self.SystemCB21.__str__()
        ret += self.MaterialCB12.__str__()
        ret += self.MaterialCB22.__str__()
        ret += self.MaterialCB32.__str__()
        ret += self.MaterialCB42.__str__()
        ret += self.SystemCB12.__str__()
        ret += self.SystemCB22.__str__()
        ret += self.HeightCB1.__str__()
        ret += self.HeightCB2.__str__()
        ret += self.HeightCB3.__str__()
        ret += self.HeightCB4.__str__()
        ret += self.DateCB1.__str__()
        ret += self.OccupancyCB1.__str__()
        ret += self.OccupancyCB2.__str__()
        ret += self.PositionCB.__str__()
        ret += self.PlanShapeCB.__str__()
        ret += self.RegularityCB1.__str__()
        ret += self.RegularityCB2.__str__()
        ret += self.RegularityCB4.__str__()
        ret += self.RegularityCB3.__str__()
        ret += self.RegularityCB5.__str__()
        ret += self.WallsCB.__str__()
        ret += self.RoofCB1.__str__()
        ret += self.RoofCB2.__str__()
        ret += self.RoofCB3.__str__()
        ret += self.RoofCB4.__str__()
        ret += self.RoofCB5.__str__()
        ret += self.FoundationsCB.__str__()
        ret += self.FloorCB1.__str__()
        ret += self.FloorCB2.__str__()
        ret += self.FloorCB3.__str__()

        return ret

    def taxt_ValidateSystem1(self):

        self.SystemCB21.empty()

        if self.SystemCB11.val() == 0 or self.SystemCB11.val() == 1:
            self.SystemCB21.disabled(True)

        else:
            self.SystemCB21.items([
                'Ductility unknown',
                'Ductile',
                'Non-ductile',
                'Base isolation and/or energy dissipation devices',
            ], val=0)
            self.SystemCB21.disabled(False)


    def taxt_ValidateSystem2(self):

        self.SystemCB22.empty()

        if self.SystemCB12.val() == 0 or self.SystemCB12.val() == 1:
            self.SystemCB22.disabled(True)

        else:
            self.SystemCB22.items([
                'Ductility unknown',
                'Ductile',
                'Non-ductile',
                'Base isolation and/or energy dissipation devices',
            ], val=0)
            self.SystemCB22.disabled(False)


    def taxt_ValidateMaterial1(self):
        self.MaterialCB21.empty()
        self.MaterialCB31.empty()
        self.MaterialCB41.empty()
        self.SystemCB11.empty()

        if self.MaterialCB11.val() == 0:
            self.MaterialCB21.disabled(True)
            self.MaterialCB31.disabled(True)
            self.MaterialCB41.disabled(True)

        elif self.MaterialCB11.val() == 2:
            self.MaterialCB21.items([
                'Unknown concrete technology',
                'Cast-in-place concrete',
                'Precast concrete',
            ], val=0)
            self.MaterialCB21.disabled(False)

        elif self.MaterialCB11.val() == 1 or  self.MaterialCB11.val() == 3 or self.MaterialCB11.val() == 4:
            self.MaterialCB21.items([
                'Unknown concrete technology',
                'Cast-in-place concrete',
                'Precast concrete',
                'Cast-in-place prestressed concrete',
                'Precast prestressed concrete',
            ], val=0)
            self.MaterialCB21.disabled(False)

        elif self.MaterialCB11.val() == 5:
            self.MaterialCB21.items([
                'Steel, unknown ',
                'Cold-formed steel members',
                'Hot-rolled steel members',
                'Steel, other ',
            ], val=0)
            self.MaterialCB21.disabled(False)

        elif self.MaterialCB11.val() == 6:
            self.MaterialCB21.items([
                'Metal, unknown ',
                'Iron',
                'Metal, other ',
            ], val=0)
            self.MaterialCB21.disabled(False)

        elif (self.MaterialCB11.val() > 6 and
                 self.MaterialCB11.val() < 11):
            self.MaterialCB21.items([
                'Masonry unit, unknown',
                'Adobe blocks',
                'Stone, unknown technology',
                'Rubble (field stone) or semi-dressed stone',
                'Dressed stone',
                'Fired clay unit, unknown type',
                'Fired clay solid bricks',
                'Fired clay hollow bricks',
                'Fired clay hollow blocks or tiles',
                'Concrete blocks, unknown type',
                'Concrete blocks, solid',
                'Concrete blocks, hollow',
                'Masonry unit, other',
            ], val=0)
            self.MaterialCB21.disabled(False)

            if self.MaterialCB11.val() == 10:
                self.MaterialCB41.items([
                'Unknown reinforcement',
                'Steel-reinforced',
                'Wood-reinforced',
                'Bamboo-, cane- or rope-reinforced',
                'Fibre reinforcing mesh',
                'Reinforced concrete bands',
                ], val=0)
                self.MaterialCB41.disabled(False)


        elif self.MaterialCB11.val() > 10 and self.MaterialCB11.val() < 14:
            self.MaterialCB21.items([
                'Unknown earth technology',
                'Rammed earth',
                'Cob or wet construction',
                'Earth technology, other',
            ], val=0)
            self.MaterialCB21.disabled(False)

        elif self.MaterialCB11.val() == 14:
            self.MaterialCB21.items([
                'Wood, unknown',
                'Heavy wood',
                'Light wood members',
                'Solid wood',
                'Wattle and daub',
                'Bamboo',
                'Wood, other',
            ], val=0)
            self.MaterialCB21.disabled(False)

        else:
            self.MaterialCB21.disabled(True)
            self.MaterialCB31.disabled(True)
            self.MaterialCB41.disabled(True)


        if self.MaterialCB11.val() == 5:
            self.MaterialCB31.items([
                'Unknown connection',
                'Welded connections',
                'Riveted connections',
                'Bolted connections',
            ], val=0)
            self.MaterialCB31.disabled(False)

        elif (self.MaterialCB11.val() > 6 and
                 self.MaterialCB11.val() < 11):
            self.MaterialCB31.items([
                'Mortar type, unknown',
                'No mortar',
                'Mud mortar',
                'Lime mortar',
                'Cement mortar',
                'Cement:lime mortar',
                'Stone, unknown type',
                'Limestone',
                'Sandstone',
                'Tuff',
                'Slate',
                'Granite',
                'Basalt',
                'Stone, other type',
            ], val=0)
            self.MaterialCB31.disabled(False)

        else:
            self.MaterialCB31.disabled(True)


        if self.MaterialCB11.val() > 10 and self.MaterialCB11.val() < 14:
            self.SystemCB11.items([
                'Unknown lateral load-resisting system',
                'No lateral load-resisting system',
                'Wall',
                'Hybrid lateral load-resisting system',
                'Other lateral load-resisting system',
            ], val=0)

        elif ((self.MaterialCB11.val() > 6 and self.MaterialCB11.val() < 11) or
                 self.MaterialCB11.val() == 14):
            self.SystemCB11.items([
                'Unknown lateral load-resisting system',
                'No lateral load-resisting system',
                'Moment frame',
                'Post and beam',
                'Wall',
                'Hybrid lateral load-resisting system',
                'Other lateral load-resisting system',
            ], val=0)

        else:
            self.SystemCB11.items([
                'Unknown lateral load-resisting system',
                'No lateral load-resisting system',
                'Moment frame',
                'Infilled frame',
                'Braced frame',
                'Post and beam',
                'Wall',
                'Dual frame-wall system',
                'Flat slab/plate or waffle slab',
                'Infilled flat slab/plate or infilled waffle slab',
                'Hybrid lateral load-resisting system',
                'Other lateral load-resisting system',
            ], val=0)


        self.SystemCB11.val(0)
        self.taxt_ValidateSystem1()


    def taxt_ValidateMaterial2(self):
        self.MaterialCB22.empty()
        self.MaterialCB32.empty()
        self.MaterialCB42.empty()
        self.SystemCB12.empty()

        if self.MaterialCB12.val() == 0:
            self.MaterialCB22.disabled(True)
            self.MaterialCB32.disabled(True)
            self.MaterialCB42.disabled(True)

        elif self.MaterialCB12.val() == 2:
            self.MaterialCB22.items([
                'Unknown concrete technology',
                'Cast-in-place concrete',
                'Precast concrete',
            ], val=0)
            self.MaterialCB22.disabled(False)

        elif self.MaterialCB12.val() == 1 or  self.MaterialCB12.val() == 3 or self.MaterialCB12.val() == 4:
            self.MaterialCB22.items([
                'Unknown concrete technology',
                'Cast-in-place concrete',
                'Precast concrete',
                'Cast-in-place prestressed concrete',
                'Precast prestressed concrete',
            ], val=0)
            self.MaterialCB22.disabled(False)

        elif self.MaterialCB12.val() == 5:
            self.MaterialCB22.items([
                'Steel, unknown ',
                'Cold-formed steel members',
                'Hot-rolled steel members',
                'Steel, other ',
            ], val=0)
            self.MaterialCB22.disabled(False)

        elif self.MaterialCB12.val() == 6:
            self.MaterialCB22.items([
                'Metal, unknown ',
                'Iron',
                'Metal, other ',
            ], val=0)
            self.MaterialCB22.disabled(False)

        elif (self.MaterialCB12.val() > 6 and
                 self.MaterialCB12.val() < 11):
            self.MaterialCB22.items([
                'Masonry unit, unknown',
                'Adobe blocks',
                'Stone, unknown technology',
                'Rubble (field stone) or semi-dressed stone',
                'Dressed stone',
                'Fired clay unit, unknown type',
                'Fired clay solid bricks',
                'Fired clay hollow bricks',
                'Fired clay hollow blocks or tiles',
                'Concrete blocks, unknown type',
                'Concrete blocks, solid',
                'Concrete blocks, hollow',
                'Masonry unit, other',
            ], val=0)
            self.MaterialCB22.disabled(False)

            if self.MaterialCB12.val() == 10:
                self.MaterialCB42.items([
                'Unknown reinforcement',
                'Steel-reinforced',
                'Wood-reinforced',
                'Bamboo-, cane- or rope-reinforced',
                'Fibre reinforcing mesh',
                'Reinforced concrete bands',
                ], val=0)
                self.MaterialCB42.disabled(False)


        elif self.MaterialCB12.val() > 10 and self.MaterialCB12.val() < 14:
            self.MaterialCB22.items([
                'Unknown earth technology',
                'Rammed earth',
                'Cob or wet construction',
                'Earth technology, other',
            ], val=0)
            self.MaterialCB22.disabled(False)

        elif self.MaterialCB12.val() == 14:
            self.MaterialCB22.items([
                'Wood, unknown',
                'Heavy wood',
                'Light wood members',
                'Solid wood',
                'Wattle and daub',
                'Bamboo',
                'Wood, other',
            ], val=0)
            self.MaterialCB22.disabled(False)

        else:
            self.MaterialCB22.disabled(True)
            self.MaterialCB32.disabled(True)
            self.MaterialCB42.disabled(True)


        if self.MaterialCB12.val() == 5:
            self.MaterialCB32.items([
                'Unknown connection',
                'Welded connections',
                'Riveted connections',
                'Bolted connections',
            ], val=0)
            self.MaterialCB32.disabled(False)

        elif (self.MaterialCB12.val() > 6 and
                 self.MaterialCB12.val() < 11):
            self.MaterialCB32.items([
                'Mortar type, unknown',
                'No mortar',
                'Mud mortar',
                'Lime mortar',
                'Cement mortar',
                'Cement:lime mortar',
                'Stone, unknown type',
                'Limestone',
                'Sandstone',
                'Tuff',
                'Slate',
                'Granite',
                'Basalt',
                'Stone, other type',
            ], val=0)
            self.MaterialCB32.disabled(False)

        else:
            self.MaterialCB32.disabled(True)


        if self.MaterialCB12.val() > 10 and self.MaterialCB12.val() < 14:
            self.SystemCB12.items([
                'Unknown lateral load-resisting system',
                'No lateral load-resisting system',
                'Wall',
                'Hybrid lateral load-resisting system',
                'Other lateral load-resisting system',
            ], val=0)

        elif ((self.MaterialCB12.val() > 6 and self.MaterialCB12.val() < 11) or
                 self.MaterialCB12.val() == 14):
            self.SystemCB12.items([
                'Unknown lateral load-resisting system',
                'No lateral load-resisting system',
                'Moment frame',
                'Post and beam',
                'Wall',
                'Hybrid lateral load-resisting system',
                'Other lateral load-resisting system',
            ], val=0)

        else:
            self.SystemCB12.items([
                'Unknown lateral load-resisting system',
                'No lateral load-resisting system',
                'Moment frame',
                'Infilled frame',
                'Braced frame',
                'Post and beam',
                'Wall',
                'Dual frame-wall system',
                'Flat slab/plate or waffle slab',
                'Infilled flat slab/plate or infilled waffle slab',
                'Hybrid lateral load-resisting system',
                'Other lateral load-resisting system',
            ], val=0)


        self.SystemCB12.val(0)
        self.taxt_ValidateSystem2()


    def taxt_ValidateRoof(self):
        self.RoofCB4.empty()
        if self.RoofCB3.val() == 0 or self.RoofCB3.val() == 7:
            self.RoofCB4.disabled(True)

        elif self.RoofCB3.val() == 1:
            self.RoofCB4.items([
                'Masonry roof, unknown',
                'Vaulted masonry roof',
                'Shallow-arched masonry roof',
                'Composite masonry and concrete roof system',
            ], selected=0)
            self.RoofCB4.disabled(False)

        elif self.RoofCB3.val() == 2:
            self.RoofCB4.items([
                'Earthen roof, unknown',
                'Vaulted earthen roofs',
            ], selected=0)
            self.RoofCB4.disabled(False)

        elif self.RoofCB3.val() == 3:
            self.RoofCB4.items([
                'Concrete roof, unknown',
                'Cast-in-place beamless RC roof',
                'Cast-in-place beam-supported RC roof',
                'Precast concrete roof with RC topping',
                'Precast concrete roof without RC topping',
            ], selected=0)
            self.RoofCB4.disabled(False)

        elif self.RoofCB3.val() == 4:
            self.RoofCB4.items([
                'Metal roof, unknown',
                'Metal beams or trusses supporting light roofing',
                'Metal roof beams supporting precast concrete slabs',
                'Composite steel roof deck and concrete slab',
            ], selected=0)
            self.RoofCB4.disabled(False)

        elif self.RoofCB3.val() == 5:
            self.RoofCB4.items([
                'Wooden roof, unknown',
                'Wooden structure with light roof covering',
                'Wooden beams or trusses with heavy roof covering',
                'Wood-based sheets on rafters or purlins',
                'Plywood panels or other light-weigth panels for roof',
                'Bamboo, straw or thatch roof',
            ], selected=0)
            self.RoofCB4.disabled(False)

        elif self.RoofCB3.val() == 6:
            self.RoofCB4.items([
                'Inflatable or tensile membrane roof',
                'Fabric roof, other',
            ], selected=0)
            self.RoofCB4.disabled(False)


    def taxt_ValidateFloor(self):
        self.FloorCB2.empty()

        if (self.FloorCB1.val() == 0 or self.FloorCB1.val() == 1 or self.FloorCB1.val() == 7):
            self.FloorCB2.disabled(True)
        elif self.FloorCB1.val() == 2:
            self.FloorCB2.items([
                'Masonry floor, unknown',
                'Vaulted masonry floor',
                'Shallow-arched masonry floor',
                'Composite cast-in place RC and masonry floor',
            ], selected=0)
            self.FloorCB2.disabled(False)

        elif self.FloorCB1.val() == 3:
            self.FloorCB2.items([
                'Earthen floor, unknown',
            ], selected=0)
            self.FloorCB2.disabled(False)

        elif self.FloorCB1.val() == 4:
            self.FloorCB2.items([
                'Concrete floor, unknown',
                'Cast-in-place beamless RC floor',
                'Cast-in-place beam-supported RC floor',
                'Precast concrete floor with RC topping',
                'Precast concrete floor without RC topping',
            ], selected=0)
            self.FloorCB2.disabled(False)

        elif self.FloorCB1.val() == 5:
            self.FloorCB2.items([
                'Metal floor, unknown',
                'Metal beams, trusses or joists supporting light flooring',
                'Metal floor beams supporting precast concrete slabs',
                'Composite steel deck and concrete slab',
            ], selected=0)
            self.FloorCB2.disabled(False)

        elif self.FloorCB1.val() == 6:
            self.FloorCB2.items([
                'Wooden floor, unknown',
                'Wood beams/trusses & joists supporting light flooring',
                'Wood beams/trusses & joists supporting heavy flooring',
                'Wood-based sheets on joists or beams',
                'Plywood panels or other light-weigth panels for floor',
            ], selected=0)
            self.FloorCB2.disabled(False)


    def taxt_ValidateHeight(self):
        self.HeightCB2.disabled(True)
        self.HeightCB3.disabled(True)
        self.HeightCB4.disabled(True)
        self.noStoreysE11.disabled(True)
        # self.noStoreysE11.removeClass('gem_field_alert')
        self.noStoreysE12.disabled(True)
        # self.noStoreysE12.removeClass('gem_field_alert')

        self.noStoreysE21.disabled(True)
        # self.noStoreysE21.removeClass('gem_field_alert')
        self.noStoreysE22.disabled(True)
        # self.noStoreysE22.removeClass('gem_field_alert')

        self.noStoreysE31.disabled(True)
        # self.noStoreysE31.removeClass('gem_field_alert')
        self.noStoreysE32.disabled(True)
        # self.noStoreysE32.removeClass('gem_field_alert')
        self.noStoreysE41.disabled(True)
        # self.noStoreysE41.removeClass('gem_field_alert')

        if self.HeightCB1.val() > 0:
            self.HeightCB2.disabled(False)
            self.HeightCB3.disabled(False)
            self.HeightCB4.disabled(False)
            self.noStoreysE11.disabled(False)
            self.noStoreysE12.disabled(False)

            if self.HeightCB1.val() == 1:
                self.noStoreysE11.disabled(False)
                self.noStoreysE12.disabled(False)

            else:
                self.noStoreysE11.disabled(False)
                self.noStoreysE12.disabled(True)


            if self.HeightCB2.val() == 0:
                self.noStoreysE21.disabled(True)
                self.noStoreysE22.disabled(True)

            elif self.HeightCB2.val() == 1:
                self.noStoreysE21.disabled(False)
                self.noStoreysE22.disabled(False)

            else:
                self.noStoreysE21.disabled(False)
                self.noStoreysE22.disabled(True)


            if self.HeightCB3.val() == 0:
                self.noStoreysE31.disabled(True)
                self.noStoreysE32.disabled(True)

            elif self.HeightCB3.val() == 1:
                self.noStoreysE31.disabled(False)
                self.noStoreysE32.disabled(False)

            else:
                self.noStoreysE31.disabled(False)
                self.noStoreysE32.disabled(True)


            if self.HeightCB4.val() == 0:
                self.noStoreysE41.disabled(True)

            else:
                self.noStoreysE41.disabled(False)


        else:
            self.noStoreysE11.disabled(True)
            self.noStoreysE12.disabled(True)


    def taxt_ValidateDate(self):
        if self.DateCB1.val() == 0:
            self.DateE1.disabled(True)
            self.DateE2.disabled(True)

        elif self.DateCB1.val() == 2:
            self.DateE1.disabled(False)
            self.DateE2.disabled(False)

        else:
            self.DateE1.disabled(False)
            self.DateE2.disabled(True)


if __name__ == '__main__':
    taxonomy = Taxonomy('taxonomy', True)
    print taxonomy
