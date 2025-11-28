st.divider()

# Show insight quote if available
if st.session_state.current_level <= 3 and st.session_state.current_level in insights:
    insight = insights[st.session_state.current_level]
    st.markdown("---")
    st.markdown("### 💭 Why This Matters")
    with st.container(border=True):
        st.markdown(f"*\"{insight['quote']}\"*")
        st.markdown("")
        st.markdown(f"**The Concept:** {insight['concept']}")import streamlit as st
from datetime import datetime

st.set_page_config(page_title="10-Level Framework", layout="wide")

# Initialize session state
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
    st.session_state.responses = {}
    st.session_state.show_report = False

# Quotes and insights
insights = {
    1: {
        "quote": "A starving crowd beats a well-fed niche every single time.",
        "concept": "You need to find people who are ALREADY searching for a solution. If the problem isn't costing them money or time, they won't buy. This question forces you to prove the market exists before you build anything."
    },
    2: {
        "quote": "People don't buy products. They buy better versions of themselves.",
        "concept": "Your customer has an identity and a vision for who they want to become. This question uncovers their aspirational self—not just what they need, but who they want to be. That's the real sale."
    },
    3: {
        "quote": "Value is the delta between the perceived outcome and the price paid.",
        "concept": "A $10K offer that delivers $100K in transformation feels like a steal. A $100 offer that delivers $50 in value feels like a scam. This question forces you to nail the perceived transformation, not the features."
    },
}

# Define all 10 levels with AWESOME questions
levels = {
    1: {
        "title": "🎯 Level 1 — So… what are we even selling?",
        "subtitle": "Problem clarity + demand validation",
        "emoji": "🔥",
        "questions": [
            "What painful problem keeps your customer up at night? (Be specific — what does it cost them?)",
            "Where are they RIGHT NOW trying to solve this? (What are they paying for? What's broken?)",
            "What would change in their life if this problem disappeared? (Paint the before/after.)"
        ],
        "report_focus": "Problem Clarity",
        "insight_key": 1
    },
    2: {
        "title": "👥 Level 2 — Who are we here for?",
        "subtitle": "Target persona + emotional triggers",
        "emoji": "💡",
        "questions": [
            "Who FEELS this problem the most intensely? (Role, industry, income level?)",
            "What makes them say 'ugh, not again' when facing this problem? (What's their trigger?)",
            "What's the ONE thing they'd do differently if they knew it was possible? (Their secret wish?)"
        ],
        "report_focus": "Persona",
        "insight_key": 2
    },
    3: {
        "title": "✨ Level 3 — Drop the magic: what makes your offer actually good?",
        "subtitle": "Value prop + feature/benefit stack + mechanism",
        "emoji": "⚡",
        "questions": [
            "What's THE transformation your offer delivers? (Not features — what changes?)",
            "Why would someone believe YOU can do this better than the alternatives? (Your unfair advantage?)",
            "What's the main objection someone throws at you right before buying? (What's the doubt?)"
        ],
        "report_focus": "Value Proposition",
        "insight_key": 3
    },
    4: {
        "title": "💰 Level 4 — Money talk… don't run away",
        "subtitle": "Pricing logic + perceived value + ROI justification",
        "emoji": "💸",
        "questions": [
            "What's the ROI someone gets from this? (Time saved? Money made? Stress reduced? Give numbers.)",
            "If someone could get this for free vs. pay for it, what would they choose and why?",
            "What price point makes them think 'wow, that's a steal' vs. 'that seems cheap'?"
        ],
        "report_focus": "Pricing"
    },
    5: {
        "title": "🛡️ Level 5 — Make them feel safe, like a warm blanket",
        "subtitle": "Guarantee + objection removal",
        "emoji": "🤝",
        "questions": [
            "What's the WORST FEAR someone has before buying? (Buyer's remorse? Won't work for them?)",
            "If you could remove ONE doubt, which would flip them from 'maybe' to 'hell yes'?",
            "What guarantee could you give that would make them feel like there's zero risk?"
        ],
        "report_focus": "Trust & Safety"
    },
    6: {
        "title": "🔥 Level 6 — Spice time: urgency, scarcity, fireworks",
        "subtitle": "Scarcity + urgency + social proof + momentum",
        "emoji": "⏰",
        "questions": [
            "What's ACTUALLY scarce about your offer? (Limited spots? Seasonal? Capacity?)",
            "Why does someone need to act NOW instead of in 3 months?",
            "Who's already won with this? (Real wins, real people, real results?)"
        ],
        "report_focus": "Momentum"
    },
    7: {
        "title": "🎨 Level 7 — Say it with style",
        "subtitle": "Messaging architecture + platform adaptation",
        "emoji": "🎤",
        "questions": [
            "If you had ONE sentence to describe this offer, what would it be? (The headline that sticks.)",
            "What story PROVES your solution works? (The origin story? Customer story? Moment of truth?)",
            "What's your ONE call-to-action? (Apply? Buy? Book? Schedule?)"
        ],
        "report_focus": "Messaging"
    },
    8: {
        "title": "🚀 Level 8 — Can you deliver what you promise?",
        "subtitle": "Delivery workflow + support + quality",
        "emoji": "✅",
        "questions": [
            "What happens in the first 24 hours after someone says YES? (How fast do they feel the magic?)",
            "If something goes wrong, how do they reach you and get help? (Speed? Empathy? Solutions?)",
            "What's the ONE thing you do better than anyone else in delivery?"
        ],
        "report_focus": "Delivery"
    },
    9: {
        "title": "📊 Level 9 — Test → tweak → dominate",
        "subtitle": "Optimization loop + feedback systems",
        "emoji": "🎯",
        "questions": [
            "What's ONE thing you'd change about your offer RIGHT NOW if you got feedback?",
            "How do you know if someone's actually winning? (What metric proves success?)",
            "What's one test you could run this week to improve conversions?"
        ],
        "report_focus": "Optimization"
    },
    10: {
        "title": "🎪 Level 10 — Lead generation: getting the right people to the party",
        "subtitle": "Lead definition + acquisition engine + nurturing",
        "emoji": "📢",
        "questions": [
            "Where do your ideal customers ALREADY hang out? (Social? Communities? Podcasts? Groups?)",
            "What would make them stop scrolling and pay attention to YOUR message?",
            "After they first hear about you, how do you stay in their mind until they're ready?"
        ],
        "report_focus": "Lead Gen"
    }
}

