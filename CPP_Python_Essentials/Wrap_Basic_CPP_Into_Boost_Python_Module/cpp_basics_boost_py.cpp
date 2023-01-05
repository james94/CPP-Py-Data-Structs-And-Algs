#include <iostream>
#include <string>

/*
C++ and Python Basics

Arrays

Structures

Pointers

Pointer To Structures

Functions

Parameter Passing Methods

Array as Parameter

Structure as Parameter

Structures and Functions
*/

// Data Types: int, float, double, string
// Functions: pass by value, pass by reference, pass by pointer

enum MEDICAL_IMAGING_TYPE {
    CT = 0,
    MRI = 1,
    PET = 2,
    SPECT = 3
}

struct medicalImagingScanner { // public attributes by default
    unsigned int yearBought;
    std::string name;
    std::string *organsScanned = ; // pointer to an array of strings
    unsigned int numOrgansScanned;
    unsigned int minutesScanned;
    double cost;
    MEDICAL_IMAGING_TYPE scannerType;
};

medicalImagingScanner askName(medicalImagingScanner medImgScanner) {
    std::cout << "Whats the medical imaging scanner name?" << std::endl;
    std::cin >> medImgScanner.name;
    return medImgScanner;
}

void askName(medicalImagingScanner& medImgScanner) {
    std::cout << "Whats the medical imaging scanner name?" << std::endl;
    std::cin >> medImgScanner.name;
}

void displayName(const medicalImagingScanner& medImgScanner) {
    std::cout << "Medical Imaging Scanner Name: " << medImgScanner.name << std::endl;
}

void displayType(const medicalImagingScanner& medImgScanner) {
    std::cout << "Medical Imaging Scanner Type: ";
    switch(medImgScanner.scannerType) {
        case CT:
            std::cout << "CT";
            break;
        case MRI:
            std::cout << "MRI";
            break;
        case PET:
            std::cout << "PET";
            break;
        case SPECT:
            std::cout << "SPECT";
            break;
    }
    std::endl;
}

void askOrgansScanned(medicalImagingScanner& medImgScanner) {
    std::cout << "How many organs were scanned?\n";
    std::cin >> medImgScanner.numOrgansScanned;

    medImgScanner.organsScanned = new std::string[medImgScanner.numOrgansScanned];

    for(int i = 0; i < medImgScanner.numOrgansScanned; i++) {
        std::cout << "What organ was scanned?\n";
        std::cin >> medImgScanner.organsScanned[i];
    }
}

void displayOrgansScanned(const medicalImagingScanner& medImgScanner) {
    if (medImgScanner.organsScanned == nullptr) {
        std::cout << "No organs scanned\n";
        return;
    }
    else if (medImgScanner.numOrgansScanned == 0) {
        std::cout << "No organs scanned\n";
        return;
    }

    std::cout << "Medical Imaging Scanned Organs: \n";
    for(int i = 0; i < medImgScanner.numOrgansScanned; i++) {
        std::cout << medImgScanner.organsScanned[i] << ", ";
    }
    std::endl;
}

void cleanupOrgansScanned(medicalImagingScanner& medImgScanner) {
    delete medImgScanner.organsScanned[]; // deallocate memory
    medImgScanner.organsScanned = nullptr; // set to nullptr to avoid dangling pointer
    medImgScanner.numOrgansScanned = 0;
}

void displayScanTime(const medicalImagingScanner& medImgScanner) {
    std::cout << "Medical Imaging Scan Time: " << medImgScanner.minutesScanned << std::endl;
}

void displayYearPurchased(const medicalImagingScanner& medImgScanner) {
    std::cout << "Medical Imaging Scanner Purchased in Year: " << medImgScanner.yearBout;
    std::cout << ". It cost: " << medImgScanner.cost << std::endl;
}

#include <boost/python.hpp>

namespace py = boost::python;


BOOST_PYTHON_MODULE(binding_pycpp_basics) {
    py::class_<MEDICAL_IMAGING_TYPE>("MEDICAL_IMAGING_TYPE"); // will this work for enum?
    py::class_<medicalImagingScanner>("medicalImagingScanner")
        .def_readwrite("cost", &medicalImagingScanner::cost)
        .def_readwrite("yearBought", &medicalImagingScanner::yearBought)
        .def_readwrite("minutesScanned", &medicalImagingScanner::minutesScanned)
        .def_readwrite("scannerType", &medicalImagingScanner::scannerType)
    ;
    py::def("askName", askName, py::return_value_policy<py::return_by_value>());
    py::def("askName", askName);
    py::def("displayName", displayName);
    py::def("displayType", displayType);
    py::def("askOrgansScanned", askOrgansScanned);
    py::def("displayOrgansScanned", displayOrgansScanned);
    py::def("cleanupOrgansScanned", cleanupOrgansScanned);
    py::def("displayScanTime", displayScanTime);
    py::def("displayYearPurchased", displayYearPurchased);
}

