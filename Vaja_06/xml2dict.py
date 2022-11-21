import numpy as np

def xml2dict(iXml, iDict, iTag_):
    iXml = ''.join(iXml)
    oDict = iDict
    idx1 = 2
    while idx1 > 0:
        iTag = iTag_.copy()
        idx1 = iXml.find('<')
        if idx1 >= 0:
            idx2 = iXml.find('>')
            tag = iXml[idx1+1:idx2]
            idx3 = iXml.find('</'+tag+'>')
            xml = iXml[idx2+1:idx3]
            idx4 = xml.find('<')

            if len(tag)>0:
                iTag.append(tag)

            if idx4 > 0:
                oDict = xml2dict(xml, oDict, iTag)
            else:
                string_for_eval = ''
                for tag_ in iTag:
                    string_before = string_for_eval
                    string_for_eval = string_for_eval + "['" + tag_ + "']"
                    try:
                        eval("oDict" + string_for_eval)
                    except:
                        eval("oDict" + string_before + ".update({tag_:{}})")
                eval("oDict" + string_before + ".update({tag_:xml})")
            iXml = iXml[idx3 + len('</' + tag + '>'):]
            idx1 = iXml.find('<')

    return oDict
