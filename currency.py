import dateparser

def create(currency_data,currency_name):
        valor_compra = currency_data['compra'].replace(',','.')
        valor_venta = currency_data['venta'].replace(',','.')
        valor_variacion = currency_data['variacion'].replace(',','.').replace('%', '')
        valor_tiempo = dateparser.parse(currency_data['fecha'])
        dolar = {
            'name': currency_name,
            'buy': float(valor_compra),
            'sell': float(valor_venta),
            'date': str(valor_tiempo).replace("T","-"), 
            'variation': float(valor_variacion),
            'classVariation': currency_data['class-variacion'],
        }
        return dolar

