# Задание 1
basketball_players = {}


def add_player(name, height):
    basketball_players[name] = height


def remove_player(name):
    if name in basketball_players:
        del basketball_players[name]
    else:
        print(f"{name} не найден в базе данных")


def search_player(name):
    if name in basketball_players:
        print(f"{name} - Рост: {basketball_players[name]}")
    else:
        print(f"{name} не найден в базе данных")


def update_player(name, new_height):
    if name in basketball_players:
        basketball_players[name] = new_height
    else:
        print(f"{name} не найден в базе данных")


add_player("LeBron James", 203)
add_player("Michael Jordan", 198)
search_player("LeBron James")
search_player("Kobe Bryant")
update_player("LeBron James", 205)
remove_player("Michael Jordan")
# Задание 2
english_french_dict = {}


def add_word(english_word, french_translation):
    english_french_dict[english_word] = french_translation


def remove_word(english_word):
    if english_word in english_french_dict:
        del english_french_dict[english_word]
    else:
        print(f"{english_word} is not found in the dictionary")


def search_word(english_word):
    if english_word in english_french_dict:
        print(f"{english_word} - Translation: {english_french_dict[english_word]}")
    else:
        print(f"{english_word} is not found in the dictionary")


def update_translation(english_word, new_french_translation):
    if english_word in english_french_dict:
        english_french_dict[english_word] = new_french_translation
    else:
        print(f"{english_word} is not found in the dictionary")


add_word("hello", "bonjour")
add_word("goodbye", "au revoir")
search_word("hello")
search_word("thank you")
update_translation("hello", "salut")
remove_word("goodbye")
# Задание 3
company_dict = {}


def add_employee_info(name, phone, email, position, office_number, skype):
    employee_info = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Position": position,
        "Office Number": office_number,
        "Skype": skype
    }
    company_dict[name] = employee_info


def remove_employee_info(name):
    if name in company_dict:
        del company_dict[name]
    else:
        print(f"{name} is not found in the company dictionary")


def search_employee_info(name):
    if name in company_dict:
        print(f"Employee Information for {name}: {company_dict[name]}")
    else:
        print(f"{name} is not found in the company dictionary")


def update_employee_info(name, new_phone, new_email, new_position, new_office_number, new_skype):
    if name in company_dict:
        company_dict[name]["Phone"] = new_phone
        company_dict[name]["Email"] = new_email
        company_dict[name]["Position"] = new_position
        company_dict[name]["Office Number"] = new_office_number
        company_dict[name]["Skype"] = new_skype
    else:
        print(f"{name} is not found in the company dictionary")


add_employee_info("John Doe", "123-456-7890", "john.doe@example.com", "Manager", "101", "john_doe_skype")
search_employee_info("John Doe")
update_employee_info("John Doe", "987-654-3210", "john.doe@newexample.com", "Senior Manager", "102", "new_john_doe_skype")
remove_employee_info("John Doe")
# Задание 4
book_collection = {}


def add_book_info(author, title, genre, year, num_pages, publisher):
    book_info = {
        "Author": author,
        "Title": title,
        "Genre": genre,
        "Year": year,
        "Number of Pages": num_pages,
        "Publisher": publisher
    }
    book_collection[title] = book_info


def remove_book_info(title):
    if title in book_collection:
        del book_collection[title]
    else:
        print(f"{title} is not found in the book collection")


def search_book_info(title):
    if title in book_collection:
        print(f"Book Information for {title}: {book_collection[title]}")
    else:
        print(f"{title} is not found in the book collection")


def update_book_info(title, new_author, new_genre, new_year, new_num_pages, new_publisher):
    if title in book_collection:
        book_collection[title]["Author"] = new_author
        book_collection[title]["Genre"] = new_genre
        book_collection[title]["Year"] = new_year
        book_collection[title]["Number of Pages"] = new_num_pages
        book_collection[title]["Publisher"] = new_publisher
    else:
        print(f"{title} is not found in the book collection")


add_book_info("J.K. Rowling", "Harry Potter and the Philosopher's Stone", "Fantasy", 1997, 223, "Bloomsbury Publishing")
search_book_info("Harry Potter and the Philosopher's Stone")
update_book_info("Harry Potter and the Philosopher's Stone", "Joanne Rowling", "Fantasy, Adventure", 1997, 320, "Scholastic")
remove_book_info("Harry Potter and the Philosopher's Stone")


