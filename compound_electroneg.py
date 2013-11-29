#!/usr/bin/env python

################################################################################
# Copyright Daniel Davies, Adam J. Jackson (2013)                              #
#                                                                              #
#  This file is part of SMACT: compound_electroneg.py is free software: you can#
#  redistribute it and/or modify it under the terms of the GNU General Public  #
#  License as published by the Free Software Foundation, either version 3 of   #
#  the License, or (at your option) any later version.                         #
#  This program is distributed in the hope that it will be useful, but WITHOUT #
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       #
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for   #
#  more details.                                                               #
#  You should have received a copy of the GNU General Public License along with#
#  this program.  If not, see <http://www.gnu.org/licenses/>.                  #
################################################################################

import sys
from numpy import product
from smact_data import get_mulliken

def compound_electroneg(verbose=False,elements=None,stoichs=None):
    """Compound electronegativity from geometric mean of elemental Mulliken electronegativities."""
        
    """Get elements and stoichiometries if not provided as argument"""
    if not elements:
        elements=raw_input("Enter elements (space separated): ")
    if not stoichs:
        stoichs=raw_input("Enter stoichiometries (space separated): ")
    elementlist=list(elements.split(" "))
    stoichslist=list(stoichs.split(" "))

    """Convert stoichslist from string to float"""
    stoichslist=map(float, stoichslist)

    """Check input for debugging"""
    #print "List of elements=", elementlist
    #print "Relative ratios=", stoichslist

    """Get mulliken values for each element"""
    for i in range(0,len(elementlist)):
        elementlist[i]=get_mulliken(elementlist[i])

    if verbose:
        print "Electronegativities of elements=", elementlist

    """Raise each electronegativity to it's appropriate power"""
    for i in range(0,len(elementlist)):
        elementlist[i]=[elementlist[i]**stoichslist[i]]

    #print "Electronegativities raised to powers=", elementlist

    """Calculate final answer"""
    prod = product(elementlist)
    #print "Product=", prod
    compelectroneg = (prod)**(1.0/(sum(stoichslist)))
    if verbose:
        print "Geometric mean = Compound 'electronegativity'=", compelectroneg
    return compelectroneg
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Compound electronegativity from geometric mean of elemental Mulliken electronegativities.")
    parser.add_argument("-e", "--elements", type=str,
                        help="Space-separated string of elements (e.g. \"Cu Zn Sn S\")"
                        )
    parser.add_argument("-s", "--stoichiometry", type=str,
                        help="Space-separated string of stoichiometry (e.g. \"2 1 1 4\")"
                        )
    parser.add_argument("-v", "--verbose", help="More verbose output [default]",
                        action="store_true")
    parser.add_argument("-q", "--quiet", help="Quiet output",
                       action="store_true")
    args=parser.parse_args()
    if args.quiet:
        verbose_flag=False
    else:
        verbose_flag=True

    print compound_electroneg(verbose=verbose_flag,elements=args.elements,
                              stoichs=args.stoichiometry)

