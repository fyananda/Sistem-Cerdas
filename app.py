import streamlit as st

st.title("💻 Sistem Rekomendasi Laptop")
st.write("Sistem Cerdas Berbasis Rule (IF–THEN)")

# =========================
# FAKTA (INPUT USER)
# =========================

budget = st.selectbox(
    "Pilih Budget:",
    ["< 5 juta", "5 - 10 juta", "> 10 juta"]
)

kebutuhan = st.selectbox(
    "Kebutuhan Utama:",
    ["Office", "Desain Grafis", "Gaming"]
)

portabilitas = st.selectbox(
    "Apakah butuh laptop ringan?",
    ["Ya", "Tidak"]
)

baterai = st.selectbox(
    "Kebutuhan daya tahan baterai:",
    ["Tinggi", "Normal"]
)

multitasking = st.selectbox(
    "Kebutuhan multitasking:",
    ["Ringan", "Berat"]
)

# =========================
# PROSES (RULE IF-THEN)
# =========================

if st.button("Dapatkan Rekomendasi"):

    rekomendasi = "Tidak ditemukan rekomendasi yang sesuai"

    # RULE 1
    if budget == "< 5 juta" and kebutuhan == "Office":
        rekomendasi = "Laptop Entry Level (Celeron / Ryzen 3, RAM 4GB)"

    # RULE 2
    elif budget == "5 - 10 juta" and kebutuhan == "Office" and multitasking == "Berat":
        rekomendasi = "Laptop Core i5 / Ryzen 5, RAM 8GB"

    # RULE 3
    elif budget == "> 10 juta" and kebutuhan == "Gaming":
        rekomendasi = "Laptop Gaming (Core i7 + GPU RTX)"

    # RULE 4
    elif kebutuhan == "Desain Grafis" and multitasking == "Berat":
        rekomendasi = "Laptop Creator (RAM 16GB + GPU Dedicated)"

    # RULE 5
    elif portabilitas == "Ya" and baterai == "Tinggi":
        rekomendasi = "Laptop Ultrabook (Tipis, ringan, baterai awet)"

    # RULE 6 (tambahan biar lebih kuat)
    elif budget == "> 10 juta" and kebutuhan == "Office":
        rekomendasi = "Laptop Premium (MacBook / Ultrabook High-End)"

    # OUTPUT
    st.success(f"💡 Rekomendasi: {rekomendasi}")