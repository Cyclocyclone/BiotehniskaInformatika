import numpy as np

def xml2dict_attr(iXML, iDict, iTag_):
    iXML = ''.join(iXML)
    oDict = iDict
    idx1 = 2
    type = 0

    while (idx1 > 0):
        iTag = iTag_.copy()
        idx1 = iXML.find('<')

        if (idx1 >= 0):
            idx2 = iXML.find('>')
            tag = iXML[idx1+1:idx2]

            idxtype = tag.find('type=')

            if idxtype > 0:
                if "number" in tag:
                    type = "number"
                else:
                    type = ""
                tag = tag[0:idxtype-1]

            idx3 = iXML.find('</' + tag + '>')
            xml = iXML[idx2+1:idx3]
            idx4 = xml.find('<')

            if (len(tag)>0):
                iTag.append(tag)

            if (idx4 > 0):
                oDict = xml2dict_attr(xml, oDict, iTag)

            else:
                string_for_eval = ''
                
                for tag_ in iTag:
                    string_before = string_for_eval
                    string_for_eval = string_for_eval + "['" + tag_ + "']"

                    try:
                        eval("oDict" + string_for_eval)
                    except:
                        eval("oDict" + string_before + ".update({tag_:{}})")

                if type == "number":
                    xml = int(xml)
                eval("oDict" + string_before + ".update({tag_:xml})")

            iXML = iXML[idx3 + len('</' + tag + '>'):]
            idx1 = iXML.find('<')

    return oDict