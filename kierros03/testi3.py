
def muuta_km_vauhdiksi(minuutit, sekunnit):
    MAILIKERROIN = 1.609344
    km_vauhti = int ((minuutit * 60 + sekunnit) / MAILIKERROIN)
    km_minuutit = km_vauhti // 60
    km_sekunnit = km_vauhti % 60
    return km_minuutit, km_sekunnit




def main():
    rivi = input("Anna nopeuden alarajan minuutit: ")
    maili_min = int(rivi)
    rivi = input("Anna nopeuden alarajan sekunnit: ")
    maili_sek = int(rivi)
    ala_min, ala_s = muuta_km_vauhdiksi(maili_min, maili_sek)
    rivi = input("Anna nopeuden ylarajan minuutit: ")
    maili_min = int(rivi)
    rivi = input("Anna nopeuden ylarajan sekunnit: ")
    maili_sek = int(rivi)
    yla_min, yla_s = muuta_km_vauhdiksi(maili_min, maili_sek)
    print("Suositeltu nopeus on", ala_min, "min", ala_s, "s / km -",
          yla_min, "min", yla_s, "s / km")


main()