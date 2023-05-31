from market import db, models, forms
import base64


#============================================ Register Student=========================================

def createFamilyID(form):

    form.familyID.data = forms.StudentForm().famID()
    form.familyID.render_kw = {'readonly':True}
    form.sID.data = forms.StudentForm().stID()
    form.sID.render_kw = {'readonly':True}

    # form.sFirstName.data= '1231231'
    # form.sMiddleName.data= '1231231'
    # form.sLastName.data= '1231231'
    # form.sCell_No.data= '1231231'
    # form.sEmail.data= '1231231'

    # #   Address Part
    # form.addressLine1.data= '1231231'
    # form.addressLine2.data= '1231231'
    # form.city.data= '1231231'
    # form.state.data= '1231231'
    # form.zipCode.data= '1231231'
    
    # #   Father
    # form.fatherFirstName.data= '1231231'
    # form.fatherMiddleName.data= '1231231'
    # form.fatherLastName.data= '1231231'
    # form.FCell_No.data= '1231231'
    # form.FEmail.data= '1231231'

    # #   Mother
    # form.motherFirstName.data= '1231231'
    # form.motherMiddleName.data= '1231231'
    # form.motherLastName.data= '1231231'    
    # form.MCell_No.data= '1231231'
    # form.MEmail.data = '1231231'
    
    return form

def renderStudent(form,famID,stdID):

    std = models.Student.query.filter_by(Family_ID = famID).first()

    if std:
        father = models.Person.query.filter_by(Person_ID = std.Father).first()
        mother = models.Person.query.filter_by(Person_ID = std.Mother).first()
        address = models.Address.query.filter_by(
            id = models.Person.query.filter_by(Person_ID = std.Student_ID).first().Address
        ).first()

        form.familyID.data = std.Family_ID
        form.fatherFirstName.data = father.First_Name
        form.fatherMiddleName.data = father.Middle_Name
        form.fatherLastName.data  = father.Last_Name
        form.fDob.data = father.Date_Of_Birth
        form.FCell_No.data = father.Cell_No
        form.FEmail.data = father.Email

        form.motherFirstName.data = mother.First_Name
        form.motherMiddleName.data = mother.Middle_Name
        form.motherLastName.data  = mother.Last_Name
        form.mDob.data = mother.Date_Of_Birth
        form.MCell_No.data = mother.Cell_No
        form.MEmail.data = mother.Email

        form.addressLine1.data = address.Address_Line_1
        form.addressLine2.data = address.Address_Line_2
        form.city.data = address.City
        form.state.data = address.State
        form.zipCode.data = address.Zip_Code

        if stdID:
            stdPerson = models.Person.query.filter_by(Person_ID = std.Student_ID).first()
            form.sID.data = std.Student_ID            
            form.sFirstName.data = stdPerson.First_Name
            form.sFirstName.render_kw = {'readonly':True}
            form.sMiddleName.data = stdPerson.Middle_Name
            form.sMiddleName.render_kw = {'readonly':True}
            form.sLastName.data = stdPerson.Last_Name
            form.sLastName.render_kw = {'readonly':True}
            form.gender.data = stdPerson.Gender
            form.gender.data = {'readonly':True}
            # form.dob.data = stdPerson.Date_Of_Birth
            # form.dob.data = {'readonly':True}
            form.sEmail.data = stdPerson.Email
            form.sEmail.render_kw = {'readonly':True}
            form.familyID.render_kw = {'readonly':True}
            form.fatherFirstName.render_kw = {'readonly':True}
            form.fatherMiddleName.render_kw = {'readonly':True}
            form.fatherLastName.render_kw  = {'readonly':True}
            form.fDob.render_kw = {'readonly':True}
            form.FCell_No.render_kw = {'readonly':True}
            form.FEmail.render_kw = {'readonly':True}

            form.motherFirstName.render_kw = {'readonly':True}
            form.motherMiddleName.render_kw = {'readonly':True}
            form.motherLastName.render_kw  = {'readonly':True}
            form.mDob.render_kw = {'readonly':True}
            form.MCell_No.render_kw = {'readonly':True}
            form.MEmail.render_kw = {'readonly':True}

            form.addressLine1.render_kw = {'readonly':True}
            form.addressLine2.render_kw = {'readonly':True}
            form.city.render_kw = {'readonly':True}
            form.state.render_kw = {'readonly':True}
            form.zipCode.render_kw = {'readonly':True}

            image = std.img

            encoded_image = base64.b64encode(image).decode('utf-8')

            # image = models.Student.query.filter_by(Student_ID = 'std10001').first().img            
            
            return form, encoded_image

        return form

    else:
        return False
    

