import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/sou3ada/Projects/ft_linear_regression/data.csv')
df_norm = df / df.max()
m = df.count()['km']

def hypothesis(x, theta0, theta1):
    return (theta0 + theta1 * x)

def cost(theta0, theta1, m):
    sum_0 = 0
    sum_1 = 0
    for i in range(1,m):
        sum_0 += (hypothesis(data['km'][i], theta0, theta1) - data['price'][i])
        sum_1 += (hypothesis(data['km'][i], theta0, theta1) - data['price'][i]) * data['km'][i]
    return ((1/m) * sum_0, (1/m) * sum_1)

def ft_gradient_descent(lr):
    theta0 = 0
    theta1 = 0
    iteration = 0
    tmp0 = 100000
    error_range = 0.0000001
    while 1 :
        prime0, prime1 = cost(theta0, theta1, m)
        theta0 -= lr * prime0
        theta1 -= lr * prime1
#         print(tmp0, prime0, tmp0-prime0)
        if tmp0 - prime0 < error_range and tmp0 - prime0 > - error_range:
            break
        tmp0 = prime0
#         theta1 = tmp1
        iteration += 1
    #print(iteration)
    return(theta0, theta1)

data = df_norm

theta0, theta1 = ft_gradient_descent(0.01)

theta0 *= df.max()['price']
theta1 *= df.max()['price'] / df.max()['km']

with open('./thetas','w') as conf:
	conf.write(str(theta0)+ ',' + str(theta1))

print('The hypothesis is:\n\t prixEstime(kms) = ', theta0 , ' + (', theta1, ' * kms)')