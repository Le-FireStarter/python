file = open('/Users/pc/Desktop/GIT/python/CatchUp_Class/main.py','r')
raw_data = file.readlines()
#print(raw_data)

for sentence in raw_data:
    if sentence.startswith('Date'):
        if sentence.find('(Fri') == -1:continue
    else:
        print(sentence)

#for link in raw_data:
   # if link.find('https://') != -1 or link.find('http://') != -1 :
       # print(link)


# email_bucket = []
# tmp_word = []
# for email in raw_data:
#     tmp_word.extend(email.split(' '))
# for text in tmp_word:
#     if text.find('@') != -1:
#         at_post = text.find('@')
#         left_part = text[:at_post]
#         right_part = text[at_post:]
#         email = left_part+right_part
#         email = email.strip('\n<>();')
#         if email != 'apache@localhost':
#             email_bucket.append(email)
    
# #print(email_bucket)

# email_dict = {}
# for email in email_bucket:
#     if not email in list(email_dict.keys()):
#         email_dict[email] = 1
#     else:
#         value = email_dict.get(email)
#         email_dict[email] = value + 1

# #email_dict = {}
# #for email in email_bucket:
# #    email_dict[email] = email_dict.get(email,0)+1

# #print(email_dict)

# #print(email_dict)

# # assignment 
# # solution 1
# # items = list(email_dict.items())
# #for key,value in items:
# #for email in (email_dict.copy().keys()):
#    # if value < 2:
#         #del email_dict[key]
# #print(email_dict)


# #solution 2
# #keys = email_dict.keys()
# for email in (email_dict.copy().keys()):
#     if email_dict[email] < 2:
#         del email_dict[email]
# print(email_dict)