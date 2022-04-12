
import mysql.connector as mysql #Imporing module mysql.connector
import sys                      #Importing sys module to use it as an exit menu in various functions

mycon=mysql.connect(host='localhost',user='root',passwd='mysql',database='LIF_LINE_HOSPITAL',charset='utf8')

if mycon.is_connected()==False:  #checking whether the connection is established or not
    print("Database not ready or connection refused by Database Server!!!")
else:
    print("Connection succesfully established")
    #creating a cursor
    mycur=mycon.cursor()
    

#global dictionaries for various medical departments
Physician={}
Orthopedician={}
Cardiologist={}
Neurologist={}
Opthalmologist={}
Gynaecologist={}
Pediatrician={}
lst=[Physician,Orthopedician,Cardiologist,Neurologist,Opthalmologist,Gynaecologist,Pediatrician]   #list containing dictionaries 
lststr=['Physician','Orthopedician','Cardiologist','Neurologist','Opthalmologist','Gynaecologist','Pediatrician']   #list containing name of the department

def initialisation():
    """used for adding the new doctors to their respective departments"""
    global Physician
    global Orthopedician
    global Cardiologist
    global Neurologist
    global Opthalmologist
    global Gynaecologist
    global Pediatrician
    
    query="select NAME,DOC_ID from DOCTOR_INFO where DEPARTMENT='Physician'"
    mycur.execute(query)
    data=mycur.fetchall()              #fetching data from the table DOCTOR_INFO
    for i in range(len(data)):
        Physician[data[i][1]]=data[i][0]   #Physician[key]=value : to add items into dictionary
        
    query="select NAME,DOC_ID from DOCTOR_INFO where DEPARTMENT='Orthopedician'"
    mycur.execute(query)
    data=mycur.fetchall()              
    for i in range(len(data)):
        Orthopedician[data[i][1]]=data[i][0]
        
    query="select NAME,DOC_ID from DOCTOR_INFO where DEPARTMENT='Cardiologist'"
    mycur.execute(query)
    data=mycur.fetchall()              
    for i in range(len(data)):
        Cardiologist[data[i][1]]=data[i][0]
        
    query="select NAME,DOC_ID from DOCTOR_INFO where DEPARTMENT='Neurologist'"
    mycur.execute(query)
    data=mycur.fetchall()             
    for i in range(len(data)):
        Neurologist[data[i][1]]=data[i][0]
        
    query="select NAME,DOC_ID from DOCTOR_INFO where DEPARTMENT='Opthalmologist'"
    mycur.execute(query)
    data=mycur.fetchall()             
    for i in range(len(data)):
        Opthalmologist[data[i][1]]=data[i][0]
        
    query="select NAME,DOC_ID from DOCTOR_INFO where DEPARTMENT='Gynaecologist'"
    mycur.execute(query)
    data=mycur.fetchall()             
    for i in range(len(data)):
        Gynaecologist[data[i][1]]=data[i][0]
        
    query="select NAME,DOC_ID from DOCTOR_INFO where DEPARTMENT='Pediatrician'"
    mycur.execute(query)
    data=mycur.fetchall()             
    for i in range(len(data)):
        Pediatrician[data[i][1]]=data[i][0]
        
    
#############################################################################   
#############################################################################       
        



def add_patient():
    """Used for registering new patients with the hospital"""
    #asking the person about his personal details
    Patient_Name=input("Enter Patient's name : ")
    sex=input("Enter Patient's sex (M/F/Others) : ")
    UID=int(input("Enter Patient's UID : "))
    DOB=input("Enter Patient's DOB in YYYY-MM-DD format : ")
    Bloodgroup=input("Enter Patient's blood group : ")
    Contact_num=int(input("Enter Patient's contact number : "))
    Address=input("Enter Patient's present address : ")
    Previous_Medical_Problems=input("Enter previous medical problems(if any):  ")
    Guardian_name=input("Enter Guardian's Name : ")
    Guardian_relation=input("Enter relation with guardian: ")
    Guardian_contact=int(input("Enter Guardian's contact number : "))
    insur_check=input("Do you have an insurance, enter y/n accordingly : ")
    if insur_check=='y':                 #in case the person has an insurance 
        InsuranceName=input("\nEnter patient's insurance name : ")
        CardNo=int(input("Enter patient's insurance card number: "))
        CardHoldersName=input("Enter card holder's name : ")
        ValidFrom=input("Enter the date of initial validation : ")
        ValidityDuration=input("Enter validity duration in years : " )
        AmountCovered=int(input("Enter the amount covered by patient's insurance :"))
        DiseasesCovered=input("Enter the diseases covered by patient's insurance : ")
        #inserting the asked information into the table REGISTERED_PATIENTS
        sqlquery="insert into REGISTERED_PATIENTS(PNAME,SEX,UID,DOB,BloodGroup,ContactNo,Address,Previous_Medical_Problems,GuardianName,GuardianRelation,GuardianContactNo,InsuranceName,CardNo,CardHoldersName,ValidFrom,ValidityDuration,AmountCovered,DiseasesCovered)values('"+Patient_Name+ "','"+sex +"'," + str(UID)+ ",'"+DOB+"','"+Bloodgroup+"',"+str(Contact_num)+",'"+Address+"','"+Previous_Medical_Problems+"','"+Guardian_name+"','"+Guardian_relation+"',"+str(Guardian_contact)+",'"+InsuranceName+"',"+str(CardNo)+",'"+CardHoldersName+"','"+ValidFrom+"','"+ValidityDuration+"',"+str(AmountCovered)+",'"+DiseasesCovered+"')"
        mycur.execute(sqlquery)
        mycon.commit()                      #commiting the query
        sqlquery1="select * from REGISTERED_PATIENTS where ContactNo="+str(Contact_num)+";"
        mycur.execute(sqlquery1)
        data=mycur.fetchall()                   #fetching data from the table with the help of contact number
    

        for row in data:
            print("\nPATIENT ID IS : ",row[0])        #displaying the ID to the person who has just registered
        print("\nThank you.","\n")
        input("\nPress enter to continue...")
         
    else:
        #in case the person does not have an insurance
        #inserting the asked information into the table REGISTERED_PATIENTS
        sqlquery="insert into REGISTERED_PATIENTS(PNAME,SEX,UID,DOB,BloodGroup,ContactNo,Address,Previous_Medical_Problems,GuardianName,GuardianRelation,GuardianContactNo)values('"+Patient_Name+ "','"+sex +"'," + str(UID)+ ",'"+DOB+"','"+Bloodgroup+"',"+str(Contact_num)+",'"+Address+"','"+Previous_Medical_Problems+"','"+Guardian_name+"','"+Guardian_relation+"',"+str(Guardian_contact)+");"
        mycur.execute(sqlquery)
        mycon.commit()                     #commiting the query
        sqlquery1="select * from REGISTERED_PATIENTS where ContactNo="+str(Contact_num)+";"
        mycur.execute(sqlquery1)
        data=mycur.fetchall()
        for row in data:
            print("\nPATIENT ID IS : ",row[0])
        print("\nThank you.","\n")
        input("\nPress enter to continue...")                #using input to wait for the user's further instructions

#############################################################################   
#############################################################################       
        
def search_id():
    """used for searching ID of a patient in various other functions if he/she does not remembers it."""
    print("\nEnter the following information to get id")
    #asking for information to get ID from the table registered_patients
    name=input("Enter name : ")
    dob=input("Enter DOB in YYYY-MM-DD format : ")
    contact_num=int(input("Enter contact number : "))
    sqlquery="select * from REGISTERED_PATIENTS where PNAME='"+name+"' and DOB='"+dob+"' and ContactNo="+str(contact_num)
    mycur.execute(sqlquery)                     #executing the query
    data=mycur.fetchall()
    count=mycur.rowcount
    if count==0:                                #checking the validity of ID using mycur.rowcount
        print("\nInvalid information")
        input("\nPress enter to continue.")
    else:
        return data[0][0]                       #returning the ID to the caller function i.e data[0][0] which is a list of tuple
    
