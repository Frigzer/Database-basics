from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased
import os

engine = create_engine("sqlite:///mydb.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Create table Autorzy
class Writer(Base):
    __tablename__ = "Autorzy"
    
    id = Column("ID_autora", Integer, primary_key=True)
    firstname = Column("Imie", String(25))
    lastname = Column("Nazwisko", String(50))
    birthDate = Column("Data_urodzenia", String(50))
    homeCountry = Column("Kraj_pochodzenia", String(100))
    
    def __init__(self, firstname, lastname, birthDate, homeCountry):
        self.firstname=firstname
        self.lastname=lastname
        self.birthDate=birthDate
        self.homeCountry=homeCountry
        
# Create table Ksiazki
class Book(Base):
    __tablename__ = "Ksiazki"
    
    id = Column("ID_ksiazki", Integer, primary_key=True)
    title = Column("Tytul", String(25))
    releaseDate = Column("Data_wydania", String(50))
    authorID = Column("ID_autora", Integer, ForeignKey("Autorzy.ID_autora"))
    
    def __init__(self, title, releaseDate, authorID):
        self.title=title
        self.releaseDate=releaseDate
        self.authorID=authorID
        
# Create table Klienci
class Client(Base):
    __tablename__ = "Klienci"
    
    id = Column("ID_klienta", Integer, primary_key=True)
    firstname = Column("Imie", String(25))
    lastname = Column("Nazwisko", String(50))
    phoneNumber = Column("nr_telefonu", String(9))
    bookID = Column("ID_ksiazki", Integer, ForeignKey("Ksiazki.ID_ksiazki"))
    
    def __init__(self, firstname, lastname, phoneNumber, bookID=None):
        self.firstname=firstname
        self.lastname=lastname
        self.phoneNumber=phoneNumber
        self.bookID=bookID
        
# Tworzenie tabeli
#Base.metadata.create_all(engine)

# Insert into Autorzy
writers = [
    Writer("George R. R.", "Martin", "20.09.1948", "Stany Zjednoczone"),
    Writer("John R. R.", "Tolkien", "03.01.1892", "Wielka Brytania"),
    Writer("Joanne", "Rowling", "31.07.1965", "Wielka Brytania"),
    Writer("Howard P.", "Lovecraft", "20.08.1890", "Stany Zjednoczone"),
    Writer("Clive S.", "Lewis", "29.11.1898", "Wielka Brytania"),
    Writer("Agatha", "Christie", "15.09.1890", "Wielka Brytania"),
    
]

# Insert into Ksiazki
books = [
    Book("Drużyna Pierścienia", "29.07.1954", 2),
    Book("Dwie Wieże", "11.11.1954", 2),
    Book("Powrót Króla", "20.10.1955", 2),
    Book("Gra o Tron", "01.08.1996", 1),
    Book("Starcie Królów", "16.11.1998", 1),
    Book("Nawałnica Mieczy", "08.08.2000", 1),
    Book("Uczta dla wron", "17.10.2005", 1),
    Book("Taniec ze smokami", "12.07.2011", 1),
    Book("Morderstwo w Orient Expressie", "01.01.1934", 6),
    Book("Śmierć na Nilu", "01.11.1937", 6),
    Book("Zew Cthulhu", "01.02.1928", 4),
    Book("Lew, czarownica i stara szafa", "16.10.1950", 5),
    Book("Książę Kaspian", "15.10.1951", 5),
    Book("Harry Potter i Kamień Filozoficzny", "26.06.1997", 3),
    Book("Harry Potter i Komnata Tajemnic", "02.07.1998", 3),
    Book("Harry Potter i więzień Azkabanu", "08.07.1999", 3),
]

# Insert into Klienci
clients = [
    Client("Cezary", "Baryka", "997998999"),
    Client("Artur", "Borubar", "112691420"),
    Client("Greg", "Lepkie-Rączki", "213700769"),
]

# Wstawienie wartości do tabel
#session.bulk_save_objects(writers)
#session.commit()

#session.bulk_save_objects(books)
#session.commit()

#session.bulk_save_objects(clients)
#session.commit()

# Utwórz alias dla tabeli Writer, aby uniknąć konfliktu nazw kolumn
writer_alias = aliased(Writer)

def display_books_by_author(selectedAuthor):
    # Funkcja książki pojedynczego autora
    books = (
        session.query(Book.title, Book.releaseDate, Writer.firstname, Writer.lastname)
        .join(Writer, Book.authorID == Writer.id)
        .filter(Book.authorID==selectedAuthor)
        .all())
    os.system("cls")
    full_name = f"{books[0].firstname} {books[0].lastname}"
    print(f"Książki napisane przez {full_name}:")
    print()
    for result in books:
        print(f"{result.title}, pierwsze wydanie: {result.releaseDate}")
        
    print()
    os.system("pause")

def display_authors():
    # Funkcja wyświetlająca autorów
    while True:
        authors = session.query(Writer).all()
        os.system("cls")
        print("Autorzy:")
        for author in authors:
            full_name = f"{author.firstname} {author.lastname}"
            print(f"{author.id}. {full_name} ({author.homeCountry}, {author.birthDate})")
            
        print()
        print("1) Sprawdź ksiązki napisane przez wybranego autora") 
        print("2) Cofnij\n")
        
        choice = input("Wybierz opcję (1/2): ")
        
        if choice == "1":
            ID_choice = input("Podaj ID autora: ")
            result = session.query(Writer).filter(Writer.id==ID_choice).first()
            if result:
                display_books_by_author(ID_choice)
            else:
                os.system("cls")
                print("Nieprawidłowe id autora. Spróbuj ponownie.")
                os.system("pause")
        elif choice == "2":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            os.system("pause")
    

def display_books():
    # Funkcja wyświetlająca książki
    query = (
        session.query(Book.id, Book.title, writer_alias.firstname, writer_alias.lastname, Book.releaseDate)
        .join(writer_alias, Book.authorID == writer_alias.id)
        .all()
    )
    os.system("cls")
    print("Książki:")
    for result in query:
        full_name = f"{result.firstname} {result.lastname}"
        print(f"{result.id}. {result.title} przez {full_name}, pierwsze wydanie: {result.releaseDate}")
        
    print()

    
def add_client():
    # Dodawanie nowego klienta
    os.system("cls")
    
    display_books()
    
    print()
    
    newFirstName = input("Imie nowego klienta: ")
    newLastName = input("Nazwisko nowego klienta: ")
    newPhoneNumber = input("Numer telefonu klienta: ")
    try:
        newBook = int(input("ID książki do wypożyczenia: "))
    except ValueError:
        newClient = Client(newFirstName, newLastName, newPhoneNumber)
    else:
        newClient = Client(newFirstName, newLastName, newPhoneNumber, newBook)

    session.add(newClient)
    
    session.commit()
    
    os.system("cls")
    
    print("Pomyślnie dodano klienta")
    os.system("pause")
    

def update_client():
    # Aktualizacja danych dla istniejącego klienta
    while True:
        try:
            choice = int(input("ID klienta do modyfikacji: "))
        except ValueError:
            print("Zła wartość. Należy podać liczbę")
            continue
        result = session.query(Client).filter(Client.id==choice).first()
        os.system("cls")
         
        if result:
            while True:
                full_name = f"{result.firstname} {result.lastname} nr. tel. {result.phoneNumber}, id książki: {result.bookID}\n"
                os.system("cls")
                print(f"{full_name}")
                
                print("Opcje:")
                print("1) Zmień imię")
                print("2) Zmień nazwisko")
                print("3) Zmien nr. telefonu")
                print("4) Zmien ksiazke")
                print("5) Anuluj\n")
                
                choice2 = input("Wybierz opcję (1/2/3/4/5): ")
                
                if choice2=="1":
                    newFirstName = input("Nowe imię: ")
                    result.firstname=newFirstName
                    session.commit()
                    os.system("cls")
                elif choice2=="1":
                    newLastName = input("Nowe nazwisko: ")
                    result.lastname=newLastName
                    session.commit()
                    os.system("cls")
                elif choice2=="3":
                    newPhoneNumber = input("Nowy numer telefonu: ")
                    result.phoneNumber = newPhoneNumber
                    session.commit()
                    os.system("cls")
                elif choice2=="4":
                    display_books()
                    try:
                        newBook = int(input("Nowa książka do wypożyczenia: "))
                    except ValueError:
                        result.bookID = None
                    else:
                        result.bookID = newBook
                    session.commit()
                    os.system("cls")
                elif choice2=="5":
                    break
                else:
                    print("Nieprawidłowy wybór. Spróbuj ponownie.")
                    os.system("pause")    
        else:
            print(f"Nie znaleziono klienta o ID {choice}.")
            os.system("pause")
            
        break

def delete_client():
    while True:
        print()
        
        try:
            choice = int(input("ID klienta do usunięcia: "))
        except ValueError:
            print("Zła wartość. Należy podać liczbę")
            continue
        result = session.query(Client).filter(Client.id==choice).first()
        os.system("cls")
        
        if result:
            session.delete(result)
            session.commit()
            os.system("cls")
            print(f"Pomyślnie usunięto klienta o ID {choice}.")
        else:
            print(f"Nie znaleziono klienta o ID {choice}.")
            
        os.system("pause")
        break
    
def display_clients():
    # Funkcja wyświetlająca klientów
    while True:
        result = (
            session.query(Client.id, Client.firstname, Client.lastname, Client.phoneNumber, Book.title)
            .outerjoin(Book, Client.bookID == Book.id)
            .all()
        )
        os.system("cls")
        print("Klienci:")        
        for r in result:
            full_name = f"{r.firstname} {r.lastname}"
            book_title = r.title if r.title else "Brak książki"
            print(f"{r.id}. {full_name} nr. tel. {r.phoneNumber}, wypożyczono: {book_title}")
            
        print()
        print("1) Dodaj nowego klienta")
        print("2) Aktualizuj informacje o kliencie")
        print("3) Usuń klienta")
        print("4) Cofnij\n")
        
        choice = input("Wybierz opcję (1/2/3/4): ")
        
        if choice == "1":
            add_client()
        elif choice == "2":
            update_client()
        elif choice == "3":
            delete_client()
        elif choice == "4":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            os.system("pause")

def main():
    while True:
        os.system("cls")
        print("Menu:")
        print("1) Wyświetl autorów")
        print("2) Wyświetl książki")
        print("3) Wyświetl klientów")
        print("4) Wyjście\n")

        choice = input("Wybierz opcję (1/2/3/4): ")

        if choice == "1":
            display_authors()
        elif choice == "2":
            display_books()
            os.system("pause")
        elif choice == "3":
            display_clients()
        elif choice == "4":
            print("Wychodzenie z programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            os.system("pause")

if __name__ == "__main__":
    main()