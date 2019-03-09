import pprint
import sys
from apiclient.discovery import build

api_key="""Enter API key"""
service = build('books', 'v1', developerKey=api_key)
request = service.volumes().list(source='public', q="""Enter book name or isbn""")
response = request.execute()
#pprint.pprint(response)
print ('Found %d books:' % len(response['items']))
for book in response.get('items', []):
    try:
      print ('Title: %s, Authors: %s, Description: %s, Rating: %s' % (
        book['volumeInfo']['title'],
        book['volumeInfo']['authors'],											
        book['volumeInfo']['description'],
        book['volumeInfo']['averageRating']))
      #other meta information can be fetched in similar fashion like date of publish, language, piblisher, etc
    except KeyError:
        print("Key error occured!!!!!!!!!!")
