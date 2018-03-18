from passlib.hash import pbkdf2_sha256


class User:
    id = None
    username = None
    password = None
    level = None

    def user(self, id, username, password, level):
        self.id = id
        self.username = username
        self.password = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16);
        self.level = level

    def change_level(self, level_key, level_num):
        if(pbkdf2_sha256.encrypt(level_key, rounds=200000, salt_size=16)):
            self.level = level_num
            print("level changed")
        else:
            print("key incorrect")

    def change_username(self, new_username):
        self.username = new_username
        print("username changed")

    def create_password(self, password):
        return pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)

    def change_password(self, new_password):
        if(pbkdf2_sha256.encrypt(new_password, rounds=200000, salt_size=16)):
            self.password = new_password
            print("Password changed")
        else:
            print("Password incorrect")

    def user_login(self, test_password):
        test = pbkdf2_sha256.verify(test_password, this.password)
        return test
