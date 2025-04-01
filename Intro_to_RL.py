import streamlit as st
import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt

st.title("Reinforcement Learning: The Basics")

st.markdown("""
Reinforcement Learning (RL) is a type of machine learning where an **agent** learns to make decisions by performing actions and receiving rewards or penalties from its **environment**.""")

st.markdown("""
The goal? Maximize total rewards over time.""")

st.markdown("""We'll explore RL with a simple and intuitive example: **the game of Blackjack**.

### 🃏 Blackjack for noobs
- Blackjack is a card game aiming to **have your card sum as close to 21 as possible, without exceeding it.**
- Players compete against a dealer, not each other.

Let's see if we teach a model to maximise its chances of winning each time.

### **But first, some terms you need to know...**
- **Agent**: The player (model making decisions).
- **Environment**: The Blackjack game scenario.
- **Rewards**:
  - **+1** if the agent wins (beats the dealer without exceeding 21).
  - **-1** if the agent loses (exceeds 21 or dealer is closer to 21).
  - **0** if it's a draw (tie with the dealer).
- **Actions** -- The model can either choose to:
  - **Hit**: Take another card. This increases your total. It's risky but potentially rewarding.
  - **Stick**: Stop taking additional cards, keep your current hand and letting the dealer play instead, hoping it beats the dealer.""")

st.markdown("""
In reinforcement learning, an **action space** defines the set of all possible actions an agent can take.
Because in Blackjack you can only 'Hit' or 'Stick', it uses a **discrete action space**, meaning the agent chooses from a fixed set of actions. Some environments, like self-driving cars for example, have **continuous action spaces**, where actions can take on any value within a range (say, steering angle).
Discrete spaces are simpler to work with, which makes Blackjack a great starting point for learning how agents explore and learn policies.
""")


st.markdown("""
Every round, your agent evaluates the *state* of the environment—in this case, the cards on the table—and chooses an action like "hit" or "stick."

In reinforcement learning, a **state** is a complete description of the environment—nothing relevant is hidden. An *observation*, on the other hand, is only a partial description of the true state, and may omit information.

When the agent has access to the full state, the environment is said to be **fully observed**. When it only receives partial observations, it’s a **partially observed environment**— often requiring memory, inference or other tricks to make good decisions.

In this demo, we simplify Blackjack to be fully observed. The agent's state includes everything it needs to act optimally:

- The total value of its hand

- Whether it has a usable ace

- The dealer's visible card

We also assume an infinite deck (cards drawn with replacement), so the agent doesn't need to track which cards have been played. There's no hidden information relevant to the decision—so the agent's "observation" is treated as the full "state."

Contrast this with real-life where Blackjack is partially observed: the dealer's second card is hidden, the deck depletes over time, and smart players use memory (like card counting) to gain an edge. Decision-making in such environments is harder because the agent has to infer or estimate the true state of the game from incomplete information.

In the following sections, we’ll explore how the agent learns an optimal policy by estimating long-term rewards for each state-action pair through interaction with the environment, and thereby learns to win more consistently.
""")

st.title("Live training Demo")

st.markdown("""
Let's watch a Reinforcement Learning agent learn how to play Blackjack through **Q-learning**. 

### 🎛️ Interactive Parameters
Open the sidebar by clicking the **›** icon to the left.
- Adjust these parameters to see how they impact the agent's learning:
    - **Episodes**: In reinforcement learning, an episode is a complete sequence of steps taken by an agent—from the initial state to a terminal state (like winning, losing, or reaching a time limit).
    It’s one full trial where the agent interacts with the environment, makes decisions, receives rewards, and learns from the outcome.
    Think of it as a single trial-and-error run, where the agent tries a strategy, sees how it goes, and uses that experience to improve next time.
    - **Learning Rate (α)**: Controls how much new information overrides old knowledge.
    A high learning rate means the agent quickly adapts based on recent rewards. A low rate makes it learn more cautiously, averaging over time.
    Think of it as how fast the agent "trusts" new experiences.
    - **Discount Factor (γ)**: Determines how much the agent cares about future rewards compared to immediate ones.
    A value close to 1 means the agent values long-term gains whereas a value near 0 makes the agent pursue quick wins.
    - **Exploration Rate (ε)**: Sets the probability that the agent tries something new instead of picking what it currently thinks is best.
    Higher ε means more random moves (exploration); lower ε means the agent sticks to what it already knows (exploitation).
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
    toggle_view = st.checkbox("View training for each episode (click again to collapse)", value=False)
    if toggle_view:
        for i, steps in enumerate(st.session_state.all_episode_steps):
            exp = st.expander(f"🔍 View Steps of Episode {i + 1}", expanded=False)
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