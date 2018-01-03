import main

def main(argv):
    testCases = { '+d+=3=+s+' : True, 'f++d+' : False, '+++++++f++d+' : True, '+++++++f++d+++=====+a' : False }

    for testString in testCases:
         assert main.SimpleSymbols(testString) is testCases[testString]
    pass
