from tkinter import * 
import tkinter as tk
import tkinter.font

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
        global D_font, T_font, S_font, I_font
        D_font = tk.font.Font(family="나눔고딕", size=20)
        T_font = tk.font.Font(family="나눔고딕", size=30, weight="bold")
        S_font = tk.font.Font(family="나눔고딕", size=15)
        I_font = tk.font.Font(family="나눔고딕", size=17)
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
        #입력 버튼
        tk.Button(self, text="입력", font=D_font, width=7).grid(column = 3, row = 8, columnspan=2)
        #리셋버튼
        def I_reset():
            S_hour.delete(0, len(S_hour.get()))
            S_minute.delete(0, len(S_minute.get()))
        tk.Button(self, text="Reset", font=D_font, width=7, command=I_reset).grid(column = 5, row = 8, columnspan=2)

class S_recommend(f):
    def __init__(self, master):
        f.__init__(self, master)
        #뒤로가기 버튼
        tk.Button(self, text="뒤로", font=D_font,
                    command=lambda: master.p_switch_frame(Main)).grid(column = 1, row = 0, padx = 30, pady = 30)
        #Blank
        tk.Label(self).grid(column = 0, row = 0, pady = 50, padx = 20)
        #타이틀
        tk.Label(self, text="최적의 수면시간 찾기", font=T_font).grid(column = 2, row = 2, padx = 140)
        tk.Label(self, text="최적의 수면시간 추천 받기", font=D_font).grid(column = 2, row = 3)

if __name__ == "__main__":
    win = tool()
    win.title("Best_sleep")
    win.geometry("1000x700")
    win.resizable(False, False)
    win.mainloop()