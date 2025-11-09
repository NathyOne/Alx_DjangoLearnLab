# delete a specific 
# DELETE
book = Book.objects.get(id=1)
book.delete()