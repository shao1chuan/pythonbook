try:
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
except ZeroDivisionError:
    print("除 0 错误")
except Exception as result:
    print("未知错误 %s" % result)
else:
    # 没有异常才会执行的代码
    print('没有异常才会执行的代码')
    pass
finally:
    # 无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行的代码")



# try:
#     # 尝试执行的代码
#     pass
# except 错误类型1:
#     # 针对错误类型1，对应的代码处理
#     pass
# except 错误类型2:
#     # 针对错误类型2，对应的代码处理
#     pass
# except (错误类型3, 错误类型4):
#     # 针对错误类型3 和 4，对应的代码处理
#     pass
# except Exception as result:
#     # 打印错误信息
#     print(result)
# else:
#     # 没有异常才会执行的代码
#     pass
# finally:
#     # 无论是否有异常，都会执行的代码
#     print("无论是否有异常，都会执行的代码")
