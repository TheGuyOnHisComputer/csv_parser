import csv

def parse_csv(filename):
        f = open(filename, 'U')

        newText = f.read()

        while ": \n" in newText:
                newText = newText.replace(": \n", ": |")
        f.close()

        with open(filename, 'w') as f:
                f.write(newText)
        f.close()

        file = open(filename, 'r')
        elements = csv.reader(file)
        arr = []
        for i in elements:
                arr.append(i)
        return arr

class contact:
        def __init__(self, row):
                self.row = row
                self.name = find_att(row, 0)
                self.move_in = find_att(row, 2)
                self.add_one = find_att(row, 3)
                self.add_two = find_att(row, 4)
                self.add_three = find_att(row, 5)
                self.city = find_att(row, 6)
                self.postcode = find_att(row, 7)
                self.fname = find_att(row, 11)
                self.lname = find_att(row, 12)
                self.phone = find_att(row, 13)
                self.email = find_att(row, 14)

def find_att(row, attr_number):
        count = 0
        att = ""
        for char in row:
                if char == "|":
                        count += 1
                elif count < attr_number:
                        continue
                elif count == attr_number:
                        att += char
                elif count > attr_number:
                        return att

def create_contacts():
        company_names = ["Shefflets", "Northwood Northampton","Sewell & Gardner", "Location Location", "Saxon Kings"]
        return company_names


def create_header(writer):
        row = ["Title","First Name","Last Name","Mobile Number","Email Address","Address Line 1","Address Line 2","Adress Line 3","City","Postcode","Move In Date","Branch ID","Branch Name","Agent Name","Agent Email"]
        writer.writerow(row)
        return

def write_csv(contact_list):
        file = open("output.csv", "w")
        w = csv.writer(file, dialect='excel')
        create_header(w)
        fill_csv(w, contact_list)
        return

def fill_csv(w, contact_list):
        for contact in contact_list:
            row = ["Unknown", contact.fname, contact.lname, contact.phone, contact.email, contact.add_one, contact.add_two, contact.add_three, contact.city, contact.postcode, contact.move_in, "Unknown", contact.name, "Unknown", "Unknown"]
            w.writerow(row)
        return

def main():
        arr = parse_csv("test.csv")
        companies = {}
        ies_in_csv = []
        other_in_csv = []
        for i in range(len(arr)):
                name = find_att(arr[i][0], 0)
                if name != "":
                        try:
                                companies[name].append(arr[i][0])
                        except KeyError:
                            companies[name] = arr[i]

        ies_comps = create_contacts()
        for i in companies.keys():
                if i in ies_comps:
                        for j in companies[i]:
                                ies_in_csv.append(contact(j))
        print(ies_in_csv)
        write_csv(ies_in_csv)

main()
