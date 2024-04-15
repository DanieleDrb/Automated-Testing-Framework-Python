from faker import Faker

from utilities.user import User


class UserFactory:

    def create_default(self):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        default_password = "ilovemydogpaco"
        password = default_password
        password_confirm = default_password
        subscribe = False
        privacy_policy = True

        return User(first_name, last_name, email,
                       phone_number, password, password_confirm,
                       subscribe, privacy_policy)
