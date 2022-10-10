from Env import Env
import numpy as np
import matplotlib.pyplot as plt
from alpha_beta import alpha_beta,alpha_beta_action

args = {'episode':10}

fig,ax = plt.subplots(figsize=(8,8))
ax.set_xlim([0,9])
ax.set_ylim([0,9])   
ax.set_xticks(np.arange(0,10,3))
ax.set_yticks(np.arange(0,10,3))
ax.grid()

env = Env()

for i_episode in range(args['episode']):
    env.reset()
    done = False
    
    while not done:
        action = alpha_beta_action(env)
        env.first_player_step(action)
        if env.is_win():
            sente,gote = env.drawing(ax)
            plt.pause(1)
            for i in range(len(gote)):
                if i+2 == len(sente):
                    sente[i+1].remove()
                sente[i].remove()
                gote[i].remove()
            print('win')
            break
        if env.is_draw():
            sente,gote = env.drawing(ax)
            plt.pause(1)
            for i in range(len(gote)):
                if i+2 == len(sente):
                    sente[i+1].remove()
                sente[i].remove()
                gote[i].remove()
            print('draw')
            break
        sente,gote = env.drawing(ax)
        plt.pause(1)
        if len(gote) == 0:
            sente[0].remove()
        for i in range(len(gote)):
            if i+2 == len(sente):
                sente[i+1].remove()
            sente[i].remove()
            gote[i].remove()
        action = int(input())
        env.second_player_step(action)
        sente,gote = env.drawing(ax)
        plt.pause(1)
        for i in range(len(sente)):
            sente[i].remove()
            gote[i].remove()
        if env.is_win():
            print('win')
            break
        if env.is_lose():
            print('lose')
            break
        if env.is_draw():
            print('draw')
            break