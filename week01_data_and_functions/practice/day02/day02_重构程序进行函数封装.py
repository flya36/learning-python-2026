'''
1. BMI 计算器：输入身高、体重，计算 BMI 指数并输出体重等级
2. **摄氏 / 华氏温度转换器**：输入温度数值和单位，实现两种温标互相转换
重构要求：
- 每个功能封装为独立函数，通过参数接收输入，通过 `return` 返回结果，不把输入输出写死在函数内部
- 为函数的参数增加**默认值**（例如 BMI 函数默认身高单位为米、温度函数默认输入为摄氏度）
- 主程序只负责调用函数、打印结果，核心计算逻辑全部放在函数中
- 尝试在一个脚本中同时定义两个函数，理解函数作用域和代码组织结构
'''
def bmi_calculator(height: float, weight: float, unit: str = "m") -> tuple | None:
    """
    计算BMI指数和体重等级
    :param height: 身高，默认单位米
    :param weight: 体重，单位千克
    :param unit: 身高单位，默认'm'（米），支持'cm'（厘米）
    :return: (BMI值, 体重等级)；参数异常返回None
    """
    if height <= 0 or weight <= 0:
        print("提示：身高体重必须为正数")
        return None
    
    # 单位转换
    if unit == "cm":
        height = height / 100
    
    bmi = round(weight / (height ** 2), 1)
    
    if bmi <= 18.5:
        level = "低体重"
    elif 18.5 < bmi <= 23.9:
        level = "正常体重"
    elif 24 <= bmi <= 27.9:
        level = "超重"
    else:
        level = "肥胖"
    
    return bmi, level


def temperature_converter(value: float, input_unit: str = "c") -> float | None:
    """
    摄氏/华氏温度双向转换
    :param value: 温度数值
    :param input_unit: 输入单位，默认'c'（摄氏），支持'f'（华氏）
    :return: 转换后的温度；单位异常返回None
    """
    input_unit = input_unit.lower()
    if input_unit == "c":
        # 摄氏转华氏
        return round(value * 9 / 5 + 32, 1)
    elif input_unit == "f":
        # 华氏转摄氏
        return round((value - 32) * 5 / 9, 1)
    else:
        print("提示：仅支持 c/f 单位")
        return None


# 主程序：只负责交互和打印
if __name__ == "__main__":
    print("1. BMI计算器")
    print("2. 温度转换器")
    choice = input("请输入功能序号：")
    
    if choice == "1":
        h = float(input("请输入身高（米）："))
        w = float(input("请输入体重（千克）："))
        result = bmi_calculator(h, w)
        if result:
            bmi, level = result
            print(f"您的BMI为：{bmi}，属于{level}")
    
    elif choice == "2":
        val = float(input("请输入温度数值："))
        unit = input("请输入输入单位（c摄氏/f华氏，默认c）：") or "c"
        res = temperature_converter(val, unit)
        if res is not None:
            target_unit = "华氏" if unit == "c" else "摄氏"
            print(f"转换后温度：{res} {target_unit}")
