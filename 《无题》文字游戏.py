#没有注释给你看给爷爬 这么简单的程序还需要注释？
#作者咸鱼味的鸽子 QQ:1727803401



print("游戏前须知:")
print("本游戏为文字游戏，基于Python运行，作者：咸鱼味的鸽子")
print("作者QQ:1727803401 原创剧情，欢迎模仿")
print("你的每一步选择将会影响结局")
print("版本1.1 更新日志：延伸了各个故事线")
TY = input("输入“同意”开始运行程序 否则将终止程序:")
if TY == '同意':
    print(None)
else :
    quit(0)
print("*你是来买酒对吧")
print("*你今年几岁了")
age = int(input("你的年龄:"))

if age < 21:
    print("*你不能买酒，美国法律规定21岁以下的人不能买酒")  
    print("*不过你可以买口香糖或可乐")
elif age >= 21:
    print("*对不起，本店的酒卖完了，给爷爬")
    print("*还是你要买可乐？")

a = input('是否要买可乐？(填yes或no):')

if a == 'yes':
    print("*好的，可乐给你了，看啥看，还不快爬")
    print("*你还需要口香糖吗")
elif a == 'no':
    print("*不买东西别站着挨着我做生意，快爬")
    print("*或者说你还要买口香糖？")
else :
    print(None)

b = input('是否要买口香糖？(填yes或no):')

if b == 'yes':
    print("*欢迎下次光临~")
elif b == 'no':
    print("*不买东西能不能快爬，**东西")
else :
    print(None)
print("*你从商店出来了，请问你要回家还是去其它地方？")

c = input("请问你要去？(写“家”或者“其它地方”):")

if c == '家':
    print("*你回到了家里")
    print("*请问你需要洗澡吗")
    c1 = input("是否要洗澡？(填写是或否)：")
    if c1 == '是':
        print("*你洗了个澡")
        print("*你感觉浑身清爽")
        print("洗完澡你想干什么?")
        c1x1 = input("你想干什么？(可选：看电视、睡觉):")
        if c1x1 == '看电视':
            print("*你坐在了沙发上")
            print("*观看着电视节目")
            print("*Demo End")
            input("按任意键退出游戏")
            exit(0)
        elif c1x1 == '睡觉':
            print("*你躺在床上")
            print("*静静地进入梦乡")
            print("*等待着...第二天的到来")
            print("可惜在这个程序里面，并没有第二天")
            print("Demo End")
            input("按任意键退出游戏")
            exit(0)
    elif c1 == '否':
        print("*你坐在了沙发上")
        print("*观看着电视节目")
        print("Demo End")
        input("按任意键退出游戏")
        exit(0)
    else :
        print("Demo End")
        input("按任意键退出游戏")
elif c == '其它地方' or '其他地方':
    print("*你选择了前往其他地方。")
    print("*请问你需要去哪里(可选目的地：广场、酒吧)")

d = input("填写你的目的地:")

if d == '广场':
    print("*你来到了广场")
    print("*你看见一群广场舞大妈在篮球场跳舞")
    print("*你很想打篮球但是被广场舞大妈们占了场地")
    print("*请问你想怎么解决这个问题")
    d1 = input("你的解决方式(打架或是友好协商)：")
    if d1 == '打架':
        import random
        d1x1 = random.randint(0,10)
        if d1x1 == 0 or 1 or 2 or 3 or 4:
            print("*你单手吊打了10个广场舞大妈，你太厉害了！")
            print("*不过你因为涉嫌寻衅滋事罪，被警方逮捕了")
            print("*不过，你缴纳了保释金，你出狱了")
            print("*接下来你要？(去酒吧或是回家)")
            d1x1x1 = input("你的选择：")
            if d1x1x1 == '家':
                 print("*你回到了家里")
                 print("*请问你需要洗澡吗")
                 d1x1x1x1 = input("是否要洗澡？(填写是或否)：")
                if d1x1x1x1 == '是':
                    print("*你洗了个澡")
                    print("*你感觉浑身清爽")
                    print("洗完澡你想干什么?")
                    d1x1x1x1x1 = input("你想干什么？(可选：看电视、睡觉):")
                    if d1x1x1x1x1 == '看电视':
                        print("*你坐在了沙发上")
                        print("*观看着电视节目")
                        print("*Demo End")
                        input("按任意键退出游戏")
                        exit(0)
                    elif d1x1x1x1x1 == '睡觉':
                        print("*你躺在床上")
                        print("*静静地进入梦乡")
                        print("*等待着...第二天的到来")
                        print("*你起床了，当前时间8:00")                        
                elif d1x1x1x1 == '否':
                    print("*你坐在了沙发上")
                    print("*观看着电视节目")
                    print("*你迷迷糊糊的起来，昨晚你看电视看着看着睡着了")
                    print("当前时间8:00")
        elif d1x1 == 5 or 6 or 7 or 8 or 9 or 10:
            print("*你失败了，你被广场舞大妈群殴致死")
            print("*你从医院醒来")
    elif d1 == '友好协商':
        print("*你上前去友好协商")
        print("*你没有耐心继续商量了")
        print("*你开始动手")
        import random
        d1x1 = random.randint(0,10)
        if d1x1 == 0:
            print("*你单手吊打了10个广场舞大妈，你太厉害了！")
            print("*不过，你缴纳了保释金，你出狱了")
        elif d1x1 == 1:
            print("*你失败了，你被广场舞大妈群殴致死")
            print("*你从医院醒来")
elif d == '酒吧':
    print("*你来到了酒吧")
    print("*你遇见了你的朋友，你朋友想与你喝酒")
    d1 = input("请问是否喝酒？(填是或否):")
    if d1 == '是':
        print("你大喝了一场")
        print("你准备开车回家")
        print("突然，你感觉失去意识")
        print("你依稀感觉有人在努力抢救你")
        print("Demo End")
        input("按任意键退出游戏")
        exit(0)
    elif d1 == '否':
        print("你谢绝了你朋友的邀请，并表示急着回家只是过来看看")
        print("*你回到了家里")
        print("*请问你需要洗澡吗")
        d1x1 = input("是否要洗澡？(填写是或否)：")
        if d1x1 == '是':
            print("*你洗了个澡")
            print("*你感觉浑身清爽")
            print("洗完澡你想干什么?")
            d1x1x1 = input("你想干什么？(可选：看电视、睡觉):")
            if d1x1x1 == '看电视':
                print("*你坐在了沙发上")
                print("*观看着电视节目")
                print("*Demo End")
                input("按任意键退出游戏")
                exit(0)
            elif d1x1x1 == '睡觉':
                print("*你躺在床上")
                print("*静静地进入梦乡")
                print("*等待着...第二天的到来")
                print("可惜在这个程序里面，并没有第二天")
                print("Demo End")
                input("按任意键退出游戏")
                exit(0)
        elif c1 == '否':
            print("*你坐在了沙发上")
            print("*观看着电视节目")
            print("Demo End")
            input("按任意键退出游戏")
            exit(0)

