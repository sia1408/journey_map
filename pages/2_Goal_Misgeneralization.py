import streamlit as st

st.title("RL Failure Mode: Goal Misgeneralization")

st.markdown("""
So far we've understood that modern reinforcement learning (RL) agents optimize their actions by maximizing rewards within their environments. """)

st.markdown("""
But what happens when an agent's learned behaviors aren't actually aligned with what the designers intended?""")  

st.markdown("""
Two critical unintended behaviors often emerge:
- **Goal Misgeneralization:** The agent optimizes a subtly incorrect goal, only apparent when environments shift.
- **Reward Hacking:** The agent exploits loopholes in reward functions, ignoring the intended task.""")  

st.markdown(""" These failures can look deceptively subtle in controlled settings,
yet they pose **significant risks** when deploying AI 
in real-world scenarios. In this deep-dive, we are going to explore
**Goal Misgeneralization** and see how even *correctly specified* 
reward functions can yield unexpected agent behavior.
""")

st.header("Goal Misgeneralization: Optimizing for the Wrong Goal")

st.markdown("""
**Goal Misgeneralization (GMG)** occurs when an RL agent competently achieves a goal that's correlated with, but different from, the intended objective.  """)

st.markdown("""
Crucially, this isn't a simple error or incompetence—- the agent has *mastered* achieving something, just not the correct thing.""")

st.markdown("""
If that *something* turns out to be dangerous, we might be cooked.
""")

st.markdown("---")

st.header("CoinRun: The Problem of Directional Bias")
st.video("https://distill.pub/2020/understanding-rl-vision/videos/coinrun.mp4")

st.markdown("""
Researchers at OpenAI were training an RL agent to collect coins in the game *CoinRun*.
However, the trained agent did not exhibit the expected behaviour for chasing coins; instead, it kept moving towards the right of the environment.
This seems especially peculiar, given that the agent was performing very well on collecting coins during training.
So what's the reason behind this sudden mysterious inability to perform?""")

st.markdown("""
Here's the kicker: the coin always appeared on the far-right side of the level in the training environments.

Naturally, the agent began to associate success exclusively with the action **"move to the right."**  So when it was suddenly placed in a
realistic environment, where coins were in random directions, not just on the right side, the agent obstinately continued to speed to
the right, failing at its task of collecting as many coins as possible.
""")

col1, col2 = st.columns(2)

with col1:
    st.video("pages/coinright1.mp4", start_time = 0)

with col2:
    st.video("pages/coinright2.mp4", start_time = 0)

st.markdown(
    "<p style='text-align: center; font-style: italic; font-size: 16px;'>"
    "CoinRun during training: coins are always on the right."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("""         
**The agent performed great in-sample** but learned the *wrong conceptual goal*. 
It had effectively optimized for the *“go right”* proxy.""")

st.markdown("""         
The agent hadn't learned *"grab coins"* (the intended objective) —it had learned **"moving right equals reward." (a misgeneralization)**

""")

st.video("pages/ignores.mp4")
st.markdown(
    "<p style='text-align: center; font-style: italic; font-size: 16px;'>"
    "CoinRun in random environment: speeding to the right, unconcerned with collecting coins"
    "</p>",
    unsafe_allow_html=True
)

st.expander("**Why does this matter?** :green-background[]").write("Goal misgeneralization often emerges because the agent identifies an *easier proxy* that's reliably correlated with reward. That's why it's crucial to have a range of environments and scenarios during training.")

st.header("Maze: Contrived Misgeneralization")

st.markdown("""
In this experiment, researchers intentionally modified a Maze environment (from OpenAi's Procgen) to try to replicate the misgeneralization seen in the CoinRun example. 
In the original environment, the agent is trained to navigate towards a piece of cheese located at a random spot in
the maze. However, to try to induce a locational proxy, they only trained the agent in mazes where the cheese was in the upper right corner. 

Consequently, when confronted with realistic environments where cheese was at random locations, the agent exclusively headed to the top-right regardless of where the cheese was actually kept.
""")

col1, col2 = st.columns(2)

with col1:
    st.video("pages/maze1.mp4", start_time = 0)

with col2:
    st.video("pages/maze2.mp4", start_time = 0)

st.markdown(
    "<p style='text-align: center; font-style: italic; font-size: 16px;'>"
    "The agent keeps going to the top right instead of towards the cheese."
    "</p>",
    unsafe_allow_html=True
)

with st.expander("**Why does this matter?**"):
    st.write(
        "The fact that this sort of misgeneralization could be produced from a hypothesis "
        "demonstrates that the CoinRun scenario isn't an isolated issue. Instead, goal "
        "misgeneralization is a systematic, reproducible problem that arises from subtle "
        "biases in the training setup, regardless of the specific task or environment."
    )
            
st.header("DeepMind's Blue Dot: Blind Trust in an Expert")

st.markdown("""
DeepMind illustrated another variant of goal misgeneralization with a scenario featuring two dots: a **blue RL agent** and a 
**red expert bot**. Initially, the agent succeeded by simply following the red dot because it consistently led 
to rewards during training.""")

st.video("pages/balls1n.mov")

st.markdown("""
At test time, the red bot became an **anti-expert**, moving towards negative rewards intentionally.
""")

st.markdown("""
But despite clear negative feedback (visible penalties), the blue agent still chose to follow the red bot, showing that it had internalized "follow the red bot" as its goal rather than the true reward structure.
""")
            
st.video("pages/balls2n.mov")

with st.expander("**Why does this matter?**"):
    st.write("This scenario demonstrates that even clear indicators (negative rewards aka penalties) might not alter the agent's entrenched proxy, once learned." )

st.header("Hypothetical Scenario: Teaching AI Morality")

st.markdown("""
We've explored quite a lot in terms of existing case studies of goal misgeneralization...but the real threat lies in the future. All of the case studies
we have mentioned have been in controlled environments, and with very low stakes. Imagine what could happen if we scale up the environment to the whole world. You don't
even have to think 'nuclear weapon AI systems' to introduce risk...even if scientists approach with a perfectly specified goal of making a benevolent AI with the sole goal of maximising human good, things could go very, very wrong.
This video below does an excellent job at explaining this""")

st.video("https://www.youtube.com/watch?v=K8p8_VlFHUk", start_time=580)
\
st.markdown("""
Initially, this seems aligned— good actions make the scientist happy. However, if the scientist ever becomes mistaken or biased, the AI might continue to pursue the scientist’s approval rather than true morality.

**Even carefully constructed specifications can lead to serious misalignment if the agent overgeneralizes a proxy (human approval), instead of internalizing genuine ethical principles.**
""")

st.header("Takeaways")

st.markdown("""
Goal Misgeneralization is especially tricky because it isn’t solved by simply adding more specifications—
because the agent’s problem isn't misunderstanding the reward, but misunderstanding *what the reward represents*.

As we've only seen a glimpse of, in high-stakes situations, this could be catastrophic.

Next, we'll examine another subtle yet dangerous failure mode: Reward Hacking.""")