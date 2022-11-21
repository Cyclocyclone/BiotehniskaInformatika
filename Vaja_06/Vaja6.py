from xml2dict import xml2dict
from dict2xml import dict2xml

# Load XML as vector
with open('sampleEHR.xml', 'r') as f:
    XML = f.read()


iDict = {}
iTag= []
EHR = xml2dict(XML, iDict, iTag)

newEHR = EHR
newEHR['medications'].update({'medications2':{}})
newEHR['medications']['medications2'].update({'name':'Ultop'})
newEHR['medications']['medications2'].update({'fullname':'Ultop 10mg trde kapsule'})
newEHR['medications']['medications2'].update({'usage':'1 kapsula vsakih 24 ur'})
newEHR['medications']['medications2'].update({'code':'040762'})
newEHR['medications']['medications2'].update({'dateOfPrescription':{}})
newEHR['medications']['medications2']['dateOfPrescription'].update({'dd ':'15 '})
newEHR['medications']['medications2']['dateOfPrescription'].update({'mm ':'06 '})
newEHR['medications']['medications2']['dateOfPrescription'].update({'yyyy ':'2012 '})
newEHR['medications']['medications2'].update({'dateOfExpiration':{}})
newEHR['medications']['medications2']['dateOfExpiration'].update({ 'dd ':'15 '})
newEHR['medications']['medications2']['dateOfExpiration'].update({ 'mm ':'06 '})
newEHR['medications']['medications2']['dateOfExpiration'].update({ 'yyyy ':'2012 '})

new_XML = dict2xml(newEHR,'','')
with open('sampleEHR2.xml', 'w') as f:
    f.write(new_XML)
