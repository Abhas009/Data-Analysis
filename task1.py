def main():
    """
    Creates a list, dictionary, and set, demonstrating basic operations.
    """

    # Create a list of fruits
    fruits = ["apple", "banana", "orange", "grape"]
    print("Original list:", fruits)

    # Add an element to the list
    fruits.append("mango")
    print("List after adding 'mango':", fruits)

    # Remove an element from the list
    fruits.remove("banana")
    print("List after removing 'banana':", fruits)

    # Modify an element in the list
    fruits[1] = "pear"
    print("List after modifying second element:", fruits)

    # Create a dictionary of student information
    students = {
        "Alice": {"age": 20, "major": "Computer Science"},
        "Bob": {"age": 22, "major": "Mathematics"}
    }
    print("\nOriginal dictionary:", students)

    # Add a new student to the dictionary
    students["Charlie"] = {"age": 21, "major": "Physics"}
    print("Dictionary after adding 'Charlie':", students)

    # Remove a student from the dictionary
    del students["Bob"]
    print("Dictionary after removing 'Bob':", students)

    # Modify a student's information
    students["Alice"]["age"] = 21
    print("Dictionary after modifying Alice's age:", students)

    # Create a set of numbers
    numbers = {1, 2, 3, 4, 5}
    print("\nOriginal set:", numbers)

    # Add an element to the set
    numbers.add(6)
    print("Set after adding 6:", numbers)

    # Remove an element from the set
    numbers.remove(3)
    print("Set after removing 3:", numbers)

if __name__ == "__main__":
    main()
