from array import array
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import math
import Best_sleep

def make_data(): #초기 그래프
    noise=1
    i=0
    bins = [220,260,310,350,400,440,490,550]
    x = np.linspace(0,780,781).reshape(-1,1)
    ##수면 만족도 예상 그래프
    y=1/44*x*((0<x)&(x<220))+ (-1/200*(x-240)*(x-240)+7)*((220<=x)&(260>x))+ (4/625*(x-285)*(x-285)+1)*((x>=260)&(x<310))+ (-3/400*(x-330)*(x-330) + 8)*((x>=310)&(x<350))+ (2/625*(x-375)*(x-375) + 3)*((x>=350)&(x<400))+ (-1/100*(x-420)*(x-420) + 9)*((x>=400)&(x<440))+(1/625*(x-465)*(x-465) + 4 )*((x>=440)&(x<490))+(-1/225*(x-520)*(x-520) + 9)*((x>=490)&(x<550))+(7+x*1/10000000000000)*((x>=550))
    
   ##noise(변수)설정
    noise = np.random.uniform(-abs(noise), abs(noise), size=y.shape)
    yy = y + noise
  
    
    return x, yy
    

def poly(x, degree=2):
    model = PolynomialFeatures(degree=degree, include_bias=False)
    x_poly = model.fit_transform(x)
    return x, x_poly


def LR(poly_x,x,y,a1):
    model = LinearRegression()
    
    model.fit(poly_x,y)

    print("w1: ", model.coef_[0][0])
    print("w2: ", model.coef_[0][1])
    print("b: ",  model.intercept_[0])
    
    
    result = model.predict(poly_x)

    plt.figure(figsize=(10, 7))

    
   
    plt.plot(x[0:a1-30],y[0:a1-30],x[a1-29:a1+30],y[a1-29:a1+30],x[a1+31:-1],y[a1+31:-1])
  
    plt.scatter(x,y)
    plt.suptitle("LR function", size=24)
    plt.legend()

    return result



x, y = make_data()

 # data input시 값 받는 부분
answerTime=450
answerSatisfy=5
y[answerTime]=answerSatisfy # y값 직접변경


x,x_poly = poly(x)

result = LR(x_poly,x,y,answerTime)
data = np.concatenate((x, y, result), axis=1)
df = pd.DataFrame(data, columns=['x', 'y', 'predict'])