# Function to generate readiness report
def generate_readiness_report():
    st.markdown("---")
    st.markdown("## 🎯 OFFER READINESS REPORT")
    st.markdown("*Based on your Level 1-3 answers*")
    
    col1, col2, col3 = st.columns(3)
    
    responses = st.session_state.responses.get("level_1", {})
    responses_2 = st.session_state.responses.get("level_2", {})
    responses_3 = st.session_state.responses.get("level_3", {})
    
    # Problem clarity
    with col1:
        problem_filled = len(responses.get(list(levels[1]["questions"])[0], "").strip()) > 20
        status = "✅ CLEAR" if problem_filled else "⚠️ FUZZY"
        st.metric("Problem Clarity", status)
        if problem_filled:
            st.caption("Your problem is REAL and specific")
        else:
            st.caption("Get more specific about the pain")
    
    # Persona
    with col2:
        persona_filled = len(responses_2.get(list(levels[2]["questions"])[0], "").strip()) > 20
        status = "✅ DEFINED" if persona_filled else "⚠️ VAGUE"
        st.metric("Persona Definition", status)
        if persona_filled:
            st.caption("You know WHO you're selling to")
        else:
            st.caption("Pin down your ideal customer")
    
    # Value Prop
    with col3:
        vp_filled = len(responses_3.get(list(levels[3]["questions"])[0], "").strip()) > 20
        status = "✅ STRONG" if vp_filled else "⚠️ WEAK"
        st.metric("Value Proposition", status)
        if vp_filled:
            st.caption("Your transformation is compelling")
        else:
            st.caption("Clarify the core transformation")
    
    st.markdown("---")
    
    # Readiness indicator
    ready_count = sum([problem_filled, persona_filled, vp_filled])
    
    if ready_count == 3:
        st.success("🚀 YOUR OFFER IS MARKET-READY! You have solid fundamentals. Move to pricing & positioning.")
    elif ready_count == 2:
        st.warning("⚡ YOU'RE ALMOST THERE. One more piece needs clarity before scaling messaging.")
    else:
        st.info("💭 STILL FOUNDATIONAL. Go deeper on problem/persona/value before spending on marketing.")

# Header with progress
st.markdown(f"## {levels[st.session_state.current_level]['emoji']} {levels[st.session_state.current_level]['title']}")
st.markdown(f"*{levels[st.session_state.current_level]['subtitle']}*")

# Animated progress bar
progress_val = st.session_state.current_level / 10
st.progress(progress_val)
st.markdown(f"**Progress: Level {st.session_state.current_level} / 10**")

st.divider()

# Get or create response for this level
level_key = f"level_{st.session_state.current_level}"
if level_key not in st.session_state.responses:
    st.session_state.responses[level_key] = {}

# Display questions with interactive styling
current_question_num = 1
for question in levels[st.session_state.current_level]["questions"]:
    with st.container(border=True):
        st.markdown(f"### Question {current_question_num}")
        st.markdown(f"> {question}")
        
        response = st.text_area(
            label=f"Your answer",
            value=st.session_state.responses[level_key].get(question, ""),
            height=100,
            label_visibility="collapsed",
            key=f"q_{st.session_state.current_level}_{current_question_num}",
            placeholder="Type your answer here..."
        )
        
        st.session_state.responses[level_key][question] = response
    
    current_question_num += 1

st.divider()

# Navigation with interactive buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.session_state.current_level > 1:
        if st.button("⬅️ Previous", use_container_width=True, key="prev_btn"):
            st.session_state.current_level -= 1
            st.session_state.show_report = False
            st.rerun()

with col2:
    st.markdown(f"<div style='text-align: center; padding: 10px; background: #f0f0f0; border-radius: 5px;'><b>{st.session_state.current_level}/10</b></div>", unsafe_allow_html=True)

with col3:
    if st.session_state.current_level < 10:
        if st.button("Next Question ➡️", use_container_width=True, key="next_btn", type="primary"):
            st.session_state.current_level += 1
            if st.session_state.current_level == 4:
                st.session_state.show_report = True
            st.rerun()
    else:
        if st.button("✅ Complete & View Results", use_container_width=True, key="done_btn", type="primary"):
            st.session_state.show_report = True
            st.rerun()

# Show report after level 3
if st.session_state.show_report and st.session_state.current_level >= 4:
    generate_readiness_report()

# Show final summary at the end
if st.session_state.current_level == 10 and st.session_state.show_report:
    st.markdown("---")
    st.markdown("## 🎉 Ready to launch? Here's your snapshot:")
    
    snapshot_data = {
        "Problem": st.session_state.responses.get("level_1", {}).get(list(levels[1]["questions"])[0], "N/A")[:100],
        "Persona": st.session_state.responses.get("level_2", {}).get(list(levels[2]["questions"])[0], "N/A")[:100],
        "Transformation": st.session_state.responses.get("level_3", {}).get(list(levels[3]["questions"])[0], "N/A")[:100],
        "Generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    
    st.json(snapshot_data)
