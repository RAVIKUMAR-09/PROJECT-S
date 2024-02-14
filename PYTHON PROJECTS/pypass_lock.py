from cryptography.fernet import Fernet

class Pypass_lock:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_doct = {}

    def create_key(self,path):
        self.key = Fernet.generate_key()
        with open(path,'w') as f:
            f.write(self.key)

    def load_key(self,path):
        with open(path,'r') as f:
            self.key = f.read()

    def crate_password_file(self,path,intail_value = None):
        self.password_file = path


        if intail_value is not None:
            for key, value in intail_value.items():
                self.add_password(key,value)

    def load_password_file(self , path):
        self.password_file = path

        with open(path ,'r' ) as f:
            for line in f:
                site,encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode())

    def add_password(self,site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file , 'a+') as f:
                encrypated = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypated.decode() + "\n")

    def get_password(self,site):
        return self.password_dict[site]
    

def main():
    password = {
        "email" : "ravi123",
        "facebokk" : "mypassword",
        "youtube" : "ravi353536",
        "instagram" : "myname122",
        "google" : "kumar5566",
        "linkdin" : "ravi112233",

    }

    pm = Pypass_lock()

    print("""What do you want to do?
    (1)  Create a new key
    (2) Load an existing key
    (3) Create new password file
    (4) Load an existing file
    (5) Add a new password
    (6) Get a password
    (7) Quit
    """)

    done = False

    while not done:

        choice = input("Enter your choice")
        if choice == "1":
            path = input("Enter path:")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path:")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path:")
            pm.crate_password_file(path , password)
        elif choice == "4":
            path = input("Enter path:")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter the site:")
            password  = input("Enter the password:")
            pm.add_password(site,password)
        elif choice == "6":
            site = input("What site do you want:")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "Q":
            done  == True
            print("Bye User and Thank you!")
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
    