#!/usr/bin/env python
from utils.taxtweb_maps import *
from utils.taxtweb_head import *

taxonomy = None

def is_not_negative_int(s):
    try:
        if int(s) < 0 or int(s) != float(s):
            return False
        else:
            return True
    except ValueError:
        return False

def is_not_negative_float(s):
    try:
        if float(s) < 0.0:
            return False
        else:
            return True
    except ValueError:
        return False

def is_in_rect_angle_float(s):
    if not is_not_negative_float(s):
        return False

    if float(s) > 90.0:
        return False
    return True

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

    def checked(self, is_checked=None):
        if is_checked is not None:
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


def taxt_Direction1RB1Click(taxt_radioitem=None):
    taxonomy.Direction2RB1.checked(True)
    taxonomy.taxt_BuildTaxonomy()

def taxt_Direction1RB2Click(taxt_radioitem=None):
    taxonomy.Direction2RB3.checked(True)
    taxonomy.taxt_BuildTaxonomy()

def taxt_Direction2RB1Click(taxt_radioitem=None):
    taxonomy.Direction1RB1.checked(True)
    taxonomy.taxt_BuildTaxonomy()

def taxt_Direction2RB3Click(taxt_radioitem=None):
    taxonomy.Direction1RB2.checked(True)
    taxonomy.taxt_BuildTaxonomy()

def taxt_OutTypeCBSelect(obj=None):
    taxonomy.taxt_BuildTaxonomy()

def taxt_SetDirection2(obj=None):
    if taxonomy.DirectionCB.checked():
        taxonomy.MaterialCB12.val(taxonomy.MaterialCB11.val())
        taxt_MaterialCB12Select()
        taxonomy.MaterialCB22.val(taxonomy.MaterialCB21.val())
        taxt_MaterialCB22Select()
        taxonomy.MaterialCB32.val(taxonomy.MaterialCB31.val())
        taxt_MaterialCB32Select()
        taxonomy.MaterialCB42.val(taxonomy.MaterialCB41.val())
        taxt_MaterialCB42Select()
        taxonomy.SystemCB12.val(taxonomy.SystemCB11.val())
        taxt_SystemCB12Select()
        taxonomy.SystemCB22.val(taxonomy.SystemCB21.val())
        taxt_SystemCB22Select()

def taxt_MaterialCB11Select(obj):
    taxonomy.taxt_ValidateMaterial1()
    taxt_SetDirection2()
    if taxonomy.DirectionCB.checked():
        taxonomy.taxt_ValidateMaterial2()

    taxonomy.taxt_BuildTaxonomy()

def taxt_MaterialCB21Select(obj=None):
    taxt_SetDirection2()
    taxonomy.taxt_BuildTaxonomy()

def taxt_MaterialCB31Select(obj=None):
    taxt_SetDirection2()
    taxonomy.taxt_BuildTaxonomy()

def taxt_MaterialCB41Select(obj=None):
    taxt_SetDirection2()
    taxonomy.taxt_BuildTaxonomy()

def taxt_SystemCB11Select(obj=None):
    taxt_SetDirection2()
    taxonomy.taxt_ValidateSystem1()
    if taxonomy.DirectionCB.checked():
        taxonomy.taxt_ValidateSystem2()
    taxonomy.taxt_BuildTaxonomy()

def taxt_SystemCB21Select(obj=None):
    taxt_SetDirection2()
    taxonomy.taxt_BuildTaxonomy()

def taxt_BreakDirection2(obj=None):
        # /* the check is performed just when called with parameter (triggered indirectly
        #   from an event or if forced by another function */
        if obj is None:
            return

        if taxonomy.DirectionCB.checked():
            if (taxonomy.MaterialCB12.val() != taxonomy.MaterialCB11.val() or
                taxonomy.MaterialCB22.val() != taxonomy.MaterialCB21.val() or
                taxonomy.MaterialCB32.val() != taxonomy.MaterialCB31.val() or
                taxonomy.MaterialCB42.val() != taxonomy.MaterialCB41.val() or
                taxonomy.SystemCB12.val() != taxonomy.SystemCB11.val() or
                taxonomy.SystemCB22.val() != taxonomy.SystemCB21.val()):
                taxonomy.DirectionCB.checked(False)


def taxt_MaterialCB12Select(obj=None):
    taxonomy.taxt_ValidateMaterial2()
    taxt_BreakDirection2(obj)
    taxonomy.taxt_ValidateSystem2()
    taxonomy.taxt_BuildTaxonomy()

def taxt_MaterialCB22Select(obj):
    taxt_BreakDirection2(obj)
    taxonomy.taxt_BuildTaxonomy()

def taxt_MaterialCB32Select(obj):
    taxt_BreakDirection2(obj)
    taxonomy.taxt_BuildTaxonomy()

def taxt_MaterialCB42Select(obj):
    taxt_BreakDirection2(obj)
    taxonomy.taxt_BuildTaxonomy()

def taxt_SystemCB12Select(obj):
    taxonomy.taxt_ValidateSystem2()
    taxt_BreakDirection2(obj)
    taxonomy.taxt_BuildTaxonomy()

def taxt_SystemCB22Select(obj):
    taxt_BreakDirection2(obj)
    taxonomy.taxt_BuildTaxonomy()

def taxt_HeightCB1Select(obj):
    taxonomy.taxt_ValidateHeight()
    taxonomy.taxt_BuildTaxonomy()

def taxt_HeightCB2Select(obj):
    taxonomy.taxt_ValidateHeight()
    taxonomy.taxt_BuildTaxonomy()

def taxt_HeightCB3Select(obj):
    taxonomy.taxt_ValidateHeight()
    taxonomy.taxt_BuildTaxonomy()

def taxt_HeightCB4Select(obj):
    taxonomy.taxt_ValidateHeight()
    taxonomy.taxt_BuildTaxonomy()

def taxt_DateCB1Select(obj):
    taxonomy.taxt_ValidateDate()
    taxonomy.taxt_BuildTaxonomy()

