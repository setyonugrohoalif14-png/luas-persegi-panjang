import streamlit as st

st.set_page_config(page_title="Luas Persegi Panjang", page_icon="🟦")

st.title("🟦 Kalkulator Luas Persegi Panjang")

st.write("Masukkan nilai panjang dan lebar, hasil langsung muncul!")

col1, col2 = st.columns(2)
with col1:
    panjang = st.number_input("Panjang (meter)", min_value=0.01, value=10.0, step=0.1)
with col2:
    lebar = st.number_input("Lebar (meter)", min_value=0.01, value=5.0, step=0.1)

luas = panjang * lebar

st.divider()
st.metric("Luas Persegi Panjang", f"{luas:,.2f} m²")
st.success(f"**{panjang} × {lebar} = {luas:,.2f} meter persegi**")

st.balloons()
