# # """
# # ____________Блокировки и обработка ошибок_______________
# #
# #
# # ___________Задача "Банковские операции":_________________
# # Необходимо создать класс Bank со следующими свойствами:
# #
# # """

from threading import Thread, Lock

lock = Lock()


class BankAccount(Thread):

    def __init__(self):
        super().__init__()
        self.amount = 1000


def deposit_task(name, n):
    global lock
    for i in range(5):
        with lock:
            account.amount += n
            print(f'Deposited {n}, {name} {account.amount}')


def withdraw_task(name, n):
    global lock
    for i in range(5):
        with lock:
            account.amount -= n
            print(f'Withdrew {n}, {name} {account.amount}')


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=('new balance is', 100))
withdraw_thread = Thread(target=withdraw_task, args=('new balance is', 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()