import streamlit as st

st.markdown("""
<style>
    .centered {
        text-align: center;
    }
</style>

<div class="centered">

#### Congrats on training your Blackjack agent! 🎉

""", unsafe_allow_html=True)
            
st.write("")
st.write("Now that you've seen Reinforcement Learning (RL) in action, let’s deepen your understanding and explore how RL works behind the scenes.")
            
st.markdown("""

To reiterate, ***Reinforcement Learning*** is a type of machine learning where an ***agent*** learns how to behave in an environment by performing ***actions*** and observing outcomes (rewards or penalties). The goal is to learn the optimal strategy (***policy***) that maximizes cumulative rewards over time.""")
            
st.markdown("""
In our Blackjack example, you witnessed an **agent** learning to play Blackjack by interacting with the game (**environment**). Let's break down exactly how this learning happens using the **Reinforcement Learning (RL) Loop**:""")

st.markdown("""
<style>
    .centered {
        text-align: center;
    }
</style>

<div class="centered">

# 🔄 The Reinforcement Learning Loop

""", unsafe_allow_html=True)

st.markdown("""
<style>
    .centered {
        text-align: center;
    }
</style>

<div class="centered">
RL consists of a simple, repeated cycle:
""", unsafe_allow_html=True)

left_co, cent_co, last_co = st.columns([1,5,1])
with cent_co:
    st.image("pages/RL_loop.webp")
    st.markdown("<p style='text-align: center; font-style: italic;'> Agent ↔ Environment interaction </p>", 
                unsafe_allow_html=True)

#final (pls work)
st.markdown("""
<style>
    .centered {
        text-align: center;
    }

    .step-box {
        background-color: rgba(240, 240, 240, 0.9); /* Light mode */
        padding: 15px;
        border-radius: 10px;
        margin: 10px auto; /* Centers block */
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        color: black;
        font-size: 18px;
        border: 1px solid rgba(0, 0, 0, 0.2);
        width: 70%; /* Ensures blocks are centered */
        text-align: center;
    }

    @media (prefers-color-scheme: dark) {
        .step-box {
            background-color: rgba(30, 30, 30, 0.9); /* Dark mode */
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
    }

    .step-heading {
        color: #ff6600; /* Orange */
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
        text-align: center;
    }

    .arrow {
        font-size: 30px;
        text-align: center;
        margin: 10px 0;
    }

</style>

<div class="centered">
""", unsafe_allow_html=True)

# Step 1

