import pandas as pd
from Product import Product

#assuming their is data into excel file into a dataframe df
#df = pd.read_excel(name of file, sheet_name=)

df = pd.read_excel('Reading.xlsx', sheet_name='products')

#before loop prsenting header
print("%20s%20s%10.2s" %("Prodcut Name","Category","Price"))
print("-"*50)

for index, row in df.iterrows():
    prodcutName=row['pName']
    category = row['Category']
    price= row['Price']
    
    currentProduct = Product(prodcutName, category, price)
    #print(currentProduct.descrip())
    pList.append(currentProduct)
    
    currentProduct.discount(5)
    #print("after: ", currentProduct.descrip())
    #format
    #allocate space for 20 strings category
    #no comma 
    print("%-20s%-20s%-10.2f" %(prodcutName,category,price))
    
    #print(prodcutName, " ", category, " ",price )
  """  
#outside the loop
print(len(pList))
for product in pList:
    print("%-20s%-20s%-10.2f" %(prodcut.getName(), producut.getcategory(),product.getprice()))
    """
#outside the loop
print()
    
