#!/home/barbara/miniconda3/bin/python3

#Thought experiment of calculating b0 and b1
#Econometrics class 12-2-20

import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('linear-regression-dataset.csv')
x_data=np.array(df['experience'])
y_data=np.array(df['salary'])

#Create new sample
def bootstrap_samples(x,y,size_s):
    mask=np.random.randint(0, len(x), size=size_s)
    return np.c_[x[mask], y[mask]]

#Make model
def make_model(inp_sample):
    x=inp_sample[:,0]
    X=sm.add_constant(x)
    y=inp_sample[:,1]
    model=sm.OLS(y,X)
    res=model.fit()
    return res.params



b0_list=[]
b1_list=[]

for n in range(0,2001):
    new_sample=bootstrap_samples(x_data,y_data, 50)
    par=make_model(new_sample)
   # print (par)
    b0_list.append(par[0])
    b1_list.append(par[1])

print ("Mean b0_hat {:.4f}".format(np.mean(np.array(b0_list))))
print ("Mean b1_hat {:.4f}".format(np.mean(np.array(b1_list))))

#Make picture
fig, ((ax1,ax2)) = plt.subplots(2,1,figsize=(7,15))       


ax1.set_title("Intercept distribution")
ax1.set_ylabel("Probability")
ax1.set_xlabel("b0_hat value")
ax1.vlines(np.mean(np.array(b0_list)), 0,0.0035, label="Mean value")
sns.distplot(b0_list, ax=ax1)

ax1.legend()
ax2.set_title("b1_hat  distribution")
ax2.set_ylabel("Probability")
ax2.set_xlabel("b1_hat value")
ax2.vlines(np.mean(np.array(b1_list)), 0,0.0190, label="Mean value")  
ax2.legend()
sns.distplot(b1_list, ax=ax2)

plt.savefig('b0_and_b1_convergence.png')
