#!/usr/bin/env python
import sys
from openquakeplatform_taxtweb.utils.taxtweb_eng import Taxonomy
from openquakeplatform_taxtweb.utils.taxtweb_maps import (
    material, mat_tech_grp, mat_prop_grp, mat_tead_grp,
    llrs_type_grp, llrs_duct_grp,
    h_aboveground, h_belowground, h_abovegrade, h_slope,
    date_type,
    occu_type, occu_spec_grp
)


def dx2human(blk, no_unknown=False):
    atoms = blk.split('+')
    if len(atoms) == 2 and atoms[1] == 'PF':
        return 'X direction parallel to the street'
    elif no_unknown is False:
        return 'X direction unspecified to the street'
    else:
        return ''


def arrdicts_flatten(arrs):
    d = {}
    for arr in arrs:
        for item in arr:
            d[item["id"]] = item
    return d


def llrs2human(blk, no_unknown=False):
    blk_out = ""
    blk_err = ""
    atoms = blk.split('+')

    llrs_types = arrdicts_flatten(llrs_type_grp)
    llrs_ducts = arrdicts_flatten(llrs_duct_grp)

    for atom in atoms:
        if atom in Taxonomy.UNKNOWN_ATOMS and no_unknown:
            continue

        if atom in llrs_types:
            if blk_out:
                blk_out += '; '
            blk_out += ('Type lateral load-resisting system: ' +
                        llrs_types[atom]['desc'])
        elif atom in llrs_ducts:
            if blk_out:
                blk_out += '; '
            blk_out += 'System ductility: ' + llrs_ducts[atom]['desc']
        else:
            blk_err += ' ' + atom + ' not found'

    return (blk_out, blk_err)


def lmat2human(blk, no_unknown=False):
    blk_out = ""
    blk_err = ""
    atoms = blk.split('+')

    mat_erials = arrdicts_flatten([material])
    mat_techs = arrdicts_flatten(mat_tech_grp)
    mat_props = arrdicts_flatten(mat_prop_grp)
    mat_teads = arrdicts_flatten(mat_tead_grp)

    for atom in atoms:
        if atom in Taxonomy.UNKNOWN_ATOMS and no_unknown:
            continue

        if atom in mat_erials:
            if blk_out:
                blk_out += '; '
            blk_out += 'Material type: ' + mat_erials[atom]['desc']
        elif atom in mat_techs:
            if blk_out:
                blk_out += '; '
            blk_out += 'Material technology: ' + mat_techs[atom]['desc']
        elif atom in mat_props:
            if blk_out:
                blk_out += '; '
            blk_out += 'Material properties: ' + mat_props[atom]['desc']
        elif atom in mat_teads:
            if blk_out:
                blk_out += '; '
            blk_out += ('Material technology (additional): ' +
                      mat_teads[atom]['desc'])
        else:
            blk_err += ' ' + atom + ' subblock not found'

    return (blk_out, blk_err)


def height2human(blk, no_unknown=False):
    blk_out = ""
    blk_err = ""
    subblks = blk.split('+')

    hei_aboveground = arrdicts_flatten([h_aboveground])
    hei_belowground = arrdicts_flatten([h_belowground])
    hei_abovegrade = arrdicts_flatten([h_abovegrade])
    hei_slope = arrdicts_flatten([h_slope])

    for subblk in subblks:
        sub2blks = subblk.split(':')
        atom = sub2blks[0]
        if atom in Taxonomy.UNKNOWN_ATOMS and no_unknown:
            continue

        if atom in hei_aboveground:
            pfx = 'Number of storeys above ground'
            desc = hei_aboveground[atom]['desc']
            sfx = ''
        elif atom in hei_belowground:
            pfx = 'Number of storeys below ground'
            desc = hei_belowground[atom]['desc']
            sfx = ''
        elif atom in hei_abovegrade:
            pfx = 'Height of ground floor level above grade'
            desc = hei_abovegrade[atom]['desc']
            sfx = ' meters'
        elif atom in hei_slope:
            pfx = 'Slope of the ground'
            desc = hei_slope[atom]['desc']
            sfx = ' degrees'
        else:
            if blk_err:
                blk_err += '; '
            blk_err += 'atom ' + atom + ' unknown'
            continue

        if blk_out:
            blk_out += '; '
        if atom in Taxonomy.ATOM_TYPE_RANGE:
            pars = sub2blks[1].split(',')
            blk_out += (pfx + ' - ' + desc + ': between ' +
                        pars[0] + ' and ' + pars[1] + sfx)
        elif atom in Taxonomy.ATOM_TYPE_VALUE:
            blk_out += (pfx + ' - ' + desc + ': ' +
                        sub2blks[1] + sfx)
        else:
            blk_out += (pfx + ' - ' + desc + sfx)

    return (blk_out, blk_err)


