d = {
    "name": ["sai", "nam", "ghhfhj"],
    "Rollno": [344, 56, 89]
}
user_name = input("Enter your name: ")
user_roll = int(input("Enter your roll number: "))
print("\nUser Input:")
print("Name:", user_name)
print("Rollno:", user_roll)
if user_name in d["name"] and user_roll in d["Rollno"]:
    print("\nUser exists!")
    index = d["name"].index(user_name)
    print("Name:", d["name"][index], "Rollno:", d["Rollno"][index])
else:
    print("\nUser not found. Adding to data...")
    d["name"].append(user_name)
    d["Rollno"].append(user_roll)
    print("Name:", user_name, "Rollno:", user_roll)
print("\nUpdated Data:", d)


#palindrome or not
a = {"Abba", "bbaa", "abbaba", "bbaabb"}
palindromes = [word for word in a if word.lower() == word[::-1].lower()]
print(palindromes)