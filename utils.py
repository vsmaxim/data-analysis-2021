import pandas as pd
from typing import Iterable
from matplotlib import pyplot as plt
import seaborn as sns


def get_stats_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    For given dataframe constructs new dataframe with numerical parameters as a rows,
    and statitical values (such as mean, std, min, max and quartiles)
    
    :param df: dataframe to perform analysis on
    :return: dataframe with calculated statistics
    """
    return df.describe().transpose().drop("count", axis=1)



def plot_distplot_matrix(df: pd.DataFrame, columns: Iterable[str], cols: int = 3):
    """
    For given dataframe and columns plots multiple dist plots (histogram with density plots).
    
    :param df: dataframe to plot graphics from
    :param columns: columns to plot
    :return: None
    """
    rows = math.ceil(len(columns) / cols)
    fig, ax = plt.subplots(rows, cols, figsize=(7 * cols, 6 * rows))

    for index, column in enumerate(columns):
        row, col = index // cols, index % cols
        current_ax = ax[row, col] if rows > 1 else ax[col]
        sns.distplot(ax=current_ax, a = df[column].dropna())
        current_ax.set_title(column, fontsize=15)
        current_ax.legend(loc='best')

    plt.show()

    

def plot_histplot_matrix(df: pd.DataFrame, columns: Iterable[str], cols: int = 3):
    """
    For given dataframe and columns plots multiple dist plots (histogram with density plots).
    
    :param df: dataframe to plot graphics from
    :param columns: columns to plot
    :return: None
    """
    rows = math.ceil(len(columns) / cols)
    fig, ax = plt.subplots(rows, cols, figsize=(7 * cols, 6 * rows))

    for index, column in enumerate(columns):
        row, col = index // cols, index % cols
        current_ax = ax[row, col] if rows > 1 else ax[col]
        sns.histplot(ax=current_ax, data=df, x=column)
        current_ax.set_title(column, fontsize=15)
        current_ax.legend(loc='best')

    plt.show()

import math



def convert_money_to_usd(v: str) -> float:
    """
    For given money string (e.g. '123 RUR', '12345 $', '1000000 EUR')
    return amount in USD. None is returned if it's not possible to construct the
    current USD amount.
    
    :param v: money string
    :return: value of money in USD
    """
    def convert_to_usd(currency: str, value: float) -> float:
        if currency == "$":
            return value
        elif currency in CODE_TO_FIX:
            currency = CODE_TO_FIX[currency]
        elif currency not in CUR_TO_USD:
            return math.nan
        return value * CUR_TO_USD[currency]

    if isinstance(v, str):
        sign, value = v.split()
        return convert_to_usd(sign, float(value))
    
    return v


CODE_TO_FIX = {
    "RUR": "RUB",
}

CUR_TO_USD = {
  "USD": 1,
  "EUR": 1.2118402047,
  "GBP": 1.4006845827,
  "INR": 0.0137824399,
  "AUD": 0.7883143098,
  "CAD": 0.7924177681,
  "SGD": 0.7545853523,
  "CHF": 1.1157317343,
  "MYR": 0.2474983458,
  "JPY": 0.0094902639,
  "CNY": 0.1548768626,
  "NZD": 0.7301028225,
  "THB": 0.0333586689,
  "HUF": 0.003381943,
  "AED": 0.2722940776,
  "HKD": 0.1289704651,
  "MXN": 0.0489366225,
  "ZAR": 0.0682113798,
  "PHP": 0.0206182686,
  "SEK": 0.1208031665,
  "IDR": 0.0000711102,
  "SAR": 0.2666666667,
  "BRL": 0.1855273137,
  "TRY": 0.1436680563,
  "KES": 0.0091119342,
  "KRW": 0.0009046443,
  "EGP": 0.063769971,
  "IQD": 0.0006851827,
  "NOK": 0.1181922067,
  "KWD": 3.3048885399,
  "RUB": 0.0134995677,
  "DKK": 0.1629504779,
  "PKR": 0.0062939562,
  "ILS": 0.3055822347,
  "PLN": 0.2702568632,
  "QAR": 0.2747252747,
  "XAU": 1784.2410124212,
  "OMR": 2.6007802341,
  "COP": 0.0002799729,
  "CLP": 0.0014110879,
  "TWD": 0.0357843931,
  "ARS": 0.0112165288,
  "CZK": 0.04680645,
  "VND": 0.0000430699,
  "MAD": 0.1124380143,
  "JOD": 1.4104372355,
  "BHD": 2.6595744681,
  "XOF": 0.0018474385,
  "LKR": 0.005114581,
  "UAH": 0.0357464238,
  "NGN": 0.0026259926,
  "TND": 0.3695449488,
  "UGX": 0.0002727007,
  "RON": 0.2485449275,
  "BDT": 0.0117863604,
  "PEN": 0.2738087773,
  "GEL": 0.3028337685,
  "XAF": 0.0018474385,
  "FJD": 0.4928230145,
  "VEF": 0.1001251564,
  "VES": 5.823e-7,
  "BYN": 0.3867822491,
  "HRK": 0.1600880594,
  "UZS": 0.0000950968,
  "BGN": 0.619604058,
  "DZD": 0.0075112429,
  "IRR": 0.0000237952,
  "DOP": 0.0173002952,
  "ISK": 0.0077877701,
  "XAG": 27.2720943618,
  "CRC": 0.001631017,
  "SYP": 0.0019501703,
  "LYD": 0.2246022918,
  "JMD": 0.0066763116,
  "MUR": 0.0249401451,
  "GHS": 0.1738338629,
  "AOA": 0.0015326846,
  "UYU": 0.0233701793,
  "AFN": 0.0129467678,
  "LBP": 0.0006633499,
  "XPF": 0.0101552209,
  "TTD": 0.1478084781,
  "TZS": 0.0004314972,
  "ALL": 0.0098035547,
  "XCD": 0.370355154,
  "GTQ": 0.1293308226,
  "NPR": 0.0085738351,
  "BOB": 0.1448212002,
  "ZWD": 0.0027631943,
  "BBD": 0.5,
  "CUC": 1,
  "LAK": 0.000106963,
  "BND": 0.7545853523,
  "BWP": 0.092329592,
  "HNL": 0.0414984101,
  "PYG": 0.0001499574,
  "ETB": 0.0251261381,
  "NAD": 0.0682113798,
  "PGK": 0.2828970781,
  "SDG": 0.0181446253,
  "MOP": 0.1252140438,
  "NIO": 0.0285246223,
  "BMD": 1,
  "KZT": 0.0023961865,
  "PAB": 1,
  "BAM": 0.619604058,
  "GYD": 0.0047607716,
  "YER": 0.0040325173,
  "MGA": 0.0002660548,
  "KYD": 1.219506224,
  "MZN": 0.0133619192,
  "RSD": 0.0103060961,
  "SCR": 0.0471717396,
  "AMD": 0.0019068067,
  "SBD": 0.1249000495,
  "AZN": 0.5882559629,
  "SLL": 0.0000981972,
  "TOP": 0.4348980443,
  "BZD": 0.4962052774,
  "MWK": 0.0012820538,
  "GMD": 0.0194498024,
  "BIF": 0.0005131827,
  "SOS": 0.0017241011,
  "HTG": 0.0131618359,
  "GNF": 0.0000998941,
  "MVR": 0.0647128781,
  "MNT": 0.0003502253,
  "CDF": 0.0005049127,
  "STN": 0.0493838942,
  "TJS": 0.0884291808,
  "KPW": 0.0011111112,
  "MMK": 0.00075245,
  "LSL": 0.0682113798,
  "LRD": 0.0057970507,
  "KGS": 0.0118281587,
  "GIP": 1.4006845827,
  "XPT": 1278.9642231501,
  "MDL": 0.0571428849,
  "CUP": 0.0377358491,
  "KHR": 0.0002467951,
  "MKD": 0.0196779112,
  "VUV": 0.0093198316,
  "MRU": 0.0276788757,
  "ANG": 0.5594404029,
  "SZL": 0.0682113798,
  "CVE": 0.0109897543,
  "SRD": 0.0709912752,
  "XPD": 2383.3351486403,
  "SVC": 0.1142857143,
  "BSD": 1,
  "XDR": 1.4429134551,
  "RWF": 0.0010249168,
  "AWG": 0.5586592179,
  "DJF": 0.0056179864,
  "BTN": 0.0137824399,
  "KMF": 0.0024632513,
  "WST": 0.3959962895,
  "SPL": 6.000000024,
  "ERN": 0.0666666667,
  "FKP": 1.4006845827,
  "SHP": 1.4006845827,
  "JEP": 1.4006845827,
  "TMT": 0.2857642001,
  "TVD": 0.7883143098,
  "IMP": 1.4006845827,
  "GGP": 1.4006845827,
  "ZMW": 0.046021039
}