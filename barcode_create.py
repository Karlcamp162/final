import barcode
from barcode.writer import ImageWriter

# Define the data to encode in the barcode
data1 = "480110123456"
data2 = "480110654321"
data3 = "480110231456"
data4 = "480110236541"
data5 = "480110231234"

# Create a Code128 barcode object
code121 = barcode.get('code128', data1, writer=ImageWriter())
code122 = barcode.get('code128', data2, writer=ImageWriter())
code123 = barcode.get('code128', data3, writer=ImageWriter())
code124 = barcode.get('code128', data4, writer=ImageWriter())
code125 = barcode.get('code128', data5, writer=ImageWriter())

# Save the barcode as an image file
filename1 = code121.save('barcode1')
filename2 = code122.save('barcode2')
filename3 = code123.save('barcode3')
filename4 = code124.save('barcode4')
filename5 = code125.save('barcode5')

print(f"Barcode saved as {filename1}.png")
