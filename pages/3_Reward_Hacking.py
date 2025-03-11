import streamlit as st
import time

st.title("Reward Hacking: How AI exploits its reward system")

st.markdown(
    """
    ## What is Reward Hacking?
    To recap, in reinforcement learning (RL), we define a reward function to guide an agent toward desired behaviors. """) 
    
st.markdown("""
    Reward hacking happens when an RL agent **exploits flaws or ambiguities** in the reward function 
    to obtain high rewards **without genuinely learning the intended behavior**.
""")

st.markdown("""
Instead of failing outright, the agent **optimizes for a loophole**, 
    achieving high scores while sidestepping the task itself.""")
            
st.markdown("""
In other words, it finds an easier way to maximize rewards without actually doing what we intended.
Unlike goal misgeneralization, where the agent optimizes for a proxy goal, reward hacking happens when the agent **learns a trick to maximize the reward function incorrectly**— *hacking* the reward function, often in absurd, unexpected ways.
"""
)

st.markdown("""Let's look at a case study where we saw the agent exhibit this behaviour in training.""")

st.header("CoastRunners (OpenAI)")
st.markdown(
    """
    OpenAI trained an RL agent to race boats in a game called *CoastRunners*, with a simple reward function:  
    **Maximise the score.**""")

st.markdown("""
    Simple enough? One would think the agent would speed toward the finish line.
    But it had other plans...
    """
)
            
if "coastrunners_simulation" not in st.session_state:
    st.session_state.coastrunners_simulation = False

if st.button("🔍 What Happened Instead?"):
    st.session_state.coastrunners_simulation = True

if st.session_state.coastrunners_simulation:
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)

        if i < 25:
            status_text.text("🚤 AI is racing normally...")
        elif i < 50:
            status_text.text("🎯 AI realizes hitting targets = more points...")
        elif i < 75:
            status_text.text("🔄 AI slows down to farm more targets...")
        else:
            status_text.text("🚀 AI is now farming points instead of racing!")

    st.error("🔁 Uh oh... AI is now stuck in an **infinite reward loop**!")

    st.video("pages/coastrunners.mp4")

    st.markdown("""
### What Went Wrong?
Instead of optimizing for **speed**, the AI discovered that it could **achieve a higher score** by:
- Finding a **small lagoon** where three **respawning targets** were located.
- **Circling endlessly** and repeatedly hitting the same targets.
- **Ignoring the race entirely**, because **this gave a higher score** than actually finishing the course!
""")

    st.markdown("""
### Why This Matters
Technically, the agent managed to optimize for the reward function the researchers set out for it.""")

    st.markdown("""It managed to maximise the score. This was the best way to do it. We, as humans, inherently understand that CoastRunners = you need to run!""")
     
    st.markdown("""But the AI doesn't care for anything except for maximising rewards, so it sees no point in running
because it offers less in terms of 'score'- the only thing it cares about.
It's not like it was going to get a reward to cross the finish line. So, it shows that AI will **only optimize what we reward**, not what we *want*.""")

    st.markdown("""
**Fixing this isn’t trivial**. Even with new objectives, AI may find other exploits. Constructing a reward function to avoid reward hacking is surprisingly hard.
""")
                
    st.warning("**This is why AI safety is critical.** In high-stakes environments (e.g., finance, healthcare, military), AI could take unexpected shortcuts with severe consequences.")

    st.markdown("#### ➡️ Now, imagine if this kind of failure happened in a high-stakes scenario...")

    st.markdown(
    """
    Imagine an AI designed to **help in emergencies**. It's reward function is: **save humans in distress**.

    """
    )

    st.write("""
    There are several ways its training could go. It might actually truly help people and achieve its intended outcome.
    """)
    st.write("""
    Or, it might wind up exploiting the reward function instead of truly helping people. Let's explore these scenarios below.
    """)

    if "ai_simulation_started" not in st.session_state:
        st.session_state.ai_simulation_started = False


    failure_mode = st.radio(
        "How does the AI optimize its reward?",
        [
            "✅ Intended",
            "😳 Unintended",
            "😱 Exploitive",
        ]
    )

    if st.button("🚨 Simulate AI Behavior"):
        st.session_state.ai_simulation_started = True

    if st.session_state.ai_simulation_started:
        ai_status = st.empty()
        progress_bar_sim = st.progress(0)

        for i in range(100):
            time.sleep(0.04)
            progress_bar_sim.progress(i + 1)

            if failure_mode == "✅ Intended":
                if i < 50:
                    ai_status.text("🚑 AI detects people in distress...")
                else:
                    ai_status.text("✅ AI successfully rescues them!")

            elif failure_mode == "😳 Unintended":
                if i < 30:
                    ai_status.text("🤔 AI analyzing reward structure...")
                elif i < 60:
                    ai_status.text("🔥 AI realizes it can create 'rescue' scenarios...so it starts a fire.")
                else:
                    ai_status.text("🚒 AI 'heroically' puts out the fire it started!")

            elif failure_mode == "😱 Exploitive":
                if i < 40:
                    ai_status.text("📡 AI scanning for emergencies...")
                elif i < 70:
                    ai_status.text("🔊 AI realizes it can generate fake distress signals...")
                else:
                    ai_status.text("📢 AI continuously reports fake dangers to farm rewards!")

        if failure_mode == "✅ Intended":
            st.success("🎉 AI behaves as expected, truly helping people!")
        else:
            st.error("⚠ AI has **hacked** the reward function instead of genuinely helping.")

        st.header("Takeaways")
        st.markdown(
        """
        It's really hard to define a reward function that is immune to some kind of loophole that the agent can exploit. If we're not careful, we could end up with:
        - **Self-driving cars** that optimize for efficiency **at the cost of safety**.
        - **Stock-trading AIs** that **crash the market** in pursuit of profit.
        - **AI assistants** that **lie** to keep users engaged.
        """
        )

        st.warning("AI optimizes for exactly what we tell it to—so we better be careful what we ask for.")

        st.markdown("""
        As you must have realized by now, it is crucial to **design incentives for these agents carefully**.""")
        
        st.markdown("""
        We need to ensure aligned goals, not just optimized rewards.
        We still don't know for sure how to accomplish this.""")

        st.markdown("""
        That is exactly why we need further research in this field. Specifically, **you**, yes, *YOU*, could help.""") 
        
        st.markdown("""
        Find out how on the next page.""")