#############################################################################   
#############################################################################       
 
    
def show_pat_personal_details():
    """used for displaying the records of a patient using his/her ID"""
    ques=input("Enter 'y' if the patient  remembers ID or else enter 'n' : ")         #asking user about whether he/she remembers the ID or not
    if ques=='y':
        pat_id=int(input("Enter PatientID: "))
        sqlquery="select * from REGISTERED_PATIENTS where RegID="+str(pat_id)     #fetching all the information using ID
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        count=mycur.rowcount
        if count==0:                    #checking the validity of ID using mycur.rowcount
            print("\nInvalid patient ID")
        else:
            print("\n")
            print("                         PATIENT INFORMATION")
            print("#"*80,"\n")
            for row in data:
                #printing information of the patient using for loop
                print("PATIENT ID                : ",row[0],"\n","NAME                      : ",row[1],"\n","SEX                       : ",row[2],"\n","UID                       : ",row[3],"\n","DOB                       : ",row[4],"\n","BLOOD GROUP               : ",row[5],"\n","CONTACT NUMBER            : ",row[6],"\n","ADDRESS                   : ",row[7],"\n","PREVIOUS MEDICAL PROBLEMS : ",row[8],"\n","GUARDIAN NAME             : ",row[9],"\n","GUARDIAN RELATION         : ",row[10],"\n","GUARDIAN'S CONTACT NUMBER : ",row[11],"\n","NAME OF INSURANCE         : ",row[12],"\n","INSURANCE CARD NUMBER     : ",row[13],"\n","CARD HOLDER'S NAME        : ",row[14],"\n","VALID FROM                : ",row[15],"\n","VALIDITY DURATION         : ",row[16],"\n","AMOUNT COVERED            : ",row[17],"\n","DISEASES COVERED          : ",row[18],sep='')
                print("\n","#"*80,sep='')
    elif ques=='n':
        a=search_id()                      #calling search_id() to get ID
        sqlquery="select * from REGISTERED_PATIENTS where RegID="+str(a)
        mycur.execute(sqlquery)
        data=mycur.fetchall()             #fetching data
        print("\n")
        print("                         PATIENT INFORMATION")
        print("#"*80,"\n")
        for row in data:
            #printing information of the patient using for loop
            print("PATIENT ID                : ",row[0],"\n","NAME                      : ",row[1],"\n","SEX                       : ",row[2],"\n","UID                       : ",row[3],"\n","DOB                       : ",row[4],"\n","BLOOD GROUP               : ",row[5],"\n","CONTACT NUMBER            : ",row[6],"\n","ADDRESS                   : ",row[7],"\n","PREVIOUS MEDICAL PROBLEMS : ",row[8],"\n","GUARDIAN NAME             : ",row[9],"\n","GUARDIAN RELATION         : ",row[10],"\n","GUARDIAN'S CONTACT NUMBER : ",row[11],"\n","NAME OF INSURANCE         : ",row[12],"\n","INSURANCE CARD NUMBER     : ",row[13],"\n","CARD HOLDER'S NAME        : ",row[14],"\n","VALID FROM                : ",row[15],"\n","VALIDITY DURATION         : ",row[16],"\n","AMOUNT COVERED            : ",row[17],"\n","DISEASES COVERED          : ",row[18],sep='')
            print("\n","#"*80,sep='')
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions

        
###############################################################################   
###############################################################################       
    
    
def patient_diagnosis_info():
    """used to insert a patient's diagnosis information into the table DIAGNOSIS_INFORMATION after he/she had made an appointmnet"""
    #using these dictionaries to get doctor's name along with ID 
    global Physician
    global Orthopedician
    global Cardiologist
    global Neurologist
    global Opthalmologist
    global Gynaecologist
    global Pediatrician
    ques=input("Enter 'y' if the patient remembers the ID or else enter 'n' : ")         #asking user about whether he/she remembers the ID or not
    if ques=='y':
       PatientID=int(input("Enter Patient's ID : "))
    elif ques=='n':
        PatientID=search_id()                                                   #calling search_id function to get the ID
    validityquery="select * from REGISTERED_PATIENTS where RegID="+str(PatientID)     #fetching all the information using ID
    mycur.execute(validityquery)
    mycur.fetchall()
    count=mycur.rowcount
    if count==0:                    #checking the validity of ID using mycur.rowcount
        print("\nInvalid patient ID")
        input("Press enter to continue...")
        return
        
    query3="select PNAME from REGISTERED_PATIENTS where RegID="+str(PatientID)
    mycur.execute(query3)
    data_name=mycur.fetchall()
    Patient_Name=data_name[0][0]                    #fetching name of patient from list of tuples having patient's name
    query="select INVESTIGATING_DOCTOR_NAME from APPOINTMENTS where RegID="+str(PatientID)+" and APP_DATE=curdate()"        #allowing only those patients who have already made an appointment
    mycur.execute(query)
    data=mycur.fetchall()
    INVESTIGATING_DOCTOR=data[0][0]                  #fetching name of doctor from list of tuples having doctor's name
    
    
    print("\n\nFollowing information is to be filled under the guidance of Dr.",INVESTIGATING_DOCTOR)
    PROBLEM_SUGGESTED=input("Enter the medical problem detected : ")
    TESTS_SUGGESTED=input("Enter medical tests suggested : ")
    MEDICINES_PRES=input("Enter medicines prescribed : ")
    #inserting the diagnosis information of the patient into the table diagnosis_information
    sqlquery="insert into DIAGNOSIS_INFORMATION(RegID,PNAME,INVESTIGATING_DOCTOR,PROBLEM_SUGGESTED,TESTS_SUGGESTED,MEDICINES_PRESCRIBED,DIAGNOSIS_DATE) values("+str(PatientID)+",'"+Patient_Name+"','"+INVESTIGATING_DOCTOR+"','"+PROBLEM_SUGGESTED+"','"+TESTS_SUGGESTED+"','"+MEDICINES_PRES+"',curdate())"
    mycur.execute(sqlquery)
    mycon.commit()                                   #commiting the query
    print("\nInformation regarding the diagnosis of ",Patient_Name ,"has been successfully added to the management system.")
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions

    
###############################################################################   
###############################################################################       
        
   
def show_patient_dia_info():
    """used to display a patient's diagnosis information."""
    ques=input("Enter 'y' if the patient remembers the ID or else enter 'n' : ")         
    if ques=='y':
       pat_id=int(input("Enter Patient's ID : "))
    elif ques=='n':
        pat_id=search_id()     #calling this function in order to get patient's ID
    
    sqlquery="select * from DIAGNOSIS_INFORMATION where RegID="+str(pat_id)             #selecting all records from dignosis_information table
    mycur.execute(sqlquery)
    data=mycur.fetchall()
    count=mycur.rowcount                #fetching  record number to check the validity of ID
    if count==0:
        print("Invalid Patient ID")
    else:
        for row in data:
            #printing the data fetched after executing the query using for loop
            print("\nDIAGNOSIS INFORMATION")
            print("#"*50)
            print("DIAGNOSIS ID         : ",row[0],"\n","PATIENT ID           : ",row[1],"\n","NAME                 : ",row[2],"\n","INVESTIGATING DOCTOR : ",row[3],"\n","SUGGESTED PROBLEM    : ",row[4],"\n","SUGGESTED TESTS      : ",row[5],"\n","MEDICINES PRESCRIBED : ",row[6],"\n","DATE OF DIAGNOSIS    : ",row[7],sep='')
            print("#"*50)
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions
    
                    
#############################################################################   
#############################################################################       


