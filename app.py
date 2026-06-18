import streamlit as st

def main():
    st.title("Seputar PTA S1 2020")

    # 1. Buat input NIM di awal
    nim = st.text_input("Masukkan NIM Anda untuk Masuk:", type="password") # Menggunakan type="password" agar NIM tersembunyi saat diketik

    # 2. Daftar NIM yang diizinkan (White-list)
    nim_terdaftar = ["200205501009", "200205502002", "200205501004", "200205502015", "200205500002"]

    # 3. Cek kondisi input
    if nim == "":
        st.info("Silakan masukkan NIM terlebih dahulu untuk mengakses sistem.")
        
    elif nim not in nim_terdaftar:
        # Jika NIM tidak ada di daftar, akses ditolak total
        st.error("Akses Ditolak! NIM Anda tidak terdaftar dalam sistem.")
        st.image("https://giphy.com", caption="Lah kamu ga diajak...") # Opsional: tambah gif/gambar lucu
        
    else:
        # Jika NIM terdaftar, baru tampilkan konten spesifik masing-masing orang
        st.success("Akses Diterima! Membuka data...")
        st.markdown("---") # Garis pembatas

        if nim == "200205501009":
            nama_pengguna = "Muhaimin"
            st.write(f'Selamat Seminar Proposal, {nama_pengguna}!')
            gambar_lokal = 'bah sod.jpg'
            # Menggunakan use_container_width karena use_column_width sudah deprecated di Streamlit versi baru
            st.image(gambar_lokal, caption='Korban Tumbuk Dada', use_container_width=True)
            
        elif nim == "200205502002":
            nama_pengguna = "Yusraul Fitrah"
            st.write(f'Sudah mki kita {nama_pengguna}, tapi semangatki jalani proses. Dan tunggui teman satu dosen PA ta kodong.')
            
        elif nim == "200205501004":
            nama_pengguna = "Hasril"
            st.write(f'Baru-baru sudah {nama_pengguna} sempro nah, nah kita mi itu paling lancar bimbingan.')
            
        elif nim == "200205502015":
            nama_pengguna = "Muhammad Ikram"
            st.write(f'Ededeh apaji kau {nama_pengguna}, kah lamami kau sudah.')
            
        elif nim == "200205500002":
            nama_pengguna = "Yaya Ferida"
            st.write(f'wiss nih {nama_pengguna} nih boss *Ferdian, lekbak tongmi tawwa')

if __name__ == '__main__':
    main()
