import numpy as np
#Sortiranje števil po bubble metodi
def BubbleSort (iVektor):
    oVektor = np.array(iVektor) #kopiraj vhodni vektor v izhodnega

    NOFI = np.size(oVektor)


    while NOFI !=1:
        newNOFI = 1

        for i in range (NOFI - 1):
            if oVektor[i+1] < oVektor[i]:
                t = oVektor[i+1]
                oVektor[i+1]=oVektor[i]
                oVektor[i]=t
                #print(oVektor)
                newNOFI = i +1
        
        NOFI = newNOFI



    return oVektor