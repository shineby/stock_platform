import FinanceDataReader as fdr
from Investar import DBUpdaterEx
# from Investar import MarketDB
from Investar import Analyzer
from DataReader import DartFss
import matplotlib.pyplot as plt
import FinanceDataReader as fdr
import pandas as pd
from datetime import datetime


class TickerName:
    STOCK_COLUME_CLOSE = 'Close'
    STOCK_COLUME_VOLUME = 'Volume'

    NONE_KS11 = ['KS11', 'none', 'KOSPI Index']
    NONE_USD_KRW = ['USD/KRW', 'none', '달러/원 환율']
    NONE_GLD = ['GLD', 'none', 'Gold']
    NONE_SP500 = ['GSPC', 'none', 'S&P500 index']
    NONE_SPY = ['SPY', 'none', 'SPY ETF']
    NONE_DBC = ['DBC', 'none', '상품/원자재 ETF']
    NONE_VTIP = ['VTPS', 'none', 'short term TIPS']
    NONE_TLT = ['TLT', 'none', 'Y20+ Treasury Bond ETF']
    NONE_IEF = ['IEF', 'none', 'Y7~10 Treasury Bond ETF']
    NONE_SHY = ['SHY', 'none', 'Y1~3 Treasury Bond ETF']
    NONE_VIX = ['VIX', 'none', 'VIX']
    NONE_VNQ = ['VNQ', 'none', 'REIT ETF']
    NONE_VYM = ['VYM', 'none', 'Dividend ETF']
    NONE_SPYV = ['SPYV', 'none', 'SPY Value']
    NONE_SPYG = ['SPYG', 'none', 'SPY Growth']
    NONE_SPYD = ['SPYD', 'none', 'SPY Dividend']
    NONE_VTIP = ['VTIP', 'none', 'Short Term TIP']

    # FRED
    FRED_T10Y2Y = ['T10Y2Y', 'fred', '10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity']
    FRED_NASDAQ = ['NASDAQCOM', 'fred', 'NASDAQ Composite Index']
    FRED_PCE = ['PCE', 'fred', 'Personal Comsumption Expenditure (개인소비지출)']
    FRED_T10YIE = ['T10YIE', 'fred', '10Y Breakeven Inflation Rate']
    FRED_REALGDP = ['GDP', 'fred', 'Real Gross Domestic Product']
    FRED_UMCSENT = ['UMCSENT', 'fred', 'University of Michigan: Consumer Sentiment ']
    FRED_CSHOMEPRICE = ['CSUSHPINSA', 'fred', 'Case-Shiller U.S. National Home Price Index ']
    FRED_HDTGPDUSQ163N = ['HDTGPDUSQ163N', 'fred', 'Household Debt to GDP for United States']
    FRED_HIGHYIELD = ['BAMLH0A0HYM2EY', 'fred', 'High Yield']
    # 실업률
    FRED_UNRATE = ['UNRATE', 'fred', 'Unemployment Rate']
    # 신규 주택 개발 시작건수
    FRED_HOUST = ['HOUST', 'fred', 'New Privately-Owned Housing Units Started: Total Units']
    # 신규 주택 판매 건 수
    FRED_NEWHOMESALE = ['HSN1F', 'fred', 'US New Home Sale']

    def __init__(self):
        pass


