from FinanceManager import *

if __name__ == '__main__':
    object = FinanceManager(1000)
    object.load_data()
    while True:
        object.run()