import streamlit as st

# പേജ് കോൺഫിഗറേഷൻ
st.set_page_config(page_title="Geography Quiz", page_icon="🌍", layout="centered")

# ക്വിസ് ഡാറ്റ
quiz_data = [
    {
        "question": "1. ലോകത്തിലെ ഏറ്റവും വലിയ മഹാസമുദ്രം ഏതാണ്?",
        "options": [
            "A. അറ്റ്ലാന്റിക് സമുദ്രം",
            "B. പസഫിക് സമുദ്രം",
            "C. ഇന്ത്യൻ സമുദ്രം",
            "D. ആർട്ടിക് സമുദ്രം",
        ],
        "answer": "B. പസഫിക് സമുദ്രം",
    },
    {
        "question": "2. ഇന്ത്യയിലെ ഏറ്റവും നീളം കൂടിയ നദി ഏതാണ്?",
        "options": ["A. ഗംഗ", "B. യമുന", "C. ഗോദാവരി", "D. ബ്രഹ്മപുത്ര"],
        "answer": "A. ഗംഗ",
    },
    {
        "question": "3. 'പിങ്ക് സിറ്റി' (Pink City) എന്നറിയപ്പെടുന്ന ഇന്ത്യൻ നഗരം ഏതാണ്?",
        "options": ["A. ഉദയ്പൂർ", "B. ജയ്പൂർ", "C. ജോധ്പൂർ", "D. അഹമ്മദാബാദ്"],
        "answer": "B. ജയ്പൂർ",
    },
    {
        "question": "4. ലോകത്തിലെ ഏറ്റവും ചെറിയ രാജ്യം ഏതാണ്?",
        "options": [
            "A. മൊണാക്കോ",
            "B. മാലദ്വീപ്",
            "C. വത്തിക്കാൻ സിറ്റി",
            "D. സാൻ മരീനോ",
        ],
        "answer": "C. വത്തിക്കാൻ സിറ്റി",
    },
    {
        "question": "5. ഏത് ഭൂഖണ്ഡത്തിലാണ് സഹാറ മരുഭൂമി സ്ഥിതി ചെയ്യുന്നത്?",
        "options": ["A. ഏഷ്യ", "B. ആഫ്രിക്ക", "C. ഓസ്ട്രേലിയ", "D. തെക്കേ അമേരിക്ക"],
        "answer": "B. ആഫ്രിക്ക",
    },
    {
        "question": "6. ലോകത്തിലെ ഏറ്റവും ഉയർന്ന പർവ്വതശിഖരം ഏതാണ്?",
        "options": [
            "A. കെ2 (K2)",
            "B. കാഞ്ചൻജംഗ",
            "C. എവറസ്റ്റ് കൊടുമുടി",
            "D. ആനമുടി",
        ],
        "answer": "C. എവറസ്റ്റ് കൊടുമുടി",
    },
    {
        "question": "7. ഏത് നദിയുടെ തീരത്താണ് ഈജിപ്ഷ്യൻ നാഗരികത വളർന്നുവന്നത്?",
        "options": ["A. നൈൽ നദി", "B. ആമസോൺ", "C. മിസിസിപ്പി", "D. സിന്ധു നദി"],
        "answer": "A. നൈൽ നദി",
    },
    {
        "question": "8. 'ഉദയസൂര്യന്റെ നാട്' (Land of the Rising Sun) എന്നറിയപ്പെടുന്ന രാജ്യം ഏതാണ്?",
        "options": ["A. നോർവേ", "B. ചൈന", "C. ജപ്പാൻ", "D. തായ്‌ലൻഡ്"],
        "answer": "C. ജപ്പാൻ",
    },
    {
        "question": "9. ഇന്ത്യയിൽ ഏറ്റവും കൂടുതൽ മഴ ലഭിക്കുന്ന സ്ഥലം ഏതാണ്?",
        "options": ["A. ചിറാപുഞ്ചി", "B. മൗസിൻറാം", "C. ചിന്നക്കനാൽ", "D. അഗുംബെ"],
        "answer": "B. മൗസിൻറാം",
    },
    {
        "question": "10. ലോകത്തിലെ ഏറ്റവും നീളം കൂടിയ നദി ഏതാണ്?",
        "options": ["A. ആമസോൺ", "B. യാങ്‌സി", "C. നൈൽ", "D. മിസിസിപ്പി"],
        "answer": "C. നൈൽ",
    },
]

st.title("🌍 Geography Quiz (ഭൂമിശാസ്ത്ര ക്വിസ്)")
st.write("ശരിയായ ഉത്തരങ്ങൾ തിരഞ്ഞെടുക്കുക, അവസാനം **Submit Quiz** അമർത്തുക.")
st.divider()

# ഉപയോക്താവിന്റെ ഉത്തരങ്ങൾ സൂക്ഷിക്കാൻ ഫോം (Form) ഉപയോഗിക്കുന്നു
with st.form("geography_quiz_form"):
    user_answers = {}

    for idx, item in enumerate(quiz_data):
        st.subheader(item["question"])
        # Radio button വഴി ഓപ്ഷനുകൾ നൽകുന്നു
        user_answers[idx] = st.radio(
            "ഉത്തരം തിരഞ്ഞെടുക്കുക:",
            options=item["options"],
            key=f"q_{idx}",
            index=None,  # ആദ്യമേ ഒന്നും സെലക്ട് ചെയ്യാതിരിക്കാൻ
        )
        st.write("---")

    submit_button = st.form_submit_button(label="🎯 Submit Quiz")

# Submit ക്ലിക്ക് ചെയ്യുമ്പോൾ സ്കോർ കണക്കാക്കുന്നു
if submit_button:
    score = 0
    total = len(quiz_data)

    for idx, item in enumerate(quiz_data):
        if user_answers[idx] == item["answer"]:
            score += 1

    st.header(f"📊 റിസൾട്ട്: {score} / {total}")

    # ഫീഡ്‌ബാക്ക് മെസ്സേജുകൾ
    if score == 10:
        st.balloons()
        st.success("🌟 തകർപ്പൻ പ്രകടനം! എല്ലാ ഉത്തരങ്ങളും ശരിയാണ്!")
    elif score >= 7:
        st.success("👍 വളരെ നല്ല പ്രകടനം!")
    elif score >= 5:
        st.info("🙂 മികച്ച ശ്രമം!")
    else:
        st.warning("📚 കൂടുതൽ പഠിച്ച് വീണ്ടും ശ്രമിക്കുക!")
