
class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.speciality = specialty
        self.available_times = []

    def get_info(self):
        return f"Shifokor ismi: {self.name}\n Mutaxassisligi: {self.speciality}\n Qabul vaqtlari: {self.available_times}"

    def add_time(self, time):
        if time not in self.available_times:
            self.available_times.append(time)
            print(f"{time} vaqt jadvalga qoshildi")
        else:
            print(f"{time} jadvalda bor")

    def remove_time(self, time):
        if time in self.available_times:
            self.available_times.remove(time)
            print(f"{time} jadvaldan olib tashlandi")
        else:
            print(f"{time} jadvalda topilmadi")

    def search_by_speciality(self, speciality):
        l = [i.get_info() for i in self.speciality if i.speciality == speciality]
        return l if len(l) > 0 else "Bunday shifokor bizda mavjud emas"


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.appointments = []

    def get_info(self):
        return f"Bemor ismi: {self.name}\n Yoshi: {self.age}\n Qabul vaqtlari: {self.appointments}"

    def book_appointment(self, hospital, doctor, time):
        hospital.book(self, doctor, time)

    def cancel_appointment(self, hospital, doctor, time):
        hospital.cancel(self, doctor, time)


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.records = {}

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"\n{doctor.name} jadvalga qoshildi")

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"\n{patient.name} jadvalga bemor qoshildi")

    def get_doctor_schedule(self, doctor):
        print(f"\n{doctor.name} ning bo'sh vaqtlar jadvali: {doctor.available_times}")

    def get_patient_appointments(self, patient):
        if patient.name in self.records:
            print(f"\n{patient.name} ning uchrashuvlari: {self.records[patient.name]}")
        else:
            print(f"{patient.name} uchrashuv yoq")


d1 = Doctor("Salima", "Kardiolog")
d2 = Doctor("Nodir", "Xirurg")

p1 = Patient("Hosila", 20)
p2 = Patient("Qobil", 35)

h1 = Hospital("Bunyod")
h1.add_doctor(d1)
h1.add_doctor(d2)
h1.add_patient(p1)
h1.add_patient(p2)

d1.add_time("14:00")
d1.add_time("17:00")
d2.add_time("11:00")
d2.add_time("13:00")

p1.book_appointment(h1, d1, "09:00")
p2.book_appointment(h1, d2, "15:00")


h1.get_doctor_schedule(d1)
h1.get_patient_appointments(p1)
print(d1.search_by_speciality("Kardiolog"))































