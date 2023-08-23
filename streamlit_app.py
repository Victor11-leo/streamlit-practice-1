import streamlit as st
from analyze import unitsSoldMonth

df = unitsSoldMonth()
st.table(df)
