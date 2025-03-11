import streamlit as st

st.set_page_config(page_title="Next Steps: AI Safety in RL", page_icon="🧠", layout="wide")

st.title("🚀 Next Steps: Contributing to AI Safety in RL")
st.subheader("How to get involved in AI safety and reinforcement learning (RL) interpretability")

st.markdown("""
Understanding and addressing concepts like goal misgeneralization and reward hacking is crucial for ensuring the safety of reinforcement learning (RL) systems.
AI safety in reinforcement learning (RL) is an underexplored but crucial area.
Unlike LLMs (large language models), where we have some interpretability tools like TransformerLens, RL remains a dark black box with even fewer ways to analyze how
and why an agent makes decisions.

If you're interested in contributing to AI safety, especially in RL interpretability, there are many open problems waiting to be tackled.

The field can use all the help you can give it.

""")

st.markdown("""
If you've made it this far, you likely care about ensuring AI systems behave as intended. This is good, because this field can use as much help as it can get.""")

st.header("Some key issues in AI Safety that we think need addressing:")

st.markdown("""
- Reinforcement learning (RL) **is widely used**, including in chain of thought, yet **AI safety research in RL is far behind LLM research**.We **lack standardized interpretability methods** for RL systems, meaning **low-hanging fruit** are waiting to be explored.
We don’t have robust tools for inspecting RL models. In fact, there’s really no standard way to measure goal misalignment.
Different studies use different methods, which makes it hard to compare results or build a systematic understanding.
We really need benchmarks and common tools for the field. We need something like an equivalent to TransformerLens that can work for RL.""")

st.markdown("""
**Perhaps this is something you can help with!** If you can build tools to probe RL models, you could make a huge impact. """)

st.markdown("""
- Some of the **biggest open problems** in **mechanistic interpretability (MechInterp)** **apply to RL but remain unsolved**.
Here's a list of these problems: - **[Concrete Problems in RL Interpretability](https://docs.google.com/spreadsheets/d/1oOdrQ80jDK-aGn-EVdDt3dg65GhmzrvBWzJ6MUZB8n4/edit?gid=0#gid=0)**""")

st.header("Resources to Start Learning:")
st.markdown("""
- **[Alignment Forum Curated Sequences](https://www.alignmentforum.org/library)** – Foundational AI safety research.
- **[Bluedot's AI Safety Fundamentals Course](https://aisafetyfundamentals.com/alignment/)** – A structured introduction to AI alignment.

AI alignment thrives on **collaboration**.  
Joining research groups and online communities will accelerate your learning and connect you with experts.

🌍 **Communities to Join:**
- **[ARENA](https://www.arena.education/)** – An interactive research mentorship platform.
- **[AI Safety Support](https://www.aisafetysupport.org/lots-of-links)** – Grants, networking, and support for new AI safety researchers.
- **[Alignment Forum](https://www.alignmentforum.org/library)** – The main discussion hub for technical AI safety.

💡 **Idea:** Join **ARENA** or **AI Safety Support** to find collaborators for an **RL safety research project**.
""")

st.info("If you’re serious about RL safety, you don’t have to do it alone. Making friends in the space goes a long way!")

st.subheader("Learn How to Make Technical Contributions")
st.markdown("""
If you want to contribute **directly to RL interpretability research**, here’s how to **go from beginner to contributor**:

🔗 **[How to Make Contributions to RL Interpretability](https://www.alignmentforum.org/posts/eqvvDM25MXLGqumnf/200-cop-in-mi-interpreting-reinforcement-learning)**

🔗 **[Alignment Research Codebases](https://www.alignmentforum.org/library)** (to get started with AI safety coding projects).""")


st.markdown("""
We can't wait to welcome you to the field!""")
