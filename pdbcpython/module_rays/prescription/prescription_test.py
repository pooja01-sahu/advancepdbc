from module_rays.prescription.prescription_model import PrescriptionModel
from module_rays.prescription.prescrption_bean import PrescriptionBean
from datetime import date


def testadd():
    pres = PrescriptionBean()
    pres.prescriptionId = 1
    pres.patientName = 'Priyanka'
    pres.doctorName = 'Ram'
    pres.prescribedDate = date(2026, 3, 1)
    model = PrescriptionModel()
    model.add(pres)


def testGet():
    pres = PrescriptionModel()
    list = pres.get(5)
    for data in list:
        print(data['prescriptionId'], '\t', data['patientName'], '\t', data['doctorName'], '\t', data['prescribedDate'])

def testupdate():
    pres = PrescriptionBean()
    pres.prescriptionId = 5
    pres.patientName = 'Janki'
    pres.doctorName = 'Rahul'
    pres.prescribedDate = date(2026, 3, 2)
    model = PrescriptionModel()
    model.update(pres)

def testDelete():
    model = PrescriptionModel()
    model.delete(4)

# testadd()
# testGet()
testupdate()