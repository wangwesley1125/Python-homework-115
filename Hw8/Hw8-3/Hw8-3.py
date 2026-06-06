'''
(Duplicate Email Address Removal) Write a function that receives a list of email
addresses and displays only the unique addresses. Treat uppercase and lowercase letters the
same. The function should use a set to get the unique email addresses from the list. Test
your function with several different lists.
'''

def remove_duplicates(list):

    seen = []
    result_email = []
    
    for email in list:
        if email.lower() not in seen:
            seen.append(email.lower())
            result_email.append(email)

    return result_email

email_list = ['john@example.com', 
              'bob@example.com', 
              'John@example.com', 
              'jOhn@example.com', 
              'jjoweek@example.com', 
              'Jjoweek@example.com',
              'Wesley@example.com',
              'wesley@example.com',
              'WESLEY@example.com',
              'wEsLeY@example.com']

result_email = remove_duplicates(email_list)
print(*list(result_email), sep="\n")
