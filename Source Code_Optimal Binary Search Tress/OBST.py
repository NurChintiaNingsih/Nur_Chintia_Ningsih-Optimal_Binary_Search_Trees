print("Nama     : NUR CHINTIA NINGSIH" )
print("NIM      : 21343011" )
print("MATKUL   : PAA" )
print("PROGRAM  : OPTIMAL BINARY SEARCH TREES" )
# Sebuah Implementasi dari rekursif Naive
# Masalah pohon pencarian biner yang optimal

# Sebuah fungsi rekursif untuk menghitung
# Biaya pohon pencarian biner yang optimal

def optCost(freq, i, j):
	
	# Kasus Dasar
	if j < i:	 # tidak ada elemen di dalam subarray ini
		return 0
	if j == i:	 # tidak ada elemen di dalam subarray ini
		return freq[i]
	
	# Dapatkan Jumlah dari freq[i], freq[i+1], ... freq[j]
	fsum = Sum(freq, i, j)
	
	# Menginisialisasi nilai minimum
	Min = 999999999999
	
	# Satu persatu pertimbangkan semua elemen sebagai
	# akar dan secara rekursif menemukan biaya dari
	# BST(binary search trees), bandingkan biaya nya dengan min
	# dan perbarui min jika diperlukan
	for r in range(i, j + 1):
		cost = (optCost(freq, i, r - 1) +
				optCost(freq, r + 1, j))
		if cost < Min:
			Min = cost
	
	# Mengembalikan Nilai Minimum
	return Min + fsum

# Fungsi Utama yang menghitung Minimum
# Biaya minimun dari Pohon Pencarian Biner. ini terutama
# Menggunakan optCost() untuk menemukan biaya optimal.
def optimalSearchTree(keys, freq, n):
	
	# Disini array keys[] diasumsikan sebagai
	# diurutkan secara berurutan dari kecil ke besar. Jika keys[]
	# tidak diurutkan, tambahkan kode untuk mengurutkan
	# keys, dan atur ulang freq[] sesuai dengan itu.
	return optCost(freq, 0, n - 1)

# Fungsi utilitas untuk mendapatkan jumlah dari
# elemen array freq[i] hingga freq[j]
def Sum(freq, i, j):
	s = 0
	for k in range(i, j + 1):
		s += freq[k]
	return s

# Kode Pengemudi
if __name__ == '__main__':
	keys = [10, 12, 20]
	freq = [34, 8, 50]
	n = len(keys)
	print("Biaya BST Optimal adalah",
		optimalSearchTree(keys, freq, n))
	
