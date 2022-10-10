from Env import Env

def alpha_beta(env,alpha,beta):
    if env.is_win():
        return 1

    if env.is_lose():
        return -1
    
    if env.is_draw():
        return 0
    
    for action in env.actions_list():
        state = env.state.copy()
        turn = env.turn()
        # print('1:',env.state)
        # print('action:{},turn:{}'.format(action,turn))
        state[action] = turn
        value = alpha_beta(Env(state),alpha,beta)
        # print('turn:{},value:{}'.format(turn,value))
        # print('alpha:{},beta:{}'.format(alpha,beta))
        #先手のターン
        if turn == 1:
            if value > alpha:
                alpha = value
            # #αカット
            # if beta != float('inf'):
            #     if beta > value:
            #         return beta
        #後手のターン
        if turn == -1:
            if value < beta:
                beta = value
            # #βカット
            if alpha >= beta:
                return beta
        # print(env.state)
        # print('turn:{},action:{},value:{},alpha:{},beta:{}'.format(turn,action,value,alpha,beta))

    if env.turn() == 1:
        return alpha
    elif env.turn() == -1:
        return beta
    else:
        print('Error')
        exit()

def alpha_beta_action(env):
    best_action = 0
    alpha = -float('inf')
    beta = float('inf')
    for action in env.actions_list():
        state = env.state.copy()
        turn = env.turn()
        state[action] = turn
        value = alpha_beta(Env(state),alpha,beta)
        if value > alpha:
            best_action = action
            alpha = value 
    
    return best_action