



import json

class Prescription:
    def __init__(self, patient_name, medication, dosage, instructions):
        self.patient_name = patient_name
        self.medication = medication
        self.dosage = dosage
        self.instructions = instructions

    def to_dict(self):
        return {
            "patient_name": self.patient_name,
            "medication": self.medication,
            "dosage": self.dosage,
            "instructions": self.instructions
        }

class PrescriptionManager:
    def __init__(self, filename='prescriptions.json'):
        self.filename = filename
        self.prescriptions = self.load_prescriptions()

    def load_prescriptions(self):
        try:

            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_prescriptions(self):
        with open(self.filename, 'w') as file:
            json.dump(self.prescriptions, file)

    def add_prescription(self, prescription):
        self.prescriptions.append(prescription.to_dict())
        self.save_prescriptions()

    def view_prescriptions(self):
        for index, prescription in enumerate(self.prescriptions):
            print(f"{index + 1}. Patient: {prescription['patient_name']}, Medication: {prescription['medication']}, Dosage: {prescription['dosage']}, Instructions: {prescription['instructions']}")

    def search_prescription(self, patient_name):
        results = [pres for pres in self.prescriptions if pres['patient_name'].lower() == patient_name.lower()]
        if results:
            for pres in results:
                print(f"Patient: {pres['patient_name']}, Medication: {pres['medication']}, Dosage: {pres['dosage']}, Instructions: {pres['instructions']}")
        else:
            print("No prescriptions found for that patient.")

    def delete_prescription(self, index):
        if 0 <= index < len(self.prescriptions):
            deleted = self.prescriptions.pop(index)
            print(f"Deleted prescription for {deleted['patient_name']}.")
            self.save_prescriptions()
        else:
            print("Invalid prescription index.")

def main():
    manager = PrescriptionManager()

    while True:
        print("\nPrescription Management System")
        print("1. Add Prescription")
        print("2. View Prescriptions")
        print("3. Search Prescription")
        print("4. Delete Prescription")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            patient_name = input("Enter patient name: ")
            medication = input("Enter medication: ")
            dosage = input("Enter dosage: ")
            instructions = input("Enter instructions: ")
            prescription = Prescription(patient_name, medication, dosage, instructions)
            manager.add_prescription(prescription)
            print("Prescription added.")

        elif choice == '2':
            manager.view_prescriptions()

        elif choice == '3':
            patient_name = input("Enter patient name to search: ")
            manager.search_prescription(patient_name)

        elif choice == '4':
            index = int(input("Enter the prescription number to delete: ")) - 1
            manager.delete_prescription(index)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
