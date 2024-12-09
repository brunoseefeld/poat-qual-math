#simulating a random walk with dependent step

import numpy as np


class walk:

    def __init__(self, prob,N):
            self.prob=prob
            self.size=N

    

            self.values=[]

            initial_value= np.random.binomial(1,prob)


            for i in range(N):

                toss=np.random.binomial(1,prob)

                if toss==0:
                    initial_value+=1

                else:
                    initial_value*=-1

                self.values.append(initial_value)


            self.S=np.array(self.values)

            self.square=self.S**2





W=walk(0.01,10000)





print(W.square)










