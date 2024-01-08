# Address Book Module

This repository contains the Address Book Module, a Python module with classes designed for creating and managing a digital address book. It includes features for contact management, such as storing, searching, editing, and deleting contact information, along with birthday tracking and serialization capabilities.

### Module Contents

- `Field`: The base class for entry fields, providing common logic for all fields.
- `Name`: Derived from Field, used for storing a contact's name. It's a mandatory field.
- `Phone`: Also derived from Field, handles phone number storage with format validation (10 digits).
- `Birthday`: Another Field derivative, responsible for storing and validating a contact's birthday.
- `Record`: Maintains information about a contact, including name and a list of phone numbers. Responsible for adding, deleting, and editing optional fields, while storing the mandatory Name field.
- `AddressBook`: Derived from UserDict, it manages contact records. Includes logic for adding, searching, and deleting entries based on contact names.

### Module Functionality

#### AddressBook Class:

- *Add Entries*: Add new contact records to the address book.
- *Search by Name or Phone*: Find entries using a partial or full match for the contact's name or phone number.
- *Delete by Name*: Remove entries based on the contact's name.
- *Save to File*: Serialiіe and save the address book to a file.
- *Load from File*: Deserialiіe and load the address book from a file.
- *Pagination*: Browse entries page by page.

#### Record Class:

- *Add Phone Numbers*: Attach phone numbers to a contact.
- *Delete Phone Numbers*: Remove specific phone numbers from a contact.
- *Edit Phone Numbers*: Modify existing phone numbers.
- *Find Phone Number*: Retrieve specific phone numbers associated with a contact.
- *Days to Birthday*: Calculate the number of days until the contact's next birthday.

#### Birthday Class:

- *Store Birthday*: Keep track of a contact's birthday.
- *Validate Birthday Format*: Ensure that the birthday is in a valid format.

### Installation

    # Clone the repository
    git clone https://github.com/alex-nuclearboy/goit-addressbook-file.git

### Usage

The module is designed for import into Python scripts where contact management is needed.

### Testing
Additionally, this repository includes a testing script that verifies the functionality of the provided classes. 
It ensures that each class and method operates as intended and that the module maintains robust and error-free performance.
