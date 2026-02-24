import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Orchid Store", layout="wide")

st.title("🌺 Orchid Paradise Store")
st.caption("Premium Orchid Collection")

# Load Data
if os.path.exists("data_produk.csv"):
    df = pd.read_csv("data_produk.csv")
else:
    st.error("File data_produk.csv tidak ditemukan!")
    st.stop()

# Sidebar Filter
st.sidebar.header("🔎 Filter Produk")

kategori_list = ["Semua"] + sorted(df["kategori"].unique().tolist())
selected_kategori = st.sidebar.selectbox("Pilih Kategori", kategori_list)

search_nama = st.sidebar.text_input("Cari Nama Anggrek")

# Filter Logic
filtered_df = df.copy()

if selected_kategori != "Semua":
    filtered_df = filtered_df[filtered_df["kategori"] == selected_kategori]

if search_nama:
    filtered_df = filtered_df[
        filtered_df["nama"].str.contains(search_nama, case=False)
    ]

st.write(f"Menampilkan {len(filtered_df)} produk")

# Display Produk
cols = st.columns(3)

for index, row in filtered_df.reset_index().iterrows():
    with cols[index % 3]:
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, row["foto"])

        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.warning(f"Gambar tidak ditemukan: {row['foto']}")

        st.subheader(row["nama"])
        st.write(row["deskripsi"])

        st.markdown(f"### 💰 Rp {row['harga']:,}")

        if row["status"].lower() == "tersedia":
            st.success("🟢 Tersedia")
        else:
            st.error("🔴 Habis")

        wa_number = "6282219890741"
        message = f"Saya ingin memesan {row['nama']}"
        wa_link = f"https://wa.me/{wa_number}?text={message.replace(' ', '%20')}"

        st.link_button("📲 Pesan via WhatsApp", wa_link)

        st.divider()

st.markdown("---")
st.caption("© 2026 Orchid Paradise Store")

