import streamlit as st
from datetime import datetime
import pytz

def main():
    st.title('World Clock')

    all_time_zones = ['UTC', 'US/Pacific', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']

    selected_zones = st.multiselect('Select up to 4 locations:', all_time_zones, default=['UTC'])

    if st.button("Refresh Times"):
        st.experimental_rerun()

    if selected_zones:
        for zone in selected_zones:
            tz = pytz.timezone(zone)
            current_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
            st.write(f"Time in {zone}: {current_time}")

if __name__ == "__main__":
    main()
