case=bin(int(input()))
bin_split=case.split("0b")
rev_bin="0b"
for i in range(len(bin_split)):
    bin_split[i]=bin_split[i][::-1]
    rev_bin+=bin_split[i]
print(int(rev_bin,2))