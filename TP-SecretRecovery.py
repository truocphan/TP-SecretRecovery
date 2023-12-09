import sys
from datetime import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--data-leaked", required=True, type=str, help="The string consisting of concatenated pairs of three characters exfiltrated from the string SECRET")
parser.add_argument("--startsWith", type=str, help="The starting character string of the string SECRET")
parser.add_argument("--endsWith", type=str, help="The ending character string of the string SECRET")
parser.add_argument("--number-of-reuses", type=int, help="The number of reuses of each element in the data_leaked array (default: 3)")
args = parser.parse_args()

# data_leaked = ["051", "0bc", "0bb", "192", "1f4", "28b", "2da", "339", "37d", "39b", "3f4", "3f6", "465", "4b3", "4e2", "51f", "53f", "56a", "5d7", "5e6", "605", "60b", "65e", "666", "66e", "6a1", "6ad", "6ee", "756", "760", "7d5", "853", "8b8", "92d", "93f", "9b7", "9ba", "a14", "a37", "a9b", "ab0", "ad9", "b0b", "b33", "b75", "b85", "bab", "ba9", "bba", "bc6", "c66", "d5d", "d76", "d93", "da3", "e28", "e4e", "e60", "ee4", "f46", "f4b", "f6a"]
# data_leaked = '0510bc0bb1921f428b2da33937d39b3f43f64654b34e251f53f56a5d75e660560b65e66666e6a16ad6ee7567607d58538b892d93f9b79baa14a37a9bab0ad9b0bb33b75b85babba9bbabc6c66d5dd76d93da3e28e4ee60ee4f46f4bf6a'
# data_leaked = "".join(list(set([SECRET[i:i+3] for i in range(len(SECRET)-2)])))
data_leaked = [args.data_leaked[i:i+3] for i in range(0, len(args.data_leaked), 3)]
startsWith = args.startsWith if args.startsWith else ""
endsWith = args.endsWith if args.endsWith else ""

if args.number_of_reuses == None:
	number_of_reuses = 3
else:
	number_of_reuses = args.number_of_reuses
	if number_of_reuses <= 0:
		parser.print_help()
		exit("\n\x1b[1;31m"+sys.argv[0]+": error: argument --number-of-reuses: must be positive\x1b[0m")


def SecretRecovery(start, leaked, leaks_used):
	print("[\x1b[34m"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\x1b[0m] " + "The SECRET retrieved: \x1b[33m{}\x1b[0m".format(start))
	# Xoa bo 3 ky tu da tim duoc khoi leaked va luu so lan su dung vao leaks_used
	if start[-3:] in leaked:
		leaks_used[start[-3:]] = 1
		leaked.remove(start[-3:])
	# Neu leaked khong con bo 3 ky tu nao thi luc nay gia tri start co the la SECRET can tim
	if len(leaked) == 0:
		if start.endswith(endsWith):
			SECRETS.append(start)
			print("[\x1b[34m"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\x1b[0m] " + "\x1b[32m==> THIS IS A SECRET.\x1b[0m\n")
		else:
			print("[\x1b[34m"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\x1b[0m] " + "\x1b[31m==> This is not a SECRET\x1b[0m\n")
	# Neu leaked van con thi tiep tuc tim cac ky tu ke tiep de tao thanh SECRET
	else:
		# Bo 3 ky tu ke tiep phai co 2 ky tu dau trung voi 2 ky tu cuoi cua gia tri start
		next = [i for i in leaked if i[:2] == start[-2:]]
		# Neu khong co bo 3 ky tu nao trong leaked thoa dieu kien thi thi kiem tra tiep trong leaks_used
		if len(next) == 0:
			# Bo 3 ky tu ke tiep phai co 2 ky tu dau trung voi 2 ky tu cuoi cua gia tri start va chi duoc su dung toi da lan
			next_ = [i for i in leaks_used.keys() if i[:2] == start[-2:] and leaks_used[i] <= number_of_reuses]
			# Neu khong co bo 3 ky tu nao trong leaks_used thoa dieu kien thi gia tri start se cham dut va khong phai la SECRET
			if len(next_) == 0:
				print("[\x1b[34m"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\x1b[0m] " + "\x1b[31m==> This is not a SECRET\x1b[0m\n")
			# Nguoc lai, neu co thi lap qua tung bo 3 ky tu thoa dieu kien tren
			else:
				for i in next_:
					# Tang gia tri cua bo 3 ky tu da dung len 1 mot don vi
					leaks_used[i] += 1
					SecretRecovery(start + i[-1], leaked[:], leaks_used)
		# Nguoc lai, neu co thi lap qua tung bo 3 ky tu thoa dieu kien tren
		else:
			for i in next:
				SecretRecovery(start + i[-1], leaked[:], leaks_used)


SECRETS = list()
# Xac dinh truoc chuoi ky tu bat dau cua SECRET
if startsWith:
	leaks_used = {}
	for i in range(len(startsWith)-2):
		if startsWith[i:i+3] in data_leaked:
			if i < len(startsWith)-3:
				leaks_used[startsWith[i:i+3]] = 1
				data_leaked.remove(startsWith[i:i+3])
		else:
			if startsWith[i:i+3] in leaks_used.keys() and leaks_used[startsWith[i:i+3]] <= number_of_reuses:
				leaks_used[startsWith[i:i+3]] += 1
			else:
				exit("[\x1b[34m"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\x1b[0m] " + "\x1b[31mThe SECRET does not start with \"\x1b[1;31m{}\x1b[0m\x1b[31m\"\x1b[0m".format(startsWith[:i+3]))
	SecretRecovery(startsWith, data_leaked[:], leaks_used)
# Gia su moi bo 3 ky tu trong data_leaked la 3 ky tu bat dau cua SECRET, sau do Brute force 
else:
	for startsWith in data_leaked:
		SecretRecovery(startsWith, data_leaked[:], {})

print("[\x1b[34m"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\x1b[0m] " + "\x1b[32mThe SECRET has been recovered:\x1b[0m")
for secret in SECRETS:
	print(" - \x1b[33m{}\x1b[0m".format(secret))
