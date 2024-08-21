#sort dictionary data: values in descending then keys on ascending order

inbox_string = "JohnDoe@gmail.com, Subject1, 09:00; JaneDoe@gmail.com, Subject2, 10:00; JohnDoe@gmail.com, \
    Subject3, 12:00; Bot@gmail.com, Subject4, 08:00; Bot@gmail.com, Subject5, 09:00"
inbox_string_arr = inbox_string.split('; ')
email_dict = {}

for email_str in inbox_string_arr:
    email_id, *_ = email_str.split(', ')
    email_dict[email_id] = email_dict.get(email_id, 0) + 1
    
print(sorted(email_dict.items(), key=lambda item: (-item[1], item[0])))

'''
output:
('Bot@gmail.com', 2), ('JohnDoe@gmail.com', 2), ('JaneDoe@gmail.com', 1)]
'''