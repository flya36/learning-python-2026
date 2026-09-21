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