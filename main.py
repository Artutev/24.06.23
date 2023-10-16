import hashlib

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

def save_credentials(username, hashed_password):
    with open('credentials.txt', 'a') as file:
        file.write(f"{username} {hashed_password}\n")

def main():
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    hashed_password = hash_password(password)
    save_credentials(username, hashed_password)

    print("Логин и хэшированный пароль сохранены в файле 'credentials.txt'.")

if __name__ == "__main__":
    main()
