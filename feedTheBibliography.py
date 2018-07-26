import requests
import re
baseURL = 'http://dx.doi.org/'
outputFile = 'testOutput.bib'
headers={'Accept':'application/x-bibtex'}
pattern='{[a-zA-Z0-9_]+,'
regexID = re.compile(pattern)
regexDOI = re.compile('doi = {[a-zA-Z0-9/.]+}')
# main loop
while True:
    inp = input('DOI: ')
    response = requests.get(baseURL+inp, headers=headers)
    if response.ok:
        print(response.text)
        baseInput= response.text
        findID = regexID.search(baseInput)
        findDOI = regexDOI.search(baseInput)

        newBIB = baseInput[:findID.start()+1] + findDOI.group(0)[6:-1] + baseInput[findID.end()-1:]
        print(newBIB)
        with open(outputFile,'a') as output:
            output.write(newBIB)
    else:print('There was an issue getting the bibtex.')
    again = input('more? ("e" to exit)')
    if again == 'e':break
