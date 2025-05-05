altura_francisco = 1.50
altura_sara = 1.10
crescimento_francisco = 0.02
crescimento_sara = 0.03
anos = 0
while altura_sara <= altura_francisco:
    altura_sara += crescimento_sara
    altura_francisco += crescimento_francisco
    anos += 1
print(f"Sara será mais alta que Francisco em {anos} anos.")