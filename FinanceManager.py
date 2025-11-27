from unittest import case
class FinanceManager:
    book = []
    def __init__(self, balance):
        self.__balance = balance

    def __str__(self):
        return f"баланс: {self.__balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def add_transaction(self,type, amount, category):
        if type == "доход":
            self.__balance += int(amount)
            self.book.append({"type": type,"amout": amount,"category": category})
        elif type == "расход":
            if self.__balance < int(amount):
                print("Затраченная сумма больше баланса. Введите другую сумму")
            else:
                self.__balance -= int(amount)
                self.book.append({"type": type,"amout": amount,"category": category})

    def get_transactions(self):
        return self.book

    def get_balance(self):
      return self.__balance

    def save_data(self):
        with open("transactions.txt", "w", encoding="UTF-8") as file:
            file.write(f"balance:{self.__balance}\n")
            for row in self.book:
                file.write(f"{row['type']},{row['amout']},{row['category']}\n")

    def load_data(self):
        with open("transactions.txt", "r", encoding="UTF-8") as file:
            contents = file.readlines()
            sum = contents[0].split(":")
            self.__balance = int(sum[1])
            for i in range (1,len(contents)):
                temp = contents[i].split(",")
                self.book.append({"type": temp[0],"amout": int(temp[1]),"category": temp[2]})

    def run(self):
        # self.load_data()
        try:
            choice = int(input(
            '''
            Выберите действие:
            1. Добавить доход/расход
            2. Показать баланс и транзакции
            3. Сохранить и выйти
            '''
            ))
            if choice not in [1, 2, 3]:
                raise Exception
        except:
            print("Выбран не существующий пункт. Выберите от 1 до 3")
            self.run()
        match choice:
            case 1:
                self.add_transaction(input('Введите тип (доход/расход): '),
                                     input('Введите сумму: '),
                                     input('Введите категорию: '))
            case 2:
                print(f"balance: {self.get_balance()}")
                for row in self.get_transactions():
                    print(f"{row['type']},{row['amout']},{row['category']}")
            case 3:
                self.save_data()
                exit()