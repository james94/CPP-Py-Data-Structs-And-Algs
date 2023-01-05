import binding_pycpp_basics

if __name__ == "__main__":
    medical_img_scan = binding_pycpp_basics.medicalImagingScanner() # create C++ Boost Python object
    medical_img_scan = binding_pycpp_basics.askName(medical_img_scan) # C++ boost py pass by value, return by value
    binding_pycpp_basics.displayName(medical_img_scan) # verify our object updated
    binding_pycpp_basics.askName(medical_img_scan) # C++ boost py pass by reference
    binding_pycpp_basics.displayName(medical_img_scan) # verify our object updated
    # add C++ boost py readwrite defs for each direct property assignment
    medical_img_scan.cost = 5099.99
    medical_img_scan.yearBought = 2018
    binding_pycpp_basics.displayYearPurchased(medical_img_scan)
    medical_img_scan.minutesScanned = 50
    binding_pycpp_basics.displayScanTime(medical_img_scan)

    medical_img_scan.scannerType = binding_pycpp_basics.MEDICAL_IMAGING_TYPE.MRI
    binding_pycpp_basics.displayType(medical_img_scan)
    binding_pycpp_basics.askOrgansScanned(medical_img_scan) # C++ boost py pass by reference
    binding_pycpp_basics.displayOrgansScanned(medical_img_scan)

    binding_pycpp_basics.cleanupOrgansScanned(medical_img_scan) # C++ boost py pass by reference, deallocate memory
    binding_pycpp_basics.displayOrgansScanned(medical_img_scan)