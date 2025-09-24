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

print(input("Hei, hva vil du gjøre? \nBestille bøker \nSelge bøker \nSe lager \nSe salg \nSkriv her: "))


bestille = "Bestille bøker"
selge = "Selge bøker"
lager = "Se lager"
salg = "Se salg"


while True:
    if input == bestille:
        # Bestille bøker
        bok = input("Skriv inn boken som skal bestilles: ")
        pris = input("Skriv inn hva boken koster: ")
        antall_varer = input("Skriv hvor mange bøker som skal bestilles: ")

        c.execute("INSERT INTO inventar (navn, pris, antall) VALUES(?,?,?)", (bok, pris, antall_varer))
        break
    elif input == selge:
        # Selge bøker
        vare_id = input("Skriv inn ID-en til boken som skal selges: ")
        dato = input("Skriv inn dato salget blir gjort: ")
        antall_salg = input("Skriv inn antall som blir solgt: ")

        c.execute("INSERT INTO salg (vare_id, dato, antall) VALUES(?,?,?)", (vare_id, dato, antall_salg))
        break
    elif input == lager:
        # Vise varelager
        c.execute("SELECT * FROM inventar")
        break
    elif input == salg:
        # Vise salg
        c.execute("SELECT * FROM salg")
        break
    else:
        print("Ugyldig input, sjekk skrivefeil og prøv igjen")
        break


print(c.fetchall())
databasekobling.commit()
databasekobling.close()