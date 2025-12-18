
class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.speciality = specialty
        self.available_times = []

    def get_info(self):
        return f"Shifokor ismi: {self.name}\n Mutaxassisligi: {self.speciality}\n Qabul vaqtlari: {self.available_times}"

    def add_time(self, time):
        if time not in self.available_times:
            return self.available_times.append(time)

    def remove_time(self, time):
        if time in self.available_times:
            return self.available_times.remove(time)

    def search_by_speciality(self, speciality):
        l = [i.get_info() for i in self. if i.speciality == speciality]
        return l if len(l) > 0 else "Bunday shifokor bizda mavjud emas"


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.appointments = []

    def get_info(self):
        return f"Bemor ismi: {self.name}\n Yoshi: {self.age}\n Qabul vaqtlari: {self.appointments}"

    def book_appointment(self, doctor, time):
        return self.hospital.book(doctor, time)

    def cancel_appointment(self, doctor, time):
        return self.hospital.cancel(doctor, time)


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.records = {}

    def add_doctor(self, doctor):
        s =  self.doctors.append(doctor)
        print(f"{s} shifokor qoshildi")

    def add_patient(self, patient):
        return self.patients.append(patient)

    def get_doctor_schedule(self, doctor):
        return f"{doctor.name} ning bosh vaqtlari: {doctor.available_times[doctor.name]}"

    def get_patient_appointments(self, patient):
        return f"{patient.name} bemorning uchrashuvlari: {patient.appointments[patient.name]}"



d1 = Doctor("Salima", "Kardiolog")
d2 = Doctor("Nodir", "Xirurg")

p1 = Patient("Hosila", 20)
p2 = Patient("Qobil", 35)

h1 = Hospital("Bunyod")
h1.add_doctor(d1)
h1.add_doctor(d2)
h1.add_patient(p1)
h1.add_patient(p2)

# print(d1.add_time("14:00"))
# print(d1.add_time("17:00"))
# print(d2.add_time("11:00"))
# print(d2.add_time("13:00"))

print(d1.search_by_speciality("Kardiolog"))































