import tkinter
from tkinter import *
#use for drop down list
from tkinter import messagebox, ttk
#widget fucntions
from tkinter import INSERT, END, WORD                                                    
import os
from tkinter import filedialog

class MedicalSystem:
    def __init__(self):
        self.mw = tkinter.Tk()
        self.mw.geometry("400x400")
        self.mw.title("Medical Centre Management System")

        #initialise for login
        self.allabel2 = None
        self.dr_log_label2 = None

        #get's current directory, used in routing paths
        self.directory = os.getcwd()

        self.doctors_path = os.path.join(self.directory, "Doctors")
        self.patients_path = os.path.join(self.directory, "Patients")
        self.admin_path = os.path.join(self.directory, "Admins")

        #Assigning intialise
        self.patients = []
        self.doctors = []

        self.button = tkinter.Button(self.mw, text="Admin", command=self.admin_open)
        self.button.pack(padx=20, pady=20)

        self.button1 = tkinter.Button(self.mw, text="Doctor", command=self.doctor_open)
        self.button1.pack(padx=20, pady=20)

        self.button2 = tkinter.Button(self.mw, text="Patient", command=self.patient_open)
        self.button2.pack(padx=20, pady=20)

        self.text_label = tkinter.Label(self.mw, text="")
        self.text_label.pack()

        self.recent_doctor = None

        self.mw.mainloop()

    def admin_open(self):
        #setup for new tkinter window
        self.mw1 = tkinter.Toplevel(self.mw)
        self.mw1.geometry("400x400")
        self.mw1.title("Admin Options")

        #button process mouse input and calls function
        self.abutton = tkinter.Button(self.mw1, text="Register", command=self.admin_register)

        #pad deals with horizontal and vertical spacing
        self.abutton.pack(padx=20, pady=20)

        self.abutton1 = tkinter.Button(self.mw1, text="Login", command=self.admin_login)
        self.abutton1.pack(padx=20, pady=20)


    def admin_register(self):
      self.mwr = tkinter.Toplevel(self.mw1)
      self.mwr.geometry("400x400")
      self.mwr.title("Admin Register")

      self.arlabel = tkinter.Label(self.mwr, text = 'Create Username').pack()
      self.arentry = tkinter.Entry(self.mwr, width = 15,)
      self.arentry.pack()
      self.arlabel1 = tkinter.Label(self.mwr, text = 'Create Password').pack()
      self.arentry1 = tkinter.Entry(self.mwr, width = 15,)
      self.arentry1.pack()
      self.arbutton = tkinter.Button(self.mwr, text = 'Enter', command = self.register_process)
      self.arbutton.pack(padx=20, pady=20)

    def register_process(self):
      #gets entry data assigns to variable
      eUsername = self.arentry.get()
      ePassword = self.arentry1.get()
      file_path = os.path.join(self.admin_path, eUsername + ".txt")

      #opens specified file path, writes info
      with open(file_path, "w") as file:
        file.write(eUsername +"\n")
        file.write(ePassword)

      #clear text in entry after success
      self.arentry.delete(0, END)
      self.arentry1.delete(0, END)

      messagebox.showinfo("Register Successful", f"Admin {eUsername} created")
      #close window
      self.mwr.destroy()



    def admin_login(self):
      self.mwl = tkinter.Toplevel(self.mw1) 
      self.mwl.geometry("400x400")
      self.mwl.title("Admin Login")

      self.allabel = tkinter.Label(self.mwl, text = 'Enter Username').pack()
      self.alentry = tkinter.Entry(self.mwl, width = 15,)
      self.alentry.pack()
      self.allabel1 = tkinter.Label(self.mwl, text = 'Enter Password').pack()
      self.alentry1 = tkinter.Entry(self.mwl, width = 15, show="*")
      self.alentry1.pack()
      self.albutton = tkinter.Button(self.mwl, text = 'Login', command = self.user_verify)
      self.albutton.pack(padx=20, pady=20)


    def user_verify(self):
      vUsername = self.alentry.get()
      vPassword = self.alentry1.get()

      self.alentry.delete(0, END)
      self.alentry1.delete(0, END)

      fileslist = os.listdir(self.admin_path)
      
      #checks for text file with correct username
      if vUsername + ".txt" in fileslist:
          #reads and verifies password in file
          file_path = os.path.join(self.admin_path, vUsername + ".txt")
          with open(file_path, "r") as admin_file:
             admin_verify = admin_file.read().splitlines()
          if vPassword == admin_verify[1]:
              if self.allabel2 == None:
                self.allabel2 = tkinter.Label(self.mwl, text='Login Successful', fg='green')
                self.allabel2.pack()
              else:
                self.allabel2.config(text=f"Login Successful", fg ='green')
                self.allabel2.pack()
              self.login_success()
          else:
             if self.allabel2 == None:
                self.allabel2 = tkinter.Label(self.mwl, text='Incorrect Password', fg='red')
                self.allabel2.pack()
             else:
                self.allabel2.config(text=f"Incorrect Password", fg ='red')
                self.allabel2.pack()
      else:
        if self.allabel2 == None:
          self.allabel2 = tkinter.Label(self.mwl, text='User not found', fg='red')
          self.allabel2.pack()
        else:
          self.allabel2.config(text=f"User not found", fg ='red')
          self.allabel2.pack()

    def login_success(self):
      self.mw_log = tkinter.Toplevel(self.mwl) 
      self.mw_log.geometry("500x500")
      self.mw_log.title("Admin Page")

      self.ls_button = tkinter.Button(self.mw_log, text="Register Doctors", command = self.doctor_Registry)
      self.ls_button.pack(padx=20, pady=20)

      self.ls_button1 = tkinter.Button(self.mw_log, text="Modify Doctors", command=self.doctors_modify)
      self.ls_button1.pack(padx=20, pady=20)

      self.ls_button2 = tkinter.Button(self.mw_log, text="Remove Doctor", command=self.remove_doctor)
      self.ls_button2.pack(padx=20, pady=20)

      self.ls_button3 = tkinter.Button(self.mw_log, text="View Patient Record", command=self.patient_record)
      self.ls_button3.pack(padx=20, pady=20)

      self.ls_button4 = tkinter.Button(self.mw_log, text="Assign Doctor", command=self.doctor_assign)
      self.ls_button4.pack(padx=20, pady=20)

      self.ls_button5 = tkinter.Button(self.mw_log, text="Total Doctors", command=self.doctor_count)
      self.ls_button5.pack(padx=20, pady=20)

      self.ls_button6 = tkinter.Button(self.mw_log, text="Modify Admin", command=self.admin_modify)
      self.ls_button6.pack(padx=20, pady=20)






    def doctor_count(self):
        #Number of doctors in Doctors folder counted
        doctors_count = len([file for file in os.listdir(self.doctors_path)]) - 1
        messagebox.showinfo("Total Doctors", f"Total number of doctors: {doctors_count}")

    def admin_modify(self):
     #opens dialogue to select doctor file
      file_path = filedialog.askopenfilename(initialdir=self.admin_path, title="Select a Doctor", filetypes=(("Text Files", "*.txt"),))

      #checks if file path selected, opens if so
      if file_path:
          with open(file_path, "r") as file:
              content = file.read()

          #New window creation, title, size
          self.mw_modify = tkinter.Toplevel(self.mw_log)
          self.mw_modify.geometry("400x400")
          self.mw_modify.title("Edit Text File")

          self.modify_label = tkinter.Label(self.mw_modify, text="Enter New Title:")
          self.modify_label.pack(pady=5)

          self.modify_entry = tkinter.Entry(self.mw_modify)
          self.modify_entry.pack(pady=5)

          #Text widget to edit text file
          modify_widget = tkinter.Text(self.mw_modify, wrap=WORD, width=40, height=10)
          modify_widget.insert(INSERT, content)
          modify_widget.pack(padx=20, pady=20)

          # Create a Save button to save changes
          button_save = tkinter.Button(self.mw_modify, text="Save Changes", command=lambda: self.save_changes2(self.modify_entry.get(), modify_widget))
          button_save.pack(pady=10)

    def save_changes2(self, new_title, modify_widget):
      modified_widget = modify_widget.get("1.0", "end-1c")

      # Constructs new file path with the updated title
      new_file_path = os.path.join(self.admin_path, f"{new_title}.txt")

      # Saves content modified to the new file
      with open(new_file_path, "w") as file:
          file.write(modified_widget)

      messagebox.showinfo("Doctor Updated", "Changes saved successfully.")

    def doctors_modify(self):
      #opens dialogue to select doctor file
      file_path = filedialog.askopenfilename(initialdir=self.doctors_path, title="Select a Doctor", filetypes=(("Text Files", "*.txt"),))

      #checks if file path selected, opens if so
      if file_path:
          with open(file_path, "r") as file:
              content = file.read()

          #New window creation, title, size
          self.mw_modify = tkinter.Toplevel(self.mw_log)
          self.mw_modify.geometry("400x400")
          self.mw_modify.title("Edit Text File")

          self.modify_label = tkinter.Label(self.mw_modify, text="Enter New Title:")
          self.modify_label.pack(pady=5)

          self.modify_entry = tkinter.Entry(self.mw_modify)
          self.modify_entry.pack(pady=5)

          #Text widget to edit text file
          modify_widget = tkinter.Text(self.mw_modify, wrap=WORD, width=40, height=10)
          modify_widget.insert(INSERT, content)
          modify_widget.pack(padx=20, pady=20)

          # Create a Save button to save changes
          button_save = tkinter.Button(self.mw_modify, text="Save Changes", command=lambda: self.save_changes(self.modify_entry.get(), modify_widget))
          button_save.pack(pady=10)

            
    def save_changes(self, new_title, modify_widget):
      modified_widget = modify_widget.get("1.0", "end-1c")

      # Constructs new file path with the updated title
      new_file_path = os.path.join(self.doctors_path, f"{new_title}.txt")

      # Saves content modified to the new file
      with open(new_file_path, "w") as file:
          file.write(modified_widget)

      messagebox.showinfo("Doctor Updated", "Changes saved successfully.")

    def remove_doctor(self):
      #New window creation, title, size
      self.mwr = tkinter.Toplevel(self.mw_log)
      self.mwr.geometry("400x400")
      self.mwr.title("Remove Doctor")

      self.remove_dlabel = tkinter.Label(self.mwr, text="Select Doctor Username to Remove:")
      self.remove_dlabel.pack(padx=10, pady=10)

      #create list containing doctors, removes .txt
      doctor_files = [file[:-4] for file in os.listdir(self.doctors_path) if file.lower().endswith(".txt") ]

      #dropdown list
      self.remove_dcombobox = ttk.Combobox(self.mwr, values=doctor_files, state="readonly")
      self.remove_dcombobox.pack(padx=10, pady=10)

      self.r_button = tkinter.Button(self.mwr, text="Remove Doctor", command=self.remove_process)
      self.r_button.pack(padx=10, pady=10)

    def remove_process(self):
      self.d_username = self.remove_dcombobox.get()

      if self.d_username:
          #filepath construction for selected username
          doctor_file_path = os.path.join(self.doctors_path, f"{self.d_username}.txt")

          #check if file path exists, removes if so
          if os.path.exists(doctor_file_path):
              os.remove(doctor_file_path)
              messagebox.showinfo("Doctor Removed", f"{self.d_username}'s login removed successfully.")
              self.remove_dcombobox.set("") 
          else:
              messagebox.showerror("Error", f"Doctor {self.d_username} not found.")
      else:
          messagebox.showwarning("Select Doctor", "Please select a doctor to remove.")


    def doctor_assign(self):
      self.mw_assign = tkinter.Toplevel(self.mw_log)
      self.mw_assign.geometry("400x400")
      self.mw_assign.title("Assign Doctor")

      #tkinter listboxes list all Patients and Doctors
      tkinter.Label(self.mw_assign, text="Doctors:").pack()
      self.drlistbox = tkinter.Listbox(self.mw_assign)
      self.drlistbox.pack()

      tkinter.Label(self.mw_assign, text="Patients:").pack()
      self.plistbox = tkinter.Listbox(self.mw_assign)
      self.plistbox.pack()

      b_assign = tkinter.Button(self.mw_assign, text="Assign Doctor", command=self.assign_process)
      b_assign.pack()

      #runs input_data function
      self.input_data()

    def assign_process(self):
      #Get selected options 
       patient_select = self.plistbox.get(tkinter.ACTIVE)
       doctor_select = self.drlistbox.get(tkinter.ACTIVE)

      #Patient and Doctor filepaths
       patient_path = os.path.join(self.patients_path, f"{patient_select}.txt")
       doctor_file_path = os.path.join(self.doctors_path, f"{doctor_select}.txt")



       if doctor_select and patient_select:
          messagebox.showinfo("Assigning", f"Patient: {patient_select} assigned to Doctor: {doctor_select}")

          #Read patient file content
          with open(patient_path, "r") as patient_file:
            patient_content = patient_file.read().strip()
          
          #Writes patient information to doctor file
          with open(doctor_file_path, "a") as doctor_file:
            doctor_file.write("\n\nBelow is the Patient you have been assigned to he has the following symptoms:\n\n")
            doctor_file.write(patient_content + "\n") 

          #stores most recently assigned doctor
          self.recent_doctor = doctor_select   
      #Error if both aren't selected
       else: 
          messagebox.showerror("Error", "Select patient and doctor")

    def input_data(self):
      patients = os.listdir(self.patients_path)
      doctors = os.listdir(self.doctors_path)

      #Loop for all Patients
      for file in patients:
        patient_path = os.path.join(self.patients_path, file)
        if os.path.isfile(patient_path):
          #Read first line of file to get patient name
           with open(patient_path, "r") as file:
              patient_info = file.readline().strip()
              #append to patient list, put to listbox
              self.patients.append(patient_info)  
              self.plistbox.insert(tkinter.END, patient_info)    

      #Loop for all doctors
      for file in doctors:
        doctor_file_path = os.path.join(self.doctors_path, file)
        if os.path.isfile(doctor_file_path):
           #Read first line of file to get Doctor name
           with open(doctor_file_path, "r") as file:
              doctor_info = file.readline().strip()
              #append to doctor list, put to listbox
              self.doctors.append(doctor_info)  
              self.drlistbox.insert(tkinter.END, doctor_info)  



    def patient_record(self):
      self.mw_record = tkinter.Toplevel(self.mw_log)
      self.mw_record.geometry("1000x1000")
      self.mw_record.title("Patient Records")
  
    
      file_path = "Enrollment/enroll.txt"
      #opens enrollment data in read mode
      with open(file_path, "r") as file:
        content = file.read()
      #large widget displaying records
      enroll_widget = tkinter.Text(self.mw_record, wrap=WORD, width=500, height=500)
      enroll_widget.insert(INSERT, content)
      enroll_widget.pack(padx=20, pady=20)


  

    def doctor_Registry(self):
      self.mw_dr = tkinter.Toplevel(self.mw_log)
      self.mw_dr.geometry("400x400")
      self.mw_dr.title("Doctor Register")


      self.drlabel = tkinter.Label(self.mw_dr, text = 'Create Doctor Fullname').pack()
      self.drentry = tkinter.Entry(self.mw_dr, width = 15,)
      self.drentry.pack()
      self.drlabel1 = tkinter.Label(self.mw_dr, text = 'Create Doctor Password').pack()
      self.drentry1 = tkinter.Entry(self.mw_dr, width = 15,)
      self.drentry1.pack()
      self.drbutton = tkinter.Button(self.mw_dr, text = 'Enter', command = self.dr_register_process)
      self.drbutton.pack(padx=20, pady=20)

    def dr_register_process(self):
      drUsername = self.drentry.get()
      drPassword = self.drentry1.get()
      file_path = os.path.join(self.doctors_path, drUsername + ".txt")
      #creates Doctor Login
      with open(file_path, "w") as file:
          file.write(drUsername +"\n")
          file.write(drPassword)

      self.drentry.delete(0, END)
      self.drentry1.delete(0, END)

      messagebox.showinfo("Register Successful", f"Doctor {drUsername} created")

    def doctor_open(self):
      self.mw_drlog = tkinter.Toplevel(self.mw) 
      self.mw_drlog.geometry("400x400")
      self.mw_drlog.title("Dr Login")

      self.dr_log_label = tkinter.Label(self.mw_drlog, text = 'Enter Fullname').pack()
      self.dr_log_entry = tkinter.Entry(self.mw_drlog, width = 15,)
      self.dr_log_entry.pack()
      self.dr_log_label1 = tkinter.Label(self.mw_drlog, text = 'Enter Password').pack()
      #ensures password is hashed
      self.dr_log_entry1 = tkinter.Entry(self.mw_drlog, width = 15, show="*")
      self.dr_log_entry1.pack()
      self.dr_log_button = tkinter.Button(self.mw_drlog, text = 'Login', command = self.doctor_verify)
      self.dr_log_button.pack(padx=20, pady=20)


    def doctor_verify(self):
      global drUsername
      drUsername = self.dr_log_entry.get()
      drPassword = self.dr_log_entry1.get()

      self.dr_log_entry.delete(0, END)
      self.dr_log_entry1.delete(0, END)

      dr_fileslist = os.listdir(self.doctors_path)

      if drUsername + ".txt" in dr_fileslist:
          file_path = os.path.join(self.doctors_path, drUsername + ".txt")
          with open(file_path, "r") as dr_file1:
              dr_verify = dr_file1.read().splitlines()
          if drPassword == dr_verify[1]:
              if self.dr_log_label2 == None:
                self.dr_log_label2 = tkinter.Label(self.mw_drlog, text='Login Successful', fg='green')
                self.dr_log_label2.pack()
              else:
                self.dr_log_label2.config(text=f"Login Successful", fg ='green')
                self.dr_log_label2.pack()
              self.dr_login_success()              
          else:
             if self.dr_log_label2 == None:
                self.dr_log_label2 = tkinter.Label(self.mw_drlog, text='Incorrect Password', fg='red')
                self.dr_log_label2.pack()
             else:
                self.dr_log_label2.config(text=f"Incorrect Password", fg ='red')
                self.dr_log_label2.pack()
      else:
        if self.dr_log_label2 == None:
          self.dr_log_label2 = tkinter.Label(self.mw_drlog, text='User not found', fg='red')
          self.dr_log_label2.pack()
        else:
          self.dr_log_label2.config(text=f"User not found", fg ='red')
          self.dr_log_label2.pack()

    def dr_login_success(self):
      self.mw_drlog1 = tkinter.Toplevel(self.mw_drlog) 
      self.mw_drlog1.geometry("400x400")
      self.mw_drlog1.title("Doctor Options")

      self.dr_records_but = tkinter.Button(self.mw_drlog1, text="View Patient Record", command = self.patient_record2)
      self.dr_records_but.pack(padx=20, pady=20)

      self.dr_appointments_but = tkinter.Button(self.mw_drlog1, text="View appointments", command=self.appointment_check)
      self.dr_appointments_but.pack(padx=20, pady=20)



    def appointment_check(self):
      #opens dialogue to select doctor file
      file_path = filedialog.askopenfilename(initialdir=self.doctors_path, title="Select a Doctor", filetypes=(("Text Files", "*.txt"),))

      #checks if file path selected, opens if so
      if file_path:
          with open(file_path, "r") as file:
              content = file.read()

          #New window creation, title, size
          self.mw_app = tkinter.Toplevel(self.mw_drlog1)
          self.mw_app.geometry("800x800")
          self.mw_app.title(f"Appointment and Doctor info for {drUsername}")


          #Text widget to edit text file
          modify_widget = tkinter.Text(self.mw_app, wrap=WORD, width=400, height=100)
          modify_widget.insert(INSERT, content)
          modify_widget.pack(padx=20, pady=20)


    def patient_record2(self):
      self.mw_record1 = tkinter.Toplevel(self.mw_drlog)
      self.mw_record1.geometry("1000x1000")
      self.mw_record1.title("Patient Records")
  
      #enters Enrollment folder to display enroll.txt
      file_path = "Enrollment/enroll.txt"
      with open(file_path, "r") as file:
        content = file.read()
      #large widget to display
      enroll_widget = tkinter.Text(self.mw_record1, wrap=WORD, width=500, height=500)
      enroll_widget.insert(INSERT, content)
      enroll_widget.pack(padx=20, pady=20)



    def patient_open(self):
      self.mw_pa = tkinter.Toplevel(self.mw) 
      self.mw_pa.geometry("400x400")
      self.mw_pa.title("Patient Login")

      self.pa_button = tkinter.Button(self.mw_pa, text="Enroll", command = self.patient_enrol)
      self.pa_button.pack(padx=20, pady=20)

      self.pa_button1 = tkinter.Button(self.mw_pa, text="Book appointment", command=self.book)
      self.pa_button1.pack(padx=20, pady=20)

      self.pa_button2 = tkinter.Button(self.mw_pa, text="View assigned doctor", command=self.patient_doctor_assign)
      self.pa_button2.pack(padx=20, pady=20)

    def patient_enrol(self):
      self.mw_enrol = tkinter.Toplevel(self.mw_pa)
      self.mw_enrol.geometry("400x400")
      self.mw_enrol.title("Patient Enroll")

      self.fname = tkinter.Label(self.mw_enrol, text='Enter Full Name')
      self.fname.pack(padx=10, pady=10)
      self.fname_entry = tkinter.Entry(self.mw_enrol)
      self.fname_entry.pack(padx=10, pady=10)

      self.age = tkinter.Label(self.mw_enrol, text='Enter Age')
      self.age.pack(padx=10, pady=10)
      self.age_entry = tkinter.Entry(self.mw_enrol)
      self.age_entry.pack(padx=10, pady=10)

      self.address = tkinter.Label(self.mw_enrol, text='Enter Address')
      self.address.pack(padx=10, pady=10)
      self.address_entry = tkinter.Entry(self.mw_enrol)
      self.address_entry.pack(padx=10, pady=10)

      self.number = tkinter.Label(self.mw_enrol, text='Enter Mobile Number')
      self.number.pack(padx=10, pady=10)
      self.number_entry = tkinter.Entry(self.mw_enrol)
      self.number_entry.pack(padx=10, pady=10)

      self.en_button = tkinter.Button(self.mw_enrol, text="Enroll", command=self.save_enrol)
      self.en_button.pack(padx=10, pady=10)


    def save_enrol(self):
      fname = self.fname_entry.get()
      age = self.age_entry.get()
      address = self.address_entry.get()
      number = self.number_entry.get()
      file_path = "Enrollment/enroll.txt"
      with open(file_path, "a") as file:
         file.write(f"Full name: {fname}\nAge: {age}\nAddress: {address}\nNumber: {number}\n\n")
 


      self.fname_entry.delete(0, END)
      self.age_entry.delete(0, END)
      self.address_entry.delete(0, END)
      messagebox.showinfo("Enrollment Success", f"{fname} enrolled in system!")
      self.mw_enrol.destroy()



    def book(self):
      self.mw_book = tkinter.Toplevel(self.mw_pa)
      self.mw_book.geometry("400x400")
      self.mw_book.title("Patient Booking")

      self.bkname = tkinter.Label(self.mw_book, text='Enter Full Name')
      self.bkname.pack(padx=10, pady=10)
      self.bkentry = tkinter.Entry(self.mw_book, width = 30)
      self.bkentry.pack(padx=10, pady=10)

      self.symptoms = tkinter.Label(self.mw_book, text='Enter Symptons')
      self.symptoms.pack(padx=10, pady=10)
      self.symptoms_widget = tkinter.Text(self.mw_book, wrap=WORD, width=40, height=10)
      self.symptoms_widget.pack(padx=10, pady=10)

      self.en_button = tkinter.Button(self.mw_book, text="Book", command=self.save_book)
      self.en_button.pack(padx=10, pady=10)


    def save_book(self):
      bkname = self.bkentry.get()
      symptoms = self.symptoms_widget.get(1.0, "end-1c")
      file_path = os.path.join(self.patients_path, bkname + ".txt")
      with open(file_path, "w") as file:
          file.write(bkname +"\n")
          file.write(symptoms)  
 


      self.bkentry.delete(0, END)
      self.symptoms_widget.delete(1.0, "end-1c")
      messagebox.showinfo("Booking Success", f"Appointment for {bkname} booked, please wait for response")
      self.mw_book.destroy()
        
    def patient_doctor_assign(self):
      #when admin has assigned doctor to patient, will show doctor once
      if self.recent_doctor == None:
        messagebox.showerror("Assigned Doctor", "You have not applied for an appointment")  
      else: 
        messagebox.showinfo("Assigned Doctor", f"Your appointment is with doctor {self.recent_doctor}")
        self.recent_doctor = None
      
        
    
    
    



gui = MedicalSystem()