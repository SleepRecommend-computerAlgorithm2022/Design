from tkinter import * 
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Sleepalgorithm

f = tk.Frame

class tool(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.p_switch_frame(Main)

    def p_switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def g_switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

    

class Main(f):
    def __init__(self, master):
        f.__init__(self, master)
        #폰트
        global D_font, T_font, S_font, I_font,BT_font
        D_font = ("나눔고딕", 20)
        T_font = ("나눔고딕", 30, "bold")
        S_font = ("나눔고딕", 15)
        I_font = ("나눔고딕", 17)
        BT_font = ("나눔고딕", 40, "bold")
        #타이틀
        tk.Label(self, text="최적의 수면시간 찾기", pady=150, font=T_font).pack()
        #수면 데이터 입력하기 버튼
        tk.Button(self, text="수면 데이터 입력하기", pady=10, padx=60, font=D_font,
                    command=lambda: master.g_switch_frame(S_data)).pack()
        #Blank
        tk.Label(self, height=1).pack()
        #최적의 수면시간 추천 받기 버튼
        tk.Button(self, text="최적의 수면시간 추천 받기", pady=10, padx=30, font=D_font,
                    command=lambda: master.g_switch_frame(S_recommend)).pack()
        #경고
        tk.Label(self, text="*반드시 데이터를 먼저 입력하세요.", fg='red', font=S_font).pack()
        

class S_data(f):
    def __init__(self, master):
        f.__init__(self, master)
        #뒤로가기 버튼
        tk.Button(self, text="뒤로", font=D_font,
                    command=lambda: master.p_switch_frame(Main)).grid(column = 1, row = 0, padx = 30, pady = 30)
        #Blank
        tk.Label(self).grid(column = 0, row = 0, pady = 50, padx = 20)
        tk.Label(self).grid(column = 2, row = 4, pady = 50, padx = 15)
        tk.Label(self).grid(column = 8, row = 5, padx = 10)             #타이틀 정렬용
        tk.Label(self).grid(column = 0, row = 7, pady = 5)
        #타이틀
        tk.Label(self, text="최적의 수면시간 찾기", font=T_font).grid(column = 3, row = 2, columnspan=6)
        tk.Label(self, text="수면 데이터 입력하기", font=D_font).grid(column = 3, row = 3, columnspan=6)
        #수면시간
        tk.Label(self, text="  수면시간:", font=D_font).grid(column = 3, row = 5)
        S_hour = tk.Entry(self, borderwidth = 3, font=I_font, width=10)
        S_hour.focus()
        S_hour.grid(column = 4, row = 5, ipady=10)
        tk.Label(self, text=" 시간 ", font=D_font).grid(column = 5, row = 5)
        S_minute = tk.Entry(self, borderwidth = 3, font=I_font, width=10)
        S_minute.grid(column = 6, row = 5, ipady=10)
        tk.Label(self, text=" 분", font=D_font).grid(column = 7, row = 5)    
        #수면 만족도
        tk.Label(self, text="수면만족도: ", font=D_font).grid(column = 3, row = 6, pady=30)
        S_safac = tk.Spinbox(self, borderwidth = 3, from_=1, to=10, font=I_font, width=9)
        S_safac.grid(column = 4, row = 6, ipady=10)
        tk.Label(self, text="*1 ~ 10 사이로 입력해주세요.", fg='red', font=S_font).grid(column = 5, row = 6, columnspan=3)
        def S_data_save():
            Sleepalgorithm.answerTime=(S_hour.get()*60)+S_minute.get()
            Sleepalgorithm.answerSatisfy=S_safac.get()
            tk.Label(self, text=f"{S_hour.get()}시간 {S_minute.get()}분 만족도 {S_safac.get()}점 저장되었습니다.", font=D_font).grid(column = 3, row = 9, columnspan=5)
            S_hour.delete(0, len(S_hour.get()))
            S_minute.delete(0, len(S_minute.get()))
        #입력 버튼
        tk.Button(self, text="입력", font=D_font, width=7, command=S_data_save).grid(column = 3, row = 8, columnspan=2)
        #리셋버튼
        def I_reset():
            S_hour.delete(0, len(S_hour.get()))
            S_minute.delete(0, len(S_minute.get()))
        tk.Button(self, text="Reset", font=D_font, width=7, command=I_reset).grid(column = 5, row = 8, columnspan=2)


class S_recommend(f):
    def __init__(self, master):
        f.__init__(self, master)
        global sleepH, sleepM
        sleepH = tk.StringVar(master)
        sleepM = tk.StringVar(master)
        #뒤로가기 버튼
        tk.Button(self, text="뒤로", font=D_font,
                    command=lambda: master.p_switch_frame(Main)).grid(column = 0, row = 0, padx = 20, pady = 30)
        #Blank
        tk.Label(self, text = "").grid(column = 0, row = 0)
        #타이틀
        tk.Label(self, text="최적의 수면시간 찾기", font=T_font).grid(column = 2, row = 1,columnspan=20,padx=200)
        tk.Label(self, text="최적의 수면시간 추천 받기", font=D_font).grid(column =2, row = 2,columnspan=20)
        #기상 시간
        tk.Label(self, text="기상 시간 입력: ", font=D_font).grid(column=9, row=4,pady=100)
        S_hour = tk.Entry(self, borderwidth = 3, font=I_font, width=7,textvariable=sleepH)
        S_hour.focus()
        S_hour.grid(column = 10, row = 4)
        tk.Label(self, text="시", font=D_font).grid(column = 11, row = 4)
        S_minute = tk.Entry(self, borderwidth = 3, font=I_font, width=7,textvariable=sleepM)
        S_minute.grid(column = 12, row = 4)
        tk.Label(self, text=" 분", font=D_font).grid(column = 13, row = 4)
        #입력 버튼
        tk.Button(self, text="입력", font=D_font, width=7,
                    command=lambda: master.g_switch_frame(S_final)).grid(column = 9, row = 5,columnspan=3)          
        #리셋 버튼
        def I_reset():
            S_hour.delete(0, len(S_hour.get()))
            S_minute.delete(0, len(S_minute.get()))
        tk.Button(self, text="Reset", font=D_font, width=7, command=I_reset).grid(column = 10, row = 5, columnspan=3)

class S_final(f):
    def __init__(self, master):
        f.__init__(self, master)
        print("d",sleepH.get(),sleepM.get())
        #blank
        tk.Label(self, text="").grid(column = 0, row = 0,padx=100,pady=3)
        tk.Label(self, text="").grid(column = 0, row = 2, pady=1)
        #그래프
        df = Sleepalgorithm.df
        figure2 = plt.figure(figsize=(6,4))
        ax2= figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self)
        line2.get_tk_widget().grid(column = 1, row = 1, columnspan=3)
        df=df[['x','y']].groupby('x').sum()
        df.plot(kind = 'line', legend=True, ax = ax2, color='dodgerblue', marker=',', fontsize = 10)
        ax2.set_title('Sleep Time')
        #입력한 기상 시간 출력
        tk.Label(self, text="입력한 기상 시간은", font=D_font).grid(column=0, row=3,columnspan=3)
        tk.Label(self, text=f"{sleepH.get()}시 {sleepM.get()}분", font=T_font).grid(column=2,row=3,sticky="e")
        tk.Label(self, text="이고", font=D_font).grid(column=3,row=3,sticky="w")
        #최적의 수면 시작 시간 출력
        tk.Label(self, text="최적의 수면 시작 시간은", font=D_font).grid(column=2, row=4,ipadx=30)
        tk.Label(self, text="00시 57분 ",font=BT_font).grid(column=2,row=5,sticky="w")
        tk.Label(self, text="입니다.", font=D_font).grid(column=2, row=5,sticky="e")
        #확인 버튼
        tk.Button(self, text="확인", font=D_font, width=7,command=lambda: master.p_switch_frame(Main)).grid(column = 2, row = 6,pady=20)

if __name__ == "__main__":
    win = tool()
    win.title("Best_sleep")
    win.geometry("1000x700")
    win.resizable(False, False)
    win.mainloop()