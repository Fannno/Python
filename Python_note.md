
## 資料型態
| 資料型態 | 範例              | 說明         |
| -------- | ---------------- | ------------ |
| `int`    | `x = 10`         | 整數         |
| `float`  | `y = 3.14`       | 浮點數       |
| `str`    | `name = "Alice"` | 字串         |
| `bool`   | `is_valid = True`| 布林值       |

**Python 直譯器會自動依照資料判斷型態**
- `'A'` -> `str`
- `1`   -> `int`
- `1.1` -> `float`
- `True` / `False` -> `bool`


## 變數命名規定與建議
**基本規則**
1. 只能包含英文字母、數字、底線 _
- 例如：`score`,` my_score`, `x1`
- 錯誤示範：`1score`、`my-score`
2. 不能以數字開頭
- 正確：`score1`
- 錯誤：`1score`
3. 大小寫敏感
- `score` 與 `Score` 是不同變數
4. 不能使用 Python 保留字
- 例如：`if`, `for`, `while`, `True`, `None`

**命名建議**
1. 使用有意義的名稱
- 例如：`total_score` 比 `ts` 更清楚
2. 使用底線分隔單字（snake_case）
- 例如：`my_variable_name`
3. 避免過短或過長
- 過短：`x`, `y`
- 過長：`this_is_a_very_long_variable_name_that_is_hard_to_read`
4. 布林值變數建議用疑問形式
- 例如：`is_valid`, `has_data`

**建立變數**
```python
score = 95
avg = 5.5
name = "Alice"
is_passed = True
```

## 常用內建函式
| 函式        | 說明                     | 範例                           |
| --------- | ---------------------- | ---------------------------- |
| `print()` | 輸出資料到螢幕               | `print("Hello, World!")`            |
| `input()` | 從使用者取得輸入               | `name = input("Enter your name: ")`        |
| `len()`   | 計算字串、列表等的長度          | `len("Hello")` → 5            |
| `type()`  | 查看變數的資料型態             | `type(10)` → `<class 'int'>` |
| `int()`   | 將資料轉成整數                | `int("123")` → 123                |
| `float()` | 將資料轉成浮點數               | `float("3.14")` → 3.14           |
| `str()`   | 將資料轉成字串                | `str(100)` → "100"               |
| `range()` | 產生一個數字序列               | `range(5)` → 0,1,2,3,4            |
| `sum()`   | 計算數字列表的總和             | `sum([1,2,3])` → 6              |

## 條件運算符號
| 運算符   | 說明         |
| ----- | ---------- |
| `**`  | 次方         |
| `//`  | 整數除法,會直接取商的整數部分 |
| `==`  | 等於         |
| `!=`  | 不等於        |
| `>`   | 大於         |
| `<`   | 小於         |
| `>=`  | 大於等於       |
| `<=`  | 小於等於       |
| `and` | 且，兩個條件都要成立 |
| `or`  | 或，任一條件成立即可 |
| `not` | 否定，條件取反    |

## print()
**基本結構**
```py
print("Hello")
```
- 用來在終端機印出訊息或變數內容

**輸出多個值**
```py
print("Name:", "Alice", 100)
```
- 可以用逗號 `,` 分隔多個項目，print 會自動在項目間加入空格

**使用 sep 設定分隔符號**
```py
print("2025", "01", "01", sep="-") # 使用 " - " 分隔
```
**使用 end 設定結尾**
```py
print("Hello", end=" ") # 結尾改為空格
print("World") # 下一個 print 會接在同一行
```
### 格式化輸出
**f-string**
```py
name = "Alice"
age = 18
print(f"{name} 的年齡是 {age}")
```
- 可以用表達式：
    ```py
    a, b = 5, 10
    print(f"{a} + {b} = {a+b}")
    ```
- 可以設定格式：
    ```py
    pi = 3.1415926
    print(f"{pi:.2f}")  # 只顯示兩位小數
    ```
**format()**
```py
print("{} 的年齡是 {}".format("Alice", 18))
```
### 常見用法整理
| 功能       | 寫法            | 範例                        |
| -------- | ------------- | ------------------------- |
| 基本輸出     | `print(x)`    | `print("Hi")`             |
| 多值輸出     | `print(a, b)` | `print(3, 4)`             |
| 自訂分隔符    | `sep`         | `print(1, 2, 3, sep="-")` |
| 自訂結尾     | `end`         | `print("A", end="*")`     |
| f-string | `f"{}"`       | `print(f"分數：{score}")`    |
## input()
**基本結構**
```py
變數 = input("提示訊息")
```
- 括號內的文字會顯示在螢幕上（提示訊息）
- 使用者輸入後按下 Enter，內容會存入變數
- `input()` 回傳一定是字串，如果要變成整數或浮點數，需要轉型

