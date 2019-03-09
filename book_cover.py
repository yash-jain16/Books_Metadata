import IPython
import json
import pprint as pprint
import urllib.request
isbn_arr=[]
json_data=open("""Path to the location of json file containing isbn number""").read()

data = json.loads(json_data)
for k in data:
	isbn_arr.append(k["isbn"])


#print(isbn_arr[0][0])
url = 'http://covers.openlibrary.org/b/isbn/'+isbn_arr[0][0]+'-L.jpg'
IPython.display.Image(url, width = 250)