def appointment():
    """used for making appointments and keeping a record of them with date and other infomation"""
    #using global statement to access the names of the doctors and IDs stored in these dictionaries
    global Physician
    global Orthopedician
    global Cardiologist
    global Neurologist
    global Opthalmologist
    global Gynaecologist
    global Pediatrician
    global lst
    appfurther='y'           #appfurther stands for further appointments
    while appfurther=='y':              #using while loop infinite times till the value of appfurther is 'y'
        ques=input("Enter 'y' if the patient remembers the ID or else enter 'n' : ")        
        if ques=='y':
            PatientID=int(input("Enter Patient's ID : "))
        elif ques=='n':
            PatientID=search_id()
        validityquery="select * from REGISTERED_PATIENTS where RegID="+str(PatientID)     #fetching all the information using ID
        mycur.execute(validityquery)
        mycur.fetchall()
        count=mycur.rowcount
        if count==0:                    #checking the validity of ID using mycur.rowcount
            print("\nInvalid patient ID")
            input("Press enter to continue...")
            return
        query3="select PNAME from REGISTERED_PATIENTS where RegID="+str(PatientID)
        mycur.execute(query3)
        data_name=mycur.fetchall()
        Patient_Name=data_name[0][0]          #fetching name
        Investigation=input("Enter present medical problem : ")
        #printing various departments of the hospital
        print("\nSelect Category of doctor according to the medical problem : ")
        print("####################################################################")
        print("1. Physician")
        print("2. Orthopedician")
        print("3. Cardiologist")
        print("4. Neurologist")
        print("5. Opthalmologist")
        print("6. Gynaecologist")
        print("7. Pediatrician")
        print("####################################################################")          
        ch2=int(input("Enter category : "))             #asking for user's choice of department
        print()
        #lst is the list containing dictionaries named after departments which further contains names of the doctors as values and their ID as key
        a=lst[ch2-1]          #'a' is the dictionary named after the department selected containing the names of doctors and their IDs and 'ch2-1' is used because choice of department starts from one but index starts from 0
        
        print("Doctors in this category are: ")
        print("####################################################################\n")
        for key in a:
            #printing names of the doctor from dictionary 'a'
            print("ID :",key,"      Dr.",a[key],"\n")                  #while traversing a dictionary, key is obtained which is used here to get the name of the doctor(value)
        print("####################################################################")        
        Doctor_num=int(input("Enter investigating doctor's id : "))   #asking for the ID which was displayed corresponding to the desired doctor
        query1="select NAME,DEPARTMENT,DEPT_NO from DOCTOR_INFO where DOC_ID ="+str(Doctor_num)
        mycur.execute(query1)
        data=mycur.fetchall()               #fetching dept and dept number using ID of the doctor
        Doctor_name=data[0][0]
        Dept=data[0][1]                     #getting department name from the list of tuples containg dept and dept_num
        Dept_num=data[0][2]                 #getting department number from the list of tuples containg dept and dept_num
        app_numquery="select max(APP_NUM) from APPOINTMENTS where DEPARTMENT='"+Dept+"' and APP_DATE=curdate() and DOC_ID="+str(Doctor_num)    #selecting maximum appointment number for current date for the selected doctor
        mycur.execute(app_numquery)
        data=mycur.fetchall()
        if data[0][0]==None:           #checking if there is no pre-existing record in the appointment table for the current date and doctor; then automatically it is assigned as 1 and further appointment nos. are assigned by adding to the last maximum appoitment number                               
            appno=1
        else:
            appno=int(data[0][0])+1    #else appointment number is obtained by adding 1 to the obtained maximum appointment number
        #inserting the information asked into the appointment table
        sqlquery="insert into APPOINTMENTS (RegID,APP_NUM,PNAME,APP_DATE,MED_PROBLEM,INVESTIGATING_DOCTOR_NAME,DEPARTMENT,DEPT_NO,DOC_ID) values("+str(PatientID)+","+str(appno)+",'"+Patient_Name+"',curdate(),'"+Investigation+"','"+Doctor_name+"','"+Dept+"',"+str(Dept_num)+","+str(Doctor_num)+");"
        mycur.execute(sqlquery)
        mycon.commit()
        print("\nAppointemnt number is : ",appno)                 #displaying the appointment number to the user
        
        #asking the user if there is a need for making further appointments or not
        appfurther=input("Enter 'y' to assign further appointments or press enter to continue.....")

#############################################################################   
#############################################################################       

        
def show_appointments():
    """used to display all the apointments datewise from the table appointments"""
    askdate=input("Enter 't' to see today's appointments or press 'd' to get appointments of some other date : " )
    if askdate=='t':
        query="select * from appointments where APP_DATE=curdate()"                #using curdate() in order to get the current or today's appointments
        mycur.execute(query)
        data=mycur.fetchall()            #data is list of tuples
    else:
        dateapp=input("Enter date(YYYY-MM-DD) to get information regarding that day's appointments : ")
        query="select * from appointments where APP_DATE='"+dateapp+"'"           #selecting only those records where the date is given
        mycur.execute(query)
        data=mycur.fetchall()            #data is list of tuples
    for row in data:
        #printing data fetched using for loop
        print("\nAPPOINTMENTS")
        print("#"*50)
        print("APPOINTMENT ID              : ",row[0],"\n","PATIENT ID                  : ",row[1],"\n","APPOINTMENT NUMBER          : ",row[2],"\n","NAME                        : ",row[3],"\n","DATE OF APPOINTMENT         : ",row[4],"\n","MEDICAL PROBLEM             : ",row[5],"\n","INVESTIGATING DOCTOR'S NAME : ",row[6],"\n","DEPARTMENT                  : ",row[7],"\n","DEPARTMENT NUMBER           : ",row[8],"DOCTOR ID                   : ",row[9],sep='')
        print("#"*50,"\n")    
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions

#############################################################################   
#############################################################################       

    
def update_patient():
    """used for updating a registered patient's information from various tables"""
    global Physician
    global Orthopedician
    global Cardiologist
    global Neurologist
    global Opthalmologist
    global Gynaecologist
    global Pediatrician
    #tab_name is a list containing the names of the tables related to patient in the database
    tab_name=['REGISTERED_PATIENTS','DIAGNOSIS_INFORMATION','APPOINTMENTS','PATIENTS_ADM_DIS']
    updfurther='y'                #updfurther refers to updating further
    while updfurther=='y':        #using while loop infinitely until there is no further need of updating more records 
        print("\n################################################################")    #printing menu containing names of tables
        print("                           MENU")
        print("################################################################")
        print("                  1.REGISTERED_PATIENTS")
        print("                  2.DIAGNOSIS_INFORMATION")
        print("                  3.APPOINTMENTS")
        print("                  4.PATIENTS_ADM_DIS")
        print("                  5.TO EXIT\n")
        ch1=int(input("Enter choice number : "))
        if ch1<1 or ch1>5:                     #checking for the validity of the choice number
            print("Invalid choice, try again")
        elif ch1==5:                           #breaking the loop in case the choice is exit
            print("Thank you.")
            break
        else:
            ques=input("Enter 'y' if the patient remembers the ID or else enter 'n' : ")         
            if ques=='y':
                PatientID=int(input("Enter Patient's ID : "))
            elif ques=='n':
                PatientID=search_id()
            query="select * from REGISTERED_PATIENTS where RegID="+str(PatientID)
            mycur.execute(query)
            dataid=mycur.fetchall()
            if dataid[0][0]==None:                         #checking if no record is obtained and thus checking the validity of the given ID
                print("Invalid Patient ID.")
            else:
                sqlquery1="desc "+tab_name[ch1-1]         #using desc command to get the name of fields in a table
                mycur.execute(sqlquery1)
                data=mycur.fetchall()
                b=len(data)
                print("\nFields in the selected choice are : \n")
                for j in range(1,b):            #running the for loop till all the fetched data is traversed
                    print(j,"---> ",data[j][0])          #using nested index to get the name of the field as returned data is in the form of a list of tuples containing names of column along with their type
                print()
                col_num=int(input("Enter the record number to be updated: "))       #asking for the choice number of the column wanted
                column=data[col_num][0]           #using col_num(column number) to get the name of the column
                typ=data[col_num][1]              #using col_num to get the datatype of the column
                queryold="select "+column+" from "+tab_name[ch1-1]+" where RegID="+str(PatientID)
                mycur.execute(queryold)
                dataold=mycur.fetchall()
                old=dataold[0][0]                 #displaying the old record 
                print("\nOld record was : ",old)
                new=input("Enter the new record: ")         #asking for the new updated record
                
                if "char" in typ or "varchar" in typ or "date" in typ:     
                    #commiting a query by checking the condition of the datatype of the column, i.e if it is not an integer then the new record can ce concatenated otherwise it is converted into a string so as to concatenate
                    sqlquery2="update"+" "+tab_name[ch1-1]+" "+"set"+" "+column+"="+'"'+new+'"'+" "+"where RegID="+str(PatientID)+";"
                    mycur.execute(sqlquery2)
                    mycon.commit()
                    print("\nRecord has been updated.")
                    

                elif "int" in typ or "bigint" in typ:
                    sqlquery2="update "+tab_name[ch1-1]+" "+"set"+" "+column+"="+str(new)+" "+"where RegID="+str(PatientID)
                    mycur.execute(sqlquery2)
                    mycon.commit()
                    print("Record has been updated.")
                    
                #asking for further instructions from the user, if the user types 'y' then the loop is continued
                updfurther=input("Enter 'y' to update futher or press any key...")

#############################################################################   
#############################################################################       


