import streamlit as st
from datetime import datetime
import pytz

st.title('World Clock')

# Define time zones you want to show
time_zones = ['UTC', 'US/Pacific', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']

# Display current time in each time zone
for zone in time_zones:
    tz = pytz.timezone(zone)
    st.write(f"Time in {zone}: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}")