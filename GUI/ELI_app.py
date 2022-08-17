from itertools import count
from pageOne import pageOne_function
from OctetGBGToggle import gbgOrOctetToggle_function
from normVariablesForOctet import normVariablesOctet_function
from runTimeVariables import runTimeVariables_Function
from normVariablesForNoFile import normVariablesNoFile_function
from worktableImage import worktableImage_Function

masterDict = {}
counter = 0
while counter == 0:
    pageOneReturn = pageOne_function()
    fileBasedNorm = pageOneReturn['fileBasedNorm']
    masterDict['fileBasedNorm'] = fileBasedNorm
    counter = counter + 1

while counter == 1:
    if fileBasedNorm == "yes":
        progressBarDictated = True
        octetOrGBGReturn = gbgOrOctetToggle_function()
        octetOrGBG = octetOrGBGReturn["fileOrigin"]
    else:
        progressBarDictated = False
        noFileNormVarReturn = normVariablesNoFile_function()
        for key, value in noFileNormVarReturn.items():
            masterDict[key] = value
    counter = counter + 1
  
    
while counter == 2:
    if fileBasedNorm == "yes":
        if octetOrGBG == "Octet":
            normVariablesOctet = normVariablesOctet_function()
            for key, value in normVariablesOctet.items():
                masterDict[key] = value
        elif octetOrGBG == "GBG":
            pass
    else:
        runTimeVariableReturn = runTimeVariables_Function(progressBarDictated)
        for key, value in runTimeVariableReturn.items():
            masterDict[key] = value
    counter = counter + 1

while counter == 3:
    if fileBasedNorm == "yes":
        runTimeVariableReturn = runTimeVariables_Function(progressBarDictated)
        for key, value in runTimeVariableReturn.items():
            masterDict[key] = value
    else:
        pass
    counter = counter + 1
    
    

#worktable Image
sourceType = str(masterDict["sourceTypeSelected"])
sourceType = sourceType.replace(" ", "")
desType = str(masterDict["desTypeSelected"])
desType = desType.replace(" ", "")
tipType = masterDict["tipTypeSelected"]
worktableImageName = "C:\Enhanced_Lynx_Interface\GUI\worktableImages\PNG\\" + tipType  + "_" + sourceType  + "_" + desType + "_worktableImage.PNG"

while counter == 4:
    worktableImage_Function(worktableImageName, sourceType, desType, tipType)
    counter = counter + 1

print("Master Dictionary")
for key, value in masterDict.items():
    print(key + ": " + str(value))


#ELI_app.py