def add_doctor():
    """used for adding new doctors to the managemnet system"""
    #using global statement in order to add the new doctor into its respective department dictionary
    global Physician
    global Orthopedician
    global Cardiologist
    global Neurologist
    global Opthalmologist
    global Gynaecologist
    global Pediatrician
    #asking for the doctor's information
    doc_name=input("Enter name : ")
    doc_uid=int(input("Enter UID : "))
    doc_sex=input("Enter sex (M/F/Others) : ")
    doc_bloodgrp=input("Enter blood group : ")
    doc_DOB=input("Enter DOB (YYYY-MM-DD) : ")
    doc_contactnum=int(input("Enter contact number : "))
    doc_emailID=input("Enter e-mail ID : ")
    print("\n")
    print("Select from the given below list of departments.\n")
    print("          ###############################")
    print("\t\t","   DEPARTMENTS")
    print("          ###############################")
    for k in range(len(lststr)):               #printing name of the department from the list(lststr) containing the name of the department using for loop 
        print("\t\t",k+1,".",lststr[k])    
    ch=int(input("Enter department number : "))  #asking for the corresponding  department number displayed using for loop
    doc_dept=lststr[ch-1]                      #getting the name of dept using index minus 1 as choices starts from 1 but index starts from 0
    
    
    dept_num=ch  #dept_num is same as the choice asked before from the displayed names of departments
    doc_qual=input("Enter qualifiactions : ")
    marital_status=input("Enter marital status (Married/Unmarried/Divorcee) : ")
    #inserting the information provided into the table called DOCTOR_INFO
    sqlquery="insert into DOCTOR_INFO(NAME,UID,SEX,BLOOD_GROUP,DOB,CONTACT_NUM,EMAIL_ID,DEPARTMENT,DEPT_NO,QUALIFICATIONS,MARITAL_STATUS)values('" +doc_name+"',"+str(doc_uid)+",'"+doc_sex+"','"+doc_bloodgrp+"','"+doc_DOB+"',"+str(doc_contactnum)+",'"+doc_emailID+"','"+doc_dept+"',"+str(dept_num)+",'"+doc_qual+"','"+marital_status+"')"         
    mycur.execute(sqlquery)
    mycon.commit()
    sqlquery1="select * from DOCTOR_INFO where CONTACT_NUM="+str(doc_contactnum)
    mycur.execute(sqlquery1)
    data=mycur.fetchall()
    #fetching data to provide the newly added doctor with his/her ID which is automatically incremented by 1 as the doctors are added to the database
     
    for row in data:
        print("\nDOCTOR ID IS : ",row[0],"\n")
    print("Thank you.\n")
    initialisation()                                   #calling this fucntion to add the doctor name to its respective department dictionary 
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions

#############################################################################   
#############################################################################       

        
def show_doc_details():
    """used to display the records of the doctors"""                  
    askinfo=input("Enter 'a' in case to get information about all doctors or enter 's' to get a specific doctor's information : ")    #asking whether to display all records or a specific doctor's record
    if askinfo=='a':
        sqlquery="select * from DOCTOR_INFO"          #selecting all records from the table DOCTOR_INFO
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        for row in data:
            #displaying all records fetched using for loop
            print("\nDOCTOR INFORMATION")
            print("#"*50)
            print("DOCTOR ID         : ",row[0],"\n","NAME              : ",row[1],"\n","UID               : ",row[2],"\n","SEX               : ",row[3],"\n","BLOOD GROUP       : ",row[4],"\n","DOB               : ",row[5],"\n","CONTACT NUMBER    : ",row[6],"\n","E-MAIL ID         : ",row[7],"\n","DEPARTMENT        : ",row[8],"\n","DEPARTMENT NUMBER : ",row[9],"\n","QUALIFICATIONS    : ",row[10],"\n","MARITAL STATUS    : ",row[11],sep='')
            print("#"*50,"\n")
    elif askinfo=='s':             #in case of displaying a specific doctor's infromation
        doc_id=int(input("Enter doctor's ID : "))
        sqlquery="select * from DOCTOR_INFO where DOC_ID="+str(doc_id)
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        count=mycur.rowcount
        if count==0:
            print("\nInvalid doctor ID")
        else:  
            for row in data:
                print("DOCTOR INFORMATION")
                print("#"*50)
                print("DOCTOR ID         : ",row[0],"\n","NAME              : ",row[1],"\n","UID               : ",row[2],"\n","SEX               : ",row[3],"\n","BLOOD GROUP       : ",row[4],"\n","DOB               : ",row[5],"\n","CONTACT NUMBER    : ",row[6],"\n","E-MAIL ID         : ",row[7],"\n","DEPARTMENT        : ",row[8],"\n","DEPARTMENT NUMBER : ",row[9],"\n","QUALIFICATIONS    : ",row[10],"\n","MARITAL STATUS    : ",row[11],sep='')
                print("#"*50,"\n")
    else:
        print("\nInvalid entry!!")         #in case when the user has neither typed'a' for all nor 's' for specific
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions
        

#############################################################################   
#############################################################################       

        
def update_doc_detail():
    """used to update the records of a doctor in the table DOCTOR_INFO"""
    global Physician
    global Orthopedician
    global Cardiologist
    global Neurologist
    global Opthalmologist
    global Gynaecologist
    global Pediatrician
    updatefurther='y'
    while updatefurther=='y':                       #using while loop infinitely till the value of updatefurther is 'y' 
        DocID=int(input("\nEnter Doctor ID : "))
        sqlquery1="select * from DOCTOR_INFO where DOC_ID="+str(DocID)+";"
        mycur.execute(sqlquery1)
        data=mycur.fetchall()
        count=mycur.rowcount
        if count==0:                           #checking the validity of the ID by fetching records using the same
            print("Invalid doctorID")
        else:
            print("\nEnter choice from the menu given below to update doctor's details.")
            sqlquery1="desc DOCTOR_INFO;"          #using this query to fetch column names and their types
            mycur.execute(sqlquery1)
            data=mycur.fetchall()
            b=len(data)                            #using data's length in order to use the for loop for  that many times    
            print("######################################################")
            for j in range(1,b):                   #starting the range from 1 because data[0][0] is the ID which cannot be updated
                print(j,"---> ",data[j][0],"\n")
            print("######################################################")
            choice=int(input("\nEnter the record number to be updated: "))
            column=data[choice][0]                #name of column is same as data[choice][0] as data is a list of tuple contains column names along with their type
            typ=data[choice][1]                   #example data=[(Name,char(20)),(Sex,char(2))] and typ is the datatype of the column selected
            oldquery="select "+column+" from DOCTOR_INFO where DOC_ID="+str(DocID)
            mycur.execute(oldquery)           
            olddata=mycur.fetchall()
            old=olddata[0][0]             #fetching the old record in order to display it
            print("\nOld record was : ",old,"\n")
            new=input("Enter the new record: ")
            
            if "char" in typ or "varchar" in typ or "date" in typ:
                sqlquery2="update DOCTOR_INFO set " + column+ "="+"'"+new+"'"+" "+"where DOC_ID="+str(DocID)+";"
            
            elif "int" in typ or "bigint" in typ:
                sqlquery2="update DOCTOR_INFO set " + column+ "=" +str(new)+" "+"where DOC_ID="+str(DocID)+";"
            
            mycur.execute(sqlquery2)
            mycon.commit()               #making the changes in database permanent
            print("\nRecord has been updated.")
            updatefurther=input("\nEnter 'y' to update further details or press any key to continue...  ")            #asking for user's further instructions
            
#############################################################################   
#############################################################################       

            
def delete_doctor():
    """used to delete the record of a doctor from the database"""
    global Physician
    global Orthopedician
    global Cardiologist
    global Neurologist
    global Opthalmologist
    global Gynaecologist
    global Pediatrician
    DocID=int(input("Enter Doctor ID : "))
    sqlquery1="select * from DOCTOR_INFO where DOC_ID="+str(DocID)+";"
    mycur.execute(sqlquery1)
    #fetching records from cursor i.e mycur
    data=mycur.fetchall()
    count=mycur.rowcount
    if count==0:                  #checking the validity of the ID
        print("Invalid Doctor ID.")
    else:
        name_doc=data[0][1]
        sqlquery="delete from DOCTOR_INFO "+"where DOC_ID="+str(DocID)+";"
        mycur.execute(sqlquery)
        mycon.commit()           #making the changes in database permanent
        print("\nThe given record of Dr.",name_doc," has now been successfully deleted.")
        
        initialisation()               #calling this fucntion to make changes in the dictionary containing names and ID of doctors as well
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions
    
#############################################################################   
#############################################################################           

