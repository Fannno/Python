h = int(input("請輸入身高(cm)："))
w = int(input("請輸入體重(kg)："))

def bmi(h,w):
    bmi_value = w/(h/100)**2 
    if bmi_value < 18.5:
        print("體重過輕")
        return bmi_value,"體重過輕"
    elif 18.5 <= bmi_value < 24:
        print("體重正常")
        return bmi_value,"體重正常"
    elif 24 <= bmi_value < 27:
        print("體重過重")
        return bmi_value,"體重過重"
    elif 27 <= bmi_value < 30:
        print("輕度肥胖")
        return bmi_value,"輕度肥胖"
    elif 30 <= bmi_value < 35:
        print("中度肥胖")
        return bmi_value,"中度肥胖"
    else:
        print("重度肥胖")
        return bmi_value,"重度肥胖"
    
value,status = bmi(h,w)
print(f"BMI值為:{value:.2f}, 體重狀況為:{status}")

