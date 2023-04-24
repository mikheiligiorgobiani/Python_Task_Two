current_users = ['jordan','mickel','misho','givi','john']
new_users = ['nini','mick','jordan','misho','avto']
for name in new_users:
    for existing_name in current_users:
        if name == existing_name:
            print(f"{name}")
