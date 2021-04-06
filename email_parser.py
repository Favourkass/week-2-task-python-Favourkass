import re

'''
sorry if my regex is every where, i compiled it as i read through what it should check
for line by line.
check if every email inputted matches my regex
i created a list to use as keys for my dictionary
split the mail using the @ sign as required
created a dictionary using my created key list and split mail


'''

def email_parser(email):
  regex = re.compile(r'([^+0-9][a-zA-Z0-9+]+)[^_+]@([^0-9][a-zA-Z0-9]+\.com)+')
  split_list = ['username','domain']
  split_mail = re.split(r'@',email)
  slit_dict = {k:y for k,y in zip(split_list,split_mail) }
  if regex.match(email):
    return slit_dict
print(email_parser('nnabuekassidy1@gmail.com'))
    
 