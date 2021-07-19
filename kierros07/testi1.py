
puhelinluettelo = {"Teekkari Teemu": "050-12345", "Fyysikko Tiina":
    "045-234567", "Kemisti Kalle": "040-765432"}

for nimi in puhelinluettelo:
    print("{:16s} {:12s}".format(nimi, puhelinluettelo[nimi]))
