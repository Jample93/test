from pandas_datareader import data
# '035420.KS' = Naver종목코드.KospiCode


naver = data.get_data_yahoo('003490.KS') #6자리 주식종목 코드 입력
print(naver.head())
print(naver.tail())

naver.to_csv('naver.csv')
naver.to_pickle('naver.pickle')

naver.to_excel('naver.xlsx')