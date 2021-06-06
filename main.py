from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem 
from AppGui import Ui_MainWindow
import sys
import sqlite3 as sql
import os 
os.system('python Connection.py')
os.system('python CreateTable.py')

global id, fistname, lastname, city, phone, email

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.btnListClick()
        self.ui.btnList.clicked.connect(self.btnListClick)
        self.ui.btnSave.clicked.connect(self.btnSaveClick)
        self.ui.btnDelete.clicked.connect(self.btnDeleteClick)
        self.ui.btnUpdate.clicked.connect(self.btnUpdateClick)
        self.ui.tblList.clicked.connect(self.ListOnClick) 
 
    def btnClear(self):
        self.ui.txtID.clear()
        self.ui.txtFirstname.clear()
        self.ui.txtLastname.clear()
        self.ui.txtCity.clear()
        self.ui.txtPhone.clear()
        self.ui.txtEmail.clear()

    def ListOnClick(self): 
        self.ui.txtID.setText(self.ui.tblList.item(self.ui.tblList.currentRow(), 0).text())
        self.ui.txtFirstname.setText(self.ui.tblList.item(self.ui.tblList.currentRow(), 1).text())
        self.ui.txtLastname.setText(self.ui.tblList.item(self.ui.tblList.currentRow(), 2).text())
        self.ui.txtCity.setText(self.ui.tblList.item(self.ui.tblList.currentRow(), 3).text())
        self.ui.txtPhone.setText(self.ui.tblList.item(self.ui.tblList.currentRow(), 4).text())
        self.ui.txtEmail.setText(self.ui.tblList.item(self.ui.tblList.currentRow(), 5).text())
 
    def btnSaveClick(self): 
        id = self.ui.txtID.text()
        firstname = self.ui.txtFirstname.text()
        lastname = self.ui.txtLastname.text()
        city = self.ui.txtCity.text()
        phone = self.ui.txtPhone.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("database.db")
            self.c = self.conn.cursor() 
            self.c.execute("INSERT INTO Users VALUES (?,?,?,?,?,?)",(id,firstname,lastname,city,phone,email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User added successfully!.')
        except Exception:
            print('Error', 'Could not add student!.')
        
        self.btnClear()
        self.btnListClick()

    def btnListClick(self):  
        self.ui.tblList.clear()
        self.ui.tblList.setColumnCount(6)
        self.ui.tblList.setHorizontalHeaderLabels(('ID','Firstname','Lastname','City','Phone','Email'))
        self.ui.tblList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('database.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM Users"
        cur.execute(selectquery) 
        rows = cur.fetchall()
         
        self.ui.tblList.setRowCount(len(rows))
        
        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                self.ui.tblList.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri))) 
    
    def btnUpdateClick(self):  
        id = self.ui.txtID.text()
        firstname = self.ui.txtFirstname.text()
        lastname = self.ui.txtLastname.text()
        city = self.ui.txtCity.text()
        phone = self.ui.txtPhone.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("database.db")
            self.c = self.conn.cursor()  
            self.c.execute("UPDATE Users SET firstname = ?, lastname = ?, city = ?, \
                phone = ?, email = ? WHERE id = ?",(firstname,lastname,city,phone,email,id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User updated successfully!.')
        except Exception:
            print('Error', 'Could not update student!.')

        self.btnClear()
        self.btnListClick()

    def btnDeleteClick(self): 
        id = self.ui.txtID.text() 

        try:
            self.conn = sql.connect("database.db")
            self.c = self.conn.cursor() 
            self.c.execute('DELETE FROM Users WHERE id = ?  ', (id,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User deleted successfully!.')
        except Exception:
            print('Error', 'Could not delete student!.')
        
        self.btnClear()
        self.btnListClick()

            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()