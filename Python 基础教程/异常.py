# 异常类型捕获演练 —— 要求用户输入整数
while True:
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
        continue
        print("111111111111111")
    except Exception as result:
        print("未知错误 %s" % result)

    else:
        print("正常执行")
    finally:
        print("执行完成，但是不保证正确")
