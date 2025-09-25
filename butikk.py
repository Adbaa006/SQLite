import sqlite3

databasekobling = sqlite3.connect("butikk.db")
c = databasekobling.cursor()

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
          dato REAL NOT NULL,
          antall INTEGER NOT NULL
          )
""")

def legge_til_vare():
    bok = input("Skriv inn boken som skal bestilles: ")
    pris = input("Skriv inn hva boken koster: ")
    antall_varer = input("Skriv hvor mange bøker som skal bestilles: ")
    c.execute("INSERT INTO inventar (navn, pris, antall) VALUES(?,?,?)", (bok, pris, antall_varer))
    databasekobling.commit()

def slett_vare():
    vare_id = input("Skriv id til varen som skal slettes: ")
    c.execute("DELETE FROM inventar WHERE id = ?", (vare_id))
    databasekobling.commit()

inn = ""

while inn != "q":
    print("""
    MENY
    1. Legg til vare
    2. Slett vare
          """)
    inn = input(": ")
    match inn:
        case "1":
            legge_til_vare()
        case "2":
            slett_vare()
    


# Selge bøker
vare_id = input("Skriv inn ID-en til boken som skal selges: ")
dato = input("Skriv inn dato salget blir gjort: ")
antall_salg = input("Skriv inn antall som blir solgt: ")

c.execute("INSERT INTO salg (vare_id, dato, antall) VALUES(?,?,?)", (vare_id, dato, antall_salg))
# Vise varelager
c.execute("SELECT * FROM inventar")
# Vise salg
c.execute("SELECT * FROM salg")



print(c.fetchall())

databasekobling.close()