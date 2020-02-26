# A Python  utility to observe the Central Limit Theorem (CLT) in action.
# Author: Neha Karanjkar

# From Wikipedia:
# "In probability theory, the central limit theorem (CLT) establishes that, in some situations, when independent random variables are added, their properly normalized sum tends toward a normal distribution (informally a "bell curve") even if the original variables themselves are not normally distributed."

# What this code does:
#
# step 1: Choose a distribution for the random variable X
# step 2: Generate a large number of samples of another random variable Y where Y is the average of N independent and identically-distributed (iid) samples of X 
# Y = (X_1 + X_2+ ...+X_N)/N
# Plot a histogram of the samples of Y to observe its distribution. What should it look like? Does it depend upon the chosen distribution of X? Draw a normal curve as reference to view the match.



import matplotlib.pyplot as plt
import random
import numpy as np
import math
import scipy.stats as stats

# The population can have an arbitrary distribution
# It has an expectation MU and std-dev SIGMA
MU=0
SIGMA=0

# define some functions to generate samples from a given distribution:
def normal():
	global  MU, SIGMA
	MU=3
	SIGMA=3
	while True:
		yield random.gauss(MU,SIGMA) # normal distribution
	
def uniform():
	global  MU, SIGMA
	MU=0.5
	SIGMA=1/math.sqrt(12)
	while True:
		yield random.uniform(0,1) # uniform distribution
	
def triangular():
	global  MU, SIGMA
	a,b,c=-5,20,0
	MU=(a+b+c)/3
	SIGMA=math.sqrt((a*a + b*b + c*c -a*b-a*c-b*c)/18)
	while True:
		yield random.triangular(a,b,c) #triangular distribution
	
def bernoulli():
	global  MU, SIGMA
	p=0.5
	MU=p
	SIGMA=math.sqrt(p*(1-p))
	while True:
		if random.random()>0.5:
			yield 1
		else:
			yield 0

# set the distribution here
RAND = uniform()

# histogram settings
sample_sizes = [10,400,1600]
num_samples = 10000 
print("generating some samples .....")

for N in sample_sizes:
	data=[]
	for i in range(num_samples):
		x=0
		for i in range(N):
			x+=next(RAND)
		x=x/N
		data.append(x)
	
	print("plotting .....")
	# plot a histogram
	num_bins =50
	plt.hist(data,bins=num_bins,label="sample size:"+str(N),density=True,alpha=0.5)
	
	# plot a normal curve superimposed on the histogram
	S=SIGMA/(math.sqrt(N))
	x_axis = np.linspace(min(data),max(data),num_bins*3)
	plt.plot(x_axis, stats.norm.pdf(x_axis, MU, S),color='k')

plt.legend()
plt.show()

