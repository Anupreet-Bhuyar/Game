import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Offer Blueprint - Level 1", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS
st.markdown("""
<style>
    * {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    body {
        background: #f8fafc;
    }
    
    .story-beat {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 36px;
        color: white;
        margin-bottom: 32px;
        box-shadow: 0 25px 70px rgba(102, 126, 234, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.15);
        animation: slideIn 0.6s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .beat-number {
        font-size: 14px;
        font-weight: 800;
        opacity: 0.8;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }
    
    .beat-question {
        font-size: 24px;
        font-weight: 700;
        line-height: 1.5;
        margin-bottom: 12px;
    }
    
    .beat-context {
        font-size: 15px;
        opacity: 0.9;
        font-weight: 500;
        line-height: 1.6;
    }
    
    .extraction-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #edf2f7 100%);
        border-radius: 16px;
        padding: 32px;
        margin-top: 32px;
        margin-bottom: 32px;
        border: 2px solid #e2e8f0;
    }
    
    .extraction-title {
        font-size: 24px;
        font-weight: 800;
        color: #1a202c;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .extraction-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        margin-bottom: 24px;
    }
    
    .extraction-item {
        background: white;
        border-radius: 12px;
        padding: 20px;
        border-left: 4px solid #667eea;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    
    .extraction-label {
        font-size: 13px;
        font-weight: 700;
        color: #667eea;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }
    
    .extraction-content {
        font-size: 15px;
        font-weight: 600;
        color: #2d3748;
        line-height: 1.6;
    }
    
    .component-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 700;
        margin-right: 8px;
        margin-top: 8px;
    }
    
    .asset-callout {
        background: #edf2f7;
        border-left: 4px solid #667eea;
        padding: 16px;
        border-radius: 8px;
        margin-top: 16px;
        font-size: 14px;
    }
    
    .asset-callout-title {
        font-weight: 700;
        color: #667eea;
        margin-bottom: 6px;
    }
    
    .asset-callout-text {
        color: #4a5568;
        line-height: 1.5;
    }
    
    .question-box {
        background: white;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 28px;
        border: 2px solid #e2e8f0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .question-box:hover {
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08);
        border-color: #667eea;
        transform: translateY(-2px);
    }
    
    .progress-counter {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 14px;
        padding: 18px 28px;
        text-align: center;
        font-weight: 800;
        font-size: 20px;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
    }
    
    .level-header {
        text-align: center;
        margin-bottom: 40px;
        animation: slideIn 0.8s ease-out;
    }
    
    .level-emoji {
        font-size: 72px;
        margin-bottom: 16px;
    }
    
    .level-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 12px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .level-subtitle {
        font-size: 22px;
        color: #2d3748;
        font-weight: 700;
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #cbd5e0, transparent);
        margin: 48px 0;
    }
    
    .summary-header {
        font-size: 28px;
        font-weight: 800;
        color: #1a202c;
        margin-bottom: 28px;
    }
    
    textarea {
        border-radius: 12px !important;
        border: 2px solid #e2e8f0 !important;
        font-family: 'Segoe UI', sans-serif !important;
        font-size: 15px !important;
        font-weight: 500 !important;
    }
    
    textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.15) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "current_q" not in st.session_state:
    st.session_state.current_q = 1
    st.session_state.answers = {}

# Story beat questions - FUN & INTERACTIVE
questions = {
    1: {
        "beat": "🎯 So… what are we even selling?",
        "title": "Problem Clarity + Demand Validation",
        "question": "🌅 Picture this: Your customer wakes up Monday morning. What's the PAINFUL, EXPENSIVE problem that makes them scream 'ugh, NOT AGAIN'? Get specific! Don't say 'they need help' — say 'they're bleeding $15K/month because X is broken'.",
        "context": "The more specific, the better. This is the ONLY reason they'll ever buy from you.",
        "extraction": {
            "label": "🔥 Core Problem Extracted",
            "content": "The real, painful, expensive problem they live with daily"
        },
        "component": {
            "name": "Problem Statement",
            "usage": "Becomes your website headline, email hook, and sales page pain section"
        },
        "asset": "💎 Website Hero Copy + Problem Definition Doc + Email Subject Lines"
    },
    2: {
        "beat": "💰 Money talk… don't run away",
        "title": "Pricing Logic + Perceived Value + ROI Justification",
        "question": "🚨 What's the REAL cost if they DON'T solve this? Give us numbers or consequences. How much money? How much time? Lost customers? Stress destroying their health? Make it REAL.",
        "context": "A specific cost ($50K/year lost) crushes a vague one ('they're losing money'). Quantify the pain.",
        "extraction": {
            "label": "💸 Cost Quantified",
            "content": "The financial and emotional price of the problem staying unsolved"
        },
        "component": {
            "name": "ROI Justification",
            "usage": "Powers your sales page, pricing justification, and ROI calculator"
        },
        "asset": "💎 Sales Page (Pain Section) + ROI Calculator + Demo Script"
    },
    3: {
        "beat": "✨ Drop the magic: what makes your offer actually good?",
        "title": "Value Prop + Feature/Benefit Stack + Mechanism",
        "question": "🚀 Fast forward 90 days. They SOLVED it. What's different? Not 'they use our tool' but 'they wake up with 30 qualified leads, stress-free, with 20 more hours in their week.' Paint the TRANSFORMATION.",
        "context": "This is the identity they're buying. Who do they become? That's the REAL magic.",
        "extraction": {
            "label": "✨ Transformation Outcome",
            "content": "The before/after story. The person they become after solving this."
        },
        "component": {
            "name": "Value Proposition",
            "usage": "Your main headline, landing page, email sequences, testimonials, and social proof"
        },
        "asset": "💎 Main Headline + Landing Page + Email Sequences + Case Studies + Testimonials"
    }
}

# Header
st.markdown(f"""
<div class='level-header'>
    <div class='level-emoji'>🔥</div>
    <div class='level-title'>Level 1: Foundation</div>
    <div class='level-subtitle'>Problem, Persona & Why They'll Buy</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Main flow
if st.session_state.current_q <= 3:
    q_data = questions[st.session_state.current_q]
    
    # Story beat setup
    st.markdown(f"""
    <div class='story-beat'>
        <div class='beat-number'>{q_data['beat']}</div>
        <div class='beat-question'>{q_data['question']}</div>
        <div class='beat-context'>💡 {q_data['context']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Question input
    st.markdown("<div class='question-box'>", unsafe_allow_html=True)
    
    answer = st.text_area(
        label="Your answer",
        value=st.session_state.answers.get(st.session_state.current_q, ""),
        height=140,
        label_visibility="collapsed",
        key=f"answer_{st.session_state.current_q}",
        placeholder="Share your answer here..."
    )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.session_state.answers[st.session_state.current_q] = answer
    
    # Show extraction only if answer provided
    if answer.strip():
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='extraction-box'>
            <div class='extraction-title'>✨ Here's What We Extracted</div>
            
            <div class='extraction-grid'>
                <div class='extraction-item'>
                    <div class='extraction-label'>{q_data['extraction']['label']}</div>
                    <div class='extraction-content'>{answer[:150]}...</div>
                </div>
                <div class='extraction-item'>
                    <div class='extraction-label'>Offer Component</div>
                    <div class='extraction-content'>{q_data['component']['name']}</div>
                </div>
            </div>
            
            <div class='extraction-item' style='grid-column: 1 / -1;'>
                <div class='extraction-label'>Where This Gets Used</div>
                <div class='extraction-content'>{q_data['component']['usage']}</div>
                <div class='asset-callout'>
                    <div class='asset-callout-title'>📦 Creative Asset:</div>
                    <div class='asset-callout-text'>{q_data['asset']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.current_q > 1:
            if st.button("⬅️ Back", use_container_width=True):
                st.session_state.current_q -= 1
                st.rerun()
    
    with col2:
        st.markdown(f"<div class='progress-counter'>{st.session_state.current_q} / 3</div>", unsafe_allow_html=True)
    
    with col3:
        if st.session_state.current_q < 3:
            if st.button("Next ➡️", use_container_width=True, type="primary"):
                if answer.strip():
                    st.session_state.current_q += 1
                    st.rerun()
                else:
                    st.warning("Please answer before moving forward!")
        else:
            if st.button("See Summary ✨", use_container_width=True, type="primary"):
                if answer.strip():
                    st.session_state.current_q = 4
                    st.rerun()
                else:
                    st.warning("Please answer before moving forward!")

else:
    # Summary page
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='level-header'>
        <div style='font-size: 64px; margin-bottom: 20px;'>✅</div>
        <div class='level-title'>Your Level 1 Blueprint</div>
        <div class='level-subtitle'>Everything extracted from your story</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    
    # Question 1 Summary
    st.markdown(f"""
    <div class='extraction-box'>
        <div class='summary-header'>🎯 So… what are we even selling?</div>
        <div style='color: #718096; margin-bottom: 20px; font-size: 14px;'>Problem Clarity + Demand Validation</div>
        
        <div class='extraction-grid'>
            <div class='extraction-item'>
                <div class='extraction-label'>🔥 The Problem</div>
                <div class='extraction-content'>{st.session_state.answers.get(1, 'Not answered')[:200]}</div>
            </div>
            <div class='extraction-item'>
                <div class='extraction-label'>Component</div>
                <div style='margin-top: 20px;'>
                    <div class='component-badge'>Problem Statement</div><br>
                </div>
            </div>
        </div>
        
        <div class='extraction-item' style='grid-column: 1 / -1;'>
            <div class='extraction-label'>💎 Creative Assets Using This</div>
            <div style='margin-top: 12px;'>
                <div class='component-badge'>Website Hero Copy</div>
                <div class='component-badge'>Problem Definition Doc</div>
                <div class='component-badge'>Email Subject Lines</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Question 2 Summary
    st.markdown(f"""
    <div class='extraction-box'>
        <div class='summary-header'>💰 Money talk… don't run away</div>
        <div style='color: #718096; margin-bottom: 20px; font-size: 14px;'>Pricing Logic + Perceived Value + ROI Justification</div>
        
        <div class='extraction-grid'>
            <div class='extraction-item'>
                <div class='extraction-label'>💸 The Cost</div>
                <div class='extraction-content'>{st.session_state.answers.get(2, 'Not answered')[:200]}</div>
            </div>
            <div class='extraction-item'>
                <div class='extraction-label'>Component</div>
                <div style='margin-top: 20px;'>
                    <div class='component-badge'>ROI Justification</div><br>
                </div>
            </div>
        </div>
        
        <div class='extraction-item' style='grid-column: 1 / -1;'>
            <div class='extraction-label'>💎 Creative Assets Using This</div>
            <div style='margin-top: 12px;'>
                <div class='component-badge'>Sales Page (Pain Section)</div>
                <div class='component-badge'>ROI Calculator</div>
                <div class='component-badge'>Demo Script</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Question 3 Summary
    st.markdown(f"""
    <div class='extraction-box'>
        <div class='summary-header'>✨ Drop the magic: what makes your offer actually good?</div>
        <div style='color: #718096; margin-bottom: 20px; font-size: 14px;'>Value Prop + Feature/Benefit Stack + Mechanism</div>
        
        <div class='extraction-grid'>
            <div class='extraction-item'>
                <div class='extraction-label'>🚀 The Transformation</div>
                <div class='extraction-content'>{st.session_state.answers.get(3, 'Not answered')[:200]}</div>
            </div>
            <div class='extraction-item'>
                <div class='extraction-label'>Component</div>
                <div style='margin-top: 20px;'>
                    <div class='component-badge'>Value Proposition</div><br>
                </div>
            </div>
        </div>
        
        <div class='extraction-item' style='grid-column: 1 / -1;'>
            <div class='extraction-label'>💎 Creative Assets Using This</div>
            <div style='margin-top: 12px;'>
                <div class='component-badge'>Main Headline</div>
                <div class='component-badge'>Landing Page</div>
                <div class='component-badge'>Email Sequences</div>
                <div class='component-badge'>Case Studies</div>
                <div class='component-badge'>Testimonials</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("⬅️ Start Over", use_container_width=True):
            st.session_state.current_q = 1
            st.session_state.answers = {}
            st.rerun()
    
    with col2:
        # Download
        json_data = json.dumps({
            "Act 1 - The Struggle": st.session_state.answers.get(1, ""),
            "Act 2 - The Cost": st.session_state.answers.get(2, ""),
            "Act 3 - The Dream": st.session_state.answers.get(3, ""),
        }, indent=2)
        
        st.download_button(
            label="📥 Download Your Answers",
            data=json_data,
            file_name=f"level1_blueprint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )
