import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_day = pd.read_csv("day.csv")

df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_day['year'] = df_day['dteday'].dt.year  

# Mapping label musim
season_mapping = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
df_day["season_label"] = df_day["season"].map(season_mapping)

# Streamlit Dashboard
st.title("📊 Dashboard Interaktif Penyewaan Sepeda")

# === Filter Interaktif ===
st.sidebar.header("Filter Data")
selected_seasons = st.sidebar.multiselect("Pilih Musim:", df_day["season_label"].unique(), default=df_day["season_label"].unique())
date_range = st.sidebar.slider("Pilih Rentang Tanggal:", min_value=df_day["dteday"].min().date(), max_value=df_day["dteday"].max().date(), value=(df_day["dteday"].min().date(), df_day["dteday"].max().date()))
selected_year = st.sidebar.selectbox("Pilih Tahun Terakhir:", sorted(df_day['year'].unique(), reverse=True))

# Filter Data
filtered_df = df_day[(df_day["season_label"].isin(selected_seasons)) & (df_day["dteday"].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))]

# Filter Data berdasarkan Tahun dan Musim
filtered_df_year = df_day[(df_day['year'] == selected_year) & (df_day["season_label"].isin(selected_seasons))]

# === Visualisasi 1: Penyewaan Sepeda Berdasarkan Hari Kerja ===
st.subheader("Perbandingan Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x=filtered_df['workingday'].map({0: 'Akhir Pekan', 1: 'Hari Kerja'}), y=filtered_df['cnt'], palette="coolwarm", ax=ax)
ax.set_xlabel("Kategori")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# === Visualisasi 2: Tren Penyewaan Berdasarkan Musim ===
st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 4))
sns.lineplot(data=filtered_df, x='dteday', y='cnt', hue='season_label', marker='o', ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.legend(title="Musim")
st.pyplot(fig)

# === Visualisasi 3: Pengaruh Hari Kerja, Suhu, dan Musim ===
st.subheader("Pengaruh Hari Kerja, Suhu, dan Musim terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 4))
sns.scatterplot(data=filtered_df_year, x='temp', y='cnt', hue='season_label', style='workingday', ax=ax)
ax.set_xlabel("Suhu (Normalized)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# === Download Data ===
st.sidebar.markdown("## Unduh Data yang Difilter")
st.sidebar.download_button(label="Download CSV", data=filtered_df.to_csv(index=False), file_name="filtered_data.csv", mime="text/csv")
