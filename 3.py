i=str(input("请输入一列字符串："))
#方法一（不确定该方法是否正确，因为题目未表述清楚在没有字符串“ol”的情况下是否要倒序）
i=i.replace("ol","fzu")
i=i[ : :-1]
print(i)