def createStudent(form, file):

    std = models.Student.query.filter_by(Family_ID = form.familyID.data).first()

    if not std:
        # ================== Creating Address =====================
        address = models.Address(
            Address_Line_1 = form.addressLine1.data,
            Address_Line_2 = form.addressLine2.data,
            City = form.city.data,
            State = form.state.data,
            Zip_Code = form.zipCode.data
        )

        db.session.add(address)
        db.session.commit()
        # try:
        #     db.session.commit()
        # except:
        #     db.session.rollback()
        #     message = 'An Error Occured while saving Address data'
        #     # flash('An Error Occured while saving Address data', category = 'danger')
        #     return message

        ad1 = models.Address.query.filter_by(
            Address_Line_1 = form.addressLine1.data,
            Address_Line_2 = form.addressLine2.data,
            City = form.city.data,
            State = form.state.data,
            Zip_Code = form.zipCode.data
        ).first()

        # ================== Creating Person as Father =====================
        fPerson = models.Person(
            Person_ID = forms.StudentForm().fatherID(),
            First_Name = form.fatherFirstName.data,
            Middle_Name = form.fatherMiddleName.data,
            Last_Name = form.fatherLastName.data,
            Cell_No = form.FCell_No.data,
            Email = form.FEmail.data,
            Date_Of_Birth = form.fDob.data,
            Gender = 'Male',
            Address = ad1.id
        )

        db.session.add(fPerson)
        db.session.commit()
        # try:
        #     db.session.commit()
        # except:
        #     db.session.rollback()            
        #     message = 'An Error Occured while saving Father data'            
        #     return message

        # ================== Creating Person as Mother =====================
        mPerson = models.Person(
            Person_ID = forms.StudentForm().motherID(),
            First_Name = form.motherFirstName.data,
            Middle_Name = form.motherMiddleName.data,
            Last_Name = form.motherLastName.data,
            Cell_No = form.MCell_No.data,
            Email = form.MEmail.data,
            Date_Of_Birth = form.mDob.data,
            Gender = 'Female',
            Address = ad1.id
        )

        db.session.add(mPerson)
        db.session.commit()
        # try:
        #     db.session.commit()
        # except:
        #     db.session.rollback()
        #     message = 'An Error Occured while saving Mother data'
        #     return message

        # IDS
        fatherID = fPerson.Person_ID
        motherID = mPerson.Person_ID
        addressID = ad1.id
    else:
        fatherID = std.Father
        motherID = std.Mother
        addressID = std.Address

    # ================== Creating Person as Student =====================

    sPerson = models.Person(
        Person_ID = form.sID.data,
        First_Name = form.sFirstName.data,
        Middle_Name = form.sMiddleName.data,            
        Last_Name = form.sLastName.data,
        Cell_No = form.sCell_No.data,
        Email = form.sEmail.data,
        Date_Of_Birth = form.dob.data,
        Gender = form.gender.data,
        Address = addressID
    )

    # ================== Creating Student =====================    

    student = models.Student(
        img = file.read(),
        Family_ID = form.familyID.data,
        Student_ID = form.sID.data,
        Father = fatherID,
        Mother = motherID
    )

    db.session.add(sPerson)
    db.session.add(student)
    db.session.commit()
    # try:
    #     db.session.commit()
    # except:
    #     db.session.rollback()
    #     message = 'An Error Occured while saving Student data'
    #     return message

    return 'Student Registered Successfully!!'


# ==================================================== End ==============================================================

# =======================================================================================================================

def getStudent():

    items = db.engine.execute('''select st.Student_ID, st.Family_ID,
                         p1.First_Name || " " || p1.Middle_Name || " " || p1.Last_Name as Name,
                         p2.First_Name || " " || p2.Middle_Name || " " || p2.Last_Name as Father_Name,
                         p3.First_Name || " " || p3.Middle_Name || " " || p3.Last_Name as Mother_Name,
                         p1.Date_Of_Birth, p1.Gender,
                         a.Address_Line_1 || " " || a.Address_Line_2 || " " || a.City || " " ||
                         a.State || " " || a.Zip_Code as Address from student st join Person p1
                         on p1.Person_ID = st.Student_ID join Person p2 on p2.Person_ID = st.Father
                         join Person p3 on p3.Person_ID = st.Mother join Address a on a.id = p1.address''')

    cols = list(items.keys())
    items = list(items)

    return items, cols

#=======================================================================================================================
#                                                    Attendance 
#=======================================================================================================================

def validateCourseAndStudent(course,grade):

    crse = models.Course.query.filter_by(Name = course, Grade = grade).first()

    if not crse:
        return False
    else:
        
        # studentCourse = Student_Course.query.filter_by(Course = crse.Course_ID, Active = 1)

        items = db.engine.execute(f'''select st.Student_ID,
                             p1.First_Name || " " || p1.Middle_Name || " " || p1.Last_Name as Student_Name
                             from Student st join Person p1 on p1.Person_ID = st.Student_ID join Student__Course
                             sc on sc.Student = st.Student_ID and sc.Course = "{crse.Course_ID}" and sc.Active = 1''')
        cols = list(items.keys())
        items = list(items)
        li = [items,cols]
        return li


def checkStudent():

    items = db.engine.execute(f'''select st.Student_ID,
                            p1.First_Name || " " || p1.Middle_Name || " " || p1.Last_Name as Student_Name
                            from Student st join Person p1 on p1.Person_ID = st.Student_ID''')
    cols = list(items.keys())
    items = list(items)
    li = [items,cols]

    return li

def doAttendance(request, course, grade):

    from datetime import date

    attendance_data = request.form.to_dict(flat=False)
    attendance = {}
    comments = {}
    for key, value in attendance_data.items():
        if key.startswith('attendance['):
            roll_no = key.split('attendance[')[1][:-1]
            attendance[roll_no] = value[0]
            pass
        if key.startswith('comments['):
            roll_no = key.split('comments[')[1][:-1]
            comments[roll_no] = value[0]
            pass
    # print(attendance, comments)

    # print(attendance.keys())

    for std in attendance.keys():

        attFlag = 1 if attendance[std] == 'present' else 0

        stdA = models.Student_Attendance.query.filter_by(
            Date_Added = date.today(),
            Student = std, Course = course).first()

        if models.Student_Attendance.query.filter_by(
            Date_Added = date.today(),
            Student = std, Course = course, 
            Attendance = attFlag).first():
            continue

        elif stdA:
            stdA.Attendance = attFlag
            db.session.add(stdA)
        
        else:
            studentCourse = models.Student_Attendance(
                                Student = std,
                                Course = course,
                                Attendance = attFlag,
                                Date_Added = date.today(),
                                Comments = comments[std]
                            )
            db.session.add(studentCourse)
    
   

    try:
        db.session.commit()
        return True
    except:        
        db.session.rollback()
        return False