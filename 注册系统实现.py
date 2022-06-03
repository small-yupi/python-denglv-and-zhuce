import random as r
import time as t
time = 15
def function(): # 定义函数function(功能)
    print("请输入要选择的模式")
    print("1=开发者模式,2=普通模式")
    pattern = input("请输入:")
    if pattern == "1": # 如果pattern(判断)的值为"1"时执行以下代码
        print("请选择你需要的功能")
        print("1=HelloWorld代码,2=python代码生成器")
        function = input("")
        if function == "1": # 如果function(功能)的值为"1"的时候执行以下代码
            import time as t # 导入time模块,并重命名为t
            while 1: # 将以下代码进行死循环
                print("请选择语言(支持C、C++、Python、Shell、Java)")
                print("会输出所选语言的HelloWorld代码")
                i = input("语言:")
                if i == "C": # 如果i的值为"C"时执行以下代码
                    print("""
                    #include<stdio.h>
                    int main()
                    {
                        printf("HelloWorld")
                        return 0;
                    }""")
                    print("")
                    print("按ctrl+c粘贴")
                    t.sleep(10)
                elif i == "C++": # 如果i的值为"C++"时执行以下代码
                    print("""
                    #include<iostream>
                    using namespace std;
                    int main()
                    {
                        cout<<"HelloWorld";
                        return 0;
                    }""")
                    print("")
                    print("按ctrl+c粘贴")
                    t.sleep(10)
                elif i == "Python": # 如果i的值为"Python"时执行以下代码
                    print("""
                    print("HelloWorld")
                    """)
                    print("")
                    print("按ctrl+c粘贴")
                    t.sleep(10)
                elif i == "Shell": # 如果i的值为"Shell"时执行以下代码
                    print("""
                    echo "HelloWorld"
                    """)
                    print("")
                    print("按ctrl+c粘贴")
                    t.sleep(10)
                elif i == "Java": # 如果i的值为"Java"时执行以下代码
                    print("""
                    public class 文件名 {
            	        public static void main(String args) {
            		        System.out.println("HelloWorld")
            	    }
            }
                    """)
                    print("")
                    print("按ctrl+c粘贴")
                    t.sleep(10)
                else: # 否则执行以下代码
                    print("输入错误")
                    print("请注意大小写")
                    t.sleep(5)
        elif function == "2": # 如果function(功能)的值为"2"时执行以下代码
            import random as r
            import time as t
            while 1:
                command = ["print","input","while","for","xx = xx","if","else","elif","def","class","list","int","float","string","dict"]
                print(r.choice(command))
                t.sleep(5)
        else:
            print("输入错误")
    elif pattern == "2":
        print("请选择你需要的功能(输入1为计算器,输入2为制作个人信息卡,按3求出5个数里的最大值,按4来求出5个数里的最小值)")
        function = input("请输入数字")
        if function == "1":  # 如果enter等于1那么执行计算器功能
            print("运算符输入xx或者**可计算次方,数字不要输入太长,且不要输入其他符号来干扰正常的运算。")
            while 1:
                sath_enter = float(input())  # 输入运算第1个数
                yunsuanfu = input("")  # 输入运算符
                sath_enter2 = float(input())  # 输入运算第2个数
                if yunsuanfu == "+":  # 如果运算符为+那么执行加法运算
                    print(f"{sath_enter}+{sath_enter2}={sath_enter + sath_enter2}")
                elif yunsuanfu == "-":  # 如果运算符为-那么执行减法运算
                    print(f"{sath_enter}-{sath_enter2}={sath_enter - sath_enter2}")
                elif yunsuanfu == "x" or yunsuanfu == "*":  # 如果运算符为x或*那么执行乘法运算
                    print(f"{sath_enter}x{sath_enter2}={sath_enter * sath_enter2}")
                elif yunsuanfu == "/":  # 如果运算符为/那么执行除法运算
                    print(f"{sath_enter}/{sath_enter2}={sath_enter / sath_enter2}")
                elif yunsuanfu == "**" or yunsuanfu == "xx":  # 如果运算符为**或xx那么执行次方运算
                    print(f"{sath_enter}的{sath_enter2}次方={sath_enter ** sath_enter2}")
                else:  # 否则输入错误
                    print("运算符输入错误")
        elif function == "2":  # 如果enter等于2执行下面的命令
            while 1:
                chinese = input("输入0生成英文版，输入1生成中文版")
                if chinese == "0":  # 如果输入0生成英文版
                    name2 = input("name")
                    age = input("age")
                    job = input("job")
                    hobbie = input("hobbie")
                    msg = f"""
                    ---------------- info of {name2} ----------------
                    Name : {name2}
                    Age  : {age}
                    job  : {job}
                    Hobbie  : {hobbie}
                    ---------------------- end ---------------------"""
                    print(msg)
                    print("")
                    print("按ctrl+c进行复制")
                elif chinese == "1":  # 输入1生成中文版
                    name3 = input("姓名")
                    age2 = input("年龄")
                    job2 = input("职业")
                    hobbie2 = input("爱好")
                    msg = f"""
                    ---------------- info of {name3} ----------------
                    姓名 : {name3}
                    年龄  : {age2}
                    职业  : {job2}
                    爱好  : {hobbie2}
                    ---------------------- end ---------------------"""
                    print(msg)
                    print("")
                    print("按ctrl+c进行复制")
                else:
                    print("输入错误")
        elif function == "3":  # 输入3执行以下程序
            while 1:
                c2 = 0
                b = 2
                max = float(input("请输入第1个数"))
                for i in range(4):  # 循环4次
                    c = float(input(f"请输入第{b}个数"))  # 输入进变量a，并转换成浮点数类型
                    if c > max:  # 对比大小
                        max = c  # 转换
                    b += 1
                print(f"最大值为{max}")  # 输出告知用户结果
        elif function == 4:  # 输入4执行以下程序
            while 1:
                c1 = 0
                b = 2
                small = float(input("请输入第1个数"))
                for i in range(4):  # 循环4次
                    c = float(input(f"请输入第{b}个数"))  # 输入进变量a，并转换成浮点数类型
                    if c < small:  # 对比大小
                        small = c  # 转换
                    b += 1
                print(f"最大值为{small}")  # 输出告知用户结果
        else:
            print("输入错误")
    # else:
    #     print("输入错误")
