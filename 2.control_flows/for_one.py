users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Create a new collection
active_users = {}
user_list = users.items() # dict_items([('Hans', 'active'), ('Éléonore', 'inactive'), ('景太郎', 'active')])

for status in user_list:
    print("status", str(status))

for user in user_list:
    print("user", str(user))

for user, status in users.items():
    print("user", str(user), "status", str(status))
    if status == 'active':
        active_users[user] = status

print(f"type of {type(user_list)}",user_list)
print(active_users)

""" 
$ python ./for_one.py
status ('Hans', 'active')
status ('Éléonore', 'inactive')
status ('景太郎', 'active')
user ('Hans', 'active')
user ('Éléonore', 'inactive')
user ('景太郎', 'active')
user Hans status active
user Éléonore status inactive
user 景太郎 status active
dict_items([('Hans', 'active'), ('Éléonore', 'inactive'), ('景太郎', 'active')])
{'Hans': 'active', '景太郎': 'active'}
"""
