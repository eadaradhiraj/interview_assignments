#For an analysis parameter k, a group of k consecutive months
#is said to be highly profitable if the values of the
#stock prices are strictly increasing for those months.
#Given the stock prices of the company for n months and
#the analysis parameter k, find the number of highly profitable months

def highly_profitable_months(stocks: list, k: int) -> int:
    seq_ln, seqs = 1, []
    for i in range(1,(len(stocks))):
        if stocks[i-1] < stocks[i]:
            seq_ln += 1
        else:
            if seq_ln >= k:
                seqs.append(seq_ln)
            seq_ln = 1
    if seq_ln >= k:
        seqs.append(seq_ln)
    cnt = 0
    for seq_ln in seqs:
        cnt += (seq_ln - k) + 1
    return (cnt)

print(
  highly_profitable_months(stocks=[5,3,5,7,8],k=3)
)
print(
  highly_profitable_months(stocks=[1,2,3,3,4,5],k=3)
)
