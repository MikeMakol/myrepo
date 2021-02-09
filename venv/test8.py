class Kenya:
    '''A simple example class'''
    i = 12345
    def __init__(self):
        return None

    def kenyabanks (self):
        banks = {"MPesa": "https://org.ke.m-pesa.com",
                "Family Bank": "https://www.pesapap.com"}
        return banks

x = Kenya()
x.kenyabanks()
print(x.kenyabanks())
for bank in x.kenyabanks():
    print(bank)
