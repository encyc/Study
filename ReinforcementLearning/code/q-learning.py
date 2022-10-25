import numpy as np

# 给定空间：
# 有一个房子，里面有五个房间（0，1，2，3，4），以及外面（5）
# 有一些房间相通，有一些不通。

# 给定环境奖赏矩阵
# R matrix
R = np.matrix([[-1, -1, -1, -1, 0, -1],
               [-1, -1, -1, 0, -1, 100],
               [-1, -1, -1, 0, -1, -1],
               [-1, 0, 0, -1, 0, -1],
               [-1, 0, 0, -1, -1, 100],
               [-1, 0, -1, -1, 0, 100]])
# 0 代表相通
# -1 代表不相通
# 100 代表外面

'''
Q的移动法则（transition rule）是个非常简单的方程：
Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]
根据该方程，Q矩阵中元素的值是等于R中相对应值和学习参数Gamma与下一状态中所有可能行动中的最大值的乘积。
虽然蠢，但我们的机器狗很有毅力。
机器狗会一个门一个门的探索直到达到目的地。
每一次到达目的地的探索便完成了一次episode学习经历。
每一次到达终点后，便开始下一次的episode。
'''

'''
Q-learning的算法步骤：
1.设置gamma参数，和R矩阵的环境奖励
2.初始化矩阵Q为03.对每一episode：   
	(1)随机选择一个状态   
	(2)DO （while 没有到达目标）           
		a.当前状态在所有可能的行动中选择一个           
		b.使用这个可能的行动然后分析到达下一个状态           
		c.基于所有可能行动获得最大值Q           
		d.计算Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]           
		e.设置下一个状态为当前状态           
		END DO  
	(3)End For上述算法被用来学习经验，每一次的episode都是一次训练季。
	   每一次训练季中，机械狗探索着环境（由R表示），接受着奖励（如果有的话）直到到达目的地。
	   训练的目的是增强机械狗的“大脑”，由Q表示。训练越多，Q矩阵优化的越好。
	   本例中，如果Q已经训练的比较良好了，即机械狗已经从蠢蠢的变聪明了，则他便不会在几个相同房间来回晃悠，而是找到最快到达目的地的门。
	   为了使用Q，机械狗只会跟踪一系列的状态（从初始到目的地）。
	   算法会找到有最高奖励的值，该值存储在当前状态的矩阵Q中。
使用步骤：
	1.设置当前状态=初始状态
	2.从当前状态，找到有最高Q值的行动
	3.设置当前状态=下一个状态
	4.重复步骤2，3直到当前状态=目标状态。
上述算法会返回从初始状态到目标状态的一系列状态。
'''
# 初始化Q的状态矩阵
# Q matrix
Q = np.matrix(np.zeros([6, 6]))

# Gamma (learning parameter).
gamma = 0.8

# Initial state. (Usually to be chosen at random)
initial_state = 1


# This function returns all available actions in the state given as an argument
def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act


# Get available actions in the current state
available_act = available_actions(initial_state)


# This function chooses at random which action to be performed within the range
# of all the available actions.
def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_act, 1))
    return next_action


# Sample next action to be performed
action = sample_next_action(available_act)


# This function updates the Q matrix according to the path selected and the Q
# learning algorithm
def update(current_state, action, gamma):
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    # Q learning formula
    Q[current_state, action] = R[current_state, action] + gamma * max_value


# Update Q matrix
update(initial_state, action, gamma)

# -------------------------------------------------------------------------------
# Training

# Train over 10 000 iterations. (Re-iterate the process above).
for i in range(10000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)

# Normalize the "trained" Q matrix
print("Trained Q matrix:")
print(Q / np.max(Q) * 100)

# -------------------------------------------------------------------------------
# Testing

# Goal state = 5
# Best sequence path starting from 2 -> 2, 3, 1, 5

current_state = 2
steps = [current_state]

while current_state != 5:

    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]

    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size=1))
    else:
        next_step_index = int(next_step_index)

    steps.append(next_step_index)
    current_state = next_step_index

# Print selected sequence of steps
print("Selected path:")
print(steps)

