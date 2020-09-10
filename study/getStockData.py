import FinanceDataReader as fdr

#  한국 시장 리스트 가져오기
krx = fdr.StockListing('KRX')

codeData = krx['Symbol']
title = krx['Name']

# 항목코드, 기준일 ~ 현재
df = fdr.DataReader(codeData[0], '2018-01-01')

# 저장

df.to_csv(codeData[0] + ".csv")