def admit_patient():
    """used to admit patients and insert their records into the table PATIENTS_ADM_DIS """
    #using these global dictionaries to provide the user with doctor name and ID
    global Physician
    global Orthopedician
    global Cardiologist
    global Neurologist
    global Opthalmologist
    global Gynaecologist
    global Pediatrician
    ques=input("Enter 'y' if the patient remembers the ID or else enter 'n' : ")     #getting ID by either asking or searching for it through search_id function    
    if ques=='y':
       PatientID=int(input("Enter Patient's ID : "))
    elif ques=='n':
        PatientID=search_id()
    
    validityquery="select * from REGISTERED_PATIENTS where RegID="+str(PatientID)     #fetching all the information using ID
    mycur.execute(validityquery)
    mycur.fetchall()
    count=mycur.rowcount
    if count==0:                    #checking the validity of ID using mycur.rowcount
        print("\nInvalid patient ID")
        input("\nPress enter to continue...")
        return
    checkadmit="select * from PATIENTS_ADM_DIS where RegID="+str(PatientID)+" and DATE_OF_DISCHARGE IS NULL"   #using this query to check whether the same patient is already admitted and had not been discharged yet
    mycur.execute(checkadmit)
    dataadmit=mycur.fetchall()
    if len(dataadmit)!=0:              #if there is a record in which Date Of Discharge is NULL then that means that the same patient had not been discharged
        print("\nPatient is already admitted , kindly discharge first in order to admit him/her again")
    else:
        #if the patient is being admitted then the user is asked to select the doctor according to the department and ID
        print("\nSelect Category of department according to the medical problem : ")
        print("####################################################################")
        print("1. Physician")
        print("2. Orthopedician")
        print("3. Cardiologist")
        print("4. Neurologist")
        print("5. Opthalmologist")
        print("6. Gynaecologist")
        print("7. Pediatrician")
        print("####################################################################")          
        ch2=int(input("Enter category : "))
        print()
        #lst is the list containing department dictionaries names which further contains names of the doctor as values and ID as key
        a=lst[ch2-1]          #'a' is the dictionary containing the names of doctors along with their IDs in the selected department and 'ch2-1' is used because choice of department starts from one but index starts from 0
        
        print("Doctors in this category are: ")
        print("####################################################################\n")
        for key in a:
            #printing names and the IDs of the doctor from dictionary 'a'
            print("ID :",key,"      Dr.",a[key],"\n")
        print("####################################################################")        
        Doctor_num=int(input("Enter investigating doctor's id : "))  
        query1="select DEPARTMENT,NAME from DOCTOR_INFO where DOC_ID="+str(Doctor_num)       #selecting various information of the doctor using his/her ID
        mycur.execute(query1)
        data=mycur.fetchall()     
        Dept=data[0][0]                             #fetching data from the executed query
        Doctor_name=data[0][1]
        while True:
            print("\n###################################################################")                              
            print("WARD TYPES")                    #now displaying the ward type in which the patient is to be admitted 
            print("###################################################################")
            print("1. General Ward." )
            print("2. Cottage Ward.")
            print("3. ICU.")
            print("###################################################################")
            numward=int(input("\nEnter type of ward no. : "))
            if numward==1:
                typeward='General'
                break
            elif numward==2:
                typeward='Cottage'
                break
            elif numward==3:
                typeward='ICU'
                break
            else:
                print("\n","Invalid choice.\n")
        ROA=input("Enter reason of admission : ")
        query3="select Ward_No from WARDS where  Department='"+Dept+"'and Type='"+typeward+"' and Avail_Beds=(select min(Avail_Beds) from wards where  Department='"+Dept+"'and Type='"+typeward+"' )"                  #selecting only those wards which are possessed by the required department and have the minimum available beds to keep up with full occupancy of the ward
        mycur.execute(query3)
        data3=mycur.fetchall()
        cnt=mycur.rowcount            #checking ward availability by counting the number of records obtained after executing the query with required conditions
        if cnt==0:
            print("\nAt the moment, there are no wards available.")
        else:
            print("\nThe available wards are : ")
            print("###################################################################")
            for row in data3:
                print("---> ",row[0])                     #printing those available wards
            print("###################################################################")
                
            wardnum=input("Enter ward number from the above available wards : ")
            query4="update WARDS set Avail_Beds=Avail_Beds-1 where Ward_No='"+wardnum+"'"             #updating the number of available beds from the selected ward number
            mycur.execute(query4)
            mycon.commit()                 #making the changes permanent in the database
            query5="select Bed_Num from "+wardnum+" where RegID is null"          #now selecting only those beds from the ward which are available 
            mycur.execute(query5)
            data5=mycur.fetchall()
            print("\nThe available beds are : ")
            print("###################################################################")
            for row in data5:                                                          #printing those available beds using for loop     
                print("---> ",row[0])    
            print("###################################################################")
            bednum=input("Enter bed number: ")
            query5="update "+wardnum+" set RegID="+str(PatientID)+" where RegID is null and Bed_Num='"+bednum+"'"          #updating the status of the ward by giving ID of the patient and by providing with the bed number
            
            mycur.execute(query5)
            mycon.commit()                #making the changes permanent in the database
            #inserting the required information into the table PATIENTS_ADM_DIS
            insertquery="insert into PATIENTS_ADM_DIS (RegID,REASON_OF_ADMISSION,DOCTOR_IN_VIGIL,DATE_OF_ADMISSION,WARD_NO,BED_NO) values("+str(PatientID)+",'"+ROA+"','"+Doctor_name+"',curdate(),'"+wardnum+"','"+bednum+"');"
            mycur.execute(insertquery)
            mycon.commit() 
            
            query6="select pname from registered_patients where RegID="+str(PatientID)              #using the same patient ID to fetch name from the table REGISTERED_PATIENTS
            mycur.execute(query6)
            data6=mycur.fetchall()
            Name=data6[0][0]
            print("\n",Name," has been admitted into ward ",wardnum,sep='')               #displaying the name of the of the patient along with the ward in which he/she is admitted
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions

#############################################################################   
#############################################################################       
                                
