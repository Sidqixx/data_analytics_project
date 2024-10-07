import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://png.pngtree.com/png-vector/20220930/ourmid/pngtree-shopping-logo-design-for-online-store-website-png-image_6239056.png")


st.title("Analisa E-commerce public dataset")

with st.expander("See explanation"): 

    #Judul
    st.title("Analisa Kota paling banyak melakukan transaksi")
        
    # Load File
    customers_df = pd.read_csv(r'C:\Users\Sidqi\OneDrive\Documents\submission\dashboard\customers_dataset.csv')

    # Menghitung jumlah transaksi per kota
    cities = customers_df["customer_city"].value_counts().reset_index()
    cities.columns = ['customer_city', 'transaction_count']

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    
    sns.barplot(x="transaction_count", y="customer_city", data=cities.head(5), palette="Blues_d", ax=ax)

    
    ax.set_ylabel(None)
    ax.set_xlabel(None)

    # Judul Plot
    ax.set_title("Top 5 Kota dengan Transaksi Terbanyak", loc="center", fontsize=15)


    ax.tick_params(axis='y', labelsize=12)


    st.pyplot(fig)
    
    st.write(
        """Pada Analisa data customer terkait penyebaran kota yang penduduknya melakukan transaksi, dapat dilihat
        bahwa sao Paulo menempati posisi pertama dengan total transaksi hampir mencapai 16000
        """
    )




def main():

    with st.expander("See explanation"):    
        st.title("Analisis Pembayaran E-commerce")

    
        ordersPayment_df = pd.read_csv(r'C:\Users\Sidqi\OneDrive\Documents\submission\dashboard\order_payments_dataset.csv')  # Sesuaikan dengan file Anda

        # Menghitung jumlah transaksi per jenis pembayaran
        payment_counts = ordersPayment_df['payment_type'].value_counts()

        # Mengambil top 3 dan mengelompokkan sisanya ke dalam kategori "Lainnya"
        top_n = 3
        top_payments = payment_counts.nlargest(top_n)
        other_count = payment_counts.sum() - top_payments.sum()
        top_payments['Others'] = other_count

        # Menampilkan hasil analisis
        st.subheader("Distribusi Jenis Pembayaran (Top 3 dan Lainnya)")

        # Plotting
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(
            top_payments, 
            labels=top_payments.index, 
            autopct='%1.1f%%', 
            startangle=90,
            textprops={'fontsize': 10},
            wedgeprops={'edgecolor': 'white'}
        )
        ax.set_title('Distribusi Jenis Pembayaran')
        ax.axis('equal')  

        
        st.pyplot(fig)

        st.write(
        """Pada Analisa data Order payment terkait metode pembayaran yang paling sering digunakan melakukan transaksi adalah
        menggunakan Credit card dengan presentase 73.9% dari total seluruh transaksi, diikuti dengan boleto 19%
        """
    )


# Run Apss
if __name__ == "__main__":
    main()
