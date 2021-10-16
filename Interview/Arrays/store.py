ItemNumber=[101,102,103,104]
ItemName=["Milk","Cheese","Ghee","Bread"]
Price=[42,50,500,40]
Stock=[10,20,15,16]
GivenItemNumer=int(input())
ItemQuantity=int(input())
if GivenItemNumer in ItemNumber:
    for i in range(0,len(ItemNumber)):
        if ItemNumber[i]==GivenItemNumer:
            if ItemQuantity<=Stock[i]:
                estimatedprice=ItemQuantity*Price[i]
                Stock[i]=Stock[i]-ItemQuantity
                print(estimatedprice)
                print(Stock[i])
            else:
                print("NO STOCK")
                break
else:
    print("INVALID ITEM NUMBER")