from tkinter import *
import csv
import os
from tkinter import messagebox 
import math
import sys
from Search import search
root=Tk()
root.geometry("700x350")
root.title("Save result")
def ext():
    root.destroy()
def search_():
    x=search()
 
def submit():
    
    path="result.csv"
    
    if os.path.exists(path):
        try:
        
             n=name_e.get()
             c=class_e.get()
             r=roll_e.get()
             f=father_e.get()
             m=mob_e.get()
    
             o1=int(Omarks_1.get())
             o2=int(Omarks_2.get())
             o3=int(Omarks_3.get())
             o4=int(Omarks_4.get())
             o5=int(Omarks_5.get())

    
             m1=int(Mmarks_1.get())
             m2=int(Mmarks_2.get())
             m3=int(Mmarks_3.get())
             m4=int(Mmarks_4.get())
             m5=int(Mmarks_5.get())
             
             
             total=o1+o2+o3+o4+o5
             per=total*100/(m1+m2+m3+m4+m5)
             per=math.ceil(per)
             
             if per>=90:
                g="A+"
             elif per>=80:
                g="A"
             elif per>=70:
                g="B+"
             elif per>=60:
                g="B"
             elif per>=50:
                g="C+"
             elif per>=40:
                g="C"
             else:
                g="Fail"
             total_e=Label(root,text=total,font=("Calibri",14)).grid(row=5,column=7)
             per_e=Label(root,text=per,font=("Calibri",14)).grid(row=6,column=7)
             grade_e=Label(root,text=g,font=("Calibri",14)).grid(row=7,column=7)

             rd=open("result.csv","a+",newline="")
             wr=csv.writer(rd)
             wr.writerow([n,c,r,f,m,o1,o2,o3,o4,o5,total,per,g])
             rd.close()
        except:
             messagebox.showinfo("showinfo", "Sorry wrong data enter in marks column or empty column")
    else:
        rd=open("result.csv","w",newline="")
        wr=csv.writer(rd)
        wr.writerow(["Name","Class","Roll No","Father Name","Mobile","English","Hindi","Science","Mathmmatics","Social science","Total","per","Grade"])
        rd.close()
        submit()

    
    

name_l=Label(root,text="Name",font=("Calibri",14))
class_l=Label(root,text="Class",font=("Calibri",14))
roll_l=Label(root,text="Roll_no",font=("Calibri",14))
father_l=Label(root,text="Father Name",font=("Calibri",14))
mob_l=Label(root,text="Mobile",font=("Calibri",14))

name_e=Entry(root)
class_e=Entry(root)
roll_e=Entry(root)
father_e=Entry(root)
mob_e=Entry(root)


name_l.grid(row=0,column=0)
class_l.grid(row=1,column=0)
roll_l.grid(row=2,column=0)
father_l.grid(row=0,column=2)
mob_l.grid(row=1,column=2)


name_e.grid(row=0,column=1)
class_e.grid(row=1,column=1)
roll_e.grid(row=2,column=1)
father_e.grid(row=0,column=3)
mob_e.grid(row=1,column=3)


SrNo_l=Label(root,text="Sr.No.",font=("Calibri",14))
Subject_l=Label(root,text="Subject",font=("Calibri",14))
Marks_obt_l=Label(root,text="Marks_obt",font=("Calibri",14))
marks_max_l=Label(root,text="Max_marks",font=("Calibri",14))
empty=Label(root,text="").grid(row=3,column=0)
empty=Label(root,text="").grid(row=4,column=0)

SrNo_l.grid(row=5,column=0)
Subject_l.grid(row=5,column=1)
Marks_obt_l.grid(row=5,column=2)
marks_max_l.grid(row=5,column=3)

sr1=Label(root,text="1",font=("Calibri",14))
sr2=Label(root,text="2",font=("Calibri",14))
sr3=Label(root,text="3",font=("Calibri",14))
sr4=Label(root,text="4",font=("Calibri",14))
sr5=Label(root,text="5",font=("Calibri",14))    


sr1.grid(row=6,column=0)
sr2.grid(row=7,column=0)
sr3.grid(row=8,column=0)
sr4.grid(row=9,column=0)
sr5.grid(row=10,column=0)


Subject_1=Label(root,text="English",font=("Calibri",14))
Subject_2=Label(root,text="Hindi",font=("Calibri",14))
Subject_3=Label(root,text="Science",font=("Calibri",14))
Subject_4=Label(root,text="Mathmatics",font=("Calibri",14))
Subject_5=Label(root,text="Social Science",font=("Calibri",14))

Subject_1.grid(row=6,column=1)
Subject_2.grid(row=7,column=1)
Subject_3.grid(row=8,column=1)
Subject_4.grid(row=9,column=1)
Subject_5.grid(row=10,column=1)


Omarks_1=Entry(root,width=10)
Omarks_2=Entry(root,width=10)
Omarks_3=Entry(root,width=10)
Omarks_4=Entry(root,width=10)
Omarks_5=Entry(root,width=10)

Omarks_1.grid(row=6,column=2)
Omarks_2.grid(row=7,column=2)
Omarks_3.grid(row=8,column=2)
Omarks_4.grid(row=9,column=2)
Omarks_5.grid(row=10,column=2)


Mmarks_1=Entry(root,width=10)
Mmarks_2=Entry(root,width=10)
Mmarks_3=Entry(root,width=10)
Mmarks_4=Entry(root,width=10)
Mmarks_5=Entry(root,width=10)

Mmarks_1.grid(row=6,column=3)
Mmarks_2.grid(row=7,column=3)
Mmarks_3.grid(row=8,column=3)
Mmarks_4.grid(row=9,column=3)
Mmarks_5.grid(row=10,column=3)





total=Label(root,text="Total",font=("Calibri",14)).grid(row=5,column=6)


per_=Label(root,text="Percentage",font=("Calibri",14)).grid(row=6,column=6)


grade=Label(root,text="Grade",font=("Calibri",14)).grid(row=7,column=6)



empty=Label(root,text="").grid(row=8,column=6)
save=Button(root,text="Save Info",width=8,bg="white")
save.grid(row=9,column=6)

upload=Button(root,text="Upload",width=8,bg="white",command=lambda:submit())
upload.grid(row=10,column=6)

upload=Button(root,text="Exit",width=8,bg="red",fg="white",command=lambda:ext())
upload.grid(row=9,column=7)


upload=Button(root,text="Search",width=8,bg="Blue",fg="white",command=lambda:search_())
upload.grid(row=10,column=7)
root.mainloop()