def show_admitted_patients():
    """used to display the records of the patients admitted in the hospital."""
    print("\n###################################################################")
    print("SEARCH FOR ADMITTED PATIENTS")             #displaying choices through which records can be classified on various grounds
    print("###################################################################")
    print("1. Admitted Today")
    print("2. Datewise")
    print("3. Patient ID-wise")
    print("4. Show All\n")
    choice=int(input("Enter choice : "))
    if choice==1:
        sqlquery="select AdmID,P.RegID,PName,sex,GuardianName,GuardianRelation,GuardianContactNo,Reason_of_admission,date_of_admission,doctor_in_vigil,ward_no,bed_no from PATIENTS_ADM_DIS P,REGISTERED_PATIENTS R where DATE_OF_ADMISSION=curdate() and date_of_discharge is null and R.RegID=P.RegID"             #curdate is used to get current date, using two tables at the same time to  fetch required data by comparing RegID in both tables
        mycur.execute(sqlquery)
        data=mycur.fetchall()                      #data is a list of tuples containing several records
        for row in data:
            #displaying record using for loop
            print("\nADMITTED PATIENTS")
            print("#"*50)
            print("ADMISSION ID              : ",row[0],"\n","PATIENT ID                : ",row[1],"\n","NAME                      : ",row[2],"\n","SEX                       : ",row[3],"\n","GUARDIAN NAME             : ",row[4],"\n","GUARDIAN RELATION         : ",row[5],"\n","GUARDIAN's CONTACT NUMBER : ",row[6],"\n","REASON OF ADMISSION       : ",row[7],"\n","DATE OF ADMISSION         : ",row[8],"\n","DOCTOR IN VIGIL           : ",row[9],"\n","WARD                      : ",row[10],"\n","BED NUMBER                : ",row[11],sep='')
            print("#"*50,"\n")
    elif choice==2:
        inpdate=input("Enter date in YYYY-MM-DD format : ")
        sqlquery="select AdmID,P.RegID,PName,sex,GuardianName,GuardianRelation,GuardianContactNo,Reason_of_admission,date_of_admission,doctor_in_vigil,ward_no,bed_no from PATIENTS_ADM_DIS P,REGISTERED_PATIENTS R where DATE_OF_ADMISSION='"+inpdate +"'and date_of_discharge is null and R.RegID=P.RegID"     #using two tables at the same time to  fetch required data by comparing RegID in both tables
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        count=mycur.rowcount
        if count==0:                      #checking the validity of the date by comparing datacount
            print("\nNone were admitted on the given date")
        else:
            for row in data:
                print("\nADMITTED PATIENTS")
                print("#"*50)
                print("ADMISSION ID              : ",row[0],"\n","PATIENT ID                : ",row[1],"\n","NAME                      : ",row[2],"\n","SEX                       : ",row[3],"\n","GUARDIAN NAME             : ",row[4],"\n","GUARDIAN RELATION         : ",row[5],"\n","GUARDIAN's CONTACT NUMBER : ",row[6],"\n","REASON OF ADMISSION       : ",row[7],"\n","DATE OF ADMISSION         : ",row[8],"\n","DOCTOR IN VIGIL           : ",row[9],"\n","WARD                      : ",row[10],"\n","BED NUMBER                : ",row[11],sep='')
                print("#"*50,"\n")
    elif choice==3:
        ques=input("Enter 'y' if the patient remembers the ID or else enter 'n' : ")         
        if ques=='y':
            pat_id=int(input("Enter Patient's ID : "))
        elif ques=='n':
            pat_id=search_id()
        sqlquery="select AdmID,P.RegID,PName,sex,GuardianName,GuardianRelation,GuardianContactNo,Reason_of_admission,date_of_admission,doctor_in_vigil,ward_no,bed_no from PATIENTS_ADM_DIS P,REGISTERED_PATIENTS R where P.RegID="+str(pat_id)+" and date_of_discharge is null and R.RegID=P.RegID"                 #using two tables at the same time to  fetch required data by comparing RegID in both tables
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        count=mycur.rowcount                #fetching  record number to check the validity of ID
        if count==0:
            print("\nInvalid Patient ID")
        else:
            for row in data:
                print("\nADMITTED PATIENTS")
                print("#"*50)
                print("ADMISSION ID              : ",row[0],"\n","PATIENT ID                : ",row[1],"\n","NAME                      : ",row[2],"\n","SEX                       : ",row[3],"\n","GUARDIAN NAME             : ",row[4],"\n","GUARDIAN RELATION         : ",row[5],"\n","GUARDIAN's CONTACT NUMBER : ",row[6],"\n","REASON OF ADMISSION       : ",row[7],"\n","DATE OF ADMISSION         : ",row[8],"\n","DOCTOR IN VIGIL           : ",row[9],"\n","WARD                      : ",row[10],"\n","BED NUMBER                : ",row[11],sep='')
                print("#"*50,"\n")
    elif choice==4:
        sqlquery="select AdmID,P.RegID,PName,sex,GuardianName,GuardianRelation,GuardianContactNo,Reason_of_admission,date_of_admission,doctor_in_vigil,ward_no,bed_no from PATIENTS_ADM_DIS P,REGISTERED_PATIENTS R where date_of_discharge is null and R.RegID=P.RegID"  #using two tables at the same time to  fetch required data by comparing RegID in both tables
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        for row in data:
            print("\nADMITTED PATIENTS")
            print("#"*50)
            print("ADMISSION ID              : ",row[0],"\n","PATIENT ID                : ",row[1],"\n","NAME                      : ",row[2],"\n","SEX                       : ",row[3],"\n","GUARDIAN NAME             : ",row[4],"\n","GUARDIAN RELATION         : ",row[5],"\n","GUARDIAN's CONTACT NUMBER : ",row[6],"\n","REASON OF ADMISSION       : ",row[7],"\n","DATE OF ADMISSION         : ",row[8],"\n","DOCTOR IN VIGIL           : ",row[9],"\n","WARD                      : ",row[10],"\n","BED NUMBER                : ",row[11],sep='')
            print("#"*50,"\n")
    else:
        print("\nInvalid choice.")
    
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions
    
#############################################################################   
#############################################################################       
                
             
def discharge_patient():
    """used to discharge patients and insert their record into the table PATIENTS_ADM_DIS""" 
    ques=input("Enter 'y' if the patient remembers the ID or else enter 'n' : ")          #asking whether the patient remembers his/her ID
    if ques=='y':
       PatientID=int(input("Enter Patient's ID : "))                                      #asking for ID and Admission ID  to fetch records  
       AdmID=int(input("Enter Admission ID : "))                                          #AdmID is being asked rather than fetched using RegID so that only authorised staff can discharge the patient  
    elif ques=='n':
        PatientID=search_id()                                                     #in case the person does not remember his/her ID, search_id function is called 
        AdmID=int(input("Enter Admission ID : "))
    validityquery="select * from REGISTERED_PATIENTS where RegID="+str(PatientID)     #fetching all the information using ID
    mycur.execute(validityquery)
    mycur.fetchall()
    count=mycur.rowcount
    if count==0:                    #checking the validity of ID using mycur.rowcount
        print("\nInvalid patient ID")
        input("Press enter to continue...")
        return
    
    checkdischarge="select date_of_discharge from PATIENTS_ADM_DIS where date_of_discharge is null and AdmID="+str(AdmID)        #using this query to check whether the patient has already been discharged or not
    mycur.execute(checkdischarge)                                                                                                #if there is no patient whose discharge date is not present then it means that he/she has already been discharged from the hospital
    datacheckdis=mycur.fetchall()
    
    
    if len(datacheckdis)==0:        #using length of data to check whether there is a record under discharge date or not
        print("\nThis patient has already been discharged from the hospital.")
        input("\nPress enter to continue...")
        return                     #in case the patient has already been discharged  , this function returns nothing and goes back to the menu
        
    
    query="select PNAME,WARD_NO,BED_NO from REGISTERED_PATIENTS R, PATIENTS_ADM_DIS A where R.RegID="+str(PatientID)+" and A.AdmID="+str(AdmID)+" and A.RegID=R.RegID"     #selecting all the necessary record using two tables by comparing RegID
    mycur.execute(query)
    data=mycur.fetchall()                                                         #fetching data in order to get the required information that is to be inserted into the table DISCARGED_PATIENTS
    name=data[0][0]
    ward_num=data[0][1]
    bednum=data[0][2]
    
    query2="update WARDS set Avail_Beds=Avail_Beds+1 where Ward_No='"+ward_num+"'"                   #updating ward in order to free up the bed that was occupied by that patient
    mycur.execute(query2)
    mycon.commit()
    
    query4="update "+ward_num+" set RegID=NULL where RegID="+str(PatientID)+" and Bed_Num='"+bednum+"'"      #updating that ward number in which the patient was admitted
    mycur.execute(query4)
    mycon.commit()
    #inserting the required information into the table PATIENTS_ADM_DIS 
    query5="update PATIENTS_ADM_DIS set  date_of_discharge=curdate() where AdmID="+str(AdmID)          #setting the date of discharge as present date using curdate() 
    mycur.execute(query5)
    mycon.commit()                                       #making the changes permanent in the database      
    
    query6="select pname from registered_patients where RegID="+str(PatientID)
    mycur.execute(query6)
    data6=mycur.fetchall()
    name=data6[0][0]
    print("\n",name," has now been successfully discharged from ward ",ward_num,sep='')
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions
   