st.markdown("""
<style>
    .centered {
        text-align: center;
    }
</style>

<div class="centered">

#### Agent observes a state. ($S_t$)

""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <p>Our blackjack agent <b>analyzes the current state</b> to make an informed decision.</p>
    <p>State = <b>Current hand sum</b> + <b>Dealer's visible card</b>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

# Step 2
st.markdown("""
<style>
    .centered {
        text-align: center;
    }
</style>

<div class="centered">

#### Agent chooses an action based on its current policy. ($A_t$)

""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <p>Based on the observed state, our agent decides which <b>action</b> to take.</p>
    <p>👉 <b>Hit</b> (take another card) OR <b>Stick</b> (keep current hand).</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

# Step 3
st.markdown("""
<style>
    .centered {
        text-align: center;
    }
</style>

<div class="centered">

#### Agent responds to environment in pursuit of reward ($R_{t+1}$, $S_{t+1}$)

""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <p>The chosen action is executed, and the environment provides feedback:</p>
    <ul style="list-style: none; padding-left: 0;">
        <li>✔ If the agent <b>Hits</b>, it receives another card → <b>new state</b>.</li>
        <li>🏆 If it <b>wins</b>, reward = <b>+1</b>.</li>
        <li>❌ If it <b>loses</b>, reward = <b>-1</b>.</li>
        <li>🤝 If it <b>draws</b>, reward = <b>0</b>.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

# Step 4
st.markdown("""
<style>
    .centered {
        text-align: center;
    }
</style>

<div class="centered">

#### Agent updates its policy

""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
    <p>Using the reward, the agent <b>updates its strategy</b> to improve future decisions.</p>
    <ul style="list-style: none; padding-left: 0;">
        <li>✅ <b>Good choices</b> (e.g., sticking on 20) get reinforced.</li>
        <li>❌ <b>Bad choices</b> (e.g., hitting on 19 and losing) get discouraged.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style="margin-top: 30px; text-align: center;">🔄 This loop repeats continuously...</h3>
<p style="text-align: center;">Each time our agent plays, it better optimises for the reward function, thus getting <b>smarter</b> at Blackjack and improving its win rate over time! </p>
</div>
""", unsafe_allow_html=True)

#the rl methods part:

st.header("The 2 Main Types of RL Methods")

st.markdown("""
Reinforcement Learning algorithms fall into two main categories:
""")

st.markdown("""
| **Method Type**    | **Description** | **Use Case** | **Example Algorithms** |
|-------------------|----------------|-------------|------------------------|
| **Policy-Based** | Directly learns a **policy** (mapping states to actions). Instead of estimating values, the agent **learns the best action to take** in each state. | Used in **continuous action spaces** where value-based methods struggle. | Policy Gradient, REINFORCE, PPO, A3C |
| **Value-Based**  | Learns a **value function** that estimates the expected future rewards for state-action pairs. The agent **chooses the action leading to the highest value**. | Best for **discrete action spaces**, like in Blackjack. | Q-Learning, Deep Q-Networks (DQN), SARSA |
""")

st.markdown("---")

st.markdown("""
### But...what is a **value function**?
A **value function** predicts how good a given state (or state-action pair) is.  
- It estimates **expected future rewards** starting from that state.
- Helps the agent decide **which state-action pair is most valuable**.

In our Blackjack demo, we used **Q-values**, which is a type of value function:
- The **Q-value** of a state-action pair tells the agent the **expected reward** for taking that action in that state.
""")


#new

st.markdown("""

Reinforcement Learning (RL) methods can be broadly categorized into two approaches:
""")

st.header(" Two Approaches to Reinforcement Learning")

st.markdown("""
RL algorithms fall into two broad categories:  

| **Method Type**    | **How It Works** | **When to Use** | **Example Algorithms** |
|-------------------|----------------|-------------|------------------------|
| **Policy-Based** | The agent learns a **policy** directly, mapping states to actions. Instead of estimating values, it focuses on **choosing the best action** for each state. | Best for **continuous action spaces** where value-based methods struggle. | Policy Gradient, REINFORCE, PPO, A3C |
| **Value-Based**  | The agent **learns the value of states and actions**, choosing the action that leads to the highest long-term reward. | Best for **discrete action spaces**, like in Blackjack. | Q-Learning, Deep Q-Networks (DQN), SARSA |

---

This distinction is **important**, because different RL problems require different approaches.  

For example, in **Blackjack**, we used a **value-based method (Q-learning)** since the game has a **discrete** set of actions: _Hit or Stick_.  

However, for something like **robot control**, where actions involve fine movements (e.g., rotating a robotic arm by a certain angle), a **policy-based method** is more practical.

---
""")

st.header("Understanding Value Functions")

st.markdown("""
To make smarter decisions, an RL agent needs to evaluate how "good" or "bad" a state or action is. This is where **value functions** come in.

A **value function** estimates the **expected future reward** an agent will receive starting from a given state (or state-action pair).  

### **Q-values**  
- If you recall, we had a table of values in the previous page. Tht was the **Q-table**. The Q-table kept record of **Q-values**; values that represent the expected reward for taking a specific action in a given state.
It kept track of these values for every possible state-action pair.
- The agent updates this table over time, thereby improving its decision-making process.

---
""")

st.subheader("How does Q-Learning work?")

st.markdown("""
In our Blackjack example, we used **Q-learning**, a **value-based RL method** that learns **optimal Q-values** by repeatedly interacting with the environment.  

Every time the agent takes an action, it updates the Q-table using the **Q-learning update rule**:

\[
Q(s,a) \leftarrow Q(s,a) + α \times [reward + γ \times max(Q(s',a')) - Q(s,a)] (I'll have to make it render the latex for this)
\]

Where:
- **\( Q(s,a) \)** = Current Q-value (expected reward for taking action **a** in state **s**).
- **\( α \) (alpha)** = Learning rate (how quickly we adjust to new information).
- **\( reward \)** = Reward received from the environment.
- **\( γ \) (gamma)** = Discount factor (importance of future rewards).
- **\( s' \)** = The new state after taking action.
- **\( max(Q(s',a')) \)** = The best possible reward expected from the next state.

---
""")
st.markdown("""
Specifically, our agent followed this process:

1️⃣ **Start in a game state:**  
   - Example: Player sum = 14, Dealer's card = 10.

2️⃣ **Choose an action (Hit or Stick):**  
   - If **exploring**, the agent picks randomly.
   - If **exploiting**, it chooses based on **highest Q-value**.

3️⃣ **Receive a reward:**  
   - **+1** for winning, **0** for a draw, **-1** for losing.

4️⃣ **Update the Q-table** using the Q-learning rule.

Over **thousands of episodes**, the agent learns which actions **maximize future rewards**, improving its gameplay over time.

---
""")

st.header("Extending Q-Learning: Deep Q-Networks (DQN)")

st.markdown("""
So far, Q-learning has worked well for **small environments** like Blackjack, where we can store all Q-values in a table.

But what happens when:
- The state space is **too large** (e.g., video games, robotics).
- We can't explicitly store a Q-table for **every possible state**?

#### **Enter Deep Q-Networks (DQN)**  

Instead of a Q-table, **DQN** uses a **deep neural network** to approximate Q-values.

This is useful because Deep Q Learning:
- Handles **high-dimensional, complex environments** (e.g., Atari games, robotics).
- Learns from **raw pixels or sensor inputs**, instead of predefined states.
- Generalizes across **many unseen states**, instead of memorizing a table.

---
""")

st.header("🚀 Where to Go Next?")

st.markdown("""
Hopefully our RL intro has hooked you onto exploring RL further. (I'll add why we need more people in RL) here are some great next steps to deepen your understanding:

📌 **[Building AlphaZero from Scratch](https://suragnair.github.io/posts/alphazero.html)**  
_Develop a chess-playing AI using deep RL and Monte Carlo tree search._

📌 **[Gymnasium RL Environments](https://gymnasium.farama.org/api/registry/)**  
_Try different RL environments beyond Blackjack._

📌 **[Pretrained RL Agents (RL Zoo)](https://github.com/DLR-RM/rl-baselines3-zoo)**  
_Experiment with pre-trained RL models._

📌 **[RL with Hugging Face](https://huggingface.co/learn/deep-rl-course/en/unit2/introduction)**  
_Hands-on Deep RL course._

---
""")