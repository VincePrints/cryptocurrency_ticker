import time
import json
import requests
import I2C_LCD_driver
import ccxt

# Set up LCD display
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()

# Display loading string
mylcd.lcd_display_string("Working...")

# Create font for arrows
fontdata1 = [
    [0b00000,
     0b00100,
     0b00100,
     0b01110,
     0b01110,
     0b11111,
     0b11111,
     0b00000],

    [0b00000,
     0b11111,
     0b11111,
     0b01110,
     0b01110,
     0b00100,
     0b00100,
     0b00000],

    [0b00000,
     0b00100,
     0b01110,
     0b11111,
     0b00000,
     0b11111,
     0b01110,
     0b00100],
]

# Import font data
mylcd.lcd_load_custom_chars(fontdata1)

# Define function to get price and arrow direction for a given currency pair
def get_price(symbol):
    try:
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker(symbol)
        last_price = ticker['last']
        previous_price = ticker['close']
        
        if last_price == previous_price:
            arrow_direction = 2
        elif last_price > previous_price:
            arrow_direction = 0
        elif last_price < previous_price:
            arrow_direction = 1
            
        return last_price, arrow_direction
    
    except (ccxt.ExchangeError, ccxt.NetworkError, ccxt.RequestTimeout) as e:
        print(f"Error querying exchange: {e}")
        return None, None

# Display time and date
while True:
    mylcd.lcd_display_string(("%s" % time.strftime("%H:%M   ")) + ("%s" % time.strftime("%m/%d/%y")), 2, 0)

    # Get BTC price and arrow direction
    btc_price, btc_direction = get_price('BTC/USDT')
    if btc_price is not None:
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ")
        time.sleep(0.4)
        mylcd.lcd_display_string(f"${btc_price:.2f}/BTC   ", 1)
        mylcd.lcd_write_char(btc_direction)

    # Get ETH price and arrow direction
    eth_price, eth_direction = get_price('ETH/USDT')
    if eth_price is not None:
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ")
        time.sleep(0.4)
        mylcd.lcd_display_string(f"${eth_price:.2f}/ETH    ", 1)
        mylcd.lcd_write_char(eth_direction)

    # Get LTC price and arrow direction
    ltc_price, ltc_direction = get_price('LTC/USDT')
    if ltc_price is not None:
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ")
        time.sleep(0.4)
        mylcd.lcd_display_string(f"${ltc_price:.2f}/LTC    ", 1)
        mylcd.lcd_write_char(ltc_direction)

    # Get XRP price and arrow direction
    xrp_price, xrp_direction = get_price('XRP/USDT')
    if xrp_price is not None:
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ")
        time.sleep(0.4)
        mylcd.lcd_display_string(f"${xrp_price:.2f}/XRP    ", 1)
        mylcd.lcd_write_char(xrp_direction)

    time.sleep(5)
