from tkinter import*
import random
import time
import datetime

payroll = Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management Systems")

def Exit():
    payroll.destroy()

def Reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    CityWeighting.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    Deductions.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtherPaymentDue.set("")
    
def PayRef():
    PayDate.set(time.strftime("%d/%m/%y"))
    Refpay=random.randint(20000,709467)
    Refpaid=("PR" + str(Refpay))
    Reference.set(Refpaid)
    
    NIpay=random.randint(4200,9467)
    NIpaid=("NI" + str(NIpay))
    NINumber.set(NIpaid)
    
def PayPeriod():
    i=datetime.datetime.now()
    TaxPeriod.set(i.month)

    NIcode=random.randint(1400,9000)
    NIco=("NICode" + str(NIcode))
    NICode.set(NIco)

def MonthlySalary():
    BS=float(BasicSalary.get())
    CW=float(CityWeighting.get())
    OT=float(OverTime.get())
    
    GPay=BS+CW+OT
    
    MTax=((BS+CW+OT)*0.18)
    TTax="Rs.",str('%.2f'%(MTax))
    Tax.set(TTax)

    MPension=((BS+CW+OT)*0.03)
    TPension="Rs.",str('%.2f'%(MPension))
    Pension.set(TPension)

    MStudentLoan=((BS+CW+OT)*0.013)
    TStudentLoan="Rs.",str('%.2f'%(MStudentLoan))
    StudentLoan.set(TStudentLoan)

    MNIPayment=((BS+CW+OT)*0.011)
    TNIPayment="Rs.",str('%.2f'%(MStudentLoan))
    NIPayment.set(TNIPayment)

    Deduct=MTax+MPension+MStudentLoan+MNIPayment
    DeductPayment="Rs.",str('%.2f'%(Deduct))
    Deductions.set(DeductPayment)
    
    Gross_Pay="Rs.",str('%.2f'%(BS+CW+OT))
    GrossPay.set(Gross_Pay)

    NPay="Rs.",str('%.2f'%(GPay-Deduct))
    NetPay.set(NPay)

    TaxablePay.set(TTax)
    PensionablePay.set(TPension)
    OtherPaymentDue.set("0.00")


EmployeeName=StringVar()
Address=StringVar()
Reference=StringVar()
EmployerName=StringVar()
CityWeighting=StringVar()
BasicSalary=StringVar()
OverTime=StringVar()
GrossPay=StringVar()
NetPay=StringVar()
Tax=StringVar()
Pension=StringVar()
StudentLoan=StringVar()
NIPayment=StringVar()
Deductions=StringVar()
PostCode=StringVar()
Gender=StringVar()
PayDate=StringVar()
TaxPeriod=StringVar()
NINumber=StringVar()
NICode=StringVar()
TaxablePay=StringVar()
PensionablePay=StringVar()
OtherPaymentDue=StringVar()

Tops=Frame(payroll, width=1350, height=50,bd=16,relief="raise")
Tops.pack(side=TOP)
LF=Frame(payroll, width=700, height=650,bd=16,relief="raise")
LF.pack(side=LEFT)
RF=Frame(payroll, width=600, height=650,bd=16,relief="raise")
RF.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial' ,50, 'bold'), text="Payroll Management Systems" ,fg="Steel blue",bd=10, anchor='w')
lblInfo.grid(row=0,column=0)

LeftInsideLF=Frame(LF, width=700, height=100,bd=8,relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=325, height=400,bd=8,relief="raise")
LeftInsideLFLF.pack(side=LEFT)
LeftInsideRFRF=Frame(LF, width=325, height=400,bd=8,relief="raise")
LeftInsideRFRF.pack(side=RIGHT)

RightInsideLF=Frame(RF, width=600, height=200,bd=8,relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=300, height=400,bd=8,relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300, height=400,bd=8,relief="raise")
RightInsideRFRF.pack(side=RIGHT)
#==#Left side
lblEmployeeName=Label(LeftInsideLF, font=('arial' ,12, 'bold'),text="Employee Name" ,fg="Steel blue",bd=10)
lblEmployeeName.grid(row=0,column=0)
txtEmployeeName=Entry(LeftInsideLF, font=('arial' ,12, 'bold'),bd=20, width=54,bg="powder blue", justify ='left',textvariable=EmployeeName)                                        
txtEmployeeName.grid(row=0,column=1)