def date2human(blk, no_unknown=False):
    blk_out = ""
    blk_err = ""
    subblks = blk.split('+')

    dt_type = arrdicts_flatten([date_type])

    for subblk in subblks:
        sub2blks = subblk.split(':')
        atom = sub2blks[0]
        if atom in Taxonomy.UNKNOWN_ATOMS and no_unknown:
            continue

        if atom in dt_type:
            pfx = 'Date of construction or retrofit'
            desc = dt_type[atom]['desc']
            sfx = ''
        else:
            if blk_err:
                blk_err += '; '
            blk_err += 'atom ' + atom + ' unknown'
            continue

        if blk_out:
            blk_out += '; '
        if atom in Taxonomy.ATOM_TYPE_RANGE:
            pars = sub2blks[1].split(',')
            blk_out += (pfx + ' - ' + desc + ': between ' +
                        pars[0] + ' and ' + pars[1] + sfx)
        elif atom in Taxonomy.ATOM_TYPE_VALUE:
            blk_out += (pfx + ' - ' + desc + ': ' +
                        sub2blks[1] + sfx)
        else:
            blk_out += (pfx + ' - ' + desc + sfx)

    return (blk_out, blk_err)


def occupancy2human(blk, no_unknown=False):
    blk_out = ""
    blk_err = ""
    atoms = blk.split('+')

    occ_types = arrdicts_flatten([occu_type])
    occ_specs = arrdicts_flatten(occu_spec_grp)

    for atom in atoms:
        if atom in Taxonomy.UNKNOWN_ATOMS and no_unknown:
            continue

        if atom in occ_types:
            if blk_out:
                blk_out += '; '
            blk_out += ('Building occupancy type: ' +
                        occ_types[atom]['desc'])
        elif atom in occ_specs:
            if blk_out:
                blk_out += '; '
            blk_out += ('Details: ' +
                        occ_specs[atom]['desc'])
        else:
            blk_err += ' ' + atom + ' subblock not found'

    return (blk_out, blk_err)


def full_text2human(full_text, no_unknown=False):
    atoms = full_text.split('/')

    # Direction specification
    s_out = dx2human(atoms[Taxonomy.POS_DX], no_unknown=no_unknown)

    dx_lmat = atoms[Taxonomy.POS_DX_LMAT]
    dy_lmat = atoms[Taxonomy.POS_DY_LMAT]
    dx_llrs = atoms[Taxonomy.POS_DX_LLRS]
    dy_llrs = atoms[Taxonomy.POS_DY_LLRS]

    if dx_lmat == dy_lmat and dx_llrs == dy_llrs:
        # Material both
        lmat_out, lmat_err = lmat2human(dx_lmat, no_unknown=no_unknown)
        # LLRS both
        llrs_out, llrs_err = llrs2human(dx_llrs, no_unknown=no_unknown)

        if lmat_out:
            if s_out:
                s_out += '; '
            s_out += lmat_out

        if llrs_out:
            if s_out:
                s_out += '; '
            s_out += llrs_out

        next_sep = '; '

    else:
        dx_out = ''
        dy_out = ''
        # Material DX
        dx_lmat_out, dx_lmat_err = lmat2human(
            dx_lmat, no_unknown=no_unknown)
        # LLRS DX
        dx_llrs_out, dx_llrs_err = llrs2human(
            dx_llrs, no_unknown=no_unknown)

        if dx_lmat_out or dx_llrs_out:
            dx_out += 'For X direction - '

            if dx_lmat_out:
                dx_out += dx_lmat_out
                if dx_llrs_out:
                    dx_out += '; '

            if dx_llrs_out:
                dx_out += dx_llrs_out

        # Material DY
        dy_lmat_out, dy_lmat_err = lmat2human(
            dy_lmat, no_unknown=no_unknown)
        # LLRS DY
        dy_llrs_out, dy_llrs_err = llrs2human(
            dy_llrs, no_unknown=no_unknown)

        if dy_lmat_out or dy_llrs_out:
            if dx_out:
                dx_out += '. '
            dy_out += 'For Y direction - '

            if dy_lmat_out:
                dy_out += dy_lmat_out
                if dy_llrs_out:
                    dy_out += '; '

            if dy_llrs_out:
                dy_out += dy_llrs_out

        if dx_lmat_out or dx_llrs_out or dy_lmat_out or dy_llrs_out:
            if s_out:
                s_out += '. '
            s_out += dx_out + dy_out
            next_sep = '. '

    # height
    hei_out, hei_err = height2human(atoms[Taxonomy.POS_HEIGHT],
                                    no_unknown=no_unknown)
    if hei_out:
        if s_out:
            s_out += next_sep
        s_out += hei_out
        next_sep = '; '

    # date
    dt_out, dt_err = date2human(atoms[Taxonomy.POS_DATE],
                                no_unknown=no_unknown)
    if dt_out:
        if s_out:
            s_out += next_sep
        s_out += dt_out
        next_sep = '; '

    # occupancy
    dt_out, dt_err = occupancy2human(atoms[Taxonomy.POS_OCCUPANCY],
                                     no_unknown=no_unknown)
    if dt_out:
        if s_out:
            s_out += next_sep
        s_out += dt_out
        next_sep = '; '
    if s_out:
        s_out += '.'

    return s_out


def taxonomy2human(s, no_unknown=True):
    t = Taxonomy('Taxonomy', True)

    full_text, full_res = t.process(s, 0)

    if full_res is None:
        s_out = full_text2human(full_text, no_unknown=no_unknown)
    else:
        s_out = "Invalid GEM Taxonomy v2.0 string: %s" % s

    return s_out


if __name__ == '__main__':
    print(taxonomy2human(sys.argv[1], no_unknown=True))
