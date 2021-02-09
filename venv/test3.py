#class Kenya:
    #def __init__(self):
        #pass

def createAListOfBanks():
    '''This print the passesd in string into this function'''
    kenyabanks = {"Mpesa": "https://org.ke.m-pesa.com",
             "Family Bank": "https://www.pesapap.familybank.com"
            }


    return kenyabanks

print(createAListOfBanks())
for bank in createAListOfBanks():
    print(bank)