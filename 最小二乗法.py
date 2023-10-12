import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def main():
    root = tk.Tk()
    # print(type(root))
    root.geometry("400x700+300+300")
    root.resizable(width=False, height=False)
    root.title("最小二乗法")
    createWidget(master=root)

    root.mainloop()


def createWidget(master: tk):
    #ラベルを設置
    label = tk.Label(master=master, text="データを入力してください")
    label.pack()
    
    entry_widgets_x = [] #エントリーウィジェットのリスト
    entry_widgets_y = []
    entry_widgets_g = []
    try:
        #テーブル用のフレーム
        t_frame = tk.Frame(master=master)
        t_frame.pack()
        #データの入力テーブル
        for i in range(21): #行数
            for j in range(2): #列数
                if i == 0:
                    if j == 0:
                        c_label = tk.Label(master=t_frame, text="x")
                        c_label.grid(row=i, column=j)
                    else:
                        c_label = tk.Label(master=t_frame, text="y")
                        c_label.grid(row=i, column=j) 
                else:
                    entry = tk.Entry(master=t_frame)
                    entry.grid(row=i, column=j)
                    if j == 0:
                        entry_widgets_x.append(entry)
                    else:
                        entry_widgets_y.append(entry)
        
        #「計算する」ボタンを設置
        button = tk.Button(master=master, text="計算してグラフを描画する", width=30, command=lambda: get_data(entry_widgets_x, entry_widgets_y, entry_widgets_g, result))
        button.pack(padx=10, pady=20)

        #グラフの情報を入力
        tk.Label(master=master, text="グラフの名前を入力してください").pack()
        g_entry = tk.Entry(master=master)
        g_entry.pack()
        entry_widgets_g.append(g_entry)
        tk.Label(master=master, text="ｘ軸の名前を入力してください").pack()
        g_entry_x = tk.Entry(master=master)
        g_entry_x.pack()
        entry_widgets_g.append(g_entry_x)
        tk.Label(master=master, text="ｙ軸の名前を入力してください").pack()
        g_entry_y = tk.Entry(master=master)
        g_entry_y.pack()
        entry_widgets_g.append(g_entry_y)
        
        #結果を出力するラベル
        result = tk.Label(master=master, text="")
        result.pack(pady=20)
        
    except Exception as e:
        result.config(text=f"Error! : {e}")
        
    
def get_data(entry_widgets_x: list, entry_widgets_y: list, entry_widgets_g: list, result: tk):
    # print("Ok")
    x_list = []
    y_list = []
    g_list = []
    
    
    for i in range(len(entry_widgets_x)):
        if entry_widgets_x[i].get() != "":
            # print(entry_widgets_x[i].get(), "x")
            x_list.append(float(entry_widgets_x[i].get()))
    for i in range(len(entry_widgets_y)):
        if entry_widgets_y[i].get() != "":
            # print(entry_widgets_y[i].get(), "y")
            y_list.append(float(entry_widgets_y[i].get()))
    for i in range(len(entry_widgets_g)):
        # print(entry_widgets_y[i].get(), "y")
        g_list.append(entry_widgets_g[i].get())        
            
    a, b = calcurate(x_list, y_list, g_list, result)
    
    #結果ラベルに反映
    result.config(text=f"a:{a}\nb:{b}")
    
    
def calcurate(x_list: list, y_list: list, g_list: list, result: tk) -> int:
    # print(x_list, y_list)
    x = np.array(x_list)
    y = np.array(y_list)
    
    try:
        a, b = np.polyfit(x, y, 1)
    except Exception as e:
        result.config(text=f"Error! : {e}")
    
    #グラフをクリア
    plt.clf()
    
    #散布図をプロット
    plt.scatter(x, y, label="散布図")
    
    #直線のデータを作成
    y = a*x+b
    
    plt.plot(x, y, label=f'y = {a}x + {b}')
    plt.title(f"{g_list[0]}", fontname="MS Gothic")
    plt.xlabel(f"{g_list[1]}", fontname="MS Gothic")
    plt.ylabel(f"{g_list[2]}", fontname="MS Gothic")
    plt.legend(loc="best", prop={"family":"MS Gothic"})
    
    #グラフを表示
    plt.show()
    return a, b
        
if __name__ == "__main__":
    main()
