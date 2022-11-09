from math import *
import matplotlib.pyplot as plt

def sigma(start_term, end_term, function): #returns sum of return value of functions from start_term to end_term, sigma function
    total = 0
    for i in range(start_term, end_term+1):
        total += function(i)
    return total

def prob_anvil_die(n): #returns probability of anvil dying at n times used
    return(comb(n-1,2)*(pow(0.12,3)*pow(0.88,n-3)))

def prob_anvil_die_before(n): #returns probability of anvil dying at or before n times used
    return(sigma(4,n,prob_anvil_die))

def generate_pdf(n): #generates probability distribution bar chart of anvil breaking from turn 3 to n
    x = []
    y = []
    ticks = []
    max_prob = 0
    max_n = 0
    for i in range(3,n+1):
        x.append(i)
        prob = prob_anvil_die(i) * 100
        if prob > max_prob:
            max_prob = prob
            max_n = i
        y.append(prob)
        if i%5 == 0:
            ticks.append(i)
    
        
    plt.axhline(y = max_prob, color = 'r', linestyle = '-')
    plt.grid(zorder=0)
    barlist = plt.bar(x, y, color ='black',width = 0.9, zorder=3, alpha=0.7)
    barlist[max_n-3].set_color('red')
    plt.xlabel("number of times used, n")
    plt.ylabel("probability, %")
    plt.title("probability of anvil breaking on the n-th use")
    plt.xticks(ticks)
    plt.yticks(list(plt.yticks()[0]) + [max_prob])
    plt.show()

def generate_cdf(n): #generates cumulative distribution bar chart of anvil dying probability from turn 3 to n
    x = []
    y = [0]
    ticks = []
    for i in range(3,n+1):
        x.append(i)
        prob = prob_anvil_die(i) * 100
        y.append(prob + y[i-3])
        if i%5 == 0:
            ticks.append(i)
    y.pop(0)
    print(x)
    print(y)
    plt.grid(zorder=0)
    plt.bar(x, y, color ='black', width = 0.9, zorder = 3, alpha = 0.7)
    plt.xlabel("number of times used, n")
    plt.ylabel("probability, %")
    plt.title("probability of anvil breaking by n uses")
    plt.xticks(ticks)
    plt.show()

def generate_pdf_line(n): #generates probability distribution line graph of anvil breaking from turn 3 to n
    x = []
    y = []
    ticks = []
    max_prob = 0
    for i in range(3,n+1):
        x.append(i)
        prob = prob_anvil_die(i) * 100
        if prob > max_prob:
            max_prob = prob
        y.append(prob)
        if i%5 == 0:
            ticks.append(i)
    
        
    plt.axhline(y = max_prob, color = 'r', linestyle = '-')
    plt.grid(zorder=0)
    plt.plot(x, y, color ='black', zorder=3, drawstyle="steps-mid")
    plt.xlabel("number of times used, n")
    plt.ylabel("probability, %")
    plt.title("probability of anvil breaking on the n-th use")
    plt.xticks(ticks)
    plt.yticks(list(plt.yticks()[0]) + [max_prob])
    plt.show()

def generate_cdf_line(n): #generates cumulative distribution line graph of anvil dying probability from turn 3 to n
    x = []
    y = [0]
    ticks = []
    for i in range(3,n+1):
        x.append(i)
        prob = prob_anvil_die(i) * 100
        y.append(prob + y[i-3])
        if i%5 == 0:
            ticks.append(i)
    y.pop(0)
    plt.grid(zorder=0)
    plt.plot(x, y, color ='black', zorder=3, drawstyle="steps-mid")
    plt.xlabel("number of times used, n")
    plt.ylabel("probability, %")
    plt.title("probability of anvil breaking by n uses")
    plt.xticks(ticks)
    plt.show()    

def est_expected_val(n):
    expt_val = 0
    for i in range(3,n+1):
        expt_val += (i*prob_anvil_die(i))
    return expt_val