#身高=input("請輸入您的身高(公尺)：")
#體重=input("請輸入您的體重(公斤)：")
#BMI=float(體重)/float(身高)**2
#print("您的BMI是："+str(BMI)+"，四捨五入後是："+str(round(BMI)))

#round()是四捨五入,math.ceil()是無條件進位,math.floor()是無條件退位

身高=input("請輸入您的身高：")
print(f"您的身高為：{身高}公分，若是您想要免兵役的話您的體重需要低於："
      f"{round(15*round(float(身高)/100,2)**2,2)}公斤，或是需要高於："
      f"{round(35*round(float(身高)/100,2)**2,2)}公斤")
#print("您的身高為："+str(身高)+
#      "公分，若是您想要免兵役的話您的體重需要低於："+
#      str(round(15*round(float(身高)/100,2)**2,2))+"公斤，或是需要高於："+
#      str(round(35*round(float(身高)/100,2)**2,2))+"公斤")