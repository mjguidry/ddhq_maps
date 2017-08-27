# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 20:22:59 2017

@author: mike
"""
from subprocess import call
import os

fips={
    '01':'AL',
    '02':'AK',
    '04':'AZ',
    '05':'AR',
    '06':'CA',
    '08':'CO',
    '09':'CT',
    '10':'DE',
    '11':'DC',
    '12':'FL',
    '13':'GA',
    '15':'HI',
    '16':'ID',
    '17':'IL',
    '18':'IN',
    '19':'IA',
    '20':'KS',
    '21':'KY',
    '22':'LA',
    '23':'ME',
    '24':'MD',
    '25':'MA',
    '26':'MI',
    '27':'MN',
    '28':'MS',
    '29':'MO',
    '30':'MT',
    '31':'NE',
    '32':'NV',
    '33':'NH',
    '34':'NJ',
    '35':'NM',
    '36':'NY',
    '37':'NC',
    '38':'ND',
    '39':'OH',
    '40':'OK',
    '41':'OR',
    '42':'PA',
    '44':'RI',
    '45':'SC',
    '46':'SD',
    '47':'TN',
    '48':'TX',
    '49':'UT',
    '50':'VT',
    '51':'VA',
    '53':'WA',
    '54':'WV',
    '55':'WI',
    '56':'WY',
    }
    
for code in fips:
    state=fips[code]
    call_str='ogr2ogr -f GeoJSON -where "STATEFP=\''+code+'\'" '
    call_str=call_str+'/home/mike/projects/mjguidry/ddhq_maps/state_maps/'+state+'.json '
    call_str=call_str+os.path.expanduser('~/shapefiles/cb_2016_us_state_500k/cb_2016_us_state_500k.shp')
    call(call_str,shell=True)
