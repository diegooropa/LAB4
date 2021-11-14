import pandas as pd

def crypto(raw, value):

    df = {'currency': [],
                  'Fechas': [],
                  'Levels': [],
                  'Volume_ask': [],
                  'Volume_bid': [],
                  'Total_volume': [],
                  'Mid_price': [],
                  'VWAP': []
                  }

    for currency in value:
        for i in list(raw[currency].keys()):
            ccy = currency
            df['currency'].append(ccy)
            fecha = i
            keys = pd.DataFrame(raw[currency][i])
            df['Fechas'].append(fecha)
            level = len(keys)
            df['Levels'].append(level)
            volume_bid = keys['bid_size'].sum()
            volume_ask = keys['ask_size'].sum()
            df['Volume_bid'].append(volume_bid)
            df['Volume_ask'].append(volume_ask)
            volume = volume_bid + volume_ask
            df['Total_volume'].append(volume)
            midprice = (keys['ask'][0] + keys['bid'][0]) / 2
            df['Mid_price'].append(midprice)
            vwap_ask = (keys['ask'] * keys['ask_size']).sum() / keys['ask_size'].sum()
            vwap_bid = (keys['bid'] * keys['bid_size']).sum() / keys['bid_size'].sum()
            vwap = (vwap_ask + vwap_bid) / 2
            df['VWAP'].append(vwap)

    return df

