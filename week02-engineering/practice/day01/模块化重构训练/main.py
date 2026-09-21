import bmi
import temp

print("1. BMI计算器")
print("2. 温度转换器")
choice = input("请输入功能序号：")

if choice == "1":
    h = float(input("请输入身高（米）："))
    w = float(input("请输入体重（千克）："))
    result = bmi.bmi_calculator(h, w)
    if result:
        b, level = result
        print(f"您的BMI为：{b}，属于{level}")

elif choice == "2":
    val = float(input("请输入温度数值："))
    unit = input("请输入输入单位(c摄氏/f华氏,默认c):") or "c"
    res = temp.temperature_converter(val, unit)
    if res is not None:
        target_unit = "华氏" if unit == "c" else "摄氏"
        print(f"转换后温度：{res} {target_unit}")