username=["产品经理","程序员","用户1"]
password=["20490813","10244201","123456"]
input_username = ""
input_password = ""
def register():
    print("开始登录(如果没有账号,请将用户名和密码都输入zhuce,来注册账户)")
    input_username = input("请输入用户名")
    input_password = input("请输入密码")
    if input_username == "zhuce" and input_password == "zhuce":
        username.append(input("请输入新的用户名"))
        password.append(input("请设置登录密码"))
register()
a = 0
record = 0
list_size = len(username)
while 1:
    a = 0
    for i in range(list_size):
        if input_username == username[a]:
            if input_password == password[a]:
                print(f"登录成功,你好:{username[a]}")
                t.sleep(1)
                function()
                break
            else:
                a += 1
        else:
            a += 1
    else:
        record += 1
    if list_size == record:
        print("用户名或密码输入错误,请重新输入")
        register()
    elif record == 6:
        record = 0
        time = time * 2
        print(f"输入错误次数过多,请输入验证码,并等待{time}秒")
        while 1:
            recaptcha = r.choice(["aAo94","12NkO","Fd9Ls","Ms19K","Sn910","9Kn1l","S69rE","euDnI","nlWs1"])
            print(recaptcha)
            input_recaptcha = input("")
            if input_recaptcha == recaptcha:
                print("输入正确,请等待...")
                t.sleep(time)
                break
            else:
                print("输入错误,请重新输入");