### 常見型態轉換寫法
```py
變數 = 資料型態(input("提示訊息"))
```
* `input("訊息")`：顯示提示訊息並取得使用者輸入（字串）
* `資料型態(...)`：把字串轉成指定的型態（如 int、float）
* 指派給變數

**範例:轉成整數**
```py
age = int(input("請輸入年齡："))
```
* 使用者輸入「20」→ 變成整數 20
* 若輸入「abc」會報錯：`ValueError`

### 搭配 try/except（避免輸入錯誤）
```py
while True:
    try:
        score = float(input("請輸入分數："))
        break
    except ValueError:
        print("請輸入有效的數字！")
```
## temp()
**如果在 Python Shell 當中想要知道某個變數對應的資料型態**
```py
type(變數名稱) #輸出：<class '資料型態'>
```
## 判斷條件 if / elif / else
**基本結構**
```py
if 條件1:
    執行程式區塊1
elif 條件2:
    執行程式區塊2
else:
    執行程式區塊3
```
- if：當條件成立時執行
- elif（可選）：前面的條件不成立，再判斷這個條件
- else（可選）：前面的條件都不成立時執行

### tips
- **使用縮排判斷程式區塊（通常是 4 個空格）**
- **如果條件成立時執行的程式碼只有一行，可以直接放在冒號之後不需換行。**
- **若某一行沒有縮排，從此行開始會被視為 if 的部分已經結束。**

## for迴圈
**基本結構**
```py
for 變數 in 可迭代物件:
    執行程式區塊
```
- 變數：每次迴圈會依序取得可迭代物
- 可迭代物件包括：
    - 字串（string）
    - 列表（list）
    - range()
    - tuple
    - dictionary（鍵或值）
### 常用
**range()**
- `range(n)` — 從 0 數到 n-1
- `range(start, end)` — 從 start 數到 end-1
- `range(start, end, step)` — 從 start 數到 end-1，間隔 step
  - `range(0, 10, 2)` = `for (int i = 0; i < 10; i += 2)`(Java)

**走訪字串**
```py
for char in "Hello":
    print(char)
```
**走訪列表**
```py
for item in [10, 20, 30]:
    print(item)
```
**走訪字典**
```py
my_dict = {"a": 1, "b": 2}
for key in my_dict:
    print(key, my_dict[key])
```

### tips
- **使用 `break` 提前結束迴圈**
- **使用 `continue` 跳過本次迴圈，進入下一次迴圈**
- **for 迴圈內的程式碼必須縮排**
- **range的結尾永遠不包含end(`for i in range(0,10):` = java的`for(int i = 0 , i < 10 i++)`)**

## enumerate()
- 同時取「索引」與「值」
- 在走訪時自動加上編號，不用自己寫變數去計數
```py
for index, value in enumerate(可迭代物件):
    執行程式區塊
```
- **範例1**
    ```py
    for index, value in enumerate(["apple", "banana", "cherry"]):
        print(index, value)
    ```
- **輸出**
    ```
    0 apple
    1 banana
    2 cherry
    ```
  - `index` 是元素的位置（從 0 開始）
  - `fruit` 是對應位置的值

- **範例2**
    ```py
    for index, char in enumerate("Hello"):
        print(index, char)
    ```
- **輸出**
    ```
    0 H
    1 e
    2 l
    3 l
    4 o
    ```

- **範例3**
    ```py
    my_dict = {"a": 1, "b": 2}
    for index, key in enumerate(my_dict):
        print(index, key, my_dict[key])
    ```
- **輸出**
    ```
    0 a 1
    1 b 2
    ```

- **範例4**
    ```py
    for index, value in enumerate(["apple", "banana", "cherry"],start=1):
        print(index, value)
    ```
- **輸出**
    ```
    1 apple
    2 banana
    3 cherry
    ```

## 雙層for迴圈
**基本結構**
```py
for 外層變數 in 外層可迭代物件:
    for 內層變數 in 內層可迭代物件:
        執行程式區塊
```
- **範例1：列印乘法表**
    ```py
    for i in range(1, 4):      # 外層迴圈控制列
        for j in range(1, 4):  # 內層迴圈控制欄
            print(i*j, end=" ")
        print()  # 換行

    ```
- **輸出**
    ```
    1 2 3 
    2 4 6 
    3 6 9 
    ```
- **範例2：二維列表走訪**
    ```py
    matrix = [
    [1, 2, 3],
    [4, 5, 6]
    ]

    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()
    ```
- **輸出**
    ```
    1 2 3 
    4 5 6 
    ```
    
- **範例3：二維列表走訪**
    ```py
    matrix = [
    [10, 20],
    [30, 40]
    ]

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            print(i, j, value)
    ```
