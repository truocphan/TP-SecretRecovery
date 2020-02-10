import time

data_leaks = ["051", "0bc", "0bb", "192", "1f4", "28b", "2da", "339", "37d", "39b", "3f4", "3f6", "465", "4b3", "4e2", "51f", "53f", "56a", "5d7", "5e6", "605", "60b", "65e", "666", "66e", "6a1", "6ad", "6ee", "756", "760", "7d5", "853", "8b8", "92d", "93f", "9b7", "9ba", "a14", "a37", "a9b", "ab0", "ad9", "b0b", "b33", "b75", "b85", "bab", "ba9", "bba", "bc6", "c66", "d5d", "d76", "d93", "da3", "e28", "e4e", "e60", "ee4", "f46", "f4b", "f6a"]

def secretRecovery(start, leaks):
	print("["+time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))+"] " + start)
	time.sleep(0.1)
	# Xoa bo 3 ky tu da tim duoc khoi data_leaks
	leaks.remove(start[-3:])
	# Neu data_leaks khong con bo 3 ky tu nao thi luc gia tri start co the la SECRET can tim
	if len(leaks) == 0:
		secret.append(start)
		print("==> THIS IS A SECRET.\n")
	# Neu data_leaks van con thi tiep tuc tim cac ky tu ke tiep de tao thanh SECRET
	else:
		# Bo 3 ky tu ke tiep phai co 2 ky tu dau trung voi 2 ky tu cuoi cua gia tri start
		next = [i for i in leaks if i[:2] == start[-2:]]
		# Neu khong co bo 3 ky tu nao thoa dieu kien thi gia tri start se cham dut va khong phai la SECRET
		if len(next) == 0:
			print("==> This is not a secret!!!\n")
		# Nguoc lai, neu co thi lap qua tung bo 3 ky tu thoa dieu kien tren
		else:
			for i in next:
				secretRecovery(start + i[-1], leaks[:])



secret = list()
# Tim bo 3 ky tu bat dau cua SECRET tu data_leaks (2 ky tu dau khong duoc trung voi 2 ki tu cuoi cua cac bo 3 ky tu con lai trong data_leaks)
start = [x for x in data_leaks if x[:2] not in [y[1:] for y in data_leaks]]
# Neu ton tai
if len(start) == 1:
	secretRecovery(start[0], data_leaks[:])
	print("YOUR SECRET IS:")
	for i in secret:
		print("[+] " + i)
# Neu khong thi gia su tung bo 3 ky tu trong data_leaks la bo 3 ky tu bat dau cua SECRET, sau do Brute force 
else:
	for start in data_leaks:
		secretRecovery(start, data_leaks[:])
		print("YOUR SECRET IS:")
		for i in secret:
			print("[+] " + i)
