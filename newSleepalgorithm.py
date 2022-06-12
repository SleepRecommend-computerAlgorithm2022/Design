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
    noise=0.5
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
    model = PolynomialFeatures(degree=degree, include_bias=True)
    x_poly = model.fit_transform(x)
    return x, x_poly

#처음 그래프 초기화
def LR(poly_x,x,y,range1_poly,range2_poly,range3_poly,range4_poly,range5_poly,range6_poly,range7_poly,range8_poly): 
    model = LinearRegression()
    model2 = LinearRegression()
    model3 = LinearRegression()
    model4 = LinearRegression()
    model5 = LinearRegression()
    model6 = LinearRegression()
    model7 = LinearRegression()
    model8 = LinearRegression()
    model9 = LinearRegression()
    

    model.fit(poly_x,y)
    model2.fit(range1_poly,y[220:259])
    model3.fit(range2_poly,y[260:309])
    model4.fit(range3_poly,y[310:349])
    model5.fit(range4_poly,y[350:399])
    model6.fit(range5_poly,y[400:439])
    model7.fit(range6_poly,y[440:489])
    model8.fit(range7_poly,y[490:549])
    model9.fit(range8_poly,y[550:780])
    

    print("w1: ", model.coef_[0][0])
    print("w2: ", model.coef_[0][1])
    print("b: ",  model.intercept_[0])
    
    
    result = model.predict(poly_x)
    result2 = model2.predict(range1_poly)
    result3 = model3.predict(range2_poly)
    result4 = model4.predict(range3_poly)
    result5 = model5.predict(range4_poly)
    result6 = model6.predict(range5_poly)
    result7 = model7.predict(range6_poly)
    result8 = model8.predict(range7_poly)
    result9 = model9.predict(range8_poly)
    

    y[220:259] = result2
    y[260:309]=result3
    y[310:349]=result4
    y[350:399]=result5
    y[400:439]=result6
    y[440:489]=result7
    y[490:549]=result8
    y[550:780]=result9
    '''  그래프 테스트 코드
    plt.figure(figsize=(10, 7))

    
   
    plt.plot(x,y)
  
    plt.scatter(x,y)
    plt.suptitle("LR function", size=24)
    plt.legend()
   
    plt.show() 
    '''
    return result

def inputLR(a1,pre_poly):
    inputdatamodel = LinearRegression()
    inputdatamodel.fit(pre_poly,y[a1-29:a1+30])
    inputresult = inputdatamodel.predict(pre_poly)
    y[a1-29:a1+30] = inputresult

#초기값 설정
x, y = make_data() 

#범위별로 다항회귀 적용
range1 = x[220:259]
range2 = x[260:309]
range3 = x[310:349]
range4 = x[350:399]
range5 = x[400:439]
range6 = x[440:489]
range7 = x[490:549]
range8 = x[550:-1]


range1,range1_poly = poly(range1)
range2,range2_poly = poly(range2)
range3,range3_poly = poly(range3)
range4,range4_poly = poly(range4)
range5,range5_poly = poly(range5)
range6,range6_poly = poly(range6)
range7,range7_poly = poly(range7)
range8,range8_poly = poly(range8)


x,x_poly = poly(x)

result = LR(x_poly,x,y,range1_poly,range2_poly,range3_poly,range4_poly,range5_poly,range6_poly,range7_poly,range8_poly)
data = np.concatenate((x, y), axis=1)
#다항회귀 그래프 결과값 x,y값으로 간단히 출력
df = pd.DataFrame(data, columns=['x', 'y'])

#데이터 받을때
answerTime=450
answerSatisfy=10
y[answerTime]=answerSatisfy # y값 직접변경
pre = x[answerTime-29:answerTime+30]
pre, pre_poly = poly(pre)
inputLR(answerTime,pre_poly)


print(df[410:460])