lblAddress=Label(LeftInsideLF, font=('arial' ,12, 'bold'), text="Address" ,fg="Steel blue",bd=10)                             
lblAddress.grid(row=1,column=0)
txtAddress=Entry(LeftInsideLF, font=('arial' ,12, 'bold'),bd=20, width=54,bg="powder blue", justify ='left',textvariable=Address)                            
txtAddress.grid(row=1,column=1)

lblReference=Label(LeftInsideLF, font=('arial' ,12, 'bold'),text="Reference" ,fg="Steel blue",bd=10)
lblReference.grid(row=2,column=0)
txtReference=Entry(LeftInsideLF, font=('arial' ,12, 'bold'),bd=20, width=54,bg="powder blue", justify ='left',textvariable=Reference)                                        
txtReference.grid(row=2,column=1)

lblEmployerName=Label(LeftInsideLF, font=('arial' ,12, 'bold'), text="Employer Name" ,fg="Steel blue",bd=10)                             
lblEmployerName.grid(row=3,column=0)
txtEmployerName=Entry(LeftInsideLF, font=('arial' ,12, 'bold'),bd=20, width=54,bg="powder blue", justify ='left',textvariable=EmployerName)                            
txtEmployerName.grid(row=3,column=1)

#==#Under Left side
lblCity=Label(LeftInsideLFLF, font=('arial' ,12, 'bold'),text="City Weighting" ,fg="Steel blue",bd=10)
lblCity.grid(row=0,column=0)
txtCity=Entry(LeftInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=CityWeighting)                                        
txtCity.grid(row=0,column=1)
#----
lblBasicSalary=Label(LeftInsideLFLF, font=('arial' ,12, 'bold'),text="Basic Salary" ,fg="Steel blue",bd=10)
lblBasicSalary.grid(row=1,column=0)
txtBasicSalary=Entry(LeftInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=BasicSalary)                                        
txtBasicSalary.grid(row=1,column=1)
#----
lblOverTime=Label(LeftInsideLFLF, font=('arial' ,12, 'bold'),text="Over Time" ,fg="Steel blue",bd=10)
lblOverTime.grid(row=2,column=0)
txtOverTime=Entry(LeftInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=OverTime)                                        
txtOverTime.grid(row=2,column=1)
#----
lblGrossPay=Label(LeftInsideLFLF, font=('arial' ,12, 'bold'),text="Gross Pay" ,fg="Steel blue",bd=10)
lblGrossPay.grid(row=3,column=0)
txtGrossPay=Entry(LeftInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=GrossPay)                                        
txtGrossPay.grid(row=3,column=1)
#----
lblNetPay=Label(LeftInsideLFLF, font=('arial' ,12, 'bold'),text="Net Pay" ,fg="Steel blue",bd=10)
lblNetPay.grid(row=4,column=0)
txtNetPay=Entry(LeftInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=NetPay)                                        
txtNetPay.grid(row=4,column=1)

#----#
lblTax=Label(LeftInsideRFRF, font=('arial' ,12, 'bold'),text="Tax" ,fg="Steel blue",bd=10)
lblTax.grid(row=0,column=0)
txtTax=Entry(LeftInsideRFRF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=Tax)                                        
txtTax.grid(row=0,column=1)
#----
lblPension=Label(LeftInsideRFRF, font=('arial' ,12, 'bold'),text="Pension" ,fg="Steel blue",bd=10)
lblPension.grid(row=1,column=0)
txtPension=Entry(LeftInsideRFRF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=Pension)                                        
txtPension.grid(row=1,column=1)
#----
lblStudentLoan=Label(LeftInsideRFRF, font=('arial' ,12, 'bold'),text="Student Loan" ,fg="Steel blue",bd=10)
lblStudentLoan.grid(row=2,column=0)
txtStudentLoan=Entry(LeftInsideRFRF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=StudentLoan)                                        
txtStudentLoan.grid(row=2,column=1)
#----
lblNIPayment=Label(LeftInsideRFRF, font=('arial' ,12, 'bold'),text="NI Payment" ,fg="Steel blue",bd=10)
lblNIPayment.grid(row=3,column=0)
txtNIPayment=Entry(LeftInsideRFRF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=NIPayment)                                        
txtNIPayment.grid(row=3,column=1)
#----
lblDeductions=Label(LeftInsideRFRF, font=('arial' ,12, 'bold'),text="Deductions" ,fg="Steel blue",bd=10)
lblDeductions.grid(row=4,column=0)
txtDeductions=Entry(LeftInsideRFRF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=Deductions)                                        
txtDeductions.grid(row=4,column=1)

