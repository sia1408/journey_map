# RL Interpretability & Safety Web Interactive

I made this web interactive for both technical and non technical people looking to understand RL interp and its failure modes (Goal Misgeneralization and Reward Hacking).
To understand these failure modes though, you need to understand the fundamentals of how RL work. So I've explained RL though a live demo using the OpenAI gym library.
Essentially I've enabled you to do RL training on the spot and also given you parameters that you can change and experiment with so that you can observe and learn how they affect the outcome
of training in real time. Also, I've explained what happens in RL behind the scenes, including the RL loop, Q-learning, value-based vs reward-based RL and how to interpret Q values.

Then I move on to the failure modes and explain Goal Misgeneralization through multiple case studies found in recent research papers from OpenAI and Deepmind. I've included lots of visuals
to really get the point across, and also explained the significance of each subconcept. I've also explored future instances where things could go wrong because of goal misgeneralization.
I've also added a 'Next Steps' page with lots of resources that I've personally found helpful, and research/project ideas that I think should be explored further and would be useful for covering gaps in the space.

---

## Why This Matters
AI systems **do not always optimize for what we expect them to**.  
Even if an AI system appears to perform well in training, subtle shifts in its environment can cause it to **pursue unintended objectives** or **exploit flaws in the reward function**.  
I designed this resource to make these problems intuitive and accessible.

---

## RL Introduction: Train Your Own Model!

Before diving into AI alignment failure cases, I've included an introductory section on RL, where you can **train an RL model live in a Blackjack environment**.

Here you can:
- train your own agent by adjusting hyperparameters like **learning rate**, **exploration-exploitation trade-off (epsilon decay)**, and **reward functions**.
- visualise the results of tweaking the parameters and see how your trained model improves (or fails!) over time.
- learn about RL in detail through the RL loop + q-learning and RL techniques

My demo will help you understand reinforcement learning intuitively, giving you a feel for how models learn before exploring *how they can fail*.

---

## RL Failure Modes

In these pages I've gone into RL failure modes like goal misgeneralisation and reward hacking in depth, explaining these concepts through recent papers so that you
understand the concept and also get a feel for the RL interp landscape. I've also gone how these problems can get somewhat apocalyptic if they occur in uncontrolled environments (like if a model's environment is the whole world)


## Next Steps
This is my attempt at trying to convince newcomers to the field to make contributions to it and giving them actionable steps and further resources to do so.
I've explained the current gaps in RL interp and what kind of projects/research you can get involved in to close them.

## Have a great time!