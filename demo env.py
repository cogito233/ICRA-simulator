env = kernal()
def demo(env, render = Flase)
    state = env.reset()
    a = self.orders
    total_reward = 0
    steps = 0
    while True:
        state, reward, done, info = env.eachstep(a)
        total_reward += reward
        if steps % 20 = 0 or done:
            print("step {} total_reward {:+0.2f}".format(steps, total_reward))
        steps += 1
        if done:
            break
    return total_reward

if __name__ == '__main__':
    demo(kernal(), render = True)