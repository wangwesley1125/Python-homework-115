url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'

protocol, separator, rest_of_url = url.partition('://')

host, separator, document_with_path = rest_of_url.partition('/')

print(host)

path, separator, document = document_with_path.rpartition('/')

print(path)