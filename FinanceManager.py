from unittest import case
import csv

from unicodedata import category

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

    # def invalid_value(self, input_func):
    #     def output_func(*args):
    #         type = args[1]
    #         while True:
    #             if type == "доход" or type == "расход":
    #                 break
    #             else:
    #                 type = input("Введен несоответствующий тип. Введите 'доход' или 'расход': ")
    #         amount = args[2]
    #         while True:
    #             try:
    #                 amount = int(amount)
    #             except ValueError:
    #                 amount = input("Введено не число. Введите число: ")
    #             else:
    #                 if amount <= 0:
    #                     amount = input("Введено не допустимое значение. Введите положительное число: ")
    #                 else:
    #                     break
    #         category = args[3]
    #         self.input_func(type, amount, category)
    #     return output_func
    #
    # @invalid_value
    def add_transaction(self,type, amount, category):
        if type == "доход":
            self.__balance += int(amount)
            self.book.append([type, amount, category])
        elif type == "расход":
            if self.__balance < int(amount):
                print("Затраченная сумма больше баланса. Введите другую сумму")
            else:
                self.__balance -= int(amount)
                self.book.append([type, amount, category])

    def get_transactions(self):
        return self.book

    def get_balance(self):
      return self.__balance

    def save_data(self):
        with open("transactions.csv", "w", newline="", encoding="UTF-8") as file:
            _list = ["balance", self.__balance]
            writer = csv.writer(file)
            writer.writerow(_list)
            writer.writerows(self.book)

    def load_data(self):
        try:
            with open("transactions.csv", "r", encoding="UTF-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.book.append(row)
                self.__balance = int(self.book[0][1])
                self.book.pop(0)
            print("Данные из файла загружены.")
        except FileNotFoundError:
            print("Данные в файле отсутствуют.")

    def run(self):
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
                    print(row[0], row[1], row[2])
            case 3:
                self.save_data()
                exit()