def main():
    _fdr = DartFss.FDR()

    # Load Data

    #====================================================================================
    # Correlation
    #====================================================================================
    start = '2010.01.01'
    end = '2021.9.22'

    stock = [TickerName.NONE_KS11[0],
             TickerName.NONE_SPY[0],
             TickerName.NONE_SPYG[0],
             TickerName.NONE_SPYD[0],
             TickerName.NONE_VYM[0],
             TickerName.NONE_SPYV[0],
             TickerName.NONE_VNQ[0],
             TickerName.NONE_VTIP[0],
             TickerName.NONE_SHY[0],
             TickerName.NONE_VTIP[0],
             TickerName.NONE_IEF[0],
             TickerName.NONE_TLT[0],
             TickerName.NONE_VIX[0],
             TickerName.NONE_DBC[0],
             TickerName.NONE_USD_KRW[0],
             TickerName.NONE_GLD[0]
             ]

    fred = {TickerName.FRED_T10Y2Y[0]: TickerName.FRED_T10Y2Y[0],
            TickerName.FRED_NASDAQ[0]: TickerName.FRED_NASDAQ[0],
            TickerName.FRED_PCE[0]: TickerName.FRED_PCE[0],
            TickerName.FRED_REALGDP[0]: TickerName.FRED_REALGDP[0],
            TickerName.FRED_UMCSENT[0]: TickerName.FRED_UMCSENT[0],
            TickerName.FRED_UNRATE[0]: TickerName.FRED_UNRATE[0],
            TickerName.FRED_T10YIE[0]: TickerName.FRED_T10YIE[0]
            }

    # df = _fdr.loadData(asset_list_stock=stock, stock_column= 'Close', asset_list_fred=fred, start=start, end=end)
    # _fdr.show_corrImage(df, start, end)

    #====================================================================================
    # Time Series
    #====================================================================================
    start = '2021.01.01'
    end = '2021.09.25'

    stock = []
    # stock = [TickerName.NONE_SP500[0]]

    fred = {TickerName.FRED_HOUST[0]: TickerName.FRED_HOUST[0],
            TickerName.FRED_PCE[0]: TickerName.FRED_PCE[0],
            TickerName.FRED_T10Y2Y[0]: TickerName.FRED_T10Y2Y[0],
            TickerName.FRED_HIGHYIELD[0]: TickerName.FRED_HIGHYIELD[0],
            TickerName.FRED_UMCSENT[0]: TickerName.FRED_UMCSENT[0],
            TickerName.FRED_HDTGPDUSQ163N[0]: TickerName.FRED_HDTGPDUSQ163N[0],
            TickerName.FRED_UNRATE[0]: TickerName.FRED_UNRATE[0],
            TickerName.FRED_NASDAQ[0]: TickerName.FRED_NASDAQ[0]}
    df = _fdr.loadData(asset_list_stock=stock, stock_column='Close', asset_list_fred=fred, start=start, end=end)
    filled = df.fillna(method="ffill")


    fig, ax = plt.subplots(nrows=4)
    # Area
    # span_start = datetime(2007, 4, 1)
    # span_end = datetime(2009, 5, 1)
    # for i in ax:
    #    i.axvspan(span_start, span_end, facecolor='gray', alpha=0.5)

    # Plot #1
    filled[[TickerName.FRED_HOUST[0], TickerName.FRED_NASDAQ[0]]].plot(secondary_y=TickerName.FRED_HOUST[0], ax=ax[0])
    plt.axhline(y=filled[TickerName.FRED_HOUST[0]].mean(), color='red', linestyle='--')
    plt.title(start + " ~ " + end + ": House Starts")

    # Plot #2
    filled[[TickerName.FRED_HDTGPDUSQ163N[0], TickerName.FRED_NASDAQ[0]]].plot(secondary_y=TickerName.FRED_HDTGPDUSQ163N[0],
                                                                               ax=ax[1])
    plt.axhline(y=filled[TickerName.FRED_HDTGPDUSQ163N[0]].mean(), color='red', linestyle='--')
    plt.title(start + " ~ " + end + ": HouseDept To GDP")

    # Plot #3
    filled[[TickerName.FRED_T10Y2Y[0], TickerName.FRED_NASDAQ[0]]].plot(secondary_y=TickerName.FRED_T10Y2Y[0], ax=ax[2])
    plt.axhline(y=filled[TickerName.FRED_T10Y2Y[0]].mean(), color='red', linestyle='--')
    plt.title(start + " ~ " + end + ": Y10 - Y2")

    # Plot #4
    filled[[TickerName.FRED_UMCSENT[0], TickerName.FRED_NASDAQ[0]]].plot(secondary_y=TickerName.FRED_UMCSENT[0],
                                                                         ax=ax[3])
    plt.axhline(y=filled[TickerName.FRED_UMCSENT[0]].mean(), color='red', linestyle='--')
    plt.title(start + " ~ " + end + ": Sentiment")

    ###############################################################
    fig, ax = plt.subplots(nrows=4)
    # Plot #1
    filled[[TickerName.FRED_HIGHYIELD[0], TickerName.FRED_NASDAQ[0]]].plot(secondary_y=TickerName.FRED_HIGHYIELD[0],
                                                                           ax=ax[0])
    plt.axhline(y=filled[TickerName.FRED_HIGHYIELD[0]].mean(), color='red', linestyle='--')
    plt.title(start + " ~ " + end + ": High Yield")

    # Plot #2
    filled[[TickerName.FRED_UNRATE[0], TickerName.FRED_NASDAQ[0]]].plot(secondary_y=TickerName.FRED_UNRATE[0],
                                                                           ax=ax[1])
    plt.axhline(y=filled[TickerName.FRED_UNRATE[0]].mean(), color='red', linestyle='--')
    plt.title(start + " ~ " + end + ": UNRATE")

    # Plot #3
    filled[[TickerName.FRED_PCE[0], TickerName.FRED_NASDAQ[0]]].plot(secondary_y=TickerName.FRED_PCE[0],
                                                                           ax=ax[2])
    plt.axhline(y=filled[TickerName.FRED_PCE[0]].mean(), color='red', linestyle='--')
    plt.title(start + " ~ " + end + ": UNRATE")
    plt.show()


if __name__ == "__main__":
    main()
