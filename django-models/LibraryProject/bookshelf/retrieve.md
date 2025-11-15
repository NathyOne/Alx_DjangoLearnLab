# retreive all books 
book = Book.objects.all()

# get using specific 
book = Book.objects.get(title="1984")
