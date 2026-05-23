import random
import tkinter as tk

# 题库
原始题库 = ('五四运动','辛亥革命','抗日战争','王阳明','拿破仑')
已用题目 = set()

# 提示库
提示词 = {
    '五四运动':('首先爆发于北京', '是一场反帝反封建的爱国革命运动', '一场由学生发起的运动','社会各阶层广泛响应','爆发于1919年'),
    '辛亥革命':('一场资产阶级革命','推翻了一个王朝的统治','革命成果最终被窃取','狭义上来说,发生于1911年','是孙中山领导的革命斗争'),
    '抗日战争':('是一场战争','经历了从局部到全面的发展过程','关键时间节点有1931年、1937年、1939年、1945年','是抵抗日本侵略的战争'),
    '王阳明':('明朝人','哲学家、军事家、教育家','心学的集大成者','提倡致良知、知行合一'),
    '拿破仑':('法国人','革命家、政治家','他极大地推动了法国大革命的发展','近代欧洲著名的军事统帅','皇帝')
}

# 全局变量
当前题目 = ""
当前提示列表 = []
提示序号 = 0

# 抽新题
def 抽新题():
    global 当前题目, 当前提示列表, 提示序号
    if len(已用题目) == len(原始题库):
        提示文本.config(state="normal")
        提示文本.delete(1.0, tk.END)
        提示文本.insert(tk.END, "🎉 恭喜你，完成今日小挑战！")
        提示文本.config(state="disabled")
        输入框.config(state="disabled")
        答题按钮.config(state="disabled")
        提示按钮.config(state="disabled")
        return
    
    # 不重复抽题
    题 = random.choice(原始题库)
    while 题 in 已用题目:
        题 = random.choice(原始题库)
    已用题目.add(题)
    
    当前题目 = 题
    当前提示列表 = 提示词[题]
    提示序号 = 0
    
    # 清空文本框，显示第一条提示
    提示文本.config(state="normal")
    提示文本.delete(1.0, tk.END)
    提示文本.insert(tk.END, f"提示1：{当前提示列表[提示序号]}\n")
    提示文本.config(state="disabled")
    提示序号 += 1
    结果标签.config(text="")
    输入框.delete(0, tk.END)

# 获取更多提示（旧提示保留，追加新提示）
def 获取提示():
    global 提示序号
    if 提示序号 < len(当前提示列表):
        提示文本.config(state="normal")
        提示文本.insert(tk.END, f"提示{提示序号+1}：{当前提示列表[提示序号]}\n")
        提示文本.config(state="disabled")
        提示序号 += 1
    else:
        提示文本.config(state="normal")
        提示文本.insert(tk.END, "提示已全部用完！\n")
        提示文本.config(state="disabled")

# 答题判断
def 答题():
    用户答案 = 输入框.get().strip()
    if 用户答案 == 当前题目:
        结果标签.config(text="✅ 回答正确！")
        窗口.after(1200, 抽新题)  # 1.2秒后自动下一题
    else:
        结果标签.config(text="❌ 回答错误，请再试！")

# --------------- UI布局 ---------------
窗口 = tk.Tk()
窗口.title("历史猜词小挑战")
窗口.geometry("480x320")
窗口.resizable(False, False)

# 多行文本框：存放所有历史提示（旧提示不消失）
提示文本 = tk.Text(窗口, font=("微软雅黑",11), height=7, width=52)
提示文本.pack(pady=12)
提示文本.config(state="disabled")

# 输入框
输入框 = tk.Entry(窗口, font=("微软雅黑",12), width=28)
输入框.pack()

# 按钮行
按钮框 = tk.Frame(窗口)
按钮框.pack(pady=12)

答题按钮 = tk.Button(按钮框, text="提交答案", command=答题, font=("微软雅黑",10), width=10)
答题按钮.grid(row=0, column=0, padx=10)

提示按钮 = tk.Button(按钮框, text="获取更多提示", command=获取提示, font=("微软雅黑",10), width=12)
提示按钮.grid(row=0, column=1)

# 对错结果
结果标签 = tk.Label(窗口, text="", font=("微软雅黑",12))
结果标签.pack()

# 启动第一题
抽新题()

窗口.mainloop()
