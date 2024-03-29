import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="")
print(conn)
cr = conn.cursor()
cr.execute("CREATE DATABASE DBXIA")
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-DATABASE CREATED-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
while (True):
    cr.execute("use DBXIA")
    conn.commit()
    print("==================================================================")
    print(" MENU ")
    print()
    print("1 -> Create Table EMPL")
    print("2 -> Insert data in Table EMPL")
    print("3 -> Display Table EMPL")
    print("4 -> Update data in Table EMPL")
    print("5 -> Display data in Ascending order")
    print("6 -> Drop Table EMPL")
    print("==================================================================")
    ch=input("Enter your choice :")
    if(ch=='1'):
        print("-.-.-.-.-.-.-.-.-.-.- CREATING TABLE EMPL -.-.-.-.-.-.-.-.-.-.-")
        print()
        cr.execute("create table EMPL(EMPNO integer, ENAME varchar(25), JOB varchar(25), MGR varchar(20), HIREDATE DATE, SAL decimal, COMM varchar(20), DEPTNO integer)")
        conn.commit()
        print("-.-.-.-.-.-.-.-.-.-.- TABLE CREATED SUCCESSFULLY -.-.-.-.-.-.-.-.-.-.-")
        print()
        cr.execute("DESC EMPL")
        for i in cr:
            print(i)
        conn.commit()
        print("=================================================================")
    elif (ch=='2'):
        print("-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.- INSERTING DATA -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print()
        cr.execute("INSERT INTO EMPL VALUES(8369,'SMITH','CLERK','8902','1990-12-18',800.00,'NULL',20)")
        cr.execute("INSERT INTO EMPL VALUES(8499,'ANYA','SALESMAN','8698','1991-02-20',1600.00,'300.00',30)")
        cr.execute("INSERT INTO EMPL VALUES(8521,'SETH','SALESMAN','8698','1991-02-22',1250.00,'500.00',30)")
        cr.execute("INSERT INTO EMPL VALUES(8566,'MAHADEVAN','MANAGER','8839','1991-04-02',2985.00,'NULL',20)")
        cr.execute("INSERT INTO EMPL VALUES(8654,'MOMIN','SALESMAN','8698','1991-09-28',1250.00,'1400.00',30)")
        cr.execute("INSERT INTO EMPL VALUES(8698,'BINA','MANAGER','8839','1991-05-01',2850.00,'NULL',30)")
        cr.execute("INSERT INTO EMPL VALUES(8839,'AMIR','PRESIDENT','NULL','1991-11-18',5000.00,'NULL',10)")
        cr.execute("INSERT INTO EMPL VALUES(8844,'KULDEEP','SALESMAN','8698','1991-09-08',1500.00,'0.00',30)")
        cr.execute("INSERT INTO EMPL VALUES(8882,'SHIVANSH','MANAGER','8839','1991-06-09',2450.00,'NULL',10)")
        cr.execute("INSERT INTO EMPL VALUES(8886,'ANOOP','CLERK','8888','1993-01-12',1100.00,'NULL',20)")
        cr.execute("INSERT INTO EMPL VALUES(8888,'SCOTT','ANALYST','8566','1992-12-09',3000.00,'NULL',20)")
        cr.execute("INSERT INTO EMPL VALUES(8900,'JATIN','CLERK','8698','1991-12-03',950.00,'NULL',30)")
        cr.execute("INSERT INTO EMPL VALUES(8902,'FAKIR','ANALYST','8566','1991-12-03',3000.00,'NULL',20)")
        cr.execute("INSERT INTO EMPL VALUES(8934,'MITA','CLERK','8882','1992-01-23',1300.00,'NULL',10)")
        conn.commit()
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- DATA INSERTED SUCCESSFULLY -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print("=================================================================")
    elif(ch=='3'):
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- DISPLAYING DATA -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print()
        cr.execute("SELECT * FROM EMPL")
        for i in cr:
            print(i)
        conn.commit()
        print("=================================================================")
        print()
    elif (ch=='4'):
        alt = "UPDATE EMPL SET MGR = '8855' WHERE JOB = 'PRESIDENT'"
        cr.execute(alt)
        conn.commit()
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- UPDATE SUCCESSFULL -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print()
    elif (ch=='5'):
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- PROCESSING DATA -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print()
        cr.execute("SELECT * FROM EMPL ORDER BY ENAME")
        for i in cr:
            print(i)
        conn.commit()
        print("=================================================================")
        print()
    elif (ch=='6'):
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- DROPPING TABLE EMPL -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print()
        cr.execute("DROP TABLE EMPL")
        conn.commit()
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- TABLE DROPPED SUCCESSFULLY -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print()
        print("========================== THANK YOU ============================")
