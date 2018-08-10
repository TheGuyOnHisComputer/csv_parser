from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, ttk
import csv

"""Please don't read any of this. It is a mess and an all-round disgrace"""

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

class agent:
        def __init__(self, row):
                self.company = row[3]
                self.name = row[0]+row[1]
                self.email = row[4]
                
class gui:
        def __init__(self, master):
                self.master = master
                master.title("Utility CSV Seperator")
                master.geometry("500x500")
                self.file_one =""
                self.file_two =""
                self.label = Tkinter.Label(master, text="First choose the original csv file sent last night.")
                self.label.pack()
                self.label2 = Tkinter.Label(master, text="Secondly choose the csv file containing the contacts")
                self.label2.pack()
                self.f1but = Tkinter.Button(master, text="Choose original csv", command= self.find_file_one)
                self.f1but.pack()
                self.f2but = Tkinter.Button(master, text="Choose contact csv", command=  self.find_file_two)
                self.f2but.pack()
                self.go = Tkinter.Button(master, text="Go", command= (lambda: output_csv(self.file_one, self.file_two)))
                self.go.pack()
                self.button = Tkinter.Button(master, text="Quit", command=master.quit)
                self.button.pack()

        def find_file_one(self):
                self.file_one = tkFileDialog.askopenfilename(title="Choose file.")
                return self.file_one

        def find_file_two(self):
                self.file_two = tkFileDialog.askopenfilename(title="Choose the csv file containing the contacts")
                return self.file_two


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

def create_contacts(contact_filename):
        c = open(contact_filename)
        rows = csv.reader(c)
        arr = []
        for i in rows:
                arr.append(i)
        contact_dict = {}
        for i in arr:
                a = agent(i)
                contact_dict[a.company] = a 
        return contact_dict
        
def create_header(writer):
        row = ["Title","First Name","Last Name","Mobile Number","Email Address","Address Line 1","Address Line 2","Adress Line 3","City","Postcode","Move In Date","Branch ID","Branch Name","Agent Name","Agent Email"]
        writer.writerow(row)
        return

def write_ies_csv(contact_list, agent_list):
        file = open("homeshift.csv", "w")
        w = csv.writer(file, dialect='excel')
        create_header(w)
        fill_csv(w, contact_list, agent_list)
        file.close()
        return

def write_other_csv(rows):
        f = open("ies.csv", 'w')
        for i in rows:
                f.write(i+"\n")
        f.close()

def fill_csv(w, contact_list, agent_list):
        for contact in contact_list:
                print(contact.name)
                agent = agent_list[contact.name]
                row = ["Unknown", contact.fname, contact.lname, contact.phone, contact.email, contact.add_one, contact.add_two, contact.add_three, contact.city, contact.postcode, contact.move_in, "Unknown", contact.name, agent.name, agent.email]
                w.writerow(row)
        return

def output_csv(file_one, file_two):
        arr = parse_csv(file_one)
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

        ies_agents = create_contacts(file_two)
        for i in companies.keys():
                if i in ies_agents.keys():
                        for j in companies[i]:
                                ies_in_csv.append(contact(j))
                else:
                        for j in companies[i]:
                                other_in_csv.append(j)
        write_ies_csv(ies_in_csv, ies_agents)
        write_other_csv(other_in_csv)


def main():
        root = Tkinter.Tk()
        g = gui(root)
        root.mainloop()

main()
