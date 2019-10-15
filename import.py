import matematika
def main():
    s = 3
    kel = matematika.KelilingKubus(s)
    vol = matematika.VolumeKubus(s)
    print("KUBUS")
    print("Sisi\t: ", s)
    print("Keliling\t: ", kel)
    print("Volume\t: ", vol)
    p = 10
    l = 8
    t = 6
    kel = matematika.KelilingBalok(p, l, t)
    vol = matematika.VolumeBalok(p, l, t)
    print("\nBALOK")
    print("Panjang\t: ", p)
    print("Lebar\t: ", l)
    print("Tinggi\t: ", t)
    print("Keliling\t: ", kel)
    print("Volume\t: ", vol)
    r = 3
    t = 8
    kel = matematika.KelilingAlasTabung(r)
    vol = matematika.VolumeTabung(r, t)
    print("\nTABUNG")
    print("Jari-jari\t: ", r)
    print("Tinggi\t: ", t)
    print("Keliling\t: ", kel)
    print("Volume\t: ", vol)
if __name__ == "__main__":
    main()