#==#Right side
lblPostCode=Label(RightInsideLF, font=('arial' ,12, 'bold'),text="PostCode" ,fg="Steel blue",bd=10)
lblPostCode.grid(row=0,column=0)
txtPostCode=Entry(RightInsideLF, font=('arial' ,12, 'bold'),bd=20, width=48,bg="powder blue", justify ='left',textvariable=PostCode)                                        
txtPostCode.grid(row=0,column=1)

lblGender=Label(RightInsideLF, font=('arial' ,12, 'bold'), text="Gender" ,fg="Steel blue",bd=10)                             
lblGender.grid(row=1,column=0)
txtGender=Entry(RightInsideLF, font=('arial' ,12, 'bold'),bd=20, width=48,bg="powder blue", justify ='left',textvariable=Gender)                            
txtGender.grid(row=1,column=1)

#==#Under Right side
lblPayDate=Label(RightInsideLFLF, font=('arial' ,12, 'bold'),text="Pay Date" ,fg="Steel blue",bd=10)
lblPayDate.grid(row=0,column=0)
txtPayDate=Entry(RightInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=PayDate)                                        
txtPayDate.grid(row=0,column=1)
#----
lblTaxPeriod=Label(RightInsideLFLF, font=('arial' ,12, 'bold'),text="Tax Period" ,fg="Steel blue",bd=10)
lblTaxPeriod.grid(row=1,column=0)
txtTaxPeriod=Entry(RightInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=TaxPeriod)                                        
txtTaxPeriod.grid(row=1,column=1)
#----
lblNINumber=Label(RightInsideLFLF, font=('arial' ,12, 'bold'),text="NI Number" ,fg="Steel blue",bd=10)
lblNINumber.grid(row=2,column=0)
txtNINumber=Entry(RightInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=NINumber)                                        
txtNINumber.grid(row=2,column=1)
#----
lblNICode=Label(RightInsideLFLF, font=('arial' ,12, 'bold'),text="NI Code" ,fg="Steel blue",bd=10)
lblNICode.grid(row=3,column=0)
txtNICode=Entry(RightInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=NICode)                                        
txtNICode.grid(row=3,column=1)
#----
lblTaxablePay=Label(RightInsideLFLF, font=('arial' ,12, 'bold'),text="Taxable Pay" ,fg="Steel blue",bd=10)
lblTaxablePay.grid(row=4,column=0)
txtTaxablePay=Entry(RightInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=TaxablePay)                                        
txtTaxablePay.grid(row=4,column=1)
#----
lblPensionablePay=Label(RightInsideLFLF, font=('arial' ,12, 'bold'),text="Pensionable Pay" ,fg="Steel blue",bd=10)
lblPensionablePay.grid(row=5,column=0)
txtPensionablePay=Entry(RightInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=PensionablePay)                                        
txtPensionablePay.grid(row=5,column=1)
#----
lblOtherPaymentDue=Label(RightInsideLFLF, font=('arial' ,12, 'bold'),text="Other Payment Due" ,fg="Steel blue",bd=10)
lblOtherPaymentDue.grid(row=6,column=0)
txtOtherPaymentDue=Entry(RightInsideLFLF, font=('arial' ,12, 'bold'),bd=10, width=18,bg="powder blue", justify ='left',textvariable=OtherPaymentDue)                                        
txtOtherPaymentDue.grid(row=6,column=1)

#----#
btnWagePayment=Button(RightInsideRFRF,padx=8,bd=8,fg="black", font=('arial' ,16, 'bold'),width=14,text="Wage Payment",bg="sky blue",command=MonthlySalary).grid(row=0,column=0)
btnResetSystem=Button(RightInsideRFRF,padx=8,bd=8,fg="black", font=('arial' ,16, 'bold'),width=14,text="Reset System",bg="sky blue",command=Reset).grid(row=1,column=0)
btnPayReference=Button(RightInsideRFRF,padx=8,bd=8,fg="black", font=('arial' ,16, 'bold'),width=14,text="Pay Reference",bg="sky blue",command=PayRef).grid(row=2,column=0)
btnPayCode=Button(RightInsideRFRF,padx=8,bd=8,fg="black", font=('arial' ,16, 'bold'),width=14,text="Pay Code",bg="sky blue",command=PayPeriod).grid(row=3,column=0)
btnExit=Button(RightInsideRFRF,padx=8,bd=8,fg="black", font=('arial' ,16, 'bold'),width=14,text="Exit",bg="sky blue",command=Exit).grid(row=4,column=0)


payroll.mainloop()