#############################################################################   
#############################################################################       

    
def show_discharged_patients(): 
    """used for displaying the patients that were discharged from the hospital, from the table PATIENTS_ADM_DIS"""
    print("\n###################################################################")
    print("SEARCH FOR DISCHARGED PATIENTS")                  #providing with different choices through which discharged patients can be searched on various grounds
    print("###################################################################")
    print("1. Discharged Today")
    print("2. Datewise")
    print("3. Patient ID-wise")
    print("4. Show All")
    choice=int(input("Enter choice : "))
    if choice==1:                                            #in case of looking up the patients that were discharged today
        sqlquery="select AdmID,P.RegID,PName,sex,Reason_of_admission,doctor_in_vigil,date_of_admission,date_of_discharge,ward_no,bed_no from PATIENTS_ADM_DIS P,REGISTERED_PATIENTS R where DATE_OF_DISCHARGE=curdate() and R.RegID=P.RegID"       #using curdate to get current date ,using two tables at the same time to  fetch required data by comparing RegID in both tables
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        

        for row in data:
            #using for loop to dispay records
            print("\nDISCHARGED PATIENTS")
            print("#"*50)
            print("DISCHARGE ID              : ",row[0],"\n","PATIENT ID                : ",row[1],"\n","NAME                      : ",row[2],"\n","SEX                       : ",row[3],"\n","REASON OF ADMISSION       : ",row[4],"\n","DOCTOR IN VIGIL           : ",row[5],"\n","DATE OF ADMISSION         : ",row[6],"\n","DATE OF DISCHARGE         : ",row[7],"\n","WARD                      : ",row[8],"\n","BED NUMBER                : ",row[9],sep='')
            print("#"*50,"\n")
    elif choice==2:
        inpdate=input("Enter date in YYYY-MM-DD : ")
        sqlquery="select AdmID,P.RegID,PName,sex,Reason_of_admission,doctor_in_vigil,date_of_admission,date_of_discharge,ward_no,bed_no from PATIENTS_ADM_DIS P,REGISTERED_PATIENTS R where DATE_OF_DISCHARGE='"+inpdate+"' and R.RegID=P.RegID"        #using two tables at the same time to  fetch required data by comparing RegID in both tables
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        count=mycur.rowcount                   
        if count==0:                                  #in case no records were fetched
            print("None were discharged on the given date")
        else:
            for row in data:
                print("\nDISCHARGED PATIENTS")
                print("#"*50)
                print("DISCHARGE ID              : ",row[0],"\n","PATIENT ID                : ",row[1],"\n","NAME                      : ",row[2],"\n","SEX                       : ",row[3],"\n","REASON OF ADMISSION       : ",row[4],"\n","DOCTOR IN VIGIL           : ",row[5],"\n","DATE OF ADMISSION         : ",row[6],"\n","DATE OF DISCHARGE         : ",row[7],"\n","WARD                      : ",row[8],"\n","BED NUMBER                : ",row[9],sep='')
                print("#"*50,"\n")
    elif choice==3:
        ques=input("Enter 'y' if the patient remembers the ID or else enter 'n' : ")         
        if ques=='y':
            pat_id=int(input("Enter Patient's ID : "))
        elif ques=='n':
            pat_id=search_id()                                 #calling search_id in case the person does not remember the ID
        sqlquery="select AdmID,P.RegID,PName,sex,Reason_of_admission,doctor_in_vigil,date_of_admission,date_of_discharge,ward_no,bed_no from PATIENTS_ADM_DIS P,REGISTERED_PATIENTS R where P.RegID="+str(pat_id)+" and R.RegID=P.RegID"       #using two tables at the same time to  fetch required data by comparing RegID in both tables
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        count=mycur.rowcount                #fetching  record number to check the validity of ID
        if count==0:
            print("\nInvalid Patient ID")
        else:
            for row in data:
                print("\nDISCHARGED PATIENTS")
                print("#"*50)
                print("DISCHARGE ID              : ",row[0],"\n","PATIENT ID                : ",row[1],"\n","NAME                      : ",row[2],"\n","SEX                       : ",row[3],"\n","REASON OF ADMISSION       : ",row[4],"\n","DOCTOR IN VIGIL           : ",row[5],"\n","DATE OF ADMISSION         : ",row[6],"\n","DATE OF DISCHARGE         : ",row[7],"\n","WARD                      : ",row[8],"\n","BED NUMBER                : ",row[9],sep='')
                print("#"*50,"\n")
    elif choice==4:
        sqlquery="select AdmID,P.RegID,PName,sex,GuardianName,GuardianRelation,GuardianContactNo,Reason_of_admission,date_of_admission,doctor_in_vigil,ward_no,bed_no from PATIENTS_ADM_DIS P,REGISTERED_PATIENTS R where R.RegID=P.RegID"     #using two tables at the same time to  fetch required data by comparing RegID in both tables 
        mycur.execute(sqlquery)
        data=mycur.fetchall()
        for row in data:
            print("\nDISCHARGED PATIENTS")
            print("#"*50)
            print("DISCHARGE ID              : ",row[0],"\n","PATIENT ID                : ",row[1],"\n","NAME                      : ",row[2],"\n","SEX                       : ",row[3],"\n","REASON OF ADMISSION       : ",row[4],"\n","DOCTOR IN VIGIL           : ",row[5],"\n","DATE OF ADMISSION         : ",row[6],"\n","DATE OF DISCHARGE         : ",row[7],"\n","WARD                      : ",row[8],"\n","BED NUMBER                : ",row[9],sep='')
            print("#"*50,"\n")
    else:
        print("\nInvalid choice.")               #in case user enters none of the choices that were displayed
    
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions

#############################################################################   
#############################################################################       
   
       
def wards_add():
    """used to add wards into the table WARDS"""
    global lststr                         #making the list of strings(Department names) global
    WN=input("Enter ward number in WN format (N is a number) : ")      #aking for ward number
    WN=WN[0].lower()+WN[1:]           #using string.lower fucntion to change the letter 'W' (eg : W1) into lower case as python is case sensitive but MySQL is not
    checktable="show tables"          #using this query to get names of the tables wich also contains the names of the wards
    mycur.execute(checktable)
    dataoftable=mycur.fetchall()
    
    for row in dataoftable:           #using for loop to get the tuples(containing table names) from the list dataoftable
        if WN in row:                 #checking whether the given ward already exists by comparing its name to all the table names internally
            print("\nWard ",WN," already exists!!!")     #if the same ward name is found then a message is displayed and the function returns nothing and goes back to the menu
            input("\nPress enter to continue...")
            return
    
    
    while True:                              #now displaying the ward type 
        print("#############################################################")
        print(" WARD TYPES")
        print("1. General Ward." )
        print("2. Cottage Ward.")
        print("3. ICU.")
        print("#############################################################")
        numward=int(input("\nEnter type of ward (choice number) : "))
        if numward==1:
            typeward='General'
            break
        elif numward==2:
            typeward='Cottage'
            break
        elif numward==3:
            typeward='ICU'
            break
        else:
            print("\n","Invalid choice.\n")                 #in case the user enters wrong number for the ward type then the loop is repeated
    print("\nSelect from the given below list of departments.")          #displaying different departments to assign the added ward to that department using lststr
    print("          ###############################")
    print("\t\t","   DEPARTMENTS")
    print("          ###############################")
    for k in range(len(lststr)):
        print("\t\t",k+1,".",lststr[k])       
    ch=int(input("\nEnter choice of department to assign this ward to : "))
    Dept=lststr[ch-1]                                                #using ch-1 because the choices displayed starts from 1 but the index of the list starts from 0
    Strnumbed=int(input("Enter no. of beds in this ward : "))
    sqlquery1="insert into WARDS values('"+WN+"','"+typeward+"','"+Dept+"',"+str(Strnumbed)+","+str(Strnumbed)+")"    #inserting the required information
    mycur.execute(sqlquery1)
    mycon.commit()  #making the changes permanent in the database
    
    
    sqlquery2="create table "+WN+"(Bed_Num char(5) primary key,RegID int);"    #simultaneously a table is created for that ward with different number of beds and availability
    mycur.execute(sqlquery2)
    mycon.commit()
    
    query3="insert into "+WN+"(Bed_Num) values"                   #now inserting the bed number using for loop till all the number of beds are covered
    stri=" "
    for i in range(1,Strnumbed+1):
        stri=stri+"('B"+str(i)+"'),"
        
    query3=query3+stri[0:len(stri)-1]  
                                            #concatenating query and using len(stri)-1 because the last "," is not supported by the SQL syntax
    mycur.execute(query3)
    mycon.commit()
    print("\nThe new ward",WN,"has successfully been added to the management system.")
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions

#############################################################################   
#############################################################################       

    
def show_wards():
    """used to display all the wards along with their several other information """
    query="select * from WARDS"
    mycur.execute(query)
    data=mycur.fetchall()                                #fetching all the data which is in the form of a list of tuples
    for row in data:
        #using for loop to display all the wards
        print("\n")
        print("    WARD INFORMATION")
        print("#"*30)
        print("WARD NAME      : ",row[0],"\n","WARD TYPE      : ",row[1],"\n","DEPARTMENT     : ",row[2],"\n","NUMBER OF BEDS : ",row[3],"\n","AVAILABLE BEDS : ",row[4],sep='')
        print("#"*30,"\n")
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions

#############################################################################   
#############################################################################       


def usersignup():
    """used to sign up new users to the database and help them enter into the management system"""
    print("+++++++++++++++++++++++++++++++++++++++\n")
    print("            SIGN UP PORTAL")
    print("+++++++++++++++++++++++++++++++++++++++\n")
    userid=input("Enter email ID (user ID) : ")
    password=input("Enter password : ")
    userlevel=input("Enter userlevel i.e Admin/Operator : ")                        #userlevel is important because it provides with two different kinds of access to the management system
    query="insert into USERS (USER_ID,PASSWORD,USER_LEVEL) values('"+userid+"','"+password+"','"+userlevel+"')"       #inserting the required infromation into the table USERS
    mycur.execute(query)
    mycon.commit()              #making the changes permanent in the database
    print("\nThe user is now is signed up.")
    input("\nPress enter to continue...")                #using input to wait for the user's further instructions
    
#############################################################################   
#############################################################################       


