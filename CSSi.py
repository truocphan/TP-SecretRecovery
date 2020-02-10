import time

secret_length = 64
leaks = ["01a", "049", "0b1", "0c5", "12a", "1ad", "1b0", "1c6", "1d1", "2a9", "2ba", "2fd", "3b8", "40c", "489", "494", "4a6", "4b4", "4d4", "4eb", "51b", "57c", "60b", "68c", "69e", "6b6", "740", "77c", "7c9", "7c8", "84a", "851", "897", "8c2", "92f", "94d", "977", "9e0", "9f1", "a68", "a85", "a92", "ad4", "b04", "b1d", "b48", "b69", "b74", "b84", "ba8", "c2b", "c57", "c6b", "c9f", "d1c", "d3b", "d4b", "d4e", "e01", "eb7", "f12", "fd3"]



def secretRecovery(start, leaks):
	print("["+time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))+"] " + start)
	time.sleep(0.2)
	try:
		leaks.remove(start[-3:])
		if len(leaks) == 0:
			print("==> YOUR SECRET IS: {}\n".format(start))
		for j in [i for i in leaks if i[:2] == start[-2:]]:
			start += j[-1]
			secretRecovery(start, leaks)
	except Exception as e:
		print("==> Your secret is not found!!!\n")



if len(leaks) == (secret_length - 2):
	starts = [x for x in leaks if x[:2] not in [y[1:] for y in leaks]]
	for start in starts:
		secretRecovery(start, leaks)
else:
	exit("ERROR!!!")
