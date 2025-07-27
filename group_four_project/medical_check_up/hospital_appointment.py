class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, reason):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.reason = reason

    def __str__(self):
        return f'Appointment {self.patient.name} with Dr. {self.doctor.doctor_name} on {self.date} for {self.reason}'