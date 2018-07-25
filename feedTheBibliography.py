import requests
baseURL = 'http://dx.doi.org/'
outputFile = 'testOutput.bib'
headers={'Accept':'application/x-bibtex'}

# main loop
while True:
    inp = input('DOI: ')
    response = requests.get(baseURL+inp, headers=headers)
    if response.ok:
        with open(outputFile,'a') as output:
            output.write(response.text)
    else:print('There was an issue getting the bibtex.')
    again = input('more? ("e" to exit)')
    if again == 'e':break