def login():
    
    """used to login into the management system and provide with different choices based on the type of user,i.e Admin or Operator"""
    print("####################################################################")
    print("                            SIGN IN                                      ")
    print("####################################################################\n")
    user=input("Enter your user ID (email) : ")                  #asking for ID and password to check the validity of the user
    password=input("Enter password : ")
    query="select * from USERS where USER_ID='"+user+"' and PASSWORD='"+password+"'"           #checking whether the provided information is correct or not
    mycur.execute(query)
    data=mycur.fetchall()
    count=mycur.rowcount
    
    if count==0:                      #in case no records are obtained,the user is denied for the access to the management system
        print("\n\nInvalid user")
        print("####################################################################")
        mycon.close()             #clean up the environment
    else:
        print("\n\nValid user")      #in case the user is valid then his/her userlevel is compared to provide with two different set of choices
        print("####################################################################")
        initialisation()             #calling initialisation to add the doctors along with their IDs into the dictionaries as soon as the program begins
        input("Press any key to enter into the management system...")
                
        userlevel=data[0][3]                    #here data is a list of tuple containing user level
        if userlevel=='Admin':                  #in case the user level is Admin then he/she would be allowed to access the administration system which contains information about the doctors
            while True:                         #using while loop to ask for choices infinite times until the user has asked for exiting  
                print("\n\n\n\n")
                print("                   WELCOME TO LIFELINE HOSPITAL")
                print("####################################################################")
                print("\n1. Patient's Management System.")
                print("2. Administration system.")
                print("3. Exit.","\n")
                print("####################################################################")
                initialchoice=int(input("Enter choice : "))
                if initialchoice==1:
                    choice=0
                    while choice!=13:                    #using while loop until the user has asked for  exiting
                        print("\n\n","                         MENU")
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print()
                        print("1.  Add Patient's details")
                        print("2.  Show Patient's Personal Details")
                        print("3.  Update patient's details.")
                        print("4.  Get an appointment.")
                        print("5.  Show appointments.")
                        print("6.  Add Patient's Diagnosis Information")
                        print("7.  Show Patient's Diagnosis Information")
                        print("8.  Admit a Patient")
                        print("9.  Show admitted patients.")
                        print("10. Discharge  a patient")
                        print("11. Show discharged patients.")
                        print("12. Show information about wards.")
                        print("13. Go back to the main menu")
                        print("14. Exit.")
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++","\n")
                        choice=int(input("Enter choice : "))                #functions are called according to the choice asked 
                        if choice==1:
                            add_patient()
                        elif choice==2:
                            show_pat_personal_details()
                        elif choice==3:
                            update_patient()
                        elif choice==4:
                            appointment()
                        elif choice==5:
                            show_appointments()
                        elif choice==6:
                            patient_diagnosis_info()    
                        elif choice==7:
                            show_patient_dia_info()                            
                        elif choice==8:                            
                            admit_patient()                            
                        elif choice==9:                            
                            show_admitted_patients()                                                        
                        elif choice==10:
                            discharge_patient()                            
                        elif choice==11:
                            show_discharged_patients()
                        elif choice==12:
                            show_wards()
                        elif choice==13:
                            print("\nThank you.")    #in case the choice is 13 to go back to the main menu the loop breaks as the condtion for the loop to run goes false
                        elif choice==14:
                            mycon.close()
                            print("\n###############################Thank you################################\n\n\n\n\n\n\n\n\n\n")      #using sys.exit( ) to totally exit out of the program and simultaneously displaying a message of thank you                      
                            sys.exit()
                        else:
                            print("\nInvalid choice,please try again.")
                            input("\nPress enter to continue.....")
                            
                elif initialchoice==2:                   #choice to enter into the Administration system 
                    choice=0
                    while choice!=8:
                        print("\n")                  
                        print("                           MENU")      #these choices are only accessible to the Admins
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++","\n")
                        print("              1. Add doctor's details ")
                        print("              2. View Information About Doctors")
                        print("              3. Update doctor's personal details.")
                        print("              4. Delete docotor's records.")
                        print("              5. Add a new ward.")
                        print("              6. Show Wards.")
                        print("              7. Sign up a new user.")
                        print("              8. Go back to the main menu.")
                        print("              9. Exit\n")
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++","\n")
                        choice=int(input("Enter choice number according to the above menu : "))
                        if choice==1:
                            add_doctor()
                        elif choice==2:
                            show_doc_details()
                        elif choice==3:
                            update_doc_detail()
                        elif choice==4:
                            delete_doctor()
                        elif choice==5:
                            wards_add()
                        elif choice==6:
                            show_wards()
                        elif choice==7:
                            usersignup()
                        elif choice==8:
                            print("Thank you.")
                        elif choice==9:
                            mycon.close()
                            print("\n###############################Thank you################################\n\n\n\n\n\n\n\n\n\n")      #using sys.exit( ) to totally exit out of the program and simultaneously displaying a message of thank you                      
                            sys.exit()
                        else:
                            print("\n","Invalid choice,try again.","\n")
                            input("Press enter to continue....")
                        

                elif initialchoice==3:            #in case the user wants to exit as soon as the main menu appears
                    print("\n\n#####################################################################\n")
                    print("Thank you ",sep='')
                    print("\n######################################################################")
                    mycon.close()      #clean up the environment
                    break
                else:
                    print("\n","Invalid choice, please try again.")     #in case the choice is not from the menu displayed then the loop is continued again
                    input("Press enter to continue....")         #waiting for user to continue using input 
            
        elif userlevel=='Operator':              #in case the user level is Operator then he/she is provided with an access to just the Patient Management System
            while True:                          #using this loop infinite times until the user asks for exiting 
                print("\n\n\n\n")
                print("                   WELCOME TO LIFELINE HOSPITAL")
                print("####################################################################")
                print("\n1. Patient's Management System.")
                print("2. Exit.","\n")
                print("####################################################################")
                initialchoice=int(input("Enter choice : "))
                if initialchoice==1:
                    choice=0
                    while choice!=13:                    #using while loop until the user has asked for  exiting
                        print("\n\n","                         MENU")
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print()
                        print("1.  Add Patient's details")
                        print("2.  Show Patient's Personal Details")
                        print("3.  Update patient's details.")
                        print("4.  Get an appointment.")
                        print("5.  Show appointments.")
                        print("6.  Add Patient's Diagnosis Information")
                        print("7.  Show Patient's Diagnosis Information")
                        print("8.  Admit a Patient")
                        print("9.  Show admitted patients.")
                        print("10. Discharge  a patient")
                        print("11. Show discharged patients.")
                        print("12. Show information about wards.")
                        print("13. Go back to the main menu")
                        print("14. Exit.")
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++","\n")
                        choice=int(input("Enter choice : "))                #functions are called according to the choice asked 
                        if choice==1:
                            add_patient()
                        elif choice==2:
                            show_pat_personal_details()
                        elif choice==3:
                            update_patient()
                        elif choice==4:
                            appointment()
                        elif choice==5:
                            show_appointments()
                        elif choice==6:
                            patient_diagnosis_info()    
                        elif choice==7:
                            show_patient_dia_info()                            
                        elif choice==8:                            
                            admit_patient()                            
                        elif choice==9:                            
                            show_admitted_patients()                                                        
                        elif choice==10:
                            discharge_patient()                            
                        elif choice==11:
                            show_discharged_patients()
                        elif choice==12:
                            show_wards()
                        elif choice==13:
                            print("\nThank you.")    #in case the choice is 13 to go back to the main menu the loop breaks as the condtion for the loop to run goes false
                        elif choice==14:
                            mycon.close()
                            print("\n###############################Thank you################################\n\n\n\n\n\n\n\n\n\n")      #using sys.exit( ) to totally exit out of the program and simultaneously displaying a message of thank you                      
                            sys.exit()
                        else:
                            print("\nInvalid choice,please try again.")
                            input("\nPress enter to continue.....")
                    
                elif initialchoice==2:
                    print("\n\n#####################################################################\n")
                    print("Thank you ",sep='')
                    print("\n######################################################################")
                    mycon.close()      #clean up the environment
                    break              #breaking the loop in case the user wants to exit
                           
                else:
                    print("\n","Invalid choice, please try again.")
                    input("\nPress enter to continue.....")
        else:
            print("Cannot enter management system.")            
            input("\nPress enter to continue.....")           #in case the user enters none of the choices that were displayed in the menu,the loop continues
            



#############################################################################   
#############################################################################       


#__main__
login()       #calling login to provide access to the management system 

    







     
