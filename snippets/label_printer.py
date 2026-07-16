import barcode
from barcode.writer import ImageWriter

def generate_barcode(data):
    # Choose the type of barcode (e.g., 'ean13', 'upca', etc.)
    EAN = barcode.get('ean13', data, writer=ImageWriter())
    
    # Save the barcode as an image file
    filename = EAN.save('barcode')
    print(f"Barcode generated and saved as {filename}")

# Example usage:
generate_barcode("5901234123457")