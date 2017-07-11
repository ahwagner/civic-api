import requests
import json

ras_genes = [
    'AKT1',
    'AKT2',
    'AKT3'
]

req = requests.get("https://civic.genome.wustl.edu/api/genes")
data = req.json()
next_page = data['_meta']['links']['next']
print(next_page)

#Alex notes: could use list comprehension (lines 16-18), represent more compactly in python
#Susanna: remove redundancy of req/page lines
while next_page is not None:
    for genes in data['records']:
        if genes['name'] in ras_genes:
            print(genes['name'])
    req = requests.get(next_page)
    data = req.json()
    print(data)
    next_page = data['_meta']['links']['next']
    print(next_page)

