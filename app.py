import streamlit as st
import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt

st.title("Reinforcement Learning: The Basics")

st.markdown("""
Reinforcement Learning (RL) is a type of machine learning where an **agent** learns to make decisions by performing actions and receiving rewards or penalties from its **environment**. The goal? Maximize total rewards over time.

We'll explore RL with a simple and intuitive example: **the game of Blackjack**.

### 🃏 **What is Blackjack?**
- Blackjack is a card game aiming to **have your card sum as close to 21 as possible, without exceeding it.**
- Players compete against a dealer, not each other.

Let's see if we teach a model to maximise its chances of winning each time.

### **But first, some terms you need to know...**
- **Agent**: The player (model making decisions).
- **Environment**: The Blackjack game scenario.
- **Actions** -- The model can either choose to:
  - **Hit**: Take another card. This increases your total. It's risky but potentially rewarding.
  - **Stick**: Stop taking additional cards, keep your current hand and letting the dealer play instead, hoping it beats the dealer.
- **Rewards**:
  - **+1** if the agent wins (beats the dealer without exceeding 21).
  - **-1** if the agent loses (exceeds 21 or dealer is closer to 21).
  - **0** if it's a draw (tie with the dealer).
""")

st.markdown("""
Every round, your **agent** evaluates the **state** (current cards) and decides the best **action** to take. Over time, the agent learns from rewards and penalties, improving its **strategy** or **policy**.

In the following sections, you'll see exactly how an RL agent learns to play Blackjack using a method called **Q-learning**.
""")

st.title("Live training Demo")

st.markdown("""
Let's watch a Reinforcement Learning agent learn how to play Blackjack through **Q-learning**. 

### 🎛️ Interactive Parameters
Open the sidebar by clicking the **›** icon to the left.
- Adjust these parameters to see how they impact the agent's learning:
    - **Episodes**: How many games the agent plays to learn.
    - **Learning Rate (α)**: How quickly the agent updates its knowledge based on new experiences.
    - **Discount Factor (γ)**: Importance of future rewards.
    - **Exploration Rate (ε)**: Probability of exploring random actions vs. using known best actions.
""")

if "trained" not in st.session_state:
    st.session_state.trained = False
if "all_episode_steps" not in st.session_state:
    st.session_state.all_episode_steps = []

st.sidebar.header("Parameters")

episodes = st.sidebar.slider("Episodes", 500, 10000, 2000, 500)
alpha = st.sidebar.slider("Learning Rate (α)", 0.01, 1.0, 0.1, 0.01)
gamma = st.sidebar.slider("Discount Factor (γ)", 0.1, 1.0, 0.95, 0.05)
epsilon = st.sidebar.slider("Exploration Rate (ε)", 0.01, 1.0, 0.1, 0.01)

env = gym.make('Blackjack-v1', sab=True)
q_table = np.zeros((32, 11, 2, 2))

if st.button("Start Training 🚀"):
    st.session_state.trained = False
    progress_bar = st.progress(0)
    rewards_history = []
    all_episode_steps = []

    for episode in range(episodes):
        state, _ = env.reset()
        done = False
        total_reward = 0
        step_details = []
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q_table[state[0], state[1], int(state[2])])
            next_state, reward, done, truncated, _ = env.step(action)
            old_value = q_table[state[0], state[1], int(state[2]), action]
            future_reward = np.max(q_table[next_state[0], next_state[1], int(next_state[2])])
            new_value = old_value + alpha * (reward + gamma * future_reward - old_value)
            q_table[state[0], state[1], int(state[2]), action] = new_value
            total_reward += reward
            step_details.append((state, action, reward, old_value, new_value))
            state = next_state
        all_episode_steps.append(step_details)
        rewards_history.append(total_reward)
        if episode % max(episodes // 100, 1) == 0:
            progress_bar.progress(episode / episodes)

    progress_bar.progress(1.0)
    st.success("✅ Training Completed!")
    st.session_state.all_episode_steps = all_episode_steps
    st.session_state.trained = True

    fig, ax = plt.subplots()
    avg_rewards = np.cumsum(rewards_history) / (np.arange(episodes) + 1)
    ax.plot(avg_rewards, label="Average Reward per Episode")
    ax.set_xlabel("Episodes")
    ax.set_ylabel("Average Reward")
    ax.set_title("Training Progress")
    ax.legend()
    st.pyplot(fig)

    wins, draws, losses = 0, 0, 0
    eval_rounds = 1000
    for _ in range(eval_rounds):
        state, _ = env.reset()
        done = False
        while not done:
            action = np.argmax(q_table[state[0], state[1], int(state[2])])
            state, reward, done, truncated, _ = env.step(action)
        if reward == 1:
            wins += 1
        elif reward == 0:
            draws += 1
        else:
            losses += 1

    st.markdown(f"""
    ## 🏆 Final Evaluation Results (1000 rounds):
    - Wins: **{wins}**
    - Draws: **{draws}**
    - Losses: **{losses}**
    """)

    st.subheader("Q-table aka the Reward Table")
    st.markdown("""
    **Q-table**: Shows expected future rewards for actions in each state.  
    - Rows represent the player's sum (state), dealer's card, and usable ace status.
    - Columns show Q-values for actions (Stick vs Hit).
    - Higher Q-values mean the action is considered better by the agent.
    """)
    sample_qtable = q_table[12:22, 1:11, :, :]
    st.dataframe(sample_qtable.reshape(-1, 2), column_config={0: "Stick", 1: "Hit"})

if st.session_state.trained:
    toggle_view = st.checkbox("View training for each episode", value=False)
    if toggle_view:
        for i, steps in enumerate(st.session_state.all_episode_steps):
            exp = st.expander(f"🔍 View Steps of Episode {i + 1}", expanded=True)
            for s in steps:
                st_str = f"**State:** Player sum={s[0][0]}, Dealer card={s[0][1]}, Usable Ace={s[0][2]}  \n"
                st_str += f"**Action:** {'Hit' if s[1] else 'Stick'}  \n"
                st_str += f"**Reward:** {s[2]}  \n"
                st_str += f"**Q-value updated:** {s[3]:.3f} → {s[4]:.3f}"
                exp.write(st_str)

st.header("Simulate Individual Rounds")
if st.button("Run Single Round"):
    state, _ = env.reset()
    done = False
    round_steps = []
    while not done:
        action = np.argmax(q_table[state[0], state[1], int(state[2])])
        round_steps.append((state, action))
        state, reward, done, truncated, _ = env.step(action)
    for idx, step in enumerate(round_steps, 1):
        s, a = step
        st.write(f"Step {idx}: Player sum={s[0]}, Dealer card={s[1]}, Usable Ace={s[2]}, Action: {'Hit' if a else 'Stick'}")
    if reward == 1:
        st.success("Agent wins! 🎉")
    elif reward == 0:
        st.info("It's a draw! 🤝")
    else:
        st.error("Agent loses! 😞")
    st.write(f"Final reward: {reward}")
