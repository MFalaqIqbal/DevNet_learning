import requests
import urllib.request
import json
import time

url = "http://localhost:8080/v1/books"

books = {
  "name": "The Art of Computer Programming",
  "authors": ["Donald Knuth"],
  "date": 1996,
  "isbn": "0-201-03801-3",
  "Test": "Yellow Ranger"
}
books_2 = {
  "name": "Book 1",
  "authors": ["1", "2"],
  "date": 2222,
  "isbn": "0-000-0000-0"
}
def response_used():
  response = requests.post(url, json=books)
  print(response.json())
  return
  
def url_used():
  payload = json.dumps(books).encode('utf8')
  request = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
  response = urllib.request.urlopen(request)
  print(response.status)
  return 

def book_put():
  response = requests.post(url, json=books_2)
  book_data = response.json()
  print(json.dumps(book_data, indent=4))
  ''' Update Authors '''
  book_data["authors"] = ["45"]
  update_book_url = "https://localhost:8080/v1/books/{}".format(book_data['uuid'])
  print(update_book_url)
  response_2 = requests.put(update_book_url, json=book_data)
  return
  
def book_delete():
  response = requests.post(url, json=books_2)
  book_data = response.json()
  update_book_url = "https://localhost:8080/v1/books/{}".format(book_data['uuid'])
  print(update_book_url)
  response = requests.delete(update_book_url)
  return

if __name__ == '__main__':
  response_used()
  url_used()
  book_put()
  book_delete()
  
  
  
  
  
  
  