class Doctor:
    def __init__(self, doctor_name, specialization, phone_no, doctor_id):
        self.doctor_name = doctor_name
        self.specialization = specialization
        self.phone_no = phone_no
        self.doctor_id = doctor_id

    def __str__(self):
        return f"Dr.{self.doctor_name} {self.specialization} - contact {self.phone_no} {self.doctor_id} "