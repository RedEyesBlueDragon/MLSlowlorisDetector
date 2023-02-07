import csv
import pandas as pd



df = pd.read_csv('dataset/dat.csv')
lst = ["10.128.0.1",   "10.128.0.2",   "10.128.0.3",   "10.128.0.4",   "10.128.0.5",   "10.128.0.6",   "10.128.0.7",   "10.128.0.8",   "10.128.0.9",   "10.128.0.10",   "10.128.0.11",   "10.128.0.12",   "10.128.0.13",   "10.128.0.14",   "10.128.0.15",   "10.128.0.16",   "10.128.0.17",   "10.128.0.18",   "10.128.0.19",   "10.128.0.20",   "10.128.0.21",   "10.128.0.22",   "10.128.0.23",   "10.128.0.24",   "10.128.0.25",   "10.128.0.26",   "10.128.0.27",   "10.128.0.28",   "10.128.0.29",   "10.128.0.30",   "10.128.0.31",   "10.128.0.32",   "10.128.0.33",   "10.128.0.34",   "10.128.0.35",   "10.128.0.36",   "10.128.0.37",   "10.128.0.38",   "10.128.0.39",   "10.128.0.40",   "10.128.0.41",   "10.128.0.42",   "10.128.0.43",   "10.128.0.44",   "10.128.0.45",   "10.128.0.46",   "10.128.0.47",   "10.128.0.48",   "10.128.0.49",   "10.128.0.50"  ] + ["10.128.0.100",   "10.128.0.101",   "10.128.0.102",   "10.128.0.103",   "10.128.0.104",   "10.128.0.105",   "10.128.0.106",   "10.128.0.107",   "10.128.0.108",   "10.128.0.109",   "10.128.0.110",   "10.128.0.111",   "10.128.0.112",   "10.128.0.113",   "10.128.0.114",   "10.128.0.115",   "10.128.0.116",   "10.128.0.117",   "10.128.0.118",   "10.128.0.119",   "10.128.0.120",   "10.128.0.121",   "10.128.0.122",   "10.128.0.123",   "10.128.0.124",   "10.128.0.125",   "10.128.0.126",   "10.128.0.127",   "10.128.0.128",   "10.128.0.129",   "10.128.0.130",   "10.128.0.131",   "10.128.0.132",   "10.128.0.133",   "10.128.0.134",   "10.128.0.135",   "10.128.0.136",   "10.128.0.137",   "10.128.0.138",   "10.128.0.139",   "10.128.0.140",   "10.128.0.141",   "10.128.0.142",   "10.128.0.143",   "10.128.0.144",   "10.128.0.145",   "10.128.0.146",   "10.128.0.147",   "10.128.0.148",   "10.128.0.149",   "10.128.0.150"]
attack = df.loc[(df["Source"].isin( lst))]

atckLst = attack.Destination.unique().tolist()
ipUniq = df.Source.unique().tolist()
ipUniq2 = ipUniq
#print(ipUniq)

data = []

column_names = ['Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info', 'Label']

with open('dataset/output.csv', 'a', newline='') as csvfile:
    # Create a CSV writer
	writer = csv.writer(csvfile)
	nbr = 0
    # Write the column names to the CSV file only if the file is empty
	if csvfile.tell() == 0:
		writer.writerow(column_names)

	for src in ipUniq:
		ipUniq2.remove(src)
		for dst in ipUniq2:
			if src != dst:
				print("-------" + src + " " + dst)
				tmp = df[((df["Source"] == src) & (df["Destination"] == dst)) | ((df["Source"] == dst) & (df["Destination"] == src))]
				count = 30
				if tmp.shape[0] > 30:
					dfTmp = tmp.iloc[: count,:]
					#print("data")
					tmpLst = [dfTmp["Time"].tolist(), dfTmp["Source"].tolist(), dfTmp["Destination"].tolist(), dfTmp["Protocol"].tolist(), dfTmp["Length"].tolist(), dfTmp["Info"].tolist()]
					if src in lst or dst in lst:
						tmpLst.append("1")
					else:
						tmpLst.append("0")	
					writer.writerow(tmpLst)
					nbr += 1
					print(nbr)
					count = 15 + count
				if tmp.shape[0] > 45:
					dfTmp = tmp.iloc[15: count,:]
					#print("data")
					tmpLst = [dfTmp["Time"].tolist(), dfTmp["Source"].tolist(), dfTmp["Destination"].tolist(), dfTmp["Protocol"].tolist(), dfTmp["Length"].tolist(), dfTmp["Info"].tolist()]
					if src in lst or dst in lst:
						tmpLst.append("1")
					else:
						tmpLst.append("0")	
					writer.writerow(tmpLst)
					nbr += 1
					print(nbr)
					count = 15 + count						
						#print(tmpLst)
				
				if tmp.shape[0] > 60:
					dfTmp = tmp.iloc[30: count,:]
					#print("data")
					tmpLst = [dfTmp["Time"].tolist(), dfTmp["Source"].tolist(), dfTmp["Destination"].tolist(), dfTmp["Protocol"].tolist(), dfTmp["Length"].tolist(), dfTmp["Info"].tolist()]
					if src in lst or dst in lst:
						tmpLst.append("1")
					else:
						tmpLst.append("0")	
					writer.writerow(tmpLst)
					nbr += 1
					print(nbr)
					count = 15 + count	

				if tmp.shape[0] > 75:
					dfTmp = tmp.iloc[45: count,:]
					#print("data")
					tmpLst = [dfTmp["Time"].tolist(), dfTmp["Source"].tolist(), dfTmp["Destination"].tolist(), dfTmp["Protocol"].tolist(), dfTmp["Length"].tolist(), dfTmp["Info"].tolist()]
					if src in lst or dst in lst:
						tmpLst.append("1")
					else:
						tmpLst.append("0")	
					writer.writerow(tmpLst)
					nbr += 1
					print(nbr)
					count = 30 + count							
						#print(tmpLst)
				
    

















