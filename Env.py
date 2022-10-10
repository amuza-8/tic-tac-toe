import random 

class Env:
    def __init__(self,state=None):
        if state is None:
            self.state = [0]*9
        else:
            self.state = state

    def is_win(self):
        #縦並び
        for i in range(3):
            if self.state[i]==1 and self.state[i+3]==1 and self.state[i+3*2]==1:
                return True
        #横並び
        for i in range(0,7,3):
            if self.state[i]==1 and self.state[i+1]==1 and self.state[i+2]==1:
                return True
        #斜め
        if self.state[0]==1 and self.state[4]==1 and self.state[8]==1:
            return True
        if self.state[2]==1 and self.state[4]==1 and self.state[6]==1:
            return True
        
        return False
    
    def is_lose(self):
        #縦並び
        for i in range(3):
            if self.state[i]==-1 and self.state[i+3]==-1 and self.state[i+3*2]==-1:
                return True
        #横並び
        for i in range(0,7,3):
            if self.state[i]==-1 and self.state[i+1]==-1 and self.state[i+2]==-1:
                return True
        #斜め
        if self.state[0]==-1 and self.state[4]==-1 and self.state[8]==-1:
            return True
        if self.state[2]==-1 and self.state[4]==-1 and self.state[6]==-1:
            return True
        
        return False
    
    def is_draw(self):
        if 0 not in self.state:
            return True
    
    def actions_list(self):
        actions = []
        for i in range(9):
            if self.state[i] == 0:
                actions.append(i)
        return actions
    
    def first_player_step(self,action=None):
        #randomでactionさせる場合
        def random_action():
            action = []
            for i in range(9):
                if self.state[i] == 0:
                    action.append(i)
            return random.choice(action)
        if action is None:
            action = random_action()
        if self.state[action] == 0:
            self.state[action] = 1
        else:
            print('違法手です')
            exit()
        
    def second_player_step(self,action=None):
        #randomでactionさせる場合
        def random_action():
            action = []
            for i in range(9):
                if self.state[i] == 0:
                    action.append(i)
            return random.choice(action)
        if action is None:
            action = random_action()
        if self.state[action] == 0:
            self.state[action] = -1
        else:
            print('違法手です')
            exit()
    
    def step(self,action):
        turn = self.turn()
        if turn == 0:
            return Env()
        if turn == 1:
            #勝手に進めているのが良くない
            self.first_player_step(action)
            state = self.state.copy()
            return Env(state)
        if turn == -1:
            self.second_player_step(action)
            state = self.state.copy()
            return Env(state)
    
    def turn(self):
        zero = 0
        one = 0
        minus_one = 0
        for i in range(9):
            if self.state[i] == 0:
                zero += 1
            elif self.state[i] == 1:
                one += 1
            else:
                minus_one += 1
        if zero == 0:
            return 0
        if one == minus_one:
            return 1
        if one>minus_one:
            return -1

    def reset(self):
        for i in range(9):
            self.state[i] = 0
    
    #描画
    def drawing(self,ax):
        def rectangle(ax,X,Y):
            d = 1
            x_arr = [[0]*len(X) for _ in range(5)]
            y_arr = [[0]*len(Y) for _ in range(5)]
            for i in range(5):
                for j in range(len(X)):
                    if i == 0:
                        x_arr[i][j] = X[j] - d
                        y_arr[i][j] = Y[j] + d
                    elif i == 1:
                        x_arr[i][j] = X[j] + d
                        y_arr[i][j] = Y[j] + d
                    elif i == 2:
                        x_arr[i][j] = X[j] + d
                        y_arr[i][j] = Y[j] - d
                    elif i == 3:
                        x_arr[i][j] = X[j] - d
                        y_arr[i][j] = Y[j] - d
                    else:
                        x_arr[i][j] = X[j] - d
                        y_arr[i][j] = Y[j] + d
            rec = ax.plot(x_arr,y_arr,color='b')
            return rec

        def cross(ax,X,Y):
            d = 1
            x_arr = [[0]*len(X) for _ in range(5)]
            y_arr = [[0]*len(Y) for _ in range(5)]
            for i in range(5):
                for j in range(len(X)):
                    if i == 0:
                        x_arr[i][j] = X[j] - d
                        y_arr[i][j] = Y[j] + d
                    elif i == 1:
                        x_arr[i][j] = X[j] + d
                        y_arr[i][j] = Y[j] - d
                    elif i == 2:
                        x_arr[i][j] = X[j]
                        y_arr[i][j] = Y[j]
                    elif i == 3:
                        x_arr[i][j] = X[j] + d
                        y_arr[i][j] = Y[j] + d
                    else:
                        x_arr[i][j] = X[j] - d
                        y_arr[i][j] = Y[j] - d
            cro = ax.plot(x_arr,y_arr,color='r')
            return cro
        
        X_rec,Y_rec = [],[]
        X_cro,Y_cro = [],[]
        for i in range(9):
            if self.state[i] == 1:
                X_rec.append(1.5+3*(i%3))
                Y_rec.append(7.5-3*(i//3))
                
            elif self.state[i] == -1:
                X_cro.append(1.5+3*(i%3))
                Y_cro.append(7.5-3*(i//3))
        return rectangle(ax,X_rec,Y_rec),cross(ax,X_cro,Y_cro)

#動作確認
if __name__ == '__main__':
    game = Env()
