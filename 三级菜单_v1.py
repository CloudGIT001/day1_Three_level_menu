# -*- coding:utf-8 -*-
# Author:xieshengsen


"""
三级菜单：
1. 运行程序输出第一级菜单
2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
3. 菜单数据保存在文件中
4. 让用户选择是否要退出
5. 有返回上一级菜单的功能
"""
Provinces  = {
    "广东省":{
        "广州市":{
            "天河区":["人口","面积"],
            "黄浦区":["人口","面积"],
            "越秀区":["人口","面积"],
            "番禺区":["人口","面积"],
        },
        "茂名市":{
            "化州": ["人口", "面积"],
            "电白": ["人口", "面积"],
            "茂南": ["人口", "面积"],
            "高州": ["人口", "面积"],
        },
        "深圳市":{
            "福田区": ["人口", "面积"],
            "罗湖区": ["人口", "面积"],
            "盐田区": ["人口", "面积"],
            "南山区": ["人口", "面积"],
        }
    },
    "广西省":{
        "玉林市": {
            "玉州区": ["人口", "面积"],
            "博白县": ["人口", "面积"],
            "陆川县": ["人口", "面积"],
            "兴业县": ["人口", "面积"],
        },
        "桂林市": {
            "青秀区": ["人口", "面积"],
            "良庆区": ["人口", "面积"],
            "武鸣区": ["人口", "面积"],
            "江南区": ["人口", "面积"],
        },
        "南宁市": {
            "永福县": ["人口", "面积"],
            "平乐县": ["人口", "面积"],
            "全州县": ["人口", "面积"],
            "七星区": ["人口", "面积"],
        }
    },
    "湖南省":{
        "长沙市": {
            "芙蓉区": ["人口", "面积"],
            "天心区": ["人口", "面积"],
            "开福区": ["人口", "面积"],
            "望城区": ["人口", "面积"],
        },
        "怀化市": {
            "中方县": ["人口", "面积"],
            "沅陵县": ["人口", "面积"],
            "洪江市": ["人口", "面积"],
            "会同县": ["人口", "面积"],
        },
        "衡阳市": {
            "蒸湘区": ["人口", "面积"],
            "石鼓区": ["人口", "面积"],
            "南岳区": ["人口", "面积"],
            "雁峰区": ["人口", "面积"],
        }
    }
}

exit_flag = False

while not exit_flag:
    for i in Provinces:
        print (i)

    choice1 = input("请选择进入1>>>：")

    if choice1 in Provinces:
        while not exit_flag:
            for i2 in Provinces[choice1]:
                print ("\t",i2)

            choice2 = input("请选择进入2，按'b'返回 >>>:")

            if choice2 in Provinces[choice1]:
                while not exit_flag:
                    for i3 in Provinces[choice1][choice2]:
                        print ("\t\t",i3)

                    choice3 = input("请选择进入3，按'b'返回 >>>:")

                    if choice3 in Provinces[choice1][choice2]:
                        while not exit_flag:
                            for i4 in Provinces[choice1][choice2][choice3]:
                                print ("\t\t\t",i4)

                            choice4 = input("最后一层，按'b'返回,按'q'退出>>>:")

                            if choice4 == "b":
                                break
                            elif choice4 == "q":
                                exit_flag = True

                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True

            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
    if choice1 == "b":
        break
    elif choice1 == "q":
        exit_flag = True