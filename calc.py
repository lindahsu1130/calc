data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 100000 == 0: 
			print(len(data))
	print('檔案讀取完了','總共有',len(data),'筆資料')
sum_len = 0
for d in data:
	sum_len += len(d)
print('每筆留言的平均長度為',sum_len/len(data))
