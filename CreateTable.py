import sqlite3 as sql

def main():
    try: 
        db = sql.connect('database.db')
        cursor = db.cursor()
        tablequery = "CREATE TABLE Users (id INT, firstname TEXT, lastname TEXT, city TEXT, phone TEXT, email TEXT)"

        cursor.execute(tablequery)
        print("Table Created Succesfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()