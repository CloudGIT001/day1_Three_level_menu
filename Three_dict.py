# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:39:12 2017

@author: xieshengsen
"""

Three_Dict  = {
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


#print(Three_Dict)

#==============================================================================
# exit_flag = False
# while not exit_flag:
#     for key1 in Three_Dict:
#         print(key1)
#     
#     choice1 = input("choice1 >>:").strip()
#     if choice1 == "b":
#         break
#     
#     if choice1 == "q":
#         exit_flag = True
#     
#     if len(choice1) == 0 or choice1 not in Three_Dict:
#         continue
#     
#     
#     while not exit_flag:
#         for key2 in Three_Dict[choice1]:
#             print(key2)
#         choice2 = input("choice2 >>:").strip()
#         
#         if choice2 == "b":
#             break
#         
#         if choice2 == "q":
#             exit_flag = True
#         
#         if len(choice2) == 0 or choice2 not in Three_Dict[choice1]:
#             continue
#         
#         
#         while not exit_flag:
#             for key3 in Three_Dict[choice1][choice2]:
#                 print(key3)
#             choice3 = input("choice3 >>:").strip()
#             
#             if choice3 == "b":
#                 break
#             
#             if choice3 == "q":
#                 exit_flag = True
#             
#             if len(choice3) == 0 or choice3 not in Three_Dict[choice1][choice2]:
#                 continue
#             
#             
#             while not exit_flag:
#                 for key4 in Three_Dict[choice1][choice2][choice3]:
#                     print(key4)
#                 choice4 = input("choice4 >>:").strip()
#                 
#                 if choice4 == "b":
#                     break
#                 
#                 if choice4 == "q":
#                     exit_flag = True
#                 
#                 if len(choice4) == 0 or choice4 not in Three_Dict[choice1][choice2][choice3]:
#                     continue
#==============================================================================
                

level = []

while True:
    for key in Three_Dict:
        print(key)               
    choice = input("choice >>:").strip()
    
    if choice == "b":
        if len(level) == 0:
            break
        Three_Dict = level[-1]
        level.pop()
        
    if len(choice) == 0 or choice not in Three_Dict:
        continue
    
    level.append(Three_Dict)
    Three_Dict = Three_Dict[choice]





















