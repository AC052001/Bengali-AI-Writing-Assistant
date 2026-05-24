import streamlit as st
from utils.nlp_engine import get_engine

# --- Page Configuration ---
st.set_page_config(
    page_title="বাংলা এআই গ্রামার চেকার",
    page_icon="IND",
    layout="wide"
)

# --- Custom CSS for Bengali Font and UI ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Hind Siliguri', sans-serif;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #15c39a;
        margin-bottom: 1rem;
    }
    
    .score-box {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .score-val {
        font-size: 2rem;
        font-weight: 800;
        color: #166534;
    }
</style>
""", unsafe_allow_html=True)

# --- Application Header ---
st.markdown('<div class="main-header">বাংলা এআই গ্রামার চেকার</div>', unsafe_allow_html=True)
st.markdown("**State of the Art NLP powered by Transformer Models**")

# --- Sidebar Settings ---
with st.sidebar:
    st.header("⚙️ সেটিংস")
    
    # Model Selection
    model_option = st.selectbox(
        "মডেল নির্বাচন করুন (Select Model)",
        ("csebuetnlp/banglat5 (Recommended)", "google/mt5-small (Faster)")
    )
    
    model_name = model_option.split(" ")[0]
    
    st.info("""
    **নির্দেশনা:**
    1. বাম পাশে আপনার লেখা লিখুন।
    2. "বিশ্লেষণ করুন" বাটনে ক্লিক করুন।
    3. ডান পাশে সংশোধিত লেখা দেখুন।
    """)

# --- Initialize Engine ---
engine = get_engine()

# --- Main Layout ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("মূল লেখা (Input Text)")
    input_text = st.text_area(
        "এখানে লিখুন বা পেস্ট করুন...",
        height=400,
        placeholder="উদাহরণ: আমি বাসায় যাইবো। আমার কাছে একটা কলম আছে।",
        key="input_area"
    )

# --- Action Area ---
st.markdown("---")
analyze_btn = st.button("🚀 বিশ্লেষণ করুন (Analyze)", use_container_width=True, type="primary")

# --- Logic Execution ---
if analyze_btn:
    if not input_text:
        st.warning("দয়া করে কিছু লিখুন!")
    else:
        with st.spinner("এআই মডেল কাজ করছে... অনুগ্রহ করে অপেক্ষা করুন।"):
            # 1. Correct Text
            corrected_text = engine.correct_grammar(input_text)
            
            # 2. Calculate Score (Heuristic)
            score = engine.calculate_score(input_text, corrected_text)
            
        # --- Display Results ---
        
        # Store in session state to persist if needed
        st.session_state['corrected'] = corrected_text
        st.session_state['score'] = score

# --- Output Area ---
if 'corrected' in st.session_state:
    with col2:
        st.subheader("সংশোধিত লেখা (Corrected Text)")
        
        # Score Badge
        score_color = "#dcfce7" if st.session_state['score'] > 80 else "#fef9c3"
        score_text = "#166534" if st.session_state['score'] > 80 else "#854d0e"
        
        st.markdown(f"""
        <div class="score-box" style="background: {score_color}; border-color: {score_text}44">
            <div style="font-size: 0.9rem; color: {score_text};">স্কোর (Score)</div>
            <div class="score-val" style="color: {score_text}">{st.session_state['score']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.info(st.session_state['corrected'])
        
        # Copy Button
        if st.button("📋 কপি করুন"):
            st.code(st.session_state['corrected'], language=None)
