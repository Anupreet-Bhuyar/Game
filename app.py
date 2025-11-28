import streamlit as st

st.set_page_config(page_title="10-Level Framework", layout="wide")

# Initialize session state
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
    st.session_state.responses = {}

# Define all 10 levels with questions
levels = {
    1: {
        "title": "Level 1 — So… what are we even selling?",
        "subtitle": "Problem clarity + demand validation",
        "questions": [
            "What is the real, painful, expensive problem you're solving?",
            "Do people already talk about this problem and pay for partial solutions?",
            "Why are current solutions failing?"
        ]
    },
    2: {
        "title": "Level 2 — Who are we here for?",
        "subtitle": "Target persona + emotional triggers",
        "questions": [
            "Who is the exact person that benefits fastest?",
            "What are their fears, desires, and frustrations?",
            "What makes them hesitate vs. what makes them say 'finally'?"
        ]
    },
    3: {
        "title": "Level 3 — Drop the magic: what makes your offer actually good?",
        "subtitle": "Value prop + feature/benefit stack + mechanism",
        "questions": [
            "What's your one dominant primary benefit?",
            "What are 3–5 natural secondary benefits?",
            "What unique mechanism creates differentiation?",
            "What bonuses remove last-minute objections?"
        ]
    },
    4: {
        "title": "Level 4 — Money talk… don't run away",
        "subtitle": "Pricing logic + perceived value + ROI justification",
        "questions": [
            "How should pricing reflect transformation, not comparison?",
            "How do you communicate value so price becomes obvious?",
            "What tiers/payment plans remove friction?",
            "How does pricing align with your business model long-term?"
        ]
    },
    5: {
        "title": "Level 5 — Make them feel safe, like a warm blanket",
        "subtitle": "Guarantee + objection removal",
        "questions": [
            "What's the biggest emotional fear your guarantee should target?",
            "What guarantee terms feel fair and simple?",
            "What operational systems must support your guarantee?",
            "Is this a trust accelerator or just marketing?"
        ]
    },
    6: {
        "title": "Level 6 — Spice time: urgency, scarcity, fireworks",
        "subtitle": "Scarcity + urgency + social proof + momentum",
        "questions": [
            "What real urgency exists (not gimmicks)?",
            "What's your actual scarcity tied to capacity or seasonality?",
            "What relatable social proof can you show?",
            "How do you deliver an instant early win?"
        ]
    },
    7: {
        "title": "Level 7 — Say it with style",
        "subtitle": "Messaging architecture + platform adaptation",
        "questions": [
            "What's your one core message governing all marketing?",
            "How does storytelling create emotional resonance?",
            "How do you adapt messaging by platform without changing meaning?",
            "How do visuals reinforce clarity and credibility?"
        ]
    },
    8: {
        "title": "Level 8 — Can you deliver what you promise?",
        "subtitle": "Delivery workflow + support + quality",
        "questions": [
            "How smooth is your onboarding experience?",
            "How fast and empathetic is your support?",
            "How does delivery scale without losing quality?",
            "How does post-purchase experience drive retention?"
        ]
    },
    9: {
        "title": "Level 9 — Test → tweak → dominate",
        "subtitle": "Optimization loop + feedback systems",
        "questions": [
            "How do you collect honest feedback, not polite feedback?",
            "What KPIs reflect the value you're delivering?",
            "What A/B tests isolate one variable?",
            "How is continuous improvement systematic, not occasional?"
        ]
    },
    10: {
        "title": "Level 10 — Lead generation: getting the right people to the party",
        "subtitle": "Lead definition + acquisition engine + nurturing",
        "questions": [
            "Who are the people actually ready (not just anyone with attention)?",
            "What lead magnets filter, qualify, and elevate?",
            "How do you build nurturing that creates clarity, not pressure?",
            "How do you track warmth signals and act at the right moment?"
        ]
    }
}

# Sidebar progress
st.sidebar.title("📊 Progress")
st.sidebar.progress(st.session_state.current_level / 10)
st.sidebar.write(f"**Level {st.session_state.current_level} of 10**")

# Main content
level_data = levels[st.session_state.current_level]

st.title(level_data["title"])
st.subheader(level_data["subtitle"])
st.divider()

# Get or create response for this level
level_key = f"level_{st.session_state.current_level}"
if level_key not in st.session_state.responses:
    st.session_state.responses[level_key] = {}

# Display questions ONE BY ONE
current_question_num = 1
for question in level_data["questions"]:
    st.write(f"**Q{current_question_num}:** {question}")
    
    response = st.text_area(
        label=f"Your answer",
        value=st.session_state.responses[level_key].get(question, ""),
        height=80,
        label_visibility="collapsed",
        key=f"q_{st.session_state.current_level}_{current_question_num}"
    )
    
    st.session_state.responses[level_key][question] = response
    st.divider()
    current_question_num += 1

# Navigation
col1, col2, col3 = st.columns(3)

with col1:
    if st.session_state.current_level > 1:
        if st.button("⬅️ Previous", use_container_width=True):
            st.session_state.current_level -= 1
            st.rerun()

with col2:
    st.write(f"**{st.session_state.current_level}/10**")

with col3:
    if st.session_state.current_level < 10:
        if st.button("Next Question ➡️", use_container_width=True):
            st.session_state.current_level += 1
            st.rerun()
    else:
        if st.button("✅ Done", use_container_width=True):
            st.balloons()
            st.success("Framework Complete!")
            st.write("**Save this in GitHub:**")
            st.code(str(st.session_state.responses), language="python")
