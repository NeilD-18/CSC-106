cover_price = float(input("What is the cover price of the book?"))
copies = float(input("How many do you want to order?"))

books_sub = (0.60 * cover_price) * copies
books_sub = round(books_sub, 2)

shipping_tot = 3 + ((copies - 1 ) * .75 )
shipping_tot = round(shipping_tot, 2)

total = books_sub + shipping_tot 

print("Books subtotal:", books_sub)
print("Shipping: ", shipping_tot)
print("Total: ", total)