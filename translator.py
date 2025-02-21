import streamlit as st
from transformers import pipeline

# Load the translation pipeline
@st.cache_resource
def load_model():
    # Using a multilingual model that supports various language pairs.
    return pipeline("translation", model="Helsinki-NLP/opus-mt-en-ROMANCE")

# Initialize the model
translator = load_model()

# Streamlit UI setup
st.title("Multilingual Translation App")
st.write("Translate text between various languages using Hugging Face's transformers.")

# Input field for the text to translate
input_text = st.text_area("Enter Text to Translate", "", height=150)

# Expanded list of languages (language codes)
languages = {
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Italian': 'it',
    'Portuguese': 'pt',
    'Dutch': 'nl',
    'Russian': 'ru',
    'Chinese': 'zh',
    'Arabic': 'ar',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Hindi': 'hi',
    'Turkish': 'tr',
    'Greek': 'el',
}

# Choose source and target languages
source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

# Button to trigger translation
if st.button("Translate"):
    if input_text:
        # Model mapping for more language pairs (a selection of languages)
        model_mapping = {
            ('en', 'fr'): 'Helsinki-NLP/opus-mt-en-fr',
            ('en', 'de'): 'Helsinki-NLP/opus-mt-en-de',
            ('en', 'es'): 'Helsinki-NLP/opus-mt-en-es',
            ('en', 'it'): 'Helsinki-NLP/opus-mt-en-it',
            ('en', 'pt'): 'Helsinki-NLP/opus-mt-en-pt',
            ('fr', 'en'): 'Helsinki-NLP/opus-mt-fr-en',
            ('de', 'en'): 'Helsinki-NLP/opus-mt-de-en',
            ('es', 'en'): 'Helsinki-NLP/opus-mt-es-en',
            ('it', 'en'): 'Helsinki-NLP/opus-mt-it-en',
            ('pt', 'en'): 'Helsinki-NLP/opus-mt-pt-en',
            ('en', 'ru'): 'Helsinki-NLP/opus-mt-en-ru',
            ('ru', 'en'): 'Helsinki-NLP/opus-mt-ru-en',
            ('en', 'zh'): 'Helsinki-NLP/opus-mt-en-zh',
            ('zh', 'en'): 'Helsinki-NLP/opus-mt-zh-en',
            ('en', 'ar'): 'Helsinki-NLP/opus-mt-en-ar',
            ('ar', 'en'): 'Helsinki-NLP/opus-mt-ar-en',
            ('en', 'ja'): 'Helsinki-NLP/opus-mt-en-ja',
            ('ja', 'en'): 'Helsinki-NLP/opus-mt-ja-en',
            ('en', 'ko'): 'Helsinki-NLP/opus-mt-en-ko',
            ('ko', 'en'): 'Helsinki-NLP/opus-mt-ko-en',
            ('en', 'hi'): 'Helsinki-NLP/opus-mt-en-hi',
            ('hi', 'en'): 'Helsinki-NLP/opus-mt-hi-en',
            ('en', 'tr'): 'Helsinki-NLP/opus-mt-en-tr',
            ('tr', 'en'): 'Helsinki-NLP/opus-mt-tr-en',
            ('en', 'el'): 'Helsinki-NLP/opus-mt-en-el',
            ('el', 'en'): 'Helsinki-NLP/opus-mt-el-en',
        }
        
        # Get the language codes for the selected languages
        src_lang_code = languages[source_lang]
        tgt_lang_code = languages[target_lang]

        # Check if the selected language pair is available in the model mapping
        if (src_lang_code, tgt_lang_code) in model_mapping:
            # Load the appropriate translation model for the selected pair
            model_name = model_mapping[(src_lang_code, tgt_lang_code)]
            translation_pipeline = pipeline("translation", model=model_name)

            # Perform the translation
            result = translation_pipeline(input_text)
            translated_text = result[0]['translation_text']

            st.subheader("Translated Text:")
            st.write(translated_text)
        else:
            st.error(f"Translation model not available for {source_lang} to {target_lang}.")
    else:
        st.error("Please enter text to translate.")
