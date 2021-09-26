# https://github.com/josw123/dart-fss
# 한국 금융감독원에서 운영하는 다트(Dart)시스템 크롤링 라이브러리
import dart_fss as dart
import FinanceDataReader as fdr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ticker_map = dict()
# KEY: Ticker,
# LIST: [<Data Source>, <설명>]

class FDR:
    def __init__(self):
        file = open("c:/dart_api_key.txt", "r")
        self.api_key = file.readline()
        self._dart = dart
        self._dart.set_api_key(self.api_key)

    def loadData(self, asset_list_stock: list, stock_column: str, asset_list_fred: dict, start: str, end: str) -> pd.DataFrame:
        '''
        :param asset_list_stock: ticker list which does not use <DataSource>
        :param asset_list_fred: ticker list which does uses <Fred>
        :param start: start date
        :param end: end date
        :return: data frame
        '''
        if not asset_list_fred and asset_list_stock.empty:
            return

        if asset_list_fred:
            if not asset_list_stock:
                close_df = pd.DataFrame()

            df_list = []
            for idx in asset_list_fred.keys():
                # print(fdr.DataReader(asset_list_fred[idx], start, end, data_source='fred'))
                df = fdr.DataReader(asset_list_fred[idx], start, end, data_source='fred')

                df_list.append(df)

            fred_df = pd.concat(df_list, axis=1)
            ret_df = fred_df

        if asset_list_stock:
            raw = self.get_data_multiple_stocks(asset_list_stock, start, end, source="")
            stock_df = self.pivot_tickers_to_columns(raw, stock_column)
            ret_df = pd.concat([fred_df, stock_df], axis=1)


        return ret_df

    def show_corrImage(self, df: pd.DataFrame, start: str, end: str):
        plt.figure(figsize=(10, 7))
        corr_df = df.corr()
        sns.heatmap(corr_df, annot=True, cmap="Greens")
        plt.title(start + " ~ " + end)
        plt.show()

    def save_to_excel(self, df: pd.DataFrame, start: str, end: str):
        # save excel file
        file_name = start + "_" + end + ".xlsx"
        df.to_excel(file_name, sheet_name=start)

    def get_data_multiple_stocks(self, tickers: str, start: str, end: str, source: str) -> dict:
        '''
        return dict adding 'Ticker' at the first
        dict = [Ticker: Str, DataFrame of Ticker: DataFrame]
        '''
        stocks = dict()

        for ticker in tickers:
            df = self.get_stock_data(ticker, start, end, source=source)
            stocks[ticker] = df
        return stocks

    def get_stock_data(self, ticker: str, start: str, end: str, source: str) -> pd.DataFrame:
        print("Reading Ticker ({}): From({}) to ({})".format(ticker, start, end))
        data = fdr.DataReader(ticker, start, end, data_source=source)
        data.insert(0, "Ticker", ticker)
        return data

    def pivot_tickers_to_columns(self, raw: dict, column: str) -> pd.DataFrame:
        items = []

        for key in raw:
            ticker_df = raw[key]
            subset = ticker_df[['Ticker', column]]
            items.append(subset)

        combined = pd.concat(items)
        ri = combined.reset_index()
        return ri.pivot("Date", "Ticker", column)

    def get_data_corr(self, df: pd.DataFrame):
        corr_df = df.corr()
        return corr_df
