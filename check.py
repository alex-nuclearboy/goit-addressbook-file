from main import AddressBook, Record, Name, Phone, Birthday

# Creating an address book
address_book = AddressBook()

# Adding records
address_book.add_record(Record("Alice", ["1234567890"], "1985-04-01"))
address_book.add_record(Record("Bob", ["2345678901", "3456789012"]))
address_book.add_record(Record("Charlie", ["4567890123"]))
address_book.add_record(
    Record("John", ["4567890125", "8963257821"], "1990-01-01"))

# Displaying all the records
print("All records:")
for name, record in address_book.items():
    print(record)

# Search for a record
print("\nSearch a record for 'Alice':")
alice_record = address_book.find("Alice")
print(alice_record)


# Displaying the number of days until the next birthday
print("\nDays until next birthday:")
records = []
records.append(address_book.find("Alice"))
records.append(address_book.find("Bob"))
records.append(address_book.find("Charlie"))
records.append(address_book.find("John"))

for record in records:
    if record and record.birthday:
        days_until_birthday = record.days_to_birthday()
        print(
            f"Days until next birthday of {record.name.value}: {days_until_birthday}")
    else:
        print(
            f"Contact '{record.name.value}' not found or birthday not set.")

# Adding a phone number
print("\nAdding a phone number for 'Bob':")
bob_record = address_book.find("Bob")
bob_record.add_phone("5678901234")
print(bob_record)

# Creating a new file
address_book.save_to_file('address_book.json')

# Deleting a phone number
print("\nDeleting a phone number for 'Charlie':")
charlie_record = address_book.find("Charlie")
charlie_record.remove_phone("4567890123")
print(charlie_record)

print("\nDeleting a phone number for 'John':")
charlie_record = address_book.find("John")
charlie_record.remove_phone("4567890125")
print(charlie_record)

# Changing a phone number
print("\nChanging a phone number for 'Alice':")
alice_record.edit_phone("1234567890", "9876543210")
print(alice_record)

# Deleting a record
print("\nDeleting a record 'Charlie':")
address_book.delete("Charlie")
print(f"Is 'Charlie' in the adress book: {'Charlie' in address_book}")

# Using an iterator
print("\nRecords with pagination (one record per page):")
for page in address_book.iterator(1):
    print(page)
    print("-" * 60)

print("\nRecords with pagination (three records per page):")
for page in address_book.iterator(3):
    print(page)
    print("-" * 60)

# Loading from a file
new_address_book = AddressBook()
new_address_book.load_from_file('address_book.json')

# Searching in the file
print("\nSearching in the file:")
search_results_name = new_address_book.search("Al")
for record in search_results_name:
    print(record)

search_results_num = new_address_book.search("234")
for record in search_results_num:
    print(record)
