import sqlite3, datetime

databasekobling = sqlite3.connect("butikk.db")
c = databasekobling.cursor()
c.execute("PRAGMA foreign_keys = ON")

c.execute("""
    CREATE TABLE IF NOT EXISTS inventar(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          navn TEXT NOT NULL,
          pris REAL NOT NULL,
          antall INTEGER NOT NULL
          )
""")
c.execute("""
    CREATE TABLE IF NOT EXISTS salg(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vare_id INTEGER,
        antall INTEGER NOT NULL,
        dato TEXT,
        FOREIGN KEY (vare_id) REFERENCES inventar(id)
        )
""")

def legge_til_vare():
    bok = input("Skriv inn boken som skal bestilles: ")
    pris = input("Skriv inn hva boken koster: ")
    antall_varer = input("Skriv hvor mange bøker som skal bestilles: ")
    c.execute("INSERT INTO inventar (navn, pris, antall) VALUES(?,?,?)", (bok, pris, antall_varer))
    databasekobling.commit()

def slett_vare():
    vare_id = input("Skriv ID-en til varen som skal slettes: ")
    c.execute("DELETE FROM inventar WHERE id = ?", (vare_id))
    databasekobling.commit()

def rediger_vare():
    vare_id = input("Skriv ID-en til varen som skal endres: ")
    c.execute("SELECT * FROM inventar WHERE id = ?", (vare_id))
    resultat = c.fetchone()
    inn = ""
    navn = resultat[1]
    pris = resultat[2]
    ant = resultat[3]

    while inn != "q":
        print(f"""
        Hva vil du redigere?
        1. Navn: {navn}
        2. Pris: {pris}
        3. Antall: {ant}
        "q" for å avslutte
        """)
        inn = input(": ")
        if inn == "1":
            navn = input("Skriv inn nytt navn: ")
        elif inn == "2":
            pris = input("Skriv inn ny pris: ")
        elif inn == "3":
            ant = input("Skriv inn nytt antall: ")
    c.execute("UPDATE inventar SET navn = ?, pris = ?, antall = ? WHERE id = ?", (navn, pris, ant, vare_id))
    databasekobling.commit()

def selge_vare():
    c.execute("SELECT * FROM inventar")
    resultat = c.fetchall()
    for vare in resultat:
        print(f"{vare[0]}. {vare[1]} - {vare[2]} kr - {vare[3]} stk")
    inn = input("Skriv inn ID-en til varen som skal selges: ")
    c.execute("SELECT * FROM inventar WHERE id = ?", (inn))
    rad = c.fetchone()
    vare_id = ""
    if rad is None:
        print(f"Fant ingen vare med ID: {inn}")
    else:
        vare_id = inn
        inn = input("Skriv antall: ")
    

inn = ""

while inn != "q":
    print("""
    MENY
    1. Legg til vare
    2. Slett vare
    3. Rediger vare
    4. Selge vare
    5. Vise rapport
    "q" for å avslutte
          """)
    inn = input(": ")
    if inn == "1":
        legge_til_vare()
    elif inn == "2":
        slett_vare()
    elif inn == "3":
        rediger_vare()
    elif inn == "4":
        selge_vare()
    
    

# Vise varelager
# c.execute("SELECT * FROM inventar")
# Vise salg
# c.execute("SELECT * FROM salg")
# print(c.fetchall())
# For Python 3.10
#match inn:
    #   case "1":
    #       legge_til_vare()
    #   case "2":
    #       slett_vare()
"""def selge_vare():
    vare_id = input("Skriv inn ID-en til varen som skal selges: ")
    dato = input("Skriv inn dato salget blir gjort: ")
    antall_salg = input("Skriv inn antall som blir solgt: ")
    c.execute("INSERT INTO salg (vare_id, dato, antall) VALUES(?,?,?)", (vare_id, dato, antall_salg))
    databasekobling.commit()
"""
databasekobling.close()