
class User:
    def __init__(self, first_name, last_name,
                 email, phone_number, password,
                 password_confirm, subscribe,
                 privacy_policy):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.password_confirm = password_confirm
        self.subscribe = subscribe
        self.privacy_policy = privacy_policy

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_password_confirm(self):
        return self.password_confirm

    def set_password_confirm(self, password_confirm):
        self.password_confirm = password_confirm

    def get_subscribe(self):
        return self.subscribe

    def set_subscribe(self, subscribe):
        self.subscribe = subscribe

    def get_privacy_policy(self):
        return self.privacy_policy

    def set_privacy_policy(self, privacy_policy):
        self.privacy_policy = privacy_policy







