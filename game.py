import streamlit as st
from PIL import Image
import time
import base64

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Bizim Hikayemiz", page_icon="❤️", layout="centered")

# --- STİL (Zarif, Siyah ve Gold) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #d4af37;
    }
    h1 {
        font-family: 'Georgia', serif;
        color: #d4af37 !important;
        text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.3);
    }
    .question-box {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
        margin-bottom: 20px;
        text-align: center;
        font-size: 1.2rem;
        font-family: 'Verdana', sans-serif;
    }
    .stButton>button {
        background-color: transparent;
        color: #d4af37;
        border-radius: 10px;
        border: 1px solid #d4af37;
        font-weight: bold;
        width: 100%;
        padding: 15px;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #d4af37;
        color: black;
        box-shadow: 0 0 20px #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

# --- OTOMATİK MÜZİK OYNATMA ---
def autoplay_audio(file_path: str):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Müzik dosyası (muzik.mp3) bulunamadı!")

# Müziği başlat
autoplay_audio("muzik.mp3")

# --- OYUN DURUMU ---
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_stage(stage_num):
    st.session_state.stage = stage_num
    st.rerun()

# --- SENARYOLAR VE SORULAR ---

# SAHNE 0: GİRİŞ
if st.session_state.stage == 0:
    st.title("❤️ BİZİM HİKAYEMİZ")
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <p>Bazı hikayeler asla bitmez...<br>
        Seni ne kadar iyi tanıdığımı (ve senin bizi ne kadar iyi hatırladığını) test etmeye hazır mısın?</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("HİKAYEYE BAŞLA ➡️"):
        set_stage(1)

# SAHNE 1: İLK BULUŞMA (FOTO 1 KULLANILIYOR)
elif st.session_state.stage == 1:
    st.title("Bölüm 1: İlk Heyecan")
    st.progress(20)
    
    st.markdown("""
    <div class="question-box">
        Hadi en başa dönelim... İlk buluşmamızın o büyüsünü hatırla.<br>
        O gün içimizi ısıtan şey neydi? Ne içmiştik?
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("A) Bol köpüklü Türk Kahvesi"):
            st.error("O gün değil... O gün daha tatlı bir başlangıç yapmıştık.")
    with col2:
        if st.button("B) Sıcak Çikolata"):
            st.success("Evet! O sıcaklık hala kalbimde...")
            time.sleep(1.5)
            # FOTO 1
            try:
                img = Image.open('foto1.jpeg')
                st.image(img, use_container_width=True)
            except:
                pass
            time.sleep(2)
            set_stage(2)

# SAHNE 2: YAZ ANISI (FOTO 2 KULLANILIYOR)
elif st.session_state.stage == 2:
    st.title("Bölüm 2: Unutulmaz Yaz")
    st.progress(40)
    
    st.markdown("""
    <div class="question-box">
        Bu yaz yaşadığımız bir an beni çok etkilemişti.<br>
        Benim için o anı "unutulmaz" kılan olay neydi?
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("A) Denizden çıkınca ayakların kirlenmesin diye seni kucağımda taşımam"):
            st.success("Seni her zaman taşırım, her yükünü alırım...")
            time.sleep(1.5)
            # FOTO 2
            try:
                img = Image.open('foto2.jpeg')
                st.image(img, use_container_width=True)
            except:
                pass
            time.sleep(2)
            set_stage(3)
    with col2:
        if st.button("B) Akşam gün batımında sahilde uzun uzun yürümemiz"):
            st.warning("Bu da çok güzeldi ama beni derinden etkileyen fedakarlık anıydı...")

# SAHNE 3: SEVGİ ÖLÇÜSÜ (FOTO 3 KULLANILIYOR)
elif st.session_state.stage == 3:
    st.title("Bölüm 3: Derinlik")
    st.progress(60)
    
    st.markdown("""
    <div class="question-box">
        Sana olan sevgimi tarif etmem gerekse...<br>
        Sence hangisi hislerime daha yakın olurdu?
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("A) Dünyalar kadar"):
            st.info("Dünya küçük kalır sevgilim...")
    with col2:
        if st.button("B) Kelimelerin ve sayıların yetmeyeceği kadar"):
            st.success("Sonsuzluk bile az kalır.")
            time.sleep(1.5)
            # FOTO 3
            try:
                img = Image.open('foto3.jpeg')
                st.image(img, use_container_width=True)
            except:
                pass
            time.sleep(2)
            set_stage(4)

# SAHNE 4: HARRY POTTER FİNALİ (FOTO 4 KULLANILIYOR)
elif st.session_state.stage == 4:
    st.title("Final: O Soru")
    st.progress(80)
    
    st.markdown("""
    <div class="question-box">
        Tıpkı Dumbledore'un o meşhur sorusundaki gibi...<br>
        <b>"After all this time?" (Bunca zaman sonra, hala mı?)</b>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("ALWAYS. (Her zaman)"):
            st.success("Always...")
            time.sleep(1)
            # FOTO 4
            try:
                img = Image.open('foto4.jpeg')
                st.image(img, use_container_width=True)
            except:
                pass
            time.sleep(2)
            set_stage(5)

# SAHNE 5: MUTLU SON (BİZ.JPEG + FOTO 5 & FOTO 6)
elif st.session_state.stage == 5:
    st.title("❤️ SENİ SEVİYORUM ❤️")
    st.progress(100)
    st.balloons()
    
    # BİZ FOTOĞRAFI (ANA FOTO)
    try:
        image = Image.open('biz.jpeg')
        st.image(image, caption="Sonsuza Dek...", use_container_width=True)
    except:
        st.error("Hata: 'biz.jpeg' fotoğrafı bulunamadı!")

    st.markdown("""
    <div style="text-align: center; margin-top: 20px; font-size: 1.3rem;">
        Hangi evrende olursak olalım, cevap hep aynı olacak.<br>
        İyi ki benimlesin.<br><br>
        <b>- Berat -</b>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h3 style='text-align: center; color: #d4af37;'>📸 Anılarımız</h3>", unsafe_allow_html=True)
    
    # GALERİ (FOTO 5 ve FOTO 6 BURADA GÖZÜKÜYOR)
    galeri_col1, galeri_col2 = st.columns(2)
    with galeri_col1:
        try:
            st.image('foto5.jpeg', use_container_width=True)
        except:
            pass
    with galeri_col2:
        try:
            st.image('foto6.jpeg', use_container_width=True)
        except:
            pass
    
    if st.button("Başa Dön 🔄"):
        set_stage(0)
