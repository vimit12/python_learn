class Bank:
    __ifsc_code = "ICIC0000591"
    _MICR = "MICR1213JKJ21312"

    def __init__(self, pin, account_type):
        self.pin = pin
        self.__account_type = account_type
        self._bank_name = "ICICI"


class User(Bank):

    def __init__(self, name, pin, account_type="Saving"):
        super().__init__(pin, account_type)
        self.name = name

    def user_detail(self):
        print(f"User Detail is - \n User name : {self.name} \n pin : {self.pin}")
        print("Account type : ", self._Bank__account_type)
        print("Branch Name : ", self._bank_name)
        print("IFSC CODE : ", self._Bank__ifsc_code)
        print("MICR CODE : ", Bank._MICR)


def main():
    obj = User("Vimit", 1234, "Current")
    obj.user_detail()


if __name__ == '__main__':
    main()
