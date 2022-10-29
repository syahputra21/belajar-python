# Membuat struk kasir
import datetime

waktu = datetime.datetime.now().strftime("%x")
tanggal = datetime.datetime.now().strftime("%x") 

# nama kasir
namakasir = input("masukkan nama kasir: ")

# tampilan awal
print(f"""
TRIWIJAYA
JL. JEND SUDIRMAN - PASAR BERSAMA
0951-323738/ 0853 54697388

#S-1271529
{tanggal}    {waktu}
============================
          ksr:  {namakasir}
============================
""")
tambahbarang = 'y'
namabarang = 0
totalbarang = 0
jumlahbarang = 0
while('y' in tambahbarang):

# nama barang
namabarang = input("masukkan nama barang: ")

# harga barang
hargabarang = int(input("masukkan harga barang: "))

# jumlah barang
jumlahbarang = int(input("masukkan jumlah barang: "))

# tampilkan barang
print(f"""
{namabarang}
PCS     {jumlahbarang:,}      {hargabarang:,}       {hargabarang * jumlahbarang:,}
""")

tambahbarang = input("Ada barang lagi?(y/n): ")