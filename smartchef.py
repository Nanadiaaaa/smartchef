import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os 

load_dotenv()

API_KEY = os.environ.get("PALM_API_KEY")

# Menambahkan penanganan kesalahan untuk memastikan API_KEY tidak kosong
if not API_KEY:
    st.error("API Key is missing. Please set PALM_API_KEY environment variable.")
    st.stop()  # Menghentikan eksekusi program jika API_KEY tidak tersedia

try:
    palm.configure(api_key=API_KEY)
except Exception as e:
    st.error(f"Error configuring Palm API: {str(e)}")
    st.stop()  # Menghentikan eksekusi program jika ada kesalahan konfigurasi API

def main():
    st.image("./download.jpg", use_column_width=100)
    st.header("Smart:red[Chef]")
    st.write("")

    # Memasukkan informasi tambahan tentang makanan
    menu_info = st.text_input("Tell me about the food you want to cook...", placeholder="Type Here ", label_visibility="visible")

    # Memasukkan informasi tentang karakteristik makanan
    flavor_info = st.selectbox("Select the flavor profile of the food:", ["Spicy", "Sweet", "Savory", "sour", "Other"])

    # Menentukan kata kunci atau frase yang menunjukkan pertanyaan tentang bahan masakan
    ingredient_keywords = ["beras", "nasi uduk", "nasi kuning", "nasi lemak", "nasi liwet", "daging sapi", "sapi", "chicken","Daging Ayam", "kambing", "cook"]

    # Memeriksa apakah input pengguna mengandung kata kunci tentang bahan masakan
    if any(keyword.lower() in menu_info.lower() for keyword in ingredient_keywords):
        # Jika ya, maka buat prompt dan kirim ke model Palm
        prompt = f"Recipe for {menu_info}. Title,Cooking method, ingredients, and characteristics: {flavor_info}."

    if  st.button("Send", use_container_width=True):
        model = "models/text-bison-001"

        try:
            response = palm.generate_text(
                model=model,
                prompt=prompt,
                max_output_tokens=2000
            )
            st.write("")
            st.header(":blue[Response]")
            st.write("")
            st.markdown(response.result, unsafe_allow_html=False, help=None)
        except Exception as e:
            st.error(f"Menu not found, please input other keywords!")

if __name__ == "__main__":
    main()
