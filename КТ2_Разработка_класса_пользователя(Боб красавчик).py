import hashlib
import re


class User:
  
    _EMAIL_PATTERN = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")

    def __init__(self, username, password, email):
        self.username = username
        self.__password_hash = self._hash(password)
        self.__email = None
        self.set_email(email)

    @staticmethod
    def _hash(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @classmethod
    def _validate_email(cls, email):
        if not isinstance(email, str) or not cls._EMAIL_PATTERN.match(email):
            raise ValueError(f"Некорректный формат email: {email}")

    @property
    def email(self):
        return self.__email

    def set_email(self, new_email):
        self._validate_email(new_email)
        self.__email = new_email

    def set_password(self, new_password):
        self.__password_hash = self._hash(new_password)

    def check_password(self, password):
        return self.__password_hash == self._hash(password)

    def display_info(self):
        print(f"Имя пользователя: {self.username}")
        print(f"Email: {self.__email}")


if __name__ == "__main__":
    user = User("Bob", "tupo123", "bob@example.com")
    user.display_info()

    print(user.check_password("tupo123"))  
    print(user.check_password("wrong"))      

    user.set_password("new_pass")
    print(user.check_password("new_pass"))   

    user.set_email("bnew@mail.ru")
    user.display_info()

    try:
        user.set_email("not-an-email")
    except ValueError as e:
        print("Ошибка:", e)