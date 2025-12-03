while True: ## 持續執行直到使用者輸入有效成績
    try: ## 嘗試執行以下程式碼
        score = int(input("請輸入成績："))
        
        if 0<=score<=100: ## 檢查成績是否在有效範圍內
            if score >=90:
                grade = "A"
            elif score >=80:
                grade = "B"
            elif score >=70:
                grade = "C"
            elif score >=60:
                grade = "D"
            else:
                grade = "F"
            print("成績等級為：", grade)
            break ## 成功執行後跳出迴圈 
        else:
            print("成績必須在 0 到 100 之間，請重新輸入。")

    except ValueError: ## 捕捉輸入非數字的錯誤

        print("請輸入有效的數字成績！")
