import csv

class Contact:
    def init(self, name, phone):
        if not phone.isdigit():
            raise ValueError("telefon faghat adad")
        self.name = name
        self.phone = phone

class PhoneBook:
    def init(self):
        self.contacts = []
    
    def add(self, name, phone):
        try:
            c = Contact(name, phone)
            self.contacts.append(c)
            print("ezafe shod")
        except ValueError:
            print("telefon eshtebah")
    
    def show(self):
        if not self.contacts:
            print("list khali")
            return
        for num, c in enumerate(self.contacts, 1):
            print(f"{num}. {c.name}: {c.phone}")
    
    def save(self):
        try:
            with open("contacts.csv", "w", newline="") as f:
                writer = csv.writer(f)
                for c in self.contacts:
                    writer.writerow([c.name, c.phone])
            print("save shod")
        except PermissionError:
            print("file baste nist")
        except:
            print("khata save")
    
    def load(self):
        try:
            with open("contacts.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 2:
                        try:
                            c = Contact(row[0], row[1])
                            self.contacts.append(c)
                        except ValueError:
                            print("telefon kharab:", row[0])
            print("load shod")
        except FileNotFoundError:
            print("file peyda nashod")
        except:
            print("khata load")

def main():
    pb = PhoneBook()
    pb.load()
    
    while True:
        print("\n1. add")
        print("2. show")
        print("3. save & exit")
        
        try:
            x = int(input("> "))
            
            if x == 1:
                name = input("name: ")
                phone = input("phone: ")
                pb.add(name, phone)
            
            elif x == 2:
                pb.show()
            
            elif x == 3:
                pb.save()
                print("khoroj")
                break
            
            else:
                print("1,2,3")
        
        except ValueError:
            print("adad vared kon")
        except KeyboardInterrupt:
            print("\nkhoroj")
            break

if name == "__main__":
    main()