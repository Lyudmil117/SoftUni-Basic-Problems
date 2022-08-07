favorite_book = input()
books_num = 0

while True:
    next_book = input()
    books_num = (books_num + 1)
    checked = books_num - 1
    if favorite_book == next_book:
        print(f"You checked {checked} books and found it. ")
        break
    elif next_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked} books.")
        break

