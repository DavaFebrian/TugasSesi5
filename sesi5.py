def calculate_ticket_price(age, height):
    if age < 2:
        return "Dilarang masuk"
    elif age < 4:
        ticket_price = 30000
        if height > 70:
            ticket_price += 10000
    elif age < 7:
        ticket_price = 40000
        if height > 120:
            ticket_price += 15000
    elif age < 10:
        ticket_price = 50000
        if height > 150:
            ticket_price += 20000
    else:
        ticket_price = 80000
    
    return f"Tarif harga: Rp {ticket_price:,}"

# Masukkan umur dan tinggi anak
age = int(input("Masukkan umur anak: "))
height = int(input("Masukkan tinggi anak (cm): "))

# Hitung dan tampilkan tarif harga
ticket_price = calculate_ticket_price(age, height)
print(ticket_price)
