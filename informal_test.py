import spacy

test_data = [('Từ 24-7 đến 31-7, bệnh nhân được mẹ là bà H.T.P 47 tuổi đón về nhà ở phường Phước Hòa (bằng xe máy), không đi đâu chỉ ra Tạp hóa Phượng, chợ Vườn Lài, phường An Sơn cùng mẹ bán tạp hóa ở đây. ', 
	{'entities': [[4, 7, 'DATE'], [13, 16, 'DATE'], [43, 47, 'NAME'], [49, 50, 'AGE']]})]

# print(test_data[0])

nlp = spacy.load("output/model-best")
doc = nlp('Đâuy là dữ liệu thử nghiệm vào ngày 24-7 ở bệnh viện Hà Nội.')

for ent in doc.ents:
	print (ent.text, ent.label_)