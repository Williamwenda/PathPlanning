'''
Env testing for CF
'''
import numpy as np

class EnvCF:
    def __init__(self):
        self.xy_min = -3.5
        self.xy_max = 3.5
        self.step = 0.1
        self.motions = [(-self.step, 0.0), (-self.step, self.step),
                        ( 0.0, self.step), (self.step, self.step),
                        ( self.step, 0.0), (self.step, -self.step), 
                        ( 0.0, -self.step), (-self.step, -self.step)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def num_round(self,num):
        return round(num,2)
    
    def obs_map(self):

        range_min = self.xy_min
        range_max = self.xy_max
        static_obs = np.array([[1.5, -2.5],
                               [0.5, -1.0],
                               [1.5,  0.0],
                               [-1.0, 0.0]])
        obs_size = 0.3

        obs = set()

        for i in np.arange(range_min,range_max, self.step):
            
            obs.add((self.num_round(i), range_min))   # bottom bound

        for i in np.arange(range_min,range_max, self.step):
            obs.add((self.num_round(i), range_max))   # top bound

        for i in np.arange(range_min,range_max, self.step):
            obs.add((range_min, self.num_round(i)))   # left bound
        for i in np.arange(range_min,range_max, self.step):
            obs.add((range_max, self.num_round(i)))   # right bound

        for i in np.arange(-1, 1, self.step):
            obs.add((self.num_round(i), 0))

        # other obstacles
        for idx in range(4):
            for i in np.arange(static_obs[idx,0]-obs_size, static_obs[idx,0]+obs_size, self.step):
                for j in np.arange(static_obs[idx,1]-obs_size, static_obs[idx,1]+obs_size, self.step):
                    obs.add((self.num_round(i), self.num_round(j)))   # left bound

        # print(obs)


        return obs




