disk_capacity_mb = 1.44  
pages_in_book = 100 
lines_per_page = 50 
chars_in_line = 25  
bytes_in_char = 4 

disk_capacity_bytes = 1.44 * 1024 * 1024 
print('Книг помещается на дискету: ', disk_capacity_bytes//(pages_in_book * lines_per_page * chars_in_line * bytes_in_char))
