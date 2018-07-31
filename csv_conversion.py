import csv

def parse_csv(filename):
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
        company_names = ["Shefflets", "Northwood Northampton","Sewell & Gardner", "Location Location"]
        return company_names

def main():
        arr = parse_csv("test.csv")
        companies = {}
        ies_output = []
        for i in range(len(arr)):
                name = find_att(arr[i][0], 0)
                if name != None:
                        companies[name] = arr[i][0]
        ies_comps = create_contacts()
        for i in companies.keys():
                if i in ies_comps:
                        ies_output.append(companies[i])
        test_name = "Sewell & Gardner"
        print(companies[test_name])
        print(find_att(companies[test_name], 6))
        ex = contact(companies[test_name])
        print(ex.__dict__)

main()
