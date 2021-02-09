import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Ha HaHa

MetaCharacters (Need to be escaped)
. ^ $ * + ? {} [] \ | ()

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
url = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.findall(text_to_search)

for match in matches:
    print(match)

