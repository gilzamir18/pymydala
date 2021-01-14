from gamygdala.engines import Gamygdala
import time
import numpy as np

NUM_EPISODES = 100
EMOTION_DECAY_SPEED = 2
for i in range(NUM_EPISODES):
    done = False
    engine = Gamygdala()
    engine.debug = False
    agent1 = engine.createAgent("EmoCha")
    goal = engine.createGoalForAgent("EmoCha", "GetGold", 1.0, False)
    newBeliefAboutGoal = {'GetGold': True}
    steps = 0
    while not done:
        roullet = np.random.random()
        if roullet < 0.1:
            engine.appraiseBelief(1.0, "EmoCha", ["GetGold"], [1.0], not newBeliefAboutGoal['GetGold'])
            newBeliefAboutGoal['GetGold'] = False
            print("Agent Win!!!")
            done = True
        elif roullet < 0.15:
            engine.appraiseBelief(1.0, "EmoCha", ["GetGold"], [-1.0], not newBeliefAboutGoal['GetGold'])
            done = True
            newBeliefAboutGoal['GetGold'] = False
            print("GameOver!!!")
        elif roullet < 0.5:
            engine.appraiseBelief(0.5, "EmoCha", ["GetGold"], [1.0], not newBeliefAboutGoal['GetGold'])
            newBeliefAboutGoal['GetGold'] = False
            print("Closer to goal!")
        elif roullet < 1.0:
            engine.appraiseBelief(0.5, "EmoCha", ["GetGold"], [-1.0], not newBeliefAboutGoal['GetGold'])
            newBeliefAboutGoal['GetGold'] = False
            print("Stayed farther from the goal!")
        time.sleep(0.1)
        agent1.decay(engine, steps*EMOTION_DECAY_SPEED)
        engine.printAllEmotions()
        time.sleep(5)
        steps += 1
    print("end epsiode: ", i)






