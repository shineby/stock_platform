import matplotlib.pyplot as plt
import OpenDartReader




# FinanceDataReaader : 한국주식,미국주식,환율,암호화폐가격 수집 라이브러리
# https://financedata.github.io/posts/finance-data-reader-users-guide.html
import FinanceDataReader as fdr




class StockReader:
    def __init__(self):
        file = open("c:/dart_api_key.txt", "r")
        api_key = file.readline()
        self.dart = OpenDartReader(api_key)

    def test(self):
        print(self.dart.list('005930', kind='A', start='2020-01-01', ))

    def read_price(self, code):
        return fdr.DataReader(code)