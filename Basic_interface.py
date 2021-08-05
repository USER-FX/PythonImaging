# 该计算器只一次性计算，不可叠加计算， 后续版本会增加内容  当前版本(1.0版本) 测试(Mac) windows或许有些差异
import tkinter as tk

windows = tk.Tk()  # 创建窗口
windows.geometry("230x310+150+150")  # 长 ， 高    (150 150 位置)
windows.resizable(0, 0) #用户窗口不可拖移修改大小
windows.title("计算器")  # 设置标题
# 0

result = tk.StringVar()  # 用来显示结果的可变文本
equation = tk.StringVar()  # 用来显示算式的可变文本

result.set(' ')  # 赋初始值
equation.set('0')  # 赋初始值


# A     获取按键值
def getnum(num):
    temp = equation.get() #get()获取可变文本内容
    temp2 = result.get()  #get()获取可变文本内容
    if temp2 != ' ':
        temp = '0'
        temp2 = ' '
        result.set(temp2)
    if temp == '0':
        temp = ''
    temp = temp + num  #获取用户输入，直到输入等于
    equation.set(temp) #显示算式的可变文本 equation = tk.StringVar()


# B  C功能 清0
def clear():
    equation.set('0')
    result.set(' ')


# c 功能 计算


def equal():
    temp = equation.get()
    temp = temp.replace('X', '*')
    temp = temp.replace('÷', '/')
    if temp == "":
        result.set("")
        return 0
    answer = eval(temp)
    answer = '%.2f' % answer
    if len(answer) >= 10:
        lenNum = len(answer)
        if 10 <= lenNum <= 11:
            answer = eval(answer)/pow(10, 10)
            result.set(str(answer)+"e"+"10")
        else:
            result.set("超过显示范围！")
    else:
        result.set(str(answer))


# d 功能 除去最后一个字符


def back():
    temp = equation.get()
    equation.set(temp[:-1])


# 结果显示框
show_uresult = tk.Label(windows, bg='white', fg='black', font=('Aral', '15'), bd='0', textvariable=equation,
                        anchor='se')
show_dresult = tk.Label(windows, bg='white', fg='red', font=('Aral', '30'), bd='0', textvariable=result,
                        anchor='se')
show_uresult.place(x='17', y='0', width='210', height='20')
show_dresult.place(x='17', y='17', width='210', height='38')

# 第一行
Button_Clear = tk.Button(windows, text="AC", height=3, width=6, command=lambda: clear())
Button_Clear.place(x=0, y=50)

Button_ADD_DEC = tk.Button(windows, text='←', height=3, width=6, command=back)
Button_ADD_DEC.place(x=57, y=50)

Button_Percent_sign = tk.Button(windows, text="%", height=3, width=6, command=lambda: getnum('%'))
Button_Percent_sign.place(x=114, y=50)

Button_division_sign = tk.Button(windows, text="÷", height=3, width=6, command=lambda: getnum('÷'))
Button_division_sign.place(x=171, y=50)
# 第二行
Button_7 = tk.Button(windows, text="7", height=3, width=6, command=lambda: getnum('7'))
Button_7.place(x=0, y=101)

Button_8 = tk.Button(windows, text="8", height=3, width=6, command=lambda: getnum('8'))
Button_8.place(x=57, y=101)

Button_9 = tk.Button(windows, text="9", height=3, width=6, command=lambda: getnum('9'))
Button_9.place(x=114, y=101)

Button_X = tk.Button(windows, text="X", height=3, width=6, command=lambda: getnum("X"))
Button_X.place(x=171, y=101)
# 第三行
Button_4 = tk.Button(windows, text="4", height=3, width=6, command=lambda: getnum('4'))
Button_4.place(x=0, y=152)

Button_5 = tk.Button(windows, text="5", height=3, width=6, command=lambda: getnum('5'))
Button_5.place(x=57, y=152)

Button_6 = tk.Button(windows, text="6", height=3, width=6, command=lambda: getnum('6'))
Button_6.place(x=114, y=152)

Button_reduce = tk.Button(windows, text="-", height=3, width=6, command=lambda: getnum('-'))
Button_reduce.place(x=171, y=152)
# 第四行
Button_1 = tk.Button(windows, text="1", height=3, width=6, command=lambda: getnum('1'))
Button_1.place(x=0, y=203)

Button_2 = tk.Button(windows, text="2", height=3, width=6, command=lambda: getnum('2'))
Button_2.place(x=57, y=203)

Button_3 = tk.Button(windows, text="3", height=3, width=6, command=lambda: getnum('3'))
Button_3.place(x=114, y=203)

Button_ADD = tk.Button(windows, text="+", height=3, width=6, command=lambda: getnum('+'))
Button_ADD.place(x=171, y=203)
# 第五行
Button_0 = tk.Button(windows, text="0", height=3, width=13, command=lambda: getnum('0'))
Button_0.place(x=0, y=254)

Button_point = tk.Button(windows, text=".", height=3, width=6, command=lambda: getnum('.'))
Button_point.place(x=114, y=254)

Button_equal = tk.Button(windows, text="=", height=3, width=6, command=lambda: equal())
Button_equal.place(x=171, y=254)

windows.mainloop()
