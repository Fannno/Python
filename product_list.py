Product_list = [
    {"name": "Product1", "price": 100},
    {"name": "Product2", "price": 200},
    {"name": "Product3", "price": 300},
    {"name": "Product4", "price": 400}
]
for i,p in enumerate(Product_list): ## 用 enumerate 取得索引值和產品資訊
    print(i,": Product_name :",p["name"],"price :", p["price"])
    ## 也可以用 f-string
    print(f"{i} : Product_name : {p['name']},price : {p['price']}")

## 用傳統的 for 迴圈
for i in range(len(Product_list)): ## 用 len() 取得產品數量
    print(f"{i} : Product_name : {Product_list[i]['name']},price : {Product_list[i]['price']}") 
    ## [i]['name']代表第 i 個產品的名稱  [i]['price']代表第 i 個產品的價格

