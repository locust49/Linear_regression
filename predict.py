import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/sou3ada/Projects/ft_linear_regression/data.csv')


def graph(data):
    plt.plot(data['km'],
             get_price(data['km']),
             c='r')
    plt.scatter(data['km'],
                data['price'],
                s=15)
    plt.ylabel("Price")
    plt.xlabel("Km")
    plt.title('Prediction of cars values per mileage')
    plt.show()


def get_price(kms):
    theta = get_thetas()
    return np.longdouble(theta[0]) + np.longdouble(theta[1]) * kms


def get_thetas():
    with open('./thetas', 'r') as conf:
        if conf is not None:
            thetas_str = conf.readline()
    if thetas_str:
        thetas = thetas_str.split(',')
        if len(thetas) != 2:
            print('Did you mess with the thetas file ? u_u')
            exit()
        else:
            return thetas
    else:
        print('Training required')


try:
    kms = np.longdouble(input("Predict price of vehicle for kms: "))
except:
    print("Error!!! please try a correct number.")
    exit()

estimated_price = get_price(kms)


if kms < 0:
    print(
        f'\nOh really ?\n...\nIf you insist, this car is worth: {estimated_price} Euro.')
elif estimated_price < 0:
    print(
        f'\nThis car is worth : {estimated_price} Euro, and still worth more than you :)')
else:
    print(f"\nThis car is worth : {estimated_price} Euro.")

graph(df)