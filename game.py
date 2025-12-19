import streamlit as st
from PIL import Image
import time

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Bizim Hikayemiz", page_icon="🌹", layout="centered")

# --- STİL (Vampir Estetiği & Romantizm) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #d4af37;
    }
    h1 {
        font-family: 'Georgia', serif;
        color: #d4af37 !important;
        text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.5);
    }
    .question-box {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #d4af37;
        margin-bottom: 20px;
        text-align: center;
        font-size: 1.2rem;
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

# --- MÜZİK OYNATICI ---
# (Sayfa her yenilendiğinde müzik başa sarabilir, bu Streamlit'in doğasıdır)
with st.sidebar:
    st.write("🎵 **Atmosfer Müziği**")
    try:
        st.audio("muzik.mp3", format="audio/mp3", start_time=0)
        st.caption("Müziği başlat ve oyuna odaklan...")
    except:
        st.error("Müzik dosyası bulunamadı (muzik.mp3).")

# --- OYUN DURUMU ---
if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_stage(stage_num):
    st.session_state.stage = stage_num
    st.rerun()

# --- SENARYOLAR VE SORULAR ---

# SAHNE 0: GİRİŞ
if st.session_state.stage == 0:
    st.title("🩸 THE ORIGINALS: BİZİM HİKAYEMİZ")
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <p><i>"Aile güçtür, ama aşk... Aşk en büyük büyüdür."</i></p>
        <p>Bu oyun senin zihnini ve kalbini test etmek için hazırlandı.<br>
        Hazırsan, sonsuzluğa adım atalım.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("BAŞLANGICA GİT ➡️"):
        set_stage(1)

# SAHNE 1: İLK GÖRÜŞ / HİSLER
elif st.session_state.stage == 1:
    st.title("Bölüm 1: İlk Bakış")
    st.progress(20)
    
    st.markdown("""
    <div class="question-box">
        Seni ilk gördüğüm o anı hatırla...<br>
        Sence o an içimden geçirdiğim ilk cümle neydi?
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("A) Bu kızın egosu kesin tavan yapmıştır."):
            st.error("Hadi oradan! O kadar da önyargılı değilim 😉")
    with col2:
        if st.button("B) Hayatımın geri kalanı şu an karşımda duruyor."):
            st.success("Evet... O an anlamıştım.")
            time.sleep(1.5)
            set_stage(2)

# SAHNE 2: KOMİK BİR DETAY (İLİŞKİ DİNAMİĞİ)
elif st.session_state.stage == 2:
    st.title("Bölüm 2: Gerçekler")
    st.progress(40)
    
    st.markdown("""
    <div class="question-box">
        Aramızda bir tartışma çıktığında olayın sonu genelde nasıl biter?
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("A) Berat haklı olduğunu kanıtlar ve konu kapanır."):
            st.warning("Keşke... Ama biliyorsun ki kazanan hep sensin!")
    with col2:
        if st.button("B) Bir bakışınla yelkenleri suya indiririm."):
            st.balloons()
            st.success("Maalesef (veya iyi ki) aynen böyle oluyor! ❤️")
            time.sleep(1.5)
            set_stage(3)

# SAHNE 3: ROMANTİK TERCİH
elif st.session_state.stage == 3:
    st.title("Bölüm 3: Sığınak")
    st.progress(60)
    
    st.markdown("""
    <div class="question-box">
        Eğer dünyadaki herkes bir gün yok olsa ve sadece ikimiz kalsak...<br>
        Benim için 'ev' neresi olurdu?
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("A) Play Station'ın başı (FC 26 oynarken)"):
            st.info("Tamam oyunları severim ama... Sen varken değil.")
    with col2:
        if st.button("B) Senin yanın, dizinin dibi."):
            st.success("Benim evim sensin.")
            time.sleep(1.5)
            set_stage(4)

# SAHNE 4: SÖZ (THE ORIGINALS GÖNDERMESİ)
elif st.session_state.stage == 4:
    st.title("Bölüm 4: Yemin")
    st.progress(80)
    
    st.markdown("""
    <div class="question-box">
        Klaus Mikaelson ailesi için ne derse, ben de senin için aynısını diyorum.<br>
        Bizim sözümüz ne?
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ALWAYS AND FOREVER (Sonsuza Dek)"):
        st.success("Always and Forever...")
        time.sleep(1)
        set_stage(5)

# SAHNE 5: FİNAL
elif st.session_state.stage == 5:
    st.title("❤️ MUTLU SONSUZLUK ❤️")
    st.progress(100)
    st.balloons()
    
    # Fotoğraf Bölümü
    try:
        image = Image.open('biz.jpg')
        st.image(image, caption="Benim Hikayem Sensin...", use_container_width=True)
    except:
        st.error("Hata: 'biz.jpg' fotoğrafını klasöre eklemeyi unutma!")

    st.markdown("""
    <div style="text-align: center; margin-top: 20px; font-size: 1.3rem;">
        Bu sadece bir oyun olabilir ama hissettiklerim gerçek.<br>
        İyi ki varsın, iyi ki benimlesin.<br><br>
        <b>- Berat -</b>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Başa Dön 🔄"):
        set_stage(0)
