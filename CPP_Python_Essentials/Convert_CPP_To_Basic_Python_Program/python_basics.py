from enum import Enum
from dataclasses import dataclass
from typing import List

class MEDICAL_IMAGING_TYPE(Enum):
    CT = 0
    MRI = 1
    PET = 2
    SPECT = 3

@dataclass
class medicalImagingScanner:
    year_bought: int
    name: str
    organs_scanned: List[str]
    num_organs_scanned: int
    minutes_scanned: int
    cost: float
    scanner_type: MEDICAL_IMAGING_TYPE

def askName(medImgScanner):
    print("Whats the medical imaging scanner name?")
    input(medImgScanner.name)
    return medImgScanner

def displayName(medImgScanner):
    print("Medical Imaging Scanner Name: {}".format(medImgScanner.name))

def displayType(medImgScanner):
    print("Medical Imaging Scanner Type: ")
    if medImgScanner.scannerType == MEDICAL_IMAGING_TYPE.CT:
        print("CT")
    elif medImgScanner.scannerType == MEDICAL_IMAGING_TYPE.MRI:
        print("MRI")
    elif medImgScanner.scannerType == MEDICAL_IMAGING_TYPE.PET:
        print("PET")
    elif medImgScanner.scannerType == MEDICAL_IMAGING_TYPE.SPECT:
        print("SPECT")

def askOrgansScanned(medImgScanner):
    print("How many organs were scanned?")
    input(medImgScanner.num_organs_scanned)

    medImgScanner.organs_scanned = list()

    for i in range(medImgScanner.num_organs_scanned):
        print("What organ was scanned?")
        input(organ_scanned)
        medImgScanner.organsScanned.append(organ_scanned)
    return

def displayOrgansScanned(medImgScanner):
    if medImgScanner.num_organs_scanned == 0:
        print("No organs scanned")
        return
    elif len(medImgScanner.organs_scanned) == 0:
        print("No organs scanned")
        return

    print("Medical Imaging Scanned Organs: ")
    for organ_scanned in medImgScanner.num_organs_scanned:
        print(organ_scanned)

def displayScanTime(medImgScanner):
    print("Medical Imaging Scan Time: {}".format(medImgScanner.minutes_scanned))

def displayYearPurchased(medImgScanner):
    print("Medical Imaging Scanner Purchased in Year: {}".format)

if __name__ == "__main__":
    medicalImagingScanner medicalImgScan
    medicalImgScan = askName(medicalImgScan)
    displayName(medicalImgScan)
    medicalImgScan.cost = 5099.99
    medicalImgScan.year_bought = 2018
    medicalImgScan.minutes_scanned = 50
    medicalImgScan.scanner_type = MEDICAL_IMAGING_TYPE.MRI
    displayType(medicalImgScan)
    askOrgansScanned(medicalImgScan)
    displayOrgansScanned(medicalImgScan)
    displayScanTime(medicalImgScan)