- **輸出**
    ```
    0 0 10
    0 1 20
    1 0 30
    1 1 40
    ```   
    
    |       | 列 0    | 列 1        |
    |-------|-------|-------|
    | **行 0**   | (0,0) | (0,1) |
    | **行 1**   | (1,0) | (1,1) |

### tips
- `break` 只會跳出最近的迴圈層
- `continue` 只會跳過最近的迴圈層的本次迴圈

## while迴圈
**基本結構**
```py
while 條件:
    執行程式區塊
```
- 當條件成立時，**重複執行**程式區塊
- 當條件不成立時，迴圈停止

### tips
- **避免無限迴圈：迴圈內務必有變數更新或`break`**
- **結合 if/else：可以用 while 迴圈持續要求有效輸入**
- **可以搭配 `try/except`：捕捉輸入錯誤，程式更健壯**

## 函式def
**基本結構**
```py
def 函式名稱(參數1, 參數2, ...):
    程式區塊
    return 回傳值  # 可選
```
* `def`：關鍵字，宣告函式
* `函式名稱`：自訂名稱（遵守變數命名規則）
* `參數`：傳入函式的值（可選）
* `return`：回傳結果（可選）

- **範例1：無參數、無回傳**
    ```py
    def say_hello():
        print("Hello World")

    say_hello()  # 呼叫函式
    ```
- **輸出**
    ```
    Hello World
    ```
    
- **範例2：有參數**
    ```py
    def greet(name):
        print(f"Hello, {name}!")

    greet("Alice")
    ```
- **輸出**
    ```
    Hello, Alice!
    ```
    
- **範例3：有回傳值**
    ```py
    def add(a, b):
        return a + b

    result = add(3, 5)
    print(result)
    ```
- **輸出**
    ```
    8
    ```   

- **範例4：預設參數**
    ```py
    def greet(name="Guest"):
        print(f"Hello, {name}!")

    greet()        # 使用預設值
    greet("Bob")   # 傳入參數
    ```
- **輸出**
    ```
    Hello, Guest!
    Hello, Bob!
    ```  
    
### tips
* **函式內部可使用任意資料型態作為參數和回傳值**
* **可以同時回傳多個值：**
    ```py
    def get_point():
        return 10, 20

    x, y = get_point()
    ```
    
## try/except
**基本結構**
```py
try:
    可能發生錯誤的程式區塊
except 錯誤類型1:
    發生錯誤類型1時執行的程式區塊
except 錯誤類型2:
    發生錯誤類型2時執行的程式區塊
else:
    如果沒有錯誤時執行的程式區塊
finally:
    無論是否發生錯誤都會執行的程式區塊
```
- try：放置可能會發生錯誤的程式碼
- except：捕捉特定錯誤並處理，避免程式崩潰
- 可以指定錯誤類型，也可以捕捉所有錯誤
- else（可選）：當 try 區塊沒有發生錯誤時執行
- finally（可選）：無論是否發生錯誤都會執行的程式碼
    - 例如檔案關閉
    ```py
    try:
        f = open("file.txt")
        data = f.read()
    except FileNotFoundError:
        print("檔案不存在")
    finally:
        f.close()
    ```
### 常用 Exception 對照表

| Exception           | 發生情況           | 使用範例                                     |
| ------------------- | -------------- | ---------------------------------------- |
| `ValueError`        | 轉型失敗、資料格式不對    | `int("abc")` → ValueError                |
| `TypeError`         | 資料型態不符合運算或函式要求 | `"1" + 2` → TypeError                    |
| `ZeroDivisionError` | 除以 0           | `10 / 0` → ZeroDivisionError             |
| `IndexError`        | 取列表或字串超出範圍     | `[1,2,3][5]` → IndexError                |
| `KeyError`          | 用不存在的鍵取字典值     | `{"a":1}["b"]` → KeyError                |
| `FileNotFoundError` | 開啟不存在的檔案       | `open("nofile.txt")` → FileNotFoundError |
| `AttributeError`    | 物件沒有該屬性或方法     | `"abc".push()` → AttributeError          |
| `NameError`         | 使用未定義的變數       | `print(x)` (x 未定義) → NameError           |
| `ImportError`       | 匯入不存在的模組       | `import notexist` → ImportError          |
| `KeyboardInterrupt` | 使用 Ctrl+C 中斷程式 | 手動中斷程式 → KeyboardInterrupt               |

### tips
- **使用多個 except：可以針對不同錯誤類型做不同處理**
- **避免捕捉所有錯誤：指定錯誤類型可以避免忽略其他潛在問題**
- **使用`except Exception as e`: 會捕捉所有錯誤並把錯誤訊息存到變數 `e`，適合在不確定錯誤類型時使用，但不建議當作常態**
