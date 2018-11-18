class User:
    def __init__(self, name, age, country):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country

    def display_profile(self):  # 引数なし
        # display_profile()はUserクラスのインスタンスメソッド
        print(f"{self.name} 国籍: {self.country} {self.age}歳")

    def change_nationality(self, country_name):  # 引数あり
        self.country = country_name


if __name__ == "__main__":
    bob = User("Bob", 15, "USA")
    bob.display_profile()
    bob.change_nationality("China")
    bob.display_profile()

    tom = User("Tom", 57, "USA")
    tom.display_profile()
    tom.change_nationality("JP")
    tom.display_profile()

    ken = User("Ken", 49, "JP")
    ken.display_profile()
    ken.change_nationality("ITA")
    ken.display_profile()
