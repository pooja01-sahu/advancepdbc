from datetime import date

class PrescriptionBean:

    def __init__(self):
        self._prescriptionId = 0
        self._patientName = ""
        self._doctorName = ""
        self._prescribedDate = None

    # 🔹 prescriptionId
    @property
    def prescriptionId(self):
        return self._prescriptionId

    @prescriptionId.setter
    def prescriptionId(self, value):
        self._prescriptionId = value

    # 🔹 patientName
    @property
    def patientName(self):
        return self._patientName

    @patientName.setter
    def patientName(self, value):
        self._patientName = value

    # 🔹 doctorName
    @property
    def doctorName(self):
        return self._doctorName

    @doctorName.setter
    def doctorName(self, value):
        self._doctorName = value

    # 🔹 prescribedDate
    @property
    def prescribedDate(self):
        return self._prescribedDate

    @prescribedDate.setter
    def prescribedDate(self, value):
        self._prescribedDate = value