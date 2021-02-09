#!/usr/bin/python3
class Kenya:

    def __int__(self):
        return None

    @staticmethod
    def kenyabanks():

        banks = ['https://org.ke.m-pesa.com',
                 'https://www.pesapap.com',
                 'https://www.azimo.com'
                 ]
        return banks

bank = Kenya
bank.kenyabanks()
print(bank.kenyabanks())
print(bank.kenyabanks().__getitem__(0))
print(bank.kenyabanks().__getitem__(1))
print(bank.kenyabanks().__getitem__(2))


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
        return x

#b = Bag()
#b.add(12)
#print(b.add(12))