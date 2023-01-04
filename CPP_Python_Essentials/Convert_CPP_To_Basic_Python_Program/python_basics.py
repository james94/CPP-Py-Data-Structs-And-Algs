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

def askName():
    return

def askName():
    return

def displayName():
    return

def displayType():
    return

def askOrgansScanned():
    return

def display