def taxt_DateE1Change(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_DateE2Change(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_OccupancyCB1Select(obj):
    taxonomy.taxt_ValidateOccupancy()
    taxonomy.taxt_BuildTaxonomy()

def taxt_OccupancyCB2Select(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_PositionCBSelect(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_PlanShapeCBSelect(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_RegularityCB1Select(obj):
    taxonomy.taxt_ValidateRegularity()
    taxonomy.taxt_BuildTaxonomy()

def taxt_RegularityCB2Select(obj):
    taxonomy.taxt_RegularityCB2Select(obj)

def taxt_RegularityCB3Select(obj):
    taxonomy.taxt_RegularityCB3Select(obj)

def taxt_RegularityCB4Select(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_RegularityCB5Select(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_WallsCBSelect(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_RoofCB1Select(obj):
    taxonomy.taxt_ValidateRoof()
    taxonomy.taxt_BuildTaxonomy()

def taxt_RoofCB2Select(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_RoofCB3Select(obj):
    taxonomy.taxt_ValidateRoof()
    taxonomy.taxt_BuildTaxonomy()

def taxt_RoofCB4Select(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_RoofCB5Select(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_FoundationsCBSelect(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_FloorCB1Select(obj):
    taxonomy.taxt_ValidateFloor()
    taxonomy.taxt_BuildTaxonomy()

def taxt_FloorCB2Select(obj):
    taxonomy.taxt_BuildTaxonomy()

def taxt_FloorCB3Select(obj):
    taxonomy.taxt_BuildTaxonomy()


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
        self.taxt_ValidateRegularity()
        self.taxt_ValidateOccupancy()
        self.taxt_BuildTaxonomy()


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


    def taxt_ValidateRegularity(self):
        self.RegularityCB2.empty()
        self.RegularityCB3.empty()
        self.RegularityCB4.empty()
        self.RegularityCB5.empty()

        default_cb2 = 0
        default_cb3 = 0

        if (self.RegularityCB1.val() == 0 or
            self.RegularityCB1.val() == 1):
            self.RegularityCB2.disabled(True)
            self.RegularityCB3.disabled(True)
            self.RegularityCB4.disabled(True)
            self.RegularityCB5.disabled(True)
            self._gem_taxonomy_regularity_postinit = -1

        elif self.RegularityCB1.val() == 2: # /* irregular case */
            # /* RegularityCB2 related part */
            reg_cb2_items = []
            if self.RegularityCB3.val() == 0 or self.RegularityCB3.val() == -1:
                reg_cb2_items.append('No irregularity')
                self.RegularityCB2.first_disabled(True)
                default_cb2 = 1
            else:
                reg_cb2_items.append('No irregularity')

            reg_cb2_items.append('Torsion eccentricity')
            reg_cb2_items.append('Re-entrant corner')
            reg_cb2_items.append('Other plan irregularity')

            self.RegularityCB2.disabled(False)
            self.RegularityCB2.items(reg_cb2_items, val=0)
            self.RegularityCB2.val(default_cb2)

            # /* RegularityCB3 related part */
            reg_cb3_items = []
            if self.RegularityCB2.val() == 0 or self.RegularityCB2.val() == -1:
                reg_cb3_items.append('No irregularity')
                self.RegularityCB3.first_disabled(True)
                default_cb3 = 1
                self._gem_taxonomy_regularity_postinit = 2
            else:
                reg_cb3_items.append('No irregularity')

            reg_cb3_items.append('Soft storey')
            reg_cb3_items.append('Cripple wall')
            reg_cb3_items.append('Short column')
            reg_cb3_items.append('Pounding potential')
            reg_cb3_items.append('Setback')
            reg_cb3_items.append('Change in vertical structure')
            reg_cb3_items.append('Other vertical irregularity')
            self.RegularityCB3.disabled(False)
            self.RegularityCB3.items(reg_cb3_items, val=0)
            self.RegularityCB3.val(default_cb3)

        taxt_RegularityCB2Select(-1)
        taxt_RegularityCB3Select(-1)
        if default_cb2 == 1:
            self._gem_taxonomy_regularity_postinit = 2
        elif default_cb3 == 1:
            self._gem_taxonomy_regularity_postinit = 3


    def taxt_ValidateRegularity2(self):

        self.RegularityCB4.empty()

        if self.RegularityCB1.val() < 2 or self.RegularityCB2.val() == 0 or self.RegularityCB2.val() == -1:
            self.RegularityCB4.disabled(True)
        else:
            self.RegularityCB4.items([
                'No irregularity',
                'Torsion eccentricity',
                'Re-entrant corner',
                'Other plan irregularity',
            ], val=0)
            self.RegularityCB4.disabled(False)

        self.taxt_ValidateRegularityCross23("2")



    def taxt_ValidateRegularityCross23(self, who):
        if who == "2":
            if self.RegularityCB2.val() != 0:
                self.RegularityCB3.first_disabled(False)
            else:
                self.RegularityCB3.first_disabled(True)

        if who == "3":
            if self.RegularityCB3.val() != 0:
                self.RegularityCB2.first_disabled(False)
            else:
                self.RegularityCB2.first_disabled(True)

    def taxt_RegularityCB2Select(self, obj):
        self.taxt_ValidateRegularity2()
        if self._gem_taxonomy_regularity_postinit == 3:
            self.RegularityCB3.val(0)
            self.taxt_ValidateRegularity3()

        self._gem_taxonomy_regularity_postinit = -1
        self.taxt_BuildTaxonomy()


    def taxt_RegularityCB3Select(self, obj):
        self.taxt_ValidateRegularity3()
        if self._gem_taxonomy_regularity_postinit == 2:
            self.RegularityCB2.val(0)
            self.taxt_ValidateRegularity2()

        self._gem_taxonomy_regularity_postinit = -1
        self.taxt_BuildTaxonomy()

    def taxt_ValidateOccupancy(self):

        self.OccupancyCB2.empty()

        if self.OccupancyCB1.val() == 0:
            self.OccupancyCB2.disabled(True)

        elif self.OccupancyCB1.val() == 1:
            self.OccupancyCB2.items([
                'Residential, unknown type',
                'Single dwelling',
                'Multi-unit, unknown type',
                '2 Units (Duplex)',
                '3-4 Units',
                '5-9 Units',
                '10-19 Units',
                '20-49 Units',
                '50+ Units',
                'Temporary lodging',
                'Institutional housing',
                'Mobile home',
                'Informal housing',
            ], val=0)
            self.OccupancyCB2.disabled(False)

        elif self.OccupancyCB1.val() == 2:
            self.OccupancyCB2.items([
                'Commercial and public, unknown type',
                'Retail trade',
                'Wholesale trade and storage (warehouse)',
                'Offices, professional/technical services',
                'Hospital/medical clinic',
                'Entertainment',
                'Public building',
                'Covered parking garage',
                'Bus station',
                'Railway station',
                'Airport',
                'Recreation and leisure',
            ], val=0)
            self.OccupancyCB2.disabled(False)

        elif self.OccupancyCB1.val() == 3:
            self.OccupancyCB2.items([
                'Mixed, unknown type',
                'Mostly residential and commercial',
                'Mostly commercial and residential',
                'Mostly commercial and industrial',
                'Mostly residential and industrial',
                'Mostly industrial and commercial',
                'Mostly industrial and residential',
            ], val=0)
            self.OccupancyCB2.disabled(False)

        elif self.OccupancyCB1.val() == 4:
            self.OccupancyCB2.items([
                'Industrial, unknown type',
                'Heavy industrial',
                'Light industrial',
            ], val=0)
            self.OccupancyCB2.disabled(False)

        elif self.OccupancyCB1.val() == 5:
            self.OccupancyCB2.items([
                'Agriculture, unknown type',
                'Produce storage',
                'Animal shelter',
                'Agricultural processing',
            ], val=0)
            self.OccupancyCB2.disabled(False)

        elif self.OccupancyCB1.val() == 6:
            self.OccupancyCB2.items([
                'Assembly, unknown type',
                'Religious gathering',
                'Arena',
                'Cinema or concert hall',
                'Other gatherings',
            ], val=0)
            self.OccupancyCB2.disabled(False)

        elif self.OccupancyCB1.val() == 7:
            self.OccupancyCB2.items([
                'Government, unknown type',
                'Government, general services',
                'Government, emergency response',
            ], val=0)
            self.OccupancyCB2.disabled(False)

        elif self.OccupancyCB1.val() == 8:
            self.OccupancyCB2.items([
                'Education, unknown type',
                'Pre-school facility',
                'School',
                'College/university, offices and/or classrooms',
                'College/university, research facilities and/or labs',
            ], val=0)
            self.OccupancyCB2.disabled(False)

        else:
            self.OccupancyCB2.disabled(True)


    def taxt_BuildTaxonomy(self):

        ResTax = None
        ResTaxFull = self.BuildTaxonomyString(0)
        out_type = self.OutTypeCB.val()

        height1 = self.HeightCB1.val()
        height2 = self.HeightCB2.val()
        height3 = self.HeightCB3.val()
        height4 = self.HeightCB4.val()
        date1 = self.DateCB1.val()
        validated = False
        validate_msg = ""
        h11 = True
        h12 = True
        h21 = True
        h22 = True
        h31 = True
        h32 = True
        d1 = True
        d2 = True

        if height1 > 0:
            if not is_not_negative_int(self.noStoreysE11.val()):
                if height1 == 1:
                    validate_msg += "Number of storey above ground: lower limit not positive integer. "

                else:
                    validate_msg += "Number of storey above ground: not positive integer. "

                # self.noStoreysE11.addClass('gem_field_alert')
                h11 = False

            else:
                # self.noStoreysE11.removeClass('gem_field_alert')
                pass


        if height1 == 1:
            if not is_not_negative_int(self.noStoreysE12.val()):
                validate_msg += "Number of storey above ground: upper limit not positive integer. "
                # self.noStoreysE12.addClass('gem_field_alert')
                h12 = False

            elif int(self.noStoreysE11.val()) == int(self.noStoreysE12.val()):
                validate_msg += "Number of storey above ground: invalid range."
                # self.noStoreysE12.addClass('gem_field_alert')
                h12 = False

            else:
                # self.noStoreysE12.removeClass('gem_field_alert')
                pass


            #  swap items if wrong order
            if h11 and h12:
                if int(self.noStoreysE11.val()) > int(self.noStoreysE12.val()):
                    swap = self.noStoreysE11.val()
                    self.noStoreysE11.val(self.noStoreysE12.val())
                    self.noStoreysE12.val(swap)

        if height2 > 0:
            if not is_not_negative_int(self.noStoreysE21.val()):
                if height2 == 1:
                    validate_msg += "Number of storey above ground: lower limit not positive integer. "
                else:
                    validate_msg += "Number of storey above ground: not positive integer. "

                # self.noStoreysE21.addClass('gem_field_alert')
                h21 = False

            else:
                # self.noStoreysE21.removeClass('gem_field_alert')
                pass



        if height2 == 1:
            if not is_not_negative_int(self.noStoreysE22.val()):
                validate_msg += "Number of storey above ground: upper limit not positive integer. "
                # self.noStoreysE22.addClass('gem_field_alert')
                h22 = False

            elif int(self.noStoreysE21.val()) == int(self.noStoreysE22.val()):
                validate_msg += "Number of storey above ground: invalid range."
                # self.noStoreysE22.addClass('gem_field_alert')
                h22 = False

            else:
                # self.noStoreysE22.removeClass('gem_field_alert')
                pass


            #  swap items if wrong order
            if h21 and h22:
                if int(self.noStoreysE21.val()) > int(self.noStoreysE22.val()):
                    swap = self.noStoreysE21.val()
                    self.noStoreysE21.val(self.noStoreysE22.val())
                    self.noStoreysE22.val(swap)

        if height3 > 0:
            if not is_not_negative_float(self.noStoreysE31.val()):
                if height3 == 1:
                    validate_msg += "Height of ground floor level: lower limit not positive real"
                else:
                    validate_msg += "Height of ground floor level: not positive real. "
                # self.noStoreysE31.addClass('gem_field_alert')
                h31 = False

            else:
                # self.noStoreysE31.removeClass('gem_field_alert')
                pass

        if height3 == 1:
            if not is_not_negative_float(self.noStoreysE32.val()):
                validate_msg += "Height of ground floor level: upper limit not positive real. "
                # self.noStoreysE32.addClass('gem_field_alert')
                h32 = False

            elif int(self.noStoreysE31.val()) == int(self.noStoreysE32.val()):
                validate_msg += "Height of ground floor level: invalid range."
                # self.noStoreysE32.addClass('gem_field_alert')
                h32 = False

            else:
                self.noStoreysE32.removeClass('gem_field_alert')


            # swap items if wrong order
            if h31 and h32:
                if parseFloat(self.noStoreysE31.val()) > parseFloat(self.noStoreysE32.val()):
                    swap = self.noStoreysE31.val()
                    self.noStoreysE31.val(self.noStoreysE32.val())
                    self.noStoreysE32.val(swap)

        if height4 > 0:
            if not is_in_rect_angle_float(self.noStoreysE41.val()):
                validate_msg += "Slope of the ground: it is not positive real between 0 and 90. "
                # self.noStoreysE41.addClass('gem_field_alert')
            else:
                # self.noStoreysE41.removeClass('gem_field_alert')
                pass



        if date1 > 0:
            if not is_not_negative_int(self.DateE1.val()) or self.DateE1.val().length > 4:
                if date1 == 2:
                    validate_msg += "Date of construction or retrofit: lower limit is not a valid date. "
                else:
                    validate_msg += "Date of construction or retrofit: it is not a valid date. "

                # self.DateE1.addClass('gem_field_alert')
                d1 = False

            else:
                # self.DateE1.removeClass('gem_field_alert')
                pass


        if date1 == 2:
            if not is_not_negative_int(self.DateE2.val()) or self.DateE2.val().length > 4:
                validate_msg += "Date of construction or retrofit: upper limit is not a valid date. "
                # self.DateE2.addClass('gem_field_alert')
                d2 = False

            elif int(self.DateE1.val()) == int(self.DateE2.val()):
                validate_msg += "Date of construction or retrofit: invalid range."
                d2 = False

            else:
                # self.DateE2.removeClass('gem_field_alert')
                pass

            # swap items if wrong order
            if d1 and d2:
                if int(self.DateE1.val()) > int(self.DateE2.val()):
                    swap = self.DateE1.val()
                    self.DateE1.val(self.DateE2.val())
                    self.DateE2.val(swap)

        if validate_msg == "":
            validated = True

        if validated:
            if out_type != 0:
                ResTax = self.BuildTaxonomyString(out_type)
            else:
                ResTax = ResTaxFull

            self._gem_taxonomy_form = ResTax
            self._gem_taxonomy_form_full = ResTaxFull

            self.resultE.val(ResTax)
            # self.permalink.attr("href", taxt_prefix + "/" +  ResTaxFull)

        else:
            self._gem_taxonomy_form = ""
            self._gem_taxonomy_form_full = ""
            self.resultE.val(validate_msg)
            # self.permalink.attr("href", taxt_prefix)


    def BuildTaxonomyString(self, out_type):
        self.Taxonomy = [0] * 50

        ResTax = None
        direction1 = None
        direction2 = None

        # /* Structural System: Direction X */

        if self.MaterialCB11.val() == 0 and (out_type == 0):
            Taxonomy[0] = 'MAT99'
        if self.MaterialCB11.val() == 1:
            Taxonomy[0] = 'C99'
        if self.MaterialCB11.val() == 2:
            Taxonomy[0] = 'CU'
        if self.MaterialCB11.val() == 3:
            Taxonomy[0] = 'CR'
        if self.MaterialCB11.val() == 4:
            Taxonomy[0] = 'SRC'

        if (self.MaterialCB11.val() > 0) and (self.MaterialCB11.val() < 5):
            if (self.MaterialCB21.val() == 0) and (out_type == 0):
                Taxonomy[1] = '+CT99'
            if self.MaterialCB21.val() == 1:
                Taxonomy[1] = '+CIP'
            if self.MaterialCB21.val() == 2:
                Taxonomy[1] = '+PC'
            if self.MaterialCB21.val() == 3:
                Taxonomy[1] = '+CIPPS'
            if self.MaterialCB21.val() == 4:
                Taxonomy[1] = '+PCPS'

        if self.MaterialCB11.val() == 5:
            Taxonomy[0] = 'S'
            if self.MaterialCB21.val() == 0 and (out_type == 0):
                Taxonomy[1] = '+S99'
            if self.MaterialCB21.val() == 1:
                Taxonomy[1] = '+SL'
            if self.MaterialCB21.val() == 2:
                Taxonomy[1] = '+SR'
            if self.MaterialCB21.val() == 3:
                Taxonomy[1] = '+SO'


        if self.MaterialCB11.val() == 6:
            Taxonomy[0] = 'ME'
            if self.MaterialCB21.val() == 0 and (out_type == 0):
                Taxonomy[1] = '+ME99'
            if self.MaterialCB21.val() == 1:
                Taxonomy[1] = '+MEIR'
            if self.MaterialCB21.val() == 2:
                Taxonomy[1] = '+MEO'


        if self.MaterialCB11.val() == 5:
            if self.MaterialCB31.val() == 0 and (out_type == 0):
                Taxonomy[2] = '+SC99'
            if self.MaterialCB31.val() == 1:
                Taxonomy[2] = '+WEL'
            if self.MaterialCB31.val() == 2:
                Taxonomy[2] = '+RIV'
            if self.MaterialCB31.val() == 3:
                Taxonomy[2] = '+BOL'


        if self.MaterialCB11.val() > 6 and self.MaterialCB11.val() < 11:
            if self.MaterialCB11.val() == 7:
                Taxonomy[0] = 'M99'
            if self.MaterialCB11.val() == 8:
                Taxonomy[0] = 'MUR'
            if self.MaterialCB11.val() == 9:
                Taxonomy[0] = 'MCF'

            if self.MaterialCB21.val() == 0 and (out_type == 0):
                Taxonomy[1] = '+MUN99'
            if self.MaterialCB21.val() == 1:
                Taxonomy[1] = '+ADO'
            if self.MaterialCB21.val() == 2:
                Taxonomy[1] = '+ST99'
            if self.MaterialCB21.val() == 3:
                Taxonomy[1] = '+STRUB'
            if self.MaterialCB21.val() == 4:
                Taxonomy[1] = '+STDRE'
            if self.MaterialCB21.val() == 5:
                Taxonomy[1] = '+CL99'
            if self.MaterialCB21.val() == 6:
                Taxonomy[1] = '+CLBRS'
            if self.MaterialCB21.val() == 7:
                Taxonomy[1] = '+CLBRH'
            if self.MaterialCB21.val() == 8:
                Taxonomy[1] = '+CLBLH'
            if self.MaterialCB21.val() == 9:
                Taxonomy[1] = '+CB99'
            if self.MaterialCB21.val() == 10:
                Taxonomy[1] = '+CBS'
            if self.MaterialCB21.val() == 11:
                Taxonomy[1] = '+CBH'
            if self.MaterialCB21.val() == 12:
                Taxonomy[1] = '+MO'

            if self.MaterialCB11.val() == 10:
                Taxonomy[0] = 'MR'
                if (self.MaterialCB41.val() == 0) and (out_type == 0):
                    Taxonomy[34] = '+MR99'
                if self.MaterialCB41.val() == 1:
                    Taxonomy[34] = '+RS'
                if self.MaterialCB41.val() == 2:
                    Taxonomy[34] = '+RW'
                if self.MaterialCB41.val() == 3:
                    Taxonomy[34] = '+RB'
                if self.MaterialCB41.val() == 4:
                    Taxonomy[34] = '+RCM'
                if self.MaterialCB41.val() == 5:
                    Taxonomy[34] = '+RCB'


            if (self.MaterialCB31.val() == 0) and (out_type == 0):
                Taxonomy[2] = '+MO99'
            if self.MaterialCB31.val() == 1:
                Taxonomy[2] = '+MON'
            if self.MaterialCB31.val() == 2:
                Taxonomy[2] = '+MOM'
            if self.MaterialCB31.val() == 3:
                Taxonomy[2] = '+MOL'
            if self.MaterialCB31.val() == 4:
                Taxonomy[2] = '+MOC'
            if self.MaterialCB31.val() == 5:
                Taxonomy[2] = '+MOCL'
            if self.MaterialCB31.val() == 6:
                Taxonomy[2] = '+SP99'
            if self.MaterialCB31.val() == 7:
                Taxonomy[2] = '+SPLI'
            if self.MaterialCB31.val() == 8:
                Taxonomy[2] = '+SPSA'
            if self.MaterialCB31.val() == 9:
                Taxonomy[2] = '+SPTU'
            if self.MaterialCB31.val() == 10:
                Taxonomy[2] = '+SPSL'
            if self.MaterialCB31.val() == 11:
                Taxonomy[2] = '+SPGR'
            if self.MaterialCB31.val() == 12:
                Taxonomy[2] = '+SPBA'
            if self.MaterialCB31.val() == 13:
                Taxonomy[2] = '+SPO'


        if (self.MaterialCB11.val()>10) and (self.MaterialCB11.val()<14):
            if self.MaterialCB11.val() == 11:
                Taxonomy[0] = 'E99'
            if self.MaterialCB11.val() == 12:
                Taxonomy[0] = 'EU'
            if self.MaterialCB11.val() == 13:
                Taxonomy[0] = 'ER'

            if (self.MaterialCB21.val() == 0) and (out_type == 0):
                Taxonomy[1] = '+ET99'
            if self.MaterialCB21.val() == 1:
                Taxonomy[1] = '+ETR'
            if self.MaterialCB21.val() == 2:
                Taxonomy[1] = '+ETC'
            if self.MaterialCB21.val() == 3:
                Taxonomy[1] = '+ETO'


        if self.MaterialCB11.val() == 14:
            Taxonomy[0] = 'W'
            if (self.MaterialCB21.val() == 0) and (out_type == 0):
                Taxonomy[1] = '+W99'
            if self.MaterialCB21.val() == 1:
                Taxonomy[1] = '+WHE'
            if self.MaterialCB21.val() == 2:
                Taxonomy[1] = '+WLI'
            if self.MaterialCB21.val() == 3:
                Taxonomy[1] = '+WS'
            if self.MaterialCB21.val() == 4:
                Taxonomy[1] = '+WWD'
            if self.MaterialCB21.val() == 5:
                Taxonomy[1] = '+WBB'
            if self.MaterialCB21.val() == 6:
                Taxonomy[1] = '+WO'


        if self.MaterialCB11.val() == 15:
            Taxonomy[0] = 'MATO'

        if (self.SystemCB11.val() == 0) and (out_type == 0):
            Taxonomy[3] = 'L99'

        if (self.MaterialCB11.val() > 10) and (self.MaterialCB11.val() < 14):
            if self.SystemCB11.val() == 1:
                Taxonomy[3] = 'LN'
            if self.SystemCB11.val() == 2:
                Taxonomy[3] = 'LWAL'
            if self.SystemCB11.val() == 3:
                Taxonomy[3] = 'LH'
            if self.SystemCB11.val() == 4:
                Taxonomy[3] = 'LO'

        elif ((self.MaterialCB11.val()>6) and (self.MaterialCB11.val()<11)) or (self.MaterialCB11.val() == 14):
            if self.SystemCB11.val() == 1:
                Taxonomy[3] = 'LN'
            if self.SystemCB11.val() == 2:
                Taxonomy[3] = 'LFM'
            if self.SystemCB11.val() == 3:
                Taxonomy[3] = 'LPB'
            if self.SystemCB11.val() == 4:
                Taxonomy[3] = 'LWAL'
            if self.SystemCB11.val() == 5:
                Taxonomy[3] = 'LH'
            if self.SystemCB11.val() == 6:
                Taxonomy[3] = 'LO'

        else:
            if self.SystemCB11.val() == 1:
                Taxonomy[3] = 'LN'
            if self.SystemCB11.val() == 2:
                Taxonomy[3] = 'LFM'
            if self.SystemCB11.val() == 3:
                Taxonomy[3] = 'LFINF'
            if self.SystemCB11.val() == 4:
                Taxonomy[3] = 'LFBR'
            if self.SystemCB11.val() == 5:
                Taxonomy[3] = 'LPB'
            if self.SystemCB11.val() == 6:
                Taxonomy[3] = 'LWAL'
            if self.SystemCB11.val() == 7:
                Taxonomy[3] = 'LDUAL'
            if self.SystemCB11.val() == 8:
                Taxonomy[3] = 'LFLS'
            if self.SystemCB11.val() == 9:
                Taxonomy[3] = 'LFLSINF'
            if self.SystemCB11.val() == 10:
                Taxonomy[3] = 'LH'
            if self.SystemCB11.val() == 11:
                Taxonomy[3] = 'LO'


        if self.SystemCB11.val() > 0:
            if (self.SystemCB21.val() == 0) and (out_type == 0):
                Taxonomy[4] = '+DU99'
            if self.SystemCB21.val() == 1:
                Taxonomy[4] = '+DUC'
            if self.SystemCB21.val() == 2:
                Taxonomy[4] = '+DNO'
            if self.SystemCB21.val() == 3:
                Taxonomy[4] = '+DBD'


        # /* Structural System: Direction Y */

        if self.MaterialCB12.val() == 0 and (out_type == 0):
            Taxonomy[5] = 'MAT99'
        if self.MaterialCB12.val() == 1:
            Taxonomy[5] = 'C99'
        if self.MaterialCB12.val() == 2:
            Taxonomy[5] = 'CU'
        if self.MaterialCB12.val() == 3:
            Taxonomy[5] = 'CR'
        if self.MaterialCB12.val() == 4:
            Taxonomy[5] = 'SRC'

        if (self.MaterialCB12.val() > 0) and (self.MaterialCB12.val() < 5):
            if (self.MaterialCB22.val() == 0) and (out_type == 0):
                Taxonomy[6] = '+CT99'
            if self.MaterialCB22.val() == 1:
                Taxonomy[6] = '+CIP'
            if self.MaterialCB22.val() == 2:
                Taxonomy[6] = '+PC'
            if self.MaterialCB22.val() == 3:
                Taxonomy[6] = '+CIPPS'
            if self.MaterialCB22.val() == 4:
                Taxonomy[6] = '+PCPS'

        if self.MaterialCB12.val() == 5:
            Taxonomy[5] = 'S'
            if self.MaterialCB22.val() == 0 and (out_type == 0):
                Taxonomy[6] = '+S99'
            if self.MaterialCB22.val() == 1:
                Taxonomy[6] = '+SL'
            if self.MaterialCB22.val() == 2:
                Taxonomy[6] = '+SR'
            if self.MaterialCB22.val() == 3:
                Taxonomy[6] = '+SO'


        if self.MaterialCB12.val() == 6:
            Taxonomy[5] = 'ME'
            if self.MaterialCB22.val() == 0 and (out_type == 0):
                Taxonomy[6] = '+ME99'
            if self.MaterialCB22.val() == 1:
                Taxonomy[6] = '+MEIR'
            if self.MaterialCB22.val() == 2:
                Taxonomy[6] = '+MEO'


        if self.MaterialCB12.val() == 5:
            if self.MaterialCB32.val() == 0 and (out_type == 0):
                Taxonomy[7] = '+SC99'
            if self.MaterialCB32.val() == 1:
                Taxonomy[7] = '+WEL'
            if self.MaterialCB32.val() == 2:
                Taxonomy[7] = '+RIV'
            if self.MaterialCB32.val() == 3:
                Taxonomy[7] = '+BOL'


        if self.MaterialCB12.val() > 6 and self.MaterialCB12.val() < 11:
            if self.MaterialCB12.val() == 7:
                Taxonomy[5] = 'M99'
            if self.MaterialCB12.val() == 8:
                Taxonomy[5] = 'MUR'
            if self.MaterialCB12.val() == 9:
                Taxonomy[5] = 'MCF'

            if self.MaterialCB22.val() == 0 and (out_type == 0):
                Taxonomy[6] = '+MUN99'
            if self.MaterialCB22.val() == 1:
                Taxonomy[6] = '+ADO'
            if self.MaterialCB22.val() == 2:
                Taxonomy[6] = '+ST99'
            if self.MaterialCB22.val() == 3:
                Taxonomy[6] = '+STRUB'
            if self.MaterialCB22.val() == 4:
                Taxonomy[6] = '+STDRE'
            if self.MaterialCB22.val() == 5:
                Taxonomy[6] = '+CL99'
            if self.MaterialCB22.val() == 6:
                Taxonomy[6] = '+CLBRS'
            if self.MaterialCB22.val() == 7:
                Taxonomy[6] = '+CLBRH'
            if self.MaterialCB22.val() == 8:
                Taxonomy[6] = '+CLBLH'
            if self.MaterialCB22.val() == 9:
                Taxonomy[6] = '+CB99'
            if self.MaterialCB22.val() == 10:
                Taxonomy[6] = '+CBS'
            if self.MaterialCB22.val() == 11:
                Taxonomy[6] = '+CBH'
            if self.MaterialCB22.val() == 12:
                Taxonomy[6] = '+MO'

            if self.MaterialCB12.val() == 10:
                Taxonomy[5] = 'MR'
                if (self.MaterialCB42.val() == 0) and (out_type == 0):
                    Taxonomy[35] = '+MR99'
                if self.MaterialCB42.val() == 1:
                    Taxonomy[35] = '+RS'
                if self.MaterialCB42.val() == 2:
                    Taxonomy[35] = '+RW'
                if self.MaterialCB42.val() == 3:
                    Taxonomy[35] = '+RB'
                if self.MaterialCB42.val() == 4:
                    Taxonomy[35] = '+RCM'
                if self.MaterialCB42.val() == 5:
                    Taxonomy[35] = '+RCB'


            if (self.MaterialCB32.val() == 0) and (out_type == 0):
                Taxonomy[7] = '+MO99'
            if self.MaterialCB32.val() == 1:
                Taxonomy[7] = '+MON'
            if self.MaterialCB32.val() == 2:
                Taxonomy[7] = '+MOM'
            if self.MaterialCB32.val() == 3:
                Taxonomy[7] = '+MOL'
            if self.MaterialCB32.val() == 4:
                Taxonomy[7] = '+MOC'
            if self.MaterialCB32.val() == 5:
                Taxonomy[7] = '+MOCL'
            if self.MaterialCB32.val() == 6:
                Taxonomy[7] = '+SP99'
            if self.MaterialCB32.val() == 7:
                Taxonomy[7] = '+SPLI'
            if self.MaterialCB32.val() == 8:
                Taxonomy[7] = '+SPSA'
            if self.MaterialCB32.val() == 9:
                Taxonomy[7] = '+SPTU'
            if self.MaterialCB32.val() == 10:
                Taxonomy[7] = '+SPSL'
            if self.MaterialCB32.val() == 11:
                Taxonomy[7] = '+SPGR'
            if self.MaterialCB32.val() == 12:
                Taxonomy[7] = '+SPBA'
            if self.MaterialCB32.val() == 13:
                Taxonomy[7] = '+SPO'


        if (self.MaterialCB12.val() > 10) and (self.MaterialCB12.val() < 14):
            if self.MaterialCB12.val() == 11:
                Taxonomy[5] = 'E99'
            if self.MaterialCB12.val() == 12:
                Taxonomy[5] = 'EU'
            if self.MaterialCB12.val() == 13:
                Taxonomy[5] = 'ER'

            if (self.MaterialCB22.val() == 0) and (out_type == 0):
                Taxonomy[6] = '+ET99'
            if self.MaterialCB22.val() == 1:
                Taxonomy[6] = '+ETR'
            if self.MaterialCB22.val() == 2:
                Taxonomy[6] = '+ETC'
            if self.MaterialCB22.val() == 3:
                Taxonomy[6] = '+ETO'


        if self.MaterialCB12.val() == 14:
            Taxonomy[5] = 'W'
            if (self.MaterialCB22.val() == 0) and (out_type == 0):
                Taxonomy[6] = '+W99'
            if self.MaterialCB22.val() == 1:
                Taxonomy[6] = '+WHE'
            if self.MaterialCB22.val() == 2:
                Taxonomy[6] = '+WLI'
            if self.MaterialCB22.val() == 3:
                Taxonomy[6] = '+WS'
            if self.MaterialCB22.val() == 4:
                Taxonomy[6] = '+WWD'
            if self.MaterialCB22.val() == 5:
                Taxonomy[6] = '+WBB'
            if self.MaterialCB22.val() == 6:
                Taxonomy[6] = '+WO'


        if self.MaterialCB12.val() == 15:
            Taxonomy[5] = 'MATO'

        if (self.SystemCB12.val() == 0) and (out_type == 0):
            Taxonomy[8] = 'L99'

        if (self.MaterialCB12.val() > 10) and (self.MaterialCB12.val() < 14):
            if self.SystemCB12.val() == 1:
                Taxonomy[8] = 'LN'
            if self.SystemCB12.val() == 2:
                Taxonomy[8] = 'LWAL'
            if self.SystemCB12.val() == 3:
                Taxonomy[8] = 'LH'
            if self.SystemCB12.val() == 4:
                Taxonomy[8] = 'LO'

        elif ((self.MaterialCB12.val() > 6) and (self.MaterialCB12.val() < 11)) or (self.MaterialCB12.val() == 14):
            if self.SystemCB12.val() == 1:
                Taxonomy[8] = 'LN'
            if self.SystemCB12.val() == 2:
                Taxonomy[8] = 'LFM'
            if self.SystemCB12.val() == 3:
                Taxonomy[8] = 'LPB'
            if self.SystemCB12.val() == 4:
                Taxonomy[8] = 'LWAL'
            if self.SystemCB12.val() == 5:
                Taxonomy[8] = 'LH'
            if self.SystemCB12.val() == 6:
                Taxonomy[8] = 'LO'

        else:
            if self.SystemCB12.val() == 1:
                Taxonomy[8] = 'LN'
            if self.SystemCB12.val() == 2:
                Taxonomy[8] = 'LFM'
            if self.SystemCB12.val() == 3:
                Taxonomy[8] = 'LFINF'
            if self.SystemCB12.val() == 4:
                Taxonomy[8] = 'LFBR'
            if self.SystemCB12.val() == 5:
                Taxonomy[8] = 'LPB'
            if self.SystemCB12.val() == 6:
                Taxonomy[8] = 'LWAL'
            if self.SystemCB12.val() == 7:
                Taxonomy[8] = 'LDUAL'
            if self.SystemCB12.val() == 8:
                Taxonomy[8] = 'LFLS'
            if self.SystemCB12.val() == 9:
                Taxonomy[8] = 'LFLSINF'
            if self.SystemCB12.val() == 10:
                Taxonomy[8] = 'LH'
            if self.SystemCB12.val() == 11:
                Taxonomy[8] = 'LO'


        if self.SystemCB12.val() > 0:
            if (self.SystemCB22.val() == 0) and (out_type == 0):
                Taxonomy[9] = '+DU99'
            if self.SystemCB22.val() == 1:
                Taxonomy[9] = '+DUC'
            if self.SystemCB22.val() == 2:
                Taxonomy[9] = '+DNO'
            if self.SystemCB22.val() == 3:
                Taxonomy[9] = '+DBD'


        if self.DateCB1.val() == 0  and (out_type == 0):
            Taxonomy[10] = 'Y99'
        if self.DateCB1.val() == 1:
            Taxonomy[10] = 'YEX:' + self.DateE1.val()
        elif self.DateCB1.val() == 2:
            Taxonomy[10] = 'YBET:' + self.DateE1.val() + "," + self.DateE2.val()
        elif self.DateCB1.val() == 3:
            Taxonomy[10] = 'YPRE:' + self.DateE1.val()
        elif self.DateCB1.val() == 4:
            Taxonomy[10] = 'YAPP:' + self.DateE1.val()

        if self.HeightCB1.val() == 0:
            if (out_type == 0):
                Taxonomy[11] ='H99'

        else:
            if self.HeightCB1.val() == 1:
                Taxonomy[11] = 'HBET:' + self.noStoreysE11.val() + ',' + self.noStoreysE12.val()
            if self.HeightCB1.val() == 2:
                Taxonomy[11] = 'HEX:' + self.noStoreysE11.val()
            if self.HeightCB1.val() == 3:
                Taxonomy[11] = 'HAPP:' + self.noStoreysE11.val()

            if self.HeightCB2.val() == 0 and (out_type == 0):
                Taxonomy[12] = '+HB99'
            if self.HeightCB2.val() == 1:
                Taxonomy[12] = '+HBBET:' + self.noStoreysE21.val() + ',' + self.noStoreysE22.val()
            if self.HeightCB2.val() == 2:
                Taxonomy[12] = '+HBEX:' + self.noStoreysE21.val()
            if self.HeightCB2.val() == 3:
                Taxonomy[12] = '+HBAPP:' + self.noStoreysE21.val()

            if self.HeightCB3.val() == 0 and (out_type == 0):
                Taxonomy[13] = '+HF99'
            if self.HeightCB3.val() == 1:
                Taxonomy[13] = '+HFBET:' + self.noStoreysE31.val() + ',' + self.noStoreysE32.val()
            if self.HeightCB3.val() == 2:
                Taxonomy[13] = '+HFEX:' + self.noStoreysE31.val()
            if self.HeightCB3.val() == 3:
                Taxonomy[13] = '+HFAPP:' + self.noStoreysE31.val()

            if self.HeightCB4.val() == 0 and (out_type == 0):
                Taxonomy[14] = '+HD99'
            if self.HeightCB4.val() == 1:
                Taxonomy[14] = '+HD:' + self.noStoreysE41.val()


        if self.OccupancyCB1.val() == 0:
            if (out_type == 0):
                Taxonomy[15] = 'OC99'

        elif self.OccupancyCB1.val() == 1:
            Taxonomy[15] = 'RES'
            if self.OccupancyCB2.val() == 0 and (out_type == 0):
                Taxonomy[16] = '+RES99'
            if self.OccupancyCB2.val() == 1:
                Taxonomy[16] = '+RES1'
            if self.OccupancyCB2.val() == 2:
                Taxonomy[16] = '+RES2'
            if self.OccupancyCB2.val() == 3:
                Taxonomy[16] = '+RES2A'
            if self.OccupancyCB2.val() == 4:
                Taxonomy[16] = '+RES2B'
            if self.OccupancyCB2.val() == 5:
                Taxonomy[16] = '+RES2C'
            if self.OccupancyCB2.val() == 6:
                Taxonomy[16] = '+RES2D'
            if self.OccupancyCB2.val() == 7:
                Taxonomy[16] = '+RES2E'
            if self.OccupancyCB2.val() == 8:
                Taxonomy[16] = '+RES2F'
            if self.OccupancyCB2.val() == 9:
                Taxonomy[16] = '+RES3'
            if self.OccupancyCB2.val() == 10:
                Taxonomy[16] = '+RES4'
            if self.OccupancyCB2.val() == 11:
                Taxonomy[16] = '+RES5'
            if self.OccupancyCB2.val() == 12:
                Taxonomy[16] = '+RES6'

        elif self.OccupancyCB1.val() == 2:
            Taxonomy[15] = 'COM'
            if self.OccupancyCB2.val() == 0 and (out_type == 0):
                Taxonomy[16] = '+COM99'
            if self.OccupancyCB2.val() == 1:
                Taxonomy[16] = '+COM1'
            if self.OccupancyCB2.val() == 2:
                Taxonomy[16] = '+COM2'
            if self.OccupancyCB2.val() == 3:
                Taxonomy[16] = '+COM3'
            if self.OccupancyCB2.val() == 4:
                Taxonomy[16] = '+COM4'
            if self.OccupancyCB2.val() == 5:
                Taxonomy[16] = '+COM5'
            if self.OccupancyCB2.val() == 6:
                Taxonomy[16] = '+COM6'
            if self.OccupancyCB2.val() == 7:
                Taxonomy[16] = '+COM7'
            if self.OccupancyCB2.val() == 8:
                Taxonomy[16] = '+COM8'
            if self.OccupancyCB2.val() == 9:
                Taxonomy[16] = '+COM9'
            if self.OccupancyCB2.val() == 10:
                Taxonomy[16] = '+COM10'
            if self.OccupancyCB2.val() == 11:
                Taxonomy[16] = '+COM11'

        elif self.OccupancyCB1.val() == 3:
            Taxonomy[15] = 'MIX'
            if self.OccupancyCB2.val() == 0 and (out_type == 0):
                Taxonomy[16] = '+MIX99'
            if self.OccupancyCB2.val() == 1:
                Taxonomy[16] = '+MIX1'
            if self.OccupancyCB2.val() == 2:
                Taxonomy[16] = '+MIX2'
            if self.OccupancyCB2.val() == 3:
                Taxonomy[16] = '+MIX3'
            if self.OccupancyCB2.val() == 4:
                Taxonomy[16] = '+MIX4'
            if self.OccupancyCB2.val() == 5:
                Taxonomy[16] = '+MIX5'
            if self.OccupancyCB2.val() == 6:
                Taxonomy[16] = '+MIX6'

        elif self.OccupancyCB1.val() == 4:
            Taxonomy[15] = 'IND'
            if self.OccupancyCB2.val() == 0 and (out_type == 0):
                Taxonomy[16] = '+IND99'
            if self.OccupancyCB2.val() == 1:
                Taxonomy[16] = '+IND1'
            if self.OccupancyCB2.val() == 2:
                Taxonomy[16] = '+IND2'

        elif self.OccupancyCB1.val() == 5:
            Taxonomy[15] = 'AGR'
            if self.OccupancyCB2.val() == 0 and (out_type == 0):
                Taxonomy[16] = '+AGR99'
            if self.OccupancyCB2.val() == 1:
                Taxonomy[16] = '+AGR1'
            if self.OccupancyCB2.val() == 2:
                Taxonomy[16] = '+AGR2'
            if self.OccupancyCB2.val() == 3:
                Taxonomy[16] = '+AGR3'

        elif self.OccupancyCB1.val() == 6:
            Taxonomy[15] = 'ASS'
            if self.OccupancyCB2.val() == 0 and (out_type == 0):
                Taxonomy[16] = '+ASS99'
            if self.OccupancyCB2.val() == 1:
                Taxonomy[16] = '+ASS1'
            if self.OccupancyCB2.val() == 2:
                Taxonomy[16] = '+ASS2'
            if self.OccupancyCB2.val() == 3:
                Taxonomy[16] = '+ASS3'
            if self.OccupancyCB2.val() == 4:
                Taxonomy[16] = '+ASS4'

        elif self.OccupancyCB1.val() == 7:
            Taxonomy[15] = 'GOV'
            if self.OccupancyCB2.val() == 0 and (out_type == 0):
                Taxonomy[16] = '+GOV99'
            if self.OccupancyCB2.val() == 1:
                Taxonomy[16] = '+GOV1'
            if self.OccupancyCB2.val() == 2:
                Taxonomy[16] = '+GOV2'

        elif self.OccupancyCB1.val() == 8:
            Taxonomy[15] = 'EDU'
            if self.OccupancyCB2.val() == 0 and (out_type == 0):
                Taxonomy[16] = '+EDU99'
            if self.OccupancyCB2.val() == 1:
                Taxonomy[16] = '+EDU1'
            if self.OccupancyCB2.val() == 2:
                Taxonomy[16] = '+EDU2'
            if self.OccupancyCB2.val() == 3:
                Taxonomy[16] = '+EDU3'
            if self.OccupancyCB2.val() == 4:
                Taxonomy[16] = '+EDU4'

        elif self.OccupancyCB1.val() == 9:
            Taxonomy[15] = 'OCO'


        if self.PositionCB.val() == 0 and (out_type == 0):
            Taxonomy[17] = 'BP99'
        elif self.PositionCB.val() == 1:
            Taxonomy[17] = 'BPD'
        elif self.PositionCB.val() == 2:
            Taxonomy[17] = 'BP1'
        elif self.PositionCB.val() == 3:
            Taxonomy[17] = 'BP2'
        elif self.PositionCB.val() == 4:
            Taxonomy[17] = 'BP3'
        elif self.PositionCB.val() == 5:
            Taxonomy[17] = 'BPI'

        if self.PlanShapeCB.val() == 0 and (out_type == 0):
            Taxonomy[18] = 'PLF99'
        elif self.PlanShapeCB.val() == 1:
            Taxonomy[18] = 'PLFSQ'
        elif self.PlanShapeCB.val() == 2:
            Taxonomy[18] = 'PLFSQO'
        elif self.PlanShapeCB.val() == 3:
            Taxonomy[18] = 'PLFR'
        elif self.PlanShapeCB.val() == 4:
            Taxonomy[18] = 'PLFRO'
        elif self.PlanShapeCB.val() == 5:
            Taxonomy[18] = 'PLFL'
        elif self.PlanShapeCB.val() == 6:
            Taxonomy[18] = 'PLFC'
        elif self.PlanShapeCB.val() == 7:
            Taxonomy[18] = 'PLFCO'
        elif self.PlanShapeCB.val() == 8:
            Taxonomy[18] = 'PLFD'
        elif self.PlanShapeCB.val() == 9:
            Taxonomy[18] = 'PLFDO'
        elif self.PlanShapeCB.val() == 10:
            Taxonomy[18] = 'PLFE'
        elif self.PlanShapeCB.val() == 11:
            Taxonomy[18] = 'PLFH'
        elif self.PlanShapeCB.val() == 12:
            Taxonomy[18] = 'PLFS'
        elif self.PlanShapeCB.val() == 13:
            Taxonomy[18] = 'PLFT'
        elif self.PlanShapeCB.val() == 14:
            Taxonomy[18] = 'PLFU'
        elif self.PlanShapeCB.val() == 15:
            Taxonomy[18] = 'PLFX'
        elif self.PlanShapeCB.val() == 16:
            Taxonomy[18] = 'PLFY'
        elif self.PlanShapeCB.val() == 17:
            Taxonomy[18] = 'PLFP'
        elif self.PlanShapeCB.val() == 18:
            Taxonomy[18] = 'PLFPO'
        elif self.PlanShapeCB.val() == 19:
            Taxonomy[18] = 'PLFI'

        if self.RegularityCB1.val() == 0:
            if (out_type == 0):
                Taxonomy[19] = 'IR99'

        else:
            if self.RegularityCB1.val() == 1:
                Taxonomy[19] = 'IRRE'
            if self.RegularityCB1.val() == 2:
                Taxonomy[19] = 'IRIR'
                if self.RegularityCB2.val() == 0 and (out_type == 0):
                    Taxonomy[20] = '+IRPP:IRN'
                if self.RegularityCB2.val() == 1:
                    Taxonomy[20] = '+IRPP:TOR'
                if self.RegularityCB2.val() == 2:
                    Taxonomy[20] = '+IRPP:REC'
                if self.RegularityCB2.val() == 3:
                    Taxonomy[20] = '+IRPP:IRHO'

                if self.RegularityCB3.val() == 0 and (out_type == 0):
                    Taxonomy[21] = '+IRVP:IRN'
                if self.RegularityCB3.val() == 1:
                    Taxonomy[21] = '+IRVP:SOS'
                if self.RegularityCB3.val() == 2:
                    Taxonomy[21] = '+IRVP:CRW'
                if self.RegularityCB3.val() == 3:
                    Taxonomy[21] = '+IRVP:SHC'
                if self.RegularityCB3.val() == 4:
                    Taxonomy[21] = '+IRVP:POP'
                if self.RegularityCB3.val() == 5:
                    Taxonomy[21] = '+IRVP:SET'
                if self.RegularityCB3.val() == 6:
                    Taxonomy[21] = '+IRVP:CHV'
                if self.RegularityCB3.val() == 7:
                    Taxonomy[21] = '+IRVP:IRVO'

                if self.RegularityCB2.val() > 0:
                    if self.RegularityCB4.val() == 0:
                        Taxonomy[22] = '+IRPS:IRN'
                    if self.RegularityCB4.val() == 1:
                        Taxonomy[22] = '+IRPS:TOR'
                    if self.RegularityCB4.val() == 2:
                        Taxonomy[22] = '+IRPS:REC'
                    if self.RegularityCB4.val() == 3:
                        Taxonomy[22] = '+IRPS:IRHO'

                if self.RegularityCB3.val() > 0:
                    if self.RegularityCB5.val() == 0:
                        Taxonomy[23] = '+IRVS:IRN'
                    if self.RegularityCB5.val() == 1:
                        Taxonomy[23] = '+IRVS:SOS'
                    if self.RegularityCB5.val() == 2:
                        Taxonomy[23] = '+IRVS:CRW'
                    if self.RegularityCB5.val() == 3:
                        Taxonomy[23] = '+IRVS:SHC'
                    if self.RegularityCB5.val() == 4:
                        Taxonomy[23] = '+IRVS:POP'
                    if self.RegularityCB5.val() == 5:
                        Taxonomy[23] = '+IRVS:SET'
                    if self.RegularityCB5.val() == 6:
                        Taxonomy[23] = '+IRVS:CHV'
                    if self.RegularityCB5.val() == 7:
                        Taxonomy[23] = '+IRVS:IRVO'




        if self.WallsCB.val() == 0 and (out_type == 0):
            Taxonomy[24] = 'EW99'
        if self.WallsCB.val() == 1:
            Taxonomy[24] = 'EWC'
        if self.WallsCB.val() == 2:
            Taxonomy[24] = 'EWG'
        if self.WallsCB.val() == 3:
            Taxonomy[24] = 'EWE'
        if self.WallsCB.val() == 4:
            Taxonomy[24] = 'EWMA'
        if self.WallsCB.val() == 5:
            Taxonomy[24] = 'EWME'
        if self.WallsCB.val() == 6:
            Taxonomy[24] = 'EWV'
        if self.WallsCB.val() == 7:
            Taxonomy[24] = 'EWW'
        if self.WallsCB.val() == 8:
            Taxonomy[24] = 'EWSL'
        if self.WallsCB.val() == 9:
            Taxonomy[24] = 'EWPL'
        if self.WallsCB.val() == 10:
            Taxonomy[24] = 'EWCB'
        if self.WallsCB.val() == 11:
            Taxonomy[24] = 'EWO'

        if self.RoofCB1.val() == 0 and (out_type == 0):
            Taxonomy[25] = 'RSH99'
        if self.RoofCB1.val() == 1:
            Taxonomy[25] = 'RSH1'
        if self.RoofCB1.val() == 2:
            Taxonomy[25] = 'RSH2'
        if self.RoofCB1.val() == 3:
            Taxonomy[25] = 'RSH3'
        if self.RoofCB1.val() == 4:
            Taxonomy[25] = 'RSH4'
        if self.RoofCB1.val() == 5:
            Taxonomy[25] = 'RSH5'
        if self.RoofCB1.val() == 6:
            Taxonomy[25] = 'RSH6'
        if self.RoofCB1.val() == 7:
            Taxonomy[25] = 'RSH7'
        if self.RoofCB1.val() == 8:
            Taxonomy[25] = 'RSH8'
        if self.RoofCB1.val() == 9:
            Taxonomy[25] = 'RSH9'
        if self.RoofCB1.val() == 10:
            Taxonomy[25] = 'RSHO'

        if self.RoofCB2.val() == 0 and (out_type == 0):
            Taxonomy[26] = 'RMT99'
        if self.RoofCB2.val() == 1:
            Taxonomy[26] = 'RMN'
        if self.RoofCB2.val() == 2:
            Taxonomy[26] = 'RMT1'
        if self.RoofCB2.val() == 3:
            Taxonomy[26] = 'RMT2'
        if self.RoofCB2.val() == 4:
            Taxonomy[26] = 'RMT3'
        if self.RoofCB2.val() == 5:
            Taxonomy[26] = 'RMT4'
        if self.RoofCB2.val() == 6:
            Taxonomy[26] = 'RMT5'
        if self.RoofCB2.val() == 7:
            Taxonomy[26] = 'RMT6'
        if self.RoofCB2.val() == 8:
            Taxonomy[26] = 'RMT7'
        if self.RoofCB2.val() == 9:
            Taxonomy[26] = 'RMT8'
        if self.RoofCB2.val() == 10:
            Taxonomy[26] = 'RMT9'
        if self.RoofCB2.val() == 11:
            Taxonomy[26] = 'RMT10'
        if self.RoofCB2.val() == 12:
            Taxonomy[26] = 'RMT11'
        if self.RoofCB2.val() == 13:
            Taxonomy[26] = 'RMTO'

        if self.RoofCB3.val() == 0:
            if (out_type == 0):
                Taxonomy[27] = 'R99'

        else:
            if self.RoofCB3.val() == 1:
                Taxonomy[27] = 'RM'
                if self.RoofCB4.val() == 0 and (out_type == 0):
                    Taxonomy[28] = 'RM99'
                if self.RoofCB4.val() == 1:
                    Taxonomy[28] = 'RM1'
                if self.RoofCB4.val() == 2:
                    Taxonomy[28] = 'RM2'
                if self.RoofCB4.val() == 3:
                    Taxonomy[28] = 'RM3'

            elif self.RoofCB3.val() == 2:
                Taxonomy[27] = 'RE'
                if self.RoofCB4.val() == 0 and (out_type == 0):
                    Taxonomy[28] = 'RE99'
                if self.RoofCB4.val() == 1:
                    Taxonomy[28] = 'RE1'

            elif self.RoofCB3.val() == 3:
                Taxonomy[27] = 'RC'
                if self.RoofCB4.val() == 0 and (out_type == 0):
                    Taxonomy[28] = 'RC99'
                if self.RoofCB4.val() == 1:
                    Taxonomy[28] = 'RC1'
                if self.RoofCB4.val() == 2:
                    Taxonomy[28] = 'RC2'
                if self.RoofCB4.val() == 3:
                    Taxonomy[28] = 'RC3'
                if self.RoofCB4.val() == 4:
                    Taxonomy[28] = 'RC4'

            elif self.RoofCB3.val() == 4:
                Taxonomy[27] = 'RME'
                if self.RoofCB4.val() == 0 and (out_type == 0):
                    Taxonomy[28] = 'RME99'
                if self.RoofCB4.val() == 1:
                    Taxonomy[28] = 'RME1'
                if self.RoofCB4.val() == 2:
                    Taxonomy[28] = 'RME2'
                if self.RoofCB4.val() == 3:
                    Taxonomy[28] = 'RME3'

            elif self.RoofCB3.val() == 5:
                Taxonomy[27] = 'RWO'
                if self.RoofCB4.val() == 0 and (out_type == 0):
                    Taxonomy[28] = 'RWO99'
                if self.RoofCB4.val() == 1:
                    Taxonomy[28] = 'RWO1'
                if self.RoofCB4.val() == 2:
                    Taxonomy[28] = 'RWO2'
                if self.RoofCB4.val() == 3:
                    Taxonomy[28] = 'RWO3'
                if self.RoofCB4.val() == 4:
                    Taxonomy[28] = 'RWO4'
                if self.RoofCB4.val() == 5:
                    Taxonomy[28] = 'RWO5'

            elif self.RoofCB3.val() == 6:
                Taxonomy[27] = 'RFA'
                if self.RoofCB4.val() == 0:
                    Taxonomy[28] = 'RFA1'
                if self.RoofCB4.val() == 1:
                    Taxonomy[28] = 'RFAO'

            elif self.RoofCB3.val() == 7:
                Taxonomy[27] = 'RO'



        if self.RoofCB5.val() == 0 and (out_type == 0):
            Taxonomy[29] = 'RWC99'
        if self.RoofCB5.val() == 1:
            Taxonomy[29] = 'RWCN'
        if self.RoofCB5.val() == 2:
            Taxonomy[29] = 'RWCP'
        if self.RoofCB5.val() == 3:
            Taxonomy[29] = 'RTD99'
        if self.RoofCB5.val() == 4:
            Taxonomy[29] = 'RTDN'
        if self.RoofCB5.val() == 5:
            Taxonomy[29] = 'RTDP'

        if self.FloorCB1.val() == 0:
            if (out_type == 0):
                Taxonomy[30] = 'F99'

        elif self.FloorCB1.val() == 1:
            Taxonomy[30] = 'FN'

        else:
            if self.FloorCB1.val() == 2:
                Taxonomy[30] = 'FM'
                if self.FloorCB2.val() == 0 and (out_type == 0):
                    Taxonomy[31] = '+FM99'
                if self.FloorCB2.val() == 1:
                    Taxonomy[31] = '+FM1'
                if self.FloorCB2.val() == 2:
                    Taxonomy[31] = '+FM2'
                if self.FloorCB2.val() == 3:
                    Taxonomy[31] = '+FM3'

            elif self.FloorCB1.val() == 3:
                Taxonomy[30] = 'FE'
                if self.FloorCB2.val() == 0 and (out_type == 0):
                    Taxonomy[31] = '+FE99'

            elif self.FloorCB1.val() == 4:
                Taxonomy[30] = 'FC'
                if self.FloorCB2.val() == 0 and (out_type == 0):
                    Taxonomy[31] = '+FC99'
                if self.FloorCB2.val() == 1:
                    Taxonomy[31] = '+FC1'
                if self.FloorCB2.val() == 2:
                    Taxonomy[31] = '+FC2'
                if self.FloorCB2.val() == 3:
                    Taxonomy[31] = '+FC3'
                if self.FloorCB2.val() == 4:
                    Taxonomy[31] = '+FC4'

            elif self.FloorCB1.val() == 5:
                Taxonomy[30] = 'FME'
                if self.FloorCB2.val() == 0 and (out_type == 0):
                    Taxonomy[31] = '+FME99'
                if self.FloorCB2.val() == 1:
                    Taxonomy[31] = '+FME1'
                if self.FloorCB2.val() == 2:
                    Taxonomy[31] = '+FME2'
                if self.FloorCB2.val() == 3:
                    Taxonomy[31] = '+FME3'

            elif self.FloorCB1.val() == 6:
                Taxonomy[30] = 'FW'
                if self.FloorCB2.val() == 0 and (out_type == 0):
                    Taxonomy[31] = '+FW99'
                if self.FloorCB2.val() == 1:
                    Taxonomy[31] = '+FW1'
                if self.FloorCB2.val() == 2:
                    Taxonomy[31] = '+FW2'
                if self.FloorCB2.val() == 3:
                    Taxonomy[31] = '+FW3'
                if self.FloorCB2.val() == 4:
                    Taxonomy[31] = '+FW4'

            elif self.FloorCB1.val() == 7:
                Taxonomy[30] = 'FO'


        if self.FloorCB3.val() == 0 and (out_type == 0):
            Taxonomy[32] = 'FWC99'
        if self.FloorCB3.val() == 1:
            Taxonomy[32] = 'FWCN'
        if self.FloorCB3.val() == 2:
            Taxonomy[32] = 'FWCP'

        if self.FoundationsCB.val() == 0 and (out_type == 0):
            Taxonomy[33] = 'FOS99'
        if self.FoundationsCB.val() == 1:
            Taxonomy[33] = 'FOSSL'
        if self.FoundationsCB.val() == 2:
            Taxonomy[33] = 'FOSN'
        if self.FoundationsCB.val() == 3:
            Taxonomy[33] = 'FOSDL'
        if self.FoundationsCB.val() == 4:
            Taxonomy[33] = 'FOSDN'
        if self.FoundationsCB.val() == 5:
            Taxonomy[33] = 'FOSO'


        # // TAIL
        direction1 = 'DX'
        direction2 = 'DY'

        if self.Direction1RB1.checked()  and (out_type == 0):
            direction1 = direction1 + '+D99'
            direction2 = direction2 + '+D99'

        elif self.Direction1RB2.checked():
            direction1 = direction1 + '+PF'
            direction2 = direction2 + '+OF'


        # /*
        #    0) direction X

        #       0 - Material type
        #       1 - Material technology
        #       34- Material tech adds
        #       2 - Material properties

        #       3 - Type of lateral system
        #       4 - System ductility

        #       direction Y

        #       5 - Material type
        #       6 - Material technology
        #       35- Material tech adds
        #       7 - Material properties

        #    5) 8 - Type of lateral system
        #       9 - System ductility

        #       11 - Height above the ground
        #       12 - Height below the ground
        #       13 - Height of grade
        #       14 - Slope of the ground

        #       10 - Date of construction

        #       15 - Occupancy type
        #       16 - Occupancy description

        #       17 - Position
        #       18 - Plan

        #    10)19 - Type of irregularity
        #       20 - Plan irregularity(primary)
        #       22 - Vertical irregularity(primary)
        #       21 - Plan irregularity(secondary)
        #       23 - Vertical irregularity(secondary)

        #       24- Material of exterior walls

        #       25 - Roof shape
        #       26 - Roof covering
        #       27 - Roof system material
        #       28 - Roof system type
        #       29 - Roof connections

        #       30 - Floor system material
        #       31 - Floor system type
        #       32 - Floor connections

        #       33 - Foundation
        #       */

        # /* roof special case */
        roof_atom_empty = True
        for i in range(25, 30):
            if Taxonomy[i] != '':
                if roof_atom_empty:
                    roof_atom_empty = False
                else:
                    Taxonomy[i] = "+" + Taxonomy[i]


        # /* floor special case */
        floor_atom_empty = True
        floor_atom_primaries = [30, 32]
        for i in floor_atom_primaries:
            if Taxonomy[i] != '':
                if floor_atom_empty:
                    floor_atom_empty = False
                else:
                    Taxonomy[i] = "+" + Taxonomy[i]


        ResTax = (direction1 + '/' + Taxonomy[0] + Taxonomy[1] + Taxonomy[34] + Taxonomy[2] +
            '/' +Taxonomy[3] + Taxonomy[4] +
            '/' + direction2 + '/' + Taxonomy[5] + Taxonomy[6] + Taxonomy[35] + Taxonomy[7] +
            '/' + Taxonomy[8] + Taxonomy[9] +
            '/' + Taxonomy[11] + Taxonomy[12] + Taxonomy[13] + Taxonomy[14] + '/' + Taxonomy[10] +
            '/' + Taxonomy[15] + Taxonomy[16] + '/' + Taxonomy[17] + '/' + Taxonomy[18] +
            '/' + Taxonomy[19] + Taxonomy[20] + Taxonomy[22] + Taxonomy[21] + Taxonomy[23] +
            '/' + Taxonomy[24] + '/' + Taxonomy[25] + Taxonomy[26] + Taxonomy[27] + Taxonomy[28] + Taxonomy[29] +
            '/' + Taxonomy[30] + Taxonomy[31] + Taxonomy[32] + '/' + Taxonomy[33])

        if out_type == 2:
            is_first = True
            ResAtoms = ResTax.split('/')
            if ResAtoms[1] == ResAtoms[4] and ResAtoms[2] == ResAtoms[5]:
                # // same params case
                ResAtoms[3] = ResAtoms[4] = ResAtoms[5] = ""
                if self.Direction1RB1.checked():
                    ResAtoms[0] = ""

                else:
                    ResAtoms[0] = "PF"


            else:
                if self.Direction1RB1.checked():
                    ResAtoms[0] = "DX"
                    ResAtoms[3] = "DY"

                else:
                    ResAtoms[0] = "DX+PF"
                    ResAtoms[3] = "DY+PO"


            ResTax = ""
            for id, v in enumerate(ResAtoms):
                if ResAtoms[id] == "":
                    continue

                if not is_first:
                    ResTax += "/"
                else:
                    is_first = False
                ResTax += ResAtoms[id]


        return (ResTax)




if __name__ == '__main__':
    taxonomy = Taxonomy('taxonomy', True)
    print taxonomy
