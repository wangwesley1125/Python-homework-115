'''
(Duplicate Email Address Removal) Write a function that receives a list of email
addresses and displays only the unique addresses. Treat uppercase and lowercase letters the
same. The function should use a set to get the unique email addresses from the list. Test
your function with several different lists.
'''

def delete_duplicate(person_id, person_email):
    # print(person_id, person_email)
    # print(type(person_email)) => str
    email_name = []

    for email in person_email.split("@example.com"):
        # print(email.lower())
        email_name.append(email)
    print(person_id, email_name)

    # print(*email_name, sep='')



email_list = [[1, "john@example.com"],
              [2, "bob@example.com"],
              [3, "John@example.com"]]

# print(len(email_list)) => 3

for i in range(len(email_list)):
    delete_duplicate(email_list[i][0], email_list[i][1])

