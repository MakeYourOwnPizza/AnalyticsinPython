"""
Modify the following google_sector_report so that it returns a json 
dump that contains the following information about each sector:
1. The sector name
2. The percentage change in sector value
3. The biggest gainer and the percentage change in the biggest gainer
4. The biggest loser and the percentage change in the biggest loser

The structure of the json is given in the assignment description on EdX.

Note:
To read files, use:

with open('filename') as f:
    lines = f.readlines()
"""
#import requests
#from bs4 import BeautifulSoup

with open ('sectorpages.txt') as f:
    sectors = f.read().split('\n')
    #print(lines)

def google_sector_report():
    sector_report = dict()
    sectors_list = list()
    
    import requests
    from bs4 import BeautifulSoup

    for sector in sectors:
        try:
            url = sector + ".htm"
        except:
            print("wrong")
            
        response = requests.get(url)
        if response.status_code == 200:
            print("Success")
        else:
            print("Failure")
    return json_string
