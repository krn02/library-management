library = {}

while True:
    print("\n1 add book")
    print("2 show book")
    print("3 issue book")
    print("4 return book")
    print("5 exit")

    choice = input("enter choice ")

    if choice == "1":
        id = input("enter book id ")
        name = input("enter book name ")
        author = input("enter author ")
        qty = int(input("enter quantity "))

        library[id] = {}
        library[id]["name :"] = name
        library[id]["author :"] = author
        library[id]["qty :"] = qty

        print("book added")

    elif choice == "2":
        if library == {}:
            print("no book")
        else:
            for b in library:
                print("id", b)
                print("name", library[b]["name"])
                print("author", library[b]["author"])
                print("quantity", library[b]["qty"])
                print()

    elif choice == "3":
        id = input("enter book id ")

        if id in library:
            if library[id]["qty"] >= 0:   # mistake: should be > 0
                library[id]["qty"] = library[id]["qty"] - 1
                print("book issued")
            else:
                print("book not available")
        else:
            print("book not found")

    elif choice == "4":
        id = input("enter book id ")

        if id in library:
            library[id]["qty"] = library[id]["qty"] + 1
            print("book returned")
        else:
            print("wrong id")

    elif choice == "5":
        print("exit")
        break

    else:
        print("invalid")