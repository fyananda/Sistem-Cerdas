import streamlit as st

# -------------------------
# DATA SEMENTARA (tanpa database)
# -------------------------
if "users" not in st.session_state:
    st.session_state.users = {"admin": "123"}

if "login" not in st.session_state:
    st.session_state.login = False

if "data_nilai" not in st.session_state:
    st.session_state.data_nilai = []

# -------------------------
# FUNGSI LOGIN
# -------------------------
def login():
    st.title("🔐 Login Sistem")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.login = True
            st.success("Login berhasil!")
        else:
            st.error("Username atau password salah!")

# -------------------------
# LOGIKA NILAI (RULE-BASED)
# -------------------------
def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    if nilai_akhir >= 85:
        grade = "A"
        ket = "Lulus (Sangat Baik)"
    elif nilai_akhir >= 70:
        grade = "B"
        ket = "Lulus (Baik)"
    elif nilai_akhir >= 60:
        grade = "C"
        ket = "Lulus (Cukup)"
    elif nilai_akhir >= 50:
        grade = "D"
        ket = "Tidak Lulus"
    else:
        grade = "E"
        ket = "Tidak Lulus"

    return nilai_akhir, grade, ket

# -------------------------
# MENU UTAMA (SETELAH LOGIN)
# -------------------------
def main_app():
    st.title("📊 Sistem Penilaian Mahasiswa")

    menu = st.sidebar.selectbox("Menu", ["Tambah Data", "Lihat Data", "Edit Data", "Hapus Data", "Logout"])

    # -------------------------
    # CREATE
    # -------------------------
    if menu == "Tambah Data":
        st.subheader("➕ Input Nilai Mahasiswa")

        nama = st.text_input("Nama Mahasiswa")
        tugas = st.number_input("Nilai Tugas", 0, 100)
        uts = st.number_input("Nilai UTS", 0, 100)
        uas = st.number_input("Nilai UAS", 0, 100)

        if st.button("Simpan"):
            nilai_akhir, grade, ket = hitung_nilai(tugas, uts, uas)

            data = {
                "nama": nama,
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": nilai_akhir,
                "grade": grade,
                "keterangan": ket
            }

            st.session_state.data_nilai.append(data)
            st.success("Data berhasil ditambahkan!")

    # -------------------------
    # READ
    # -------------------------
    elif menu == "Lihat Data":
        st.subheader("📋 Data Mahasiswa")

        if st.session_state.data_nilai:
            st.table(st.session_state.data_nilai)
        else:
            st.info("Belum ada data")

    # -------------------------
    # UPDATE
    # -------------------------
    elif menu == "Edit Data":
        st.subheader("✏️ Edit Data")

        if st.session_state.data_nilai:
            index = st.selectbox("Pilih Data", range(len(st.session_state.data_nilai)))

            data = st.session_state.data_nilai[index]

            nama = st.text_input("Nama", data["nama"])
            tugas = st.number_input("Tugas", 0, 100, data["tugas"])
            uts = st.number_input("UTS", 0, 100, data["uts"])
            uas = st.number_input("UAS", 0, 100, data["uas"])

            if st.button("Update"):
                nilai_akhir, grade, ket = hitung_nilai(tugas, uts, uas)

                st.session_state.data_nilai[index] = {
                    "nama": nama,
                    "tugas": tugas,
                    "uts": uts,
                    "uas": uas,
                    "akhir": nilai_akhir,
                    "grade": grade,
                    "keterangan": ket
                }

                st.success("Data berhasil diupdate!")
        else:
            st.info("Tidak ada data untuk diedit")

    # -------------------------
    # DELETE
    # -------------------------
    elif menu == "Hapus Data":
        st.subheader("🗑️ Hapus Data")

        if st.session_state.data_nilai:
            index = st.selectbox("Pilih Data", range(len(st.session_state.data_nilai)))

            if st.button("Hapus"):
                st.session_state.data_nilai.pop(index)
                st.success("Data berhasil dihapus!")
        else:
            st.info("Tidak ada data")

    # -------------------------
    # LOGOUT
    # -------------------------
    elif menu == "Logout":
        st.session_state.login = False
        st.success("Berhasil logout!")

# -------------------------
# FLOW UTAMA
# -------------------------
if not st.session_state.login:
    login()
else:
    main_app()
