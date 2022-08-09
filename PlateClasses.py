from csv import reader
import csv
from datetime import datetime


#time management
current_datetime = datetime.now()
time = current_datetime.strftime("%d.%m.%Y %H.%M.%S")
time = time.replace(" ", "_")
time = str(time)



class QuantPlate_Octet:
    numInstances = 0

    plate1of4 = ["A1", "C1", "E1", "G1", "I1", "K1", "M1", "O1", "A3", "C3", "E3", "G3", "I3", "K3", "M3", "O3", "A5", "C5", "E5", "G5", "I5", "K5", "M5", "O5", "A7", "C7", "E7", "G7", "I7", "K7", "M7", "O7", "A9", "C9", "E9", "G9", "I9", "K9", "M9", "O9", "A11", "C11", "E11", "G11", "I11", "K11", "M11", "O11", "A13", "C13", "E13", "G13", "I13", "K13", "M13", "O13", "A15", "C15", "E15", "G15", "I15", "K15", "M15", "O15", "A17", "C17", "E17", "G17", "I17", "K17", "M17", "O17", "A19", "C19", "E19", "G19", "I19", "K19", "M19", "O19", "A21", "C21", "E21", "G21", "I21", "K21", "M21", "O21", "A23", "C23", "E23", "G23", "I23", "K23", "M23", "O23"]
    plate2of4 = ["A2", "C2", "E2", "G2", "I2", "K2", "M2", "O2", "A4", "C4", "E4", "G4", "I4", "K4", "M4", "O4", "A6", "C6", "E6", "G6", "I6", "K6", "M6", "O6", "A8", "C8", "E8", "G8", "I8", "K8", "M8", "O8", "A10", "C10", "E10", "G10", "I10", "K10", "M10", "O1", "A12", "C12", "E12", "G12", "I12", "K12", "M12", "O12", "A14", "C14", "E14", "G14", "I14", "K14", "M14", "O14", "A16", "C16", "E16", "G16", "I16", "K16", "M16", "O16", "A18", "C18", "E18", "G18", "I18", "K18", "M18", "O18", "A20", "C20", "E20", "G20", "I20", "K20", "M20", "O20", "A22", "C22", "E22", "G22", "I22", "K22", "M22", "O22", "A24", "C24", "E24", "G24", "I24", "K24", "M24", "O24"]
    plate3of4 = ["B1", "D1", "F1", "H1", "J1", "L1", "N1", "P1", "B3", "D3", "F3", "H3", "J3", "L3", "N3", "P3", "B5", "D5", "F5", "H5", "J5", "L5", "N5", "P5", "B7", "D7", "F7", "H7", "J7", "L7", "N7", "P7", "B9", "D9", "F9", "H9", "J9", "L9", "N9", "P9", "B11", "D11", "F11", "H11", "J11", "L11", "N11", "P11", "B13", "D13", "F13", "H13", "J13", "L13", "N13", "P13", "B15", "D15", "F15", "H15", "J15", "L15", "N15", "P15", "B17", "D17", "F17", "H17", "J17", "L17", "N17", "P17", "B19", "D19", "F19", "H19", "J19", "L19", "N19", "P19", "B21", "D21", "F21", "H21", "J21", "L21", "N21", "P21", "B23", "D23", "F23", "H23", "J23", "L23", "N23", "P23"]
    plate4of4 = ["B2", "D2", "F2", "H2", "J2", "L2", "N2", "P2", "B4", "D4", "F4", "H4", "J4", "L4", "N4", "P4", "B6", "D6", "F6", "H6", "J6", "L6", "N6", "P6", "B8", "D8", "F8", "H8", "J8", "L8", "N8", "P8", "B10", "D10", "F10", "H10", "J10", "L10", "N10", "P1", "B12", "D12", "F12", "H12", "J12", "L12", "N12", "P12", "B14", "D14", "F14", "H14", "J14", "L14", "N14", "P14", "B16", "D16", "F16", "H16", "J16", "L16", "N16", "P16", "B18", "D18", "F18", "H18", "J18", "L18", "N18", "P18", "B20", "D20", "F20", "H20", "J20", "L20", "N20", "P20", "B22", "D22", "F22", "H22", "J22", "L22", "N22", "P22", "B24", "D24", "F24", "H24", "J24", "L24", "N24", "P24"]
    
    def __init__(self, plateNum, octetFilePath, numberOfQuads_fromOctetPlate):
        self.platenNum = plateNum
        self.octetFilePath = octetFilePath
        self.numberOfQuads_fromOctetPlate = numberOfQuads_fromOctetPlate
        QuantPlate_Octet.numInstances += 1 #numInstance is the total count of class instances created
        self.count = QuantPlate_Octet.numInstances #count is the object instance number
        self.octetQuantsDict_Quad1 = {}
        self.octetQuantsDict_Quad2 = {}
        self.octetQuantsDict_Quad3 = {}
        self.octetQuantsDict_Quad4 = {}
        self.octetQuants_Quad1 = []
        self.octetQuants_Quad2 = []
        self.octetQuants_Quad3 = []
        self.octetQuants_Quad4 = []
        self.octetBarcode = "OctetPlate" + str(self.count)


    #reads incoming octet raw file and capture well id and qant value into a dictionary based on the quad of the 384 well plate the well id is in
    def setQuantDictionary(self):
        with open(self.octetFilePath, "r") as f:
            file_reader = reader(f)
            counter = 0
            for i in file_reader:
                if counter != 0: 
                    wellID = i[5]
                    octetConc = i[12]
                    counter = counter + 1
                    if self.numberOfQuads_fromOctetPlate >= 1: 
                        if wellID in self.plate1of4:
                            self.octetQuantsDict_Quad1[wellID] = octetConc
                    if self.numberOfQuads_fromOctetPlate >= 2:    
                        if wellID in self.plate2of4:
                            self.octetQuantsDict_Quad2[wellID] = octetConc
                    if self.numberOfQuads_fromOctetPlate >= 3:   
                        if wellID in self.plate3of4:
                            self.octetQuantsDict_Quad3[wellID] = octetConc
                    if self.numberOfQuads_fromOctetPlate >= 4:   
                        if wellID in self.plate4of4:
                            self.octetQuantsDict_Quad4[wellID] = octetConc
                else:
                    counter = counter + 1

    #adds dictoary values quant value) to the octetQuants_Quad list based on strict order of the plate#of# list struct
    def quantListCreator(self, dict, read_lst, write_lst):
        counter = 0
        while counter < 96:
            for key, value in dict.items():
                if counter < 96:
                    if key == read_lst[counter]:
                        write_lst.append(value)
                        counter += 1
        return write_lst
    
    def masterQuantParser(self):
        self.setQuantDictionary()
        if self.numberOfQuads_fromOctetPlate >= 1:
            self.quantListCreator(self.octetQuantsDict_Quad1, self.plate1of4, self.octetQuants_Quad1)
        if self.numberOfQuads_fromOctetPlate >= 2:
            self.quantListCreator(self.octetQuantsDict_Quad2, self.plate2of4, self.octetQuants_Quad2)
        if self.numberOfQuads_fromOctetPlate >= 3:
            self.quantListCreator(self.octetQuantsDict_Quad3, self.plate3of4, self.octetQuants_Quad3)
        if self.numberOfQuads_fromOctetPlate >= 4:
            self.quantListCreator(self.octetQuantsDict_Quad4, self.plate4of4, self.octetQuants_Quad4)

    def getOctetQuants_Quad1(self):
        return self.octetQuants_Quad1
    def getOctetQuants_Quad2(self):
        return self.octetQuants_Quad2
    def getOctetQuants_Quad3(self):
        return self.octetQuants_Quad3
    def getOctetQuants_Quad4(self):
        return self.octetQuants_Quad4
    


class NormPlate:
    numInstances = 0
    

    def __init__(self, plateNum, targetConc, targetVol, neatVol):
        self.plateNum = plateNum
        self.targetConc = targetConc
        self.targetVol = targetVol
        self.neatVol = neatVol
        self.supVolList = []
        self.dilVolList = []
        NormPlate.numInstances += 1 #numInstance is the total count of class instances created
        self.count = NormPlate.numInstances #count is the object instance number
        self.SupCSVInput = "C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time + "\SupCSVInput_" + str(self.count) + "_" + time + ".csv"
        self.DilCSVInput =  "C:\codeBASE\Lynx\output_Test_files\Lynx_Input_" + time + "\DilCSVInput_" + str(self.count) + "_" + time + ".csv"

    #gets Sup CSV input file path
    def getSupCSVInput(self):
        return self.SupCSVInput

    #gets Dil CSV input file path 
    def getDilCSVInput(self):
        return self.DilCSVInput
    #gets parsed quant data list
    def getQuantData(self):
        return self.quantDatalst
    
    #method used locally by other methods in class only
    def supCalc(self, quantConc):
        supVol = (self.targetConc/quantConc) * self.targetVol
        if supVol > self.targetVol:
            finalSupVol = self.neatVol
        else:
            finalSupVol = supVol
        finalSupVol = round(finalSupVol, 2)
        # finalSupVol = quantConc
        return finalSupVol

    def volListCreation(self, quantDatalst):
        for i in quantDatalst:
            quantConc = i
            quantConc = float(quantConc)
            supVol = self.supCalc(quantConc)
            dilVol = self.targetVol - supVol
            dilVol = round(dilVol, 2)
            self.supVolList.append(str(supVol))
            self.dilVolList.append(str(dilVol))

    def getSupVolList(self):
        return(self.supVolList)

    def getDilVolList(self):
        return(self.dilVolList)

    def plateFormatFileWriter(self, writer, lst):
        writer("VI;12;8")
        for i in range(1, 13):
                writer("," + str(i))
        aplhaList = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(0, 8):
            writer("\n")
            writer(aplhaList[i])
            for j in range(i, 96, 8):
                writer("," + lst[j])

    def inputCSVFileWriter(self):
        with open(self.SupCSVInput, "w") as SUP:
            writer = SUP.write
            self.plateFormatFileWriter(writer, self.supVolList)

        with open(self.DilCSVInput, "w") as DIL:
            writer = DIL.write
            self.plateFormatFileWriter(writer, self.dilVolList)


#testingPlatesAsObjects.py