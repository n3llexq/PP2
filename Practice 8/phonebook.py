import re
from connect import get_connection

def init_procedures():
    conn = get_connection()
    for filename in ["procedures.sql", "functions.sql"]:
        with open(filename, "r", encoding="utf-8") as f:
            sql = f.read()
        blocks = re.findall(
            r'CREATE\s+OR\s+REPLACE\s+(?:PROCEDURE|FUNCTION)[\s\S]*?\$\$\s*;',
            sql,
            re.IGNORECASE
        )
        with conn.cursor() as cur:
            for block in blocks:
                cur.execute(block)
    conn.commit()
    conn.close()
    print("Процедуры/функции обновлены")

def search_contacts():
    conn = get_connection()
    cur = conn.cursor()

    keyword = input("Search: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE firstname ILIKE %s OR secondname ILIKE %s OR phonenumber ILIKE %s",
        ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%')
    )

    rows = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    if rows:
        print("\nResults:")
        for row in rows:
            print(row)
    else:
        print("No contacts found.")

def insert_contact():
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone: ")
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s, %s)", (name, surname, phone))
    
    conn.commit()
    cur.close()
    conn.close()
    
    print("Contact inserted/updated")

def bulk_insert():
    n = int(input("How many contacts to insert? "))
    contacts = []

    for _ in range(n):
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        contacts.append((name, surname, phone))

    conn = get_connection()
    cur = conn.cursor()

    for name, surname, phone in contacts:
        cur.execute(
            "INSERT INTO phonebook(firstname, secondname, phonenumber) VALUES (%s, %s, %s)",
            (name, surname, phone)
        )

    conn.commit()
    cur.close()
    conn.close()

    print(f"{n} contacts added successfully.")

def delete_contact():
    value = input("Name or surname or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE firstname = %s OR secondname = %s OR phonenumber = %s",
        (value, value, value)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact deleted (if existed).")

def show_paginated():
    limit = int(input("Number of rows per page: "))
    offset = int(input("Offset: "))
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s,%s)", (limit, offset))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found")

    conn.commit()
    cur.close()
    conn.close()

def menu():
    init_procedures()
    while True:
        print("""
1. Search contacts
2. Insert/Update contact
3. Bulk insert contacts
4. Delete contact
5. Show paginated contacts
6. Exit
""")
        choice = input("Choose: ")
        if choice == "1":
            search_contacts()
        elif choice == "2":
            insert_contact()
        elif choice == "3":
            bulk_insert()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            show_paginated()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()