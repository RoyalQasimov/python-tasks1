a_login = "test"
a_password = "12345"

login = input("Login:")
password = input("Password:")

if not login and not password:
    print("login ve passwordu daxil etmemisiz")

elif not login or not password:
    if not login:
        print("login daxil edilmeyib")
    else:
        print("password daxil edilmeyib")

elif login == a_login and password == a_password:
    print("xos gelmisiz")
elif login != a_login:
    print("Login sehvdi")
elif password != a_password:
    print("password sehvdi")
else:
    print("Login ve password sehvdi")

