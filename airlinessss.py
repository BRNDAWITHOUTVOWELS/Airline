import pickle
import os

def deets():
    details=[]
    while True:
        fno=int(input("enter flight number:"))
        fname=input("enter flight name:")
        timings=input("enter timings:")
        source=input("enter source:")
        dest=input("enter destination:")
        numseat=int(input('enter total no of seats available:'))
        avail=int(input("enter available seats:"))
        r=int(input("enter no of reserved seats:"))
        cost=int(input("enter cost of flight:"))
        data=[fno,fname,timings,source,dest,numseat,avail,r,cost]
        details.append(data)
        ch=input("do you wish to add more?")
        if ch=='N'or ch=='n':
            break
    f=open("flight",'wb')
    pickle.dump(details,f)
    print("written details")
    f.close()




def show():
    f=open("flight",'rb')
    fdeet=pickle.load(f)
    print("FLIGHTNUMBER     FLIGHTNAME      FLIGHT_TIMINGS      DEPARTURE   ARRIVAL     TOTAL_NO_OF_SEATS    AVAILABLE_SEATS    RESERVED    COST")
    for R in fdeet: 
        fno=R[0]
        fname=R[1]
        timings=R[2]
        source=R[3]
        dest=R[4]
        numseat=R[5]
        avail=R[6]
        r=R[7]
        cost=R[8]
        print('{:15}{:15}{:15}{:15}{:15}{:15}{:15}{:15}{:15}'.format(fno,fname,timings,source,dest,numseat,avail,r,cost))
        print()
    f.close()



def passenger():
    passen=[]
    f=open("flight","rb")
    f1=open("passenger_details","ab+")
    pname=input("enter passenger name")
    pnum=int(input('enter phone number:'))
    psource=input("enter source :")
    pdest=input("enter destination:")
    pno=int(input(" enter no of passengers:"))
    p=[pname,pnum,psource,pdest,pno]
    
    rec=pickle.load(f)
    print(rec)
    for r in rec:
        if r[3]==psource and r[4]==pdest:
            fn=r[0]
            fname=r[1]
            ft=r[2]
            cost=r[8]
            total=cost*pno
            p=p+[fn,fname,ft,cost,total]
            passen.append(p)
            pickle.dump(passen,f1)
        else:
            print("Flight not found")
            break
    
    f.close()
    f1.close()


def pass_deets():
    f=open("passenger_details","rb")
    data=pickle.load(f)
    name=input("enter name:")
    for rec in data:
        if rec[0]==name:
            nam=rec[0]
            number=rec[1]
            source=rec[2]
            dest=rec[3]
            pn=rec[4]
            fn=rec[5]
            fname=rec[6]
            ft=rec[7]
            total=rec[9]
            print("NAME     PHONE_NUMBER     DEPARTURE      ARRIVAL     NO_OF_SEATS     FLIGHT_NUMBER    FLIGHT_NAME    TIMINGS     TOTAL_COST")
            print(nam,number,source,dest,pn,fn,fname,ft,total)
        else:
            print("Name not found")
    f.close()
            

t=input("enter management or customer m/c:")
if t=='c':
    while True:
        #for customer use
        print()
        print("1.display flight details")
        print("2.buy tickets")
        print("3.display your ticket")
        print("4.cancel tickets")
        print("5.Quit")
        c=int(input("enter choice:"))
        if c==1:
            show()
        elif c==2:
            passenger()
        elif c==3:
            pass_deets()
        elif c==4:
            cancel()
        elif c==5:
            print("Thank You.Have a Nice Day.")
            break
        else:
            print("invalid choice.")
if t=='m':
    pas=0000
    p=int(input("enter management password:"))
    if p==pas:
        print("Access granted")
        while True:
            print()
            print("1.Add flight details")
            print("2.Quit")
            c=int(input("enter choice:"))
            if c==1:
                deets()
            elif c==2:
                print("Thank you")
                break
            else:
                print("invalid choice.Try Again")
                break
    else:
        print("wrong password")
            
            
    
        
        
    
    


        
    

    
