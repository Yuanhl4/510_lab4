import streamlit as st
from datetime import datetime
import pytz
import yfinance as yf

def main():
    st.title('World Clock with Additional Features')

    all_time_zones = ['UTC', 'US/Pacific', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']
    selected_zones = st.multiselect('Select up to 4 locations:', all_time_zones, default=['UTC'])

    if st.button("Refresh Times"):
        st.experimental_rerun()

    if selected_zones:
        for zone in selected_zones:
            tz = pytz.timezone(zone)
            current_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
            st.write(f"Time in {zone}: {current_time}")

    st.sidebar.title("UNIX Timestamp Converter")
    unix_input = st.sidebar.number_input("Enter UNIX Timestamp:", value=int(datetime.now().timestamp()), step=1)
    if st.sidebar.button("Convert Timestamp"):
        human_time = datetime.utcfromtimestamp(unix_input).strftime('%Y-%m-%d %H:%M:%S')
        st.sidebar.write(f"Converted Time: {human_time}")

    stock_symbol = st.sidebar.text_input("Enter stock symbol (e.g., AAPL):", value="AAPL")
    if st.sidebar.button("Fetch Stock Price"):
        stock_data = yf.Ticker(stock_symbol)
        try:
            stock_price = stock_data.history(period='1d')['Close'].iloc[-1]
            st.sidebar.write(f"Latest closing price for {stock_symbol}: ${stock_price:.2f}")
        except Exception as e:
            st.sidebar.write(f"Failed to fetch data for {stock_symbol}: {e}")

if __name__ == "__main__":
    main()