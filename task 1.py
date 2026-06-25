import streamlit as st
from deep_translator import GoogleTranslator

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #334155
    );
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:white;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:30px;
}

.translation-box{
    background-color:#1e293b;
    padding:20px;
    border-radius:15px;
    color:white;
    font-size:18px;
    border:1px solid #475569;
}

.history-card{
    background-color:#1e293b;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# TITLE
# -------------------------

st.markdown(
    '<div class="main-title">AI Language Translator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Translate text instantly between languages</div>',
    unsafe_allow_html=True
)

# -------------------------
# LANGUAGES
# -------------------------

languages = {
    "Auto Detect": "auto",
    "English 🇺🇸": "en",
    "Hindi 🇮🇳": "hi",
    "French 🇫🇷": "fr",
    "Spanish 🇪🇸": "es",
    "German 🇩🇪": "de",
    "Japanese 🇯🇵": "ja",
    "Korean 🇰🇷": "ko",
    "Chinese 🇨🇳": "zh-CN"
}

# -------------------------
# HISTORY
# -------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# INPUT
# -------------------------

text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type something here..."
)

# -------------------------
# LANGUAGE SELECTORS
# -------------------------

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "From",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "To",
        list(languages.keys())[1:]
    )

# -------------------------
# TRANSLATE BUTTON
# -------------------------

if st.button("Translate", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        try:

            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.markdown("### Translation")

            st.markdown(
                f"""
                <div class="translation-box">
                {translated}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Save history

            st.session_state.history.insert(
                0,
                {
                    "original": text,
                    "translated": translated,
                    "from": source_lang,
                    "to": target_lang
                }
            )

        except Exception as e:
            st.error(f"Error: {e}")

# -------------------------
# HISTORY SECTION
# -------------------------

if st.session_state.history:

    st.markdown("---")
    st.subheader("Translation History")

    for item in st.session_state.history:

        st.markdown(
            f"""
            <div class="history-card">
            <b>{item['from']}</b> ➜ <b>{item['to']}</b><br><br>
            <b>Original:</b><br>
            {item['original']}<br><br>

            <b>Translated:</b><br>
            {item['translated']}
            </div>
            """,
            unsafe_allow_html=True
        )
