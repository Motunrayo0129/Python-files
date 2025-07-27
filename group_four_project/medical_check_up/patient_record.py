class PatientRecord:
    def __init__(self, patient_id, patient_name, dob, phone_no, medical_history=None):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.dob = dob
        self.phone_no = phone_no
        self.medical_history = medical_history

    def add_medical_history(self, medical_history):
        self.medical_history = medical_history.append(self.medical_history)

    def __str__(self):
        return (f'patient name: {self.patient_name} patient id: {self.patient_id} DOB: {self.dob} phone no: {self.phone_no}'
                f'medical history: {self.medical_history} else no medical history')S