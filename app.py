import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Offer Blueprint", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS - Pure Awesome
st.markdown("""
<style>
    * {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    body {
        background: #f8fafc;
    }
    
    .insight-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 40px;
        color: white;
        margin-bottom: 32px;
        box-shadow: 0 25px 70px rgba(102, 126, 234, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
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
    
    .insight-quote {
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 20px;
        line-height: 1.4;
        letter-spacing: -0.5px;
    }
    
    .insight-concept {
        font-size: 17px;
        line-height: 1.8;
        opacity: 0.98;
        font-weight: 500;
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
        margin-bottom: 8px;
    }
    
    .level-desc {
        font-size: 16px;
        color: #718096;
        font-weight: 500;
    }
    
    .question-box {
        background: white;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 28px;
        border: 2px solid #e2e8f0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        border-left: 6px solid #667eea;
    }
    
    .question-box:hover {
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08);
        border-left-color: #764ba2;
        transform: translateY(-2px);
    }
    
    .question-num {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        font-weight: 800;
        font-size: 14px;
        margin-bottom: 16px;
        letter-spacing: 1px;
    }
    
    .question-text {
        font-size: 20px;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 20px;
        line-height: 1.6;
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
    
    .asset-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        margin-top: 40px;
    }
    
    .asset-card {
        background: white;
        border-radius: 16px;
        padding: 32px;
        border: 2px solid #e2e8f0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        animation: fadeIn 0.8s ease-out;
    }
    
    .asset-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.1);
        border-color: #667eea;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .asset-icon {
        font-size: 40px;
        margin-bottom: 12px;
    }
    
    .asset-title {
        font-size: 20px;
        font-weight: 800;
        color: #1a202c;
        margin-bottom: 12px;
    }
    
    .asset-desc {
        font-size: 15px;
        color: #4a5568;
        line-height: 1.7;
        margin-bottom: 20px;
    }
    
    .components-list {
        background: linear-gradient(135deg, #f5f7fa 0%, #edf2f7 100%);
        border-radius: 12px;
        padding: 16px;
    }
    
    .component-item {
        display: flex;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #e2e8f0;
        font-size: 14px;
        font-weight: 600;
        color: #2d3748;
    }
    
    .component-item:last-child {
        border-bottom: none;
    }
    
    .component-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin-right: 12px;
        flex-shrink: 0;
    }
    
    .assets-section {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 20px;
        padding: 48px;
        margin-top: 48px;
        border: 2px solid rgba(102, 126, 234, 0.1);
    }
    
    .assets-title {
        font-size: 40px;
        font-weight: 900;
        color: #1a202c;
        margin-bottom: 8px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .assets-subtitle {
        font-size: 18px;
        color: #4a5568;
        margin-bottom: 32px;
        font-weight: 600;
    }
    
    .nav-button {
        border-radius: 12px;
        font-weight: 700;
        font-size: 16px;
        padding: 14px 28px;
        transition: all 0.3s ease;
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
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #cbd5e0, transparent);
        margin: 48px 0;
    }
    
    @media (max-width: 768px) {
        .asset-grid {
            grid-template-columns: 1fr;
        }
        
        .level-title {
            font-size: 40px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
    st.session_state.responses = {}

# Insights
insights = {
    1: {
        "quote": "A starving crowd beats a well-fed niche every single time.",
        "concept": "You need people ALREADY searching for solutions. If the problem isn't costing them money or time, they won't buy. This proves your market exists."
    },
    2: {
        "quote": "People don't buy products. They buy better versions of themselves.",
        "concept": "Your customer wants an identity change. This uncovers their aspirational self—not what they need, but who they want to become. That's the real sale."
    },
    3: {
        "quote": "Value is the delta between perceived outcome and price paid.",
        "concept": "A $10K offer delivering $100K feels like a steal. Your job is to nail the perceived transformation, not just features."
    },
}

# Framework
levels = {
    1: {
        "title": "Level 1",
        "heading": "Problem, Persona & Why They'll Buy",
        "subtitle": "The Foundation",
        "emoji": "🔥",
        "questions": [
            "What painful problem keeps your target customer up at night, where are they trying to solve it NOW, and what would their life look like if this disappeared?",
            "Who FEELS this problem most intensely, what frustrates them, and what aspirational version of themselves are they chasing?"
        ],
        "insight_key": 1,
        "assets": {
            "q1": {
                "icon": "📋",
                "title": "Problem Definition Doc",
                "description": "A one-pager explaining the core problem, current solutions they use (and why they fail), and the promised transformation.",
                "components": ["Problem Statement", "Current Workarounds", "Pain Point Cost", "Desired Outcome"]
            },
            "q2": {
                "icon": "👥",
                "title": "Buyer Persona Profile",
                "description": "A detailed portrait: their role, frustrations, fears, and the identity/status they're chasing.",
                "components": ["Demographics", "Psychographics", "Emotional Triggers", "Aspirational Identity"]
            }
        }
    },
    2: {
        "title": "Level 2",
        "heading": "Offer, Value & Trust",
        "subtitle": "The Offer Architecture",
        "emoji": "⚡",
        "questions": [
            "What's THE transformation your offer delivers (not features), why would they believe YOU, and what's the main objection they'll throw at you?",
            "What's the biggest emotional fear before buying, and what guarantee or proof would flip them from 'maybe' to 'hell yes'?"
        ],
        "insight_key": 2,
        "assets": {
            "q1": {
                "icon": "🎁",
                "title": "Value Proposition Kit",
                "description": "The transformation promise, unfair advantage, proof of concept, and objection-busting content pieces.",
                "components": ["Transformation Statement", "Competitive Advantage", "Feature-to-Benefit Map", "Objection Handlers"]
            },
            "q2": {
                "icon": "🛡️",
                "title": "Trust & Safety Layer",
                "description": "Guarantees, testimonials, case studies, and risk-reversal mechanics that remove buyer hesitation.",
                "components": ["Money-Back Guarantee", "Success Stories", "Case Study Template", "Risk-Reversal Copy"]
            }
        }
    },
    3: {
        "title": "Level 3",
        "heading": "Messaging, Pricing & Launch",
        "subtitle": "The Go-to-Market Blueprint",
        "emoji": "🚀",
        "questions": [
            "What's your ONE-sentence headline, what story proves it works, what's your core CTA, and where do your customers already hang out?",
            "What's the ROI they get, what price feels like a steal vs. cheap, and what real urgency or scarcity do you have?"
        ],
        "insight_key": 3,
        "assets": {
            "q1": {
                "icon": "📢",
                "title": "Marketing Message Stack",
                "description": "Your headline, subheading, core story, CTAs, and channel-specific messaging for different platforms.",
                "components": ["Headline", "Hero Copy", "Social Posts", "Email Sequences", "Sales Page"]
            },
            "q2": {
                "icon": "💰",
                "title": "Pricing & Scarcity Plan",
                "description": "ROI calculator, pricing tiers, value communication, urgency hooks, and real scarcity mechanics.",
                "components": ["ROI Breakdown", "Pricing Tiers", "Value Justification", "Urgency Hooks", "Scarcity Rules"]
            }
        }
    }
}

# Show insight at top
if st.session_state.current_level in insights:
    insight = insights[st.session_state.current_level]
    st.markdown(f"""
    <div class='insight-card'>
        <div class='insight-quote'>"{insight['quote']}"</div>
        <div class='insight-concept'>{insight['concept']}</div>
    </div>
    """, unsafe_allow_html=True)

# Header
level_data = levels[st.session_state.current_level]
st.markdown(f"""
<div class='level-header'>
    <div class='level-emoji'>{level_data['emoji']}</div>
    <div class='level-title'>{level_data['title']}</div>
    <div class='level-subtitle'>{level_data['heading']}</div>
    <div class='level-desc'>{level_data['subtitle']}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Questions
level_key = f"level_{st.session_state.current_level}"
if level_key not in st.session_state.responses:
    st.session_state.responses[level_key] = {}

q_num = 1
for question in level_data['questions']:
    st.markdown(f"""
    <div class='question-box'>
        <div class='question-num'>Question {q_num}</div>
        <div class='question-text'>{question}</div>
    </div>
    """, unsafe_allow_html=True)
    
    response = st.text_area(
        label=f"Your answer",
        value=st.session_state.responses[level_key].get(question, ""),
        height=120,
        label_visibility="collapsed",
        key=f"q_{st.session_state.current_level}_{q_num}",
        placeholder="Your answer here..."
    )
    
    st.session_state.responses[level_key][question] = response
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Show assets for this question
    asset_key = f"q{q_num}"
    asset = level_data['assets'][asset_key]
    
    st.markdown(f"""
    <div class='assets-section'>
        <div class='assets-title'>{asset['icon']} {asset['title']}</div>
        <div class='assets-subtitle'>{asset['description']}</div>
        <div class='components-list'>
    """, unsafe_allow_html=True)
    
    for component in asset['components']:
        st.markdown(f"<div class='component-item'><div class='component-dot'></div>{component}</div>", unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    q_num += 1

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.current_level > 1:
        if st.button("⬅️ Previous", use_container_width=True, key="prev_btn"):
            st.session_state.current_level -= 1
            st.rerun()

with col2:
    st.markdown(f"<div class='progress-counter'>{st.session_state.current_level} / 3</div>", unsafe_allow_html=True)

with col3:
    if st.session_state.current_level < 3:
        if st.button("Next ➡️", use_container_width=True, key="next_btn", type="primary"):
            st.session_state.current_level += 1
            st.rerun()
    else:
        if st.button("✅ Complete", use_container_width=True, key="done_btn", type="primary"):
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class='level-header'>
                <div style='font-size: 64px; margin-bottom: 20px;'>🎉</div>
                <div class='level-title'>Your Creative Assets Are Ready</div>
                <div class='level-desc'>Everything you need to build, based on YOUR answers</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            
            # Extract answers
            l1_q1 = st.session_state.responses.get("level_1", {}).get(levels[1]["questions"][0], "")
            l1_q2 = st.session_state.responses.get("level_1", {}).get(levels[1]["questions"][1], "")
            l2_q1 = st.session_state.responses.get("level_2", {}).get(levels[2]["questions"][0], "")
            l2_q2 = st.session_state.responses.get("level_2", {}).get(levels[2]["questions"][1], "")
            l3_q1 = st.session_state.responses.get("level_3", {}).get(levels[3]["questions"][0], "")
            l3_q2 = st.session_state.responses.get("level_3", {}).get(levels[3]["questions"][1], "")
            
            # LEVEL 1 ASSETS
            st.markdown(f"""
            <div class='assets-section'>
                <div class='assets-title'>🔥 LEVEL 1: Foundation Assets</div>
                <div class='assets-subtitle'>Your problem, persona, and market validation</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>📋</div>
                <div class='asset-title'>1. Problem Definition Document</div>
                <div class='asset-desc'><strong>What to build:</strong> A one-pager that positions your solution</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Core Problem Statement:**")
                if l1_q1:
                    st.markdown(f"> {l1_q1.split('?')[0].strip()}?")
                else:
                    st.markdown("> *[Your problem here]*")
            with col2:
                st.markdown("**Current Workarounds They Use:**")
                if l1_q1 and "NOW" in l1_q1:
                    st.markdown("> Extract their current solution attempts from your answer")
                else:
                    st.markdown("> *[What they're using now]*")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>👥</div>
                <div class='asset-title'>2. Buyer Persona Profile (One-Pager)</div>
                <div class='asset-desc'><strong>What to build:</strong> Visual persona template with their dreams & fears</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("**Who They Are:**")
                if l1_q2:
                    parts = l1_q2.split(",")
                    st.markdown(f"> {parts[0].strip() if parts else '[Role/Title]'}")
                else:
                    st.markdown("> *[Their role/industry]*")
            with col2:
                st.markdown("**What Frustrates Them:**")
                if l1_q2:
                    st.markdown(f"> Daily friction in their work/life")
                else:
                    st.markdown("> *[Key frustrations]*")
            with col3:
                st.markdown("**Their Secret Dream:**")
                if l1_q2 and "aspirational" in l1_q2.lower():
                    st.markdown(f"> The identity they want to claim")
                else:
                    st.markdown("> *[Who they want to become]*")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>🎯</div>
                <div class='asset-title'>3. Market Validation Checklist</div>
                <div class='asset-desc'><strong>What to build:</strong> Evidence that this market exists & has money</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            - [ ] Interview 5 people with this problem
            - [ ] Document what they're currently paying for
            - [ ] Quantify the cost of the problem (time/money lost)
            - [ ] Find 3 competitors or partial solutions they use
            - [ ] Screenshot their frustrations in public (Twitter, Reddit, forums)
            """)
            
            # LEVEL 2 ASSETS
            st.markdown(f"""
            <div class='assets-section'>
                <div class='assets-title'>⚡ LEVEL 2: Offer & Trust Assets</div>
                <div class='assets-subtitle'>Your value prop, competitive advantage, and risk reversal</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>🎁</div>
                <div class='asset-title'>4. Value Proposition One-Liner</div>
                <div class='asset-desc'><strong>What to build:</strong> The core transformation in one sentence</div>
            </div>
            """, unsafe_allow_html=True)
            
            if l2_q1:
                st.info(f"**Your Transformation:** {l2_q1.split('?')[0].strip()}?")
            else:
                st.info("**Your Transformation:** [What fundamentally changes for them]")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>🏆</div>
                <div class='asset-title'>5. Competitive Advantage Statement</div>
                <div class='asset-desc'><strong>What to build:</strong> Why THEY can deliver this better</div>
            </div>
            """, unsafe_allow_html=True)
            
            if l2_q1:
                st.warning("**Your Unfair Advantage:** Extract why you're different from your answer above")
            else:
                st.warning("**Your Unfair Advantage:** [What makes you unique]")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>🔥</div>
                <div class='asset-title'>6. Objection Handler Documents</div>
                <div class='asset-desc'><strong>What to build:</strong> FAQ, blog posts, and email sequences</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Main Objection to Address:**")
                if l2_q1:
                    st.markdown(f"> The 'doubt' they have before buying")
                else:
                    st.markdown("> *[What's their main hesitation?]*")
            with col2:
                st.markdown("**Proof Points to Include:**")
                st.markdown("> • Testimonials\n> • Case studies\n> • Before/After comparisons\n> • Data/Results")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>🛡️</div>
                <div class='asset-title'>7. Trust & Risk-Reversal Kit</div>
                <div class='asset-desc'><strong>What to build:</strong> Guarantee, testimonials, social proof</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Their Biggest Fear:**")
                if l2_q2:
                    st.markdown(f"> Extract from: What's the emotional fear?")
                else:
                    st.markdown("> *[What do they fear losing?]*")
            with col2:
                st.markdown("**Your Guarantee:**")
                if l2_q2:
                    st.markdown(f"> Design to remove that specific fear")
                else:
                    st.markdown("> *[Money back? Results guaranteed? Risk reversal?]*")
            
            # LEVEL 3 ASSETS
            st.markdown(f"""
            <div class='assets-section'>
                <div class='assets-title'>🚀 LEVEL 3: Launch & Go-to-Market Assets</div>
                <div class='assets-subtitle'>Messaging, pricing, and customer acquisition</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>📢</div>
                <div class='asset-title'>8. Marketing Headline & Hero Copy</div>
                <div class='asset-desc'><strong>What to build:</strong> Your website hero section text</div>
            </div>
            """, unsafe_allow_html=True)
            
            if l3_q1:
                st.success(f"**Your Headline:** Extract the one-sentence offer from your answer")
            else:
                st.success("**Your Headline:** [What's your core promise?]")
            
            st.markdown("**Hero Copy Template:**\n- Headline\n- Subheading (why them specifically)\n- Main benefit\n- Call to action")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>📖</div>
                <div class='asset-title'>9. Proof Story & Case Study Template</div>
                <div class='asset-desc'><strong>What to build:</strong> The narrative that proves it works</div>
            </div>
            """, unsafe_allow_html=True)
            
            if l3_q1:
                st.markdown("**Your Proof Story:** The story that shows this works (origin/customer success)")
            else:
                st.markdown("**Your Proof Story:** [What evidence do you have?]")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>💰</div>
                <div class='asset-title'>10. Pricing & ROI Justification Document</div>
                <div class='asset-desc'><strong>What to build:</strong> Show ROI so price feels like a steal</div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("**ROI They Get:**")
                if l3_q2:
                    st.markdown("> Time saved? Money made? Status gained?")
                else:
                    st.markdown("> *[Quantify the win]*")
            with col2:
                st.markdown("**Price Point (Steal Zone):**")
                if l3_q2:
                    st.markdown("> Where they think 'wow, that's cheap'")
                else:
                    st.markdown("> *[What feels like great value?]*")
            with col3:
                st.markdown("**Real Scarcity/Urgency:**")
                if l3_q2:
                    st.markdown("> Limited spots? Deadline? Seasonal?")
                else:
                    st.markdown("> *[What's actually scarce?]*")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>📱</div>
                <div class='asset-title'>11. Multi-Channel Content Stack</div>
                <div class='asset-desc'><strong>What to build:</strong> Content adapted for each platform</div>
            </div>
            """, unsafe_allow_html=True)
            
            channels = {
                "Twitter/X": "20-char punchy hooks + proof",
                "LinkedIn": "Thought leadership + case study",
                "Facebook": "Emotional + transformation angle",
                "Email": "Story-driven sequences",
                "Landing Page": "Hero copy + proof + CTA",
                "Sales Page": "Full VSL script + testimonials"
            }
            
            for platform, what_to_do in channels.items():
                st.markdown(f"✓ **{platform}:** {what_to_do}")
            
            st.markdown("""
            <div class='asset-card'>
                <div class='asset-icon'>🎯</div>
                <div class='asset-title'>12. Customer Acquisition Plan</div>
                <div class='asset-desc'><strong>What to build:</strong> Where to find & reach your people</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            - [ ] Identify 3 platforms where customers hang out
            - [ ] Create a lead magnet that solves a micro-problem
            - [ ] Build email nurture sequence (5-7 emails)
            - [ ] Design sales page conversion flow
            - [ ] Set up tracking & analytics
            - [ ] Plan initial customer outreach campaign
            """)
            
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class='level-header'>
                <div style='font-size: 48px; margin-bottom: 16px;'>✅</div>
                <div class='level-title'>You Have Everything You Need</div>
                <div class='level-desc'>12 Creative Assets Ready to Build • Download Your Answers • Start Creating Today</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Download button
            import json
            all_responses = st.session_state.responses
            json_str = json.dumps(all_responses, indent=2)
            st.download_button(
                label="📥 Download Your Complete Blueprint (JSON)",
                data=json_str,
                file_name=f"offer_blueprint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
