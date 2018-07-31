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
        ies_output = []
        companies = {}
        for i in range(len(arr)):
                name = find_att(arr[i][0], 0)
                print(name)
                if name != None:
                        companies[name] = arr[i]
        ies_comps = create_contacts()
        for i in companies.keys():
                if i in ies_comps:
                        ies_output.append(companies[i])
        print(companies)

main()
