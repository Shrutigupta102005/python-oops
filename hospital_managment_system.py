class Doctor:
    def __init__(self, doc_id, doc_name, specializations):
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.specializations = specializations

    def get_doctor_info(self):
        return {'Doctor ID': self.doc_id, 'Doctor Name': self.doc_name, 'Specializations': self.specializations}


class Patient:
    def __init__(self, patient_id, pname, age, gender, contact):
        self.patient_id = patient_id
        self.pname = pname
        self.age = age
        self.gender = gender
        self.contact = contact

    def get_patient_info(self):
        return {'Patient ID': self.patient_id, 'Patient Name': self.pname, 'Age': self.age, 'Gender': self.gender,
                'Contact': self.contact}


class MedicalRecords:
    def __init__(self):
        self.__records = {}

    def add_record(self, patient, doctor, diagnosis, medication):
        self.__records[patient.get_patient_info()['Patient ID']] = {
            'Patient': patient.get_patient_info(),
            'Doctor': doctor.get_doctor_info(),
            'Diagnosis': diagnosis,
            'Medication': medication
        }

    def get_records(self):
        return self.__records


# Create patients
patient1 = Patient(1, 'John Doe', 30, 'Male', '123-456-7890')
patient2 = Patient(2, 'Jane Smith', 25, 'Female', '987-654-3210')

# Create doctors
doctor1 = Doctor(101, 'Dr. Ahmed', 'Cardiologist')
doctor2 = Doctor(102, 'Dr. Fatima', 'Pediatrician')

# Create medical records
medical_records = MedicalRecords()
medical_records.add_record(patient1, doctor1, 'Heart condition', 'Aspirin')
medical_records.add_record(patient2, doctor2, 'Common cold', 'Antibiotics')

# Display records
print(medical_records.get_records())
