while 1 == 1:

   print("игра в кости")

   import random

   input("нажмите enter чтобы начать игру")

   gamer1 = random.randint(1,6)
   print("ваше число:")
   print(gamer1)

   input("нажмите enter чтобы продлжить игру")

   gamer2 = random.randint(1,6)
   print("число противника:")
   print(gamer2)
   
   if gamer1 >gamer2:
       print("вы победили!! :)")
   elif gamer1 ==gamer2:
       print("ничья")
   else:
       print("вы проиграли :(")
       
   igra = imput("сыграть еще?(введите q чтобы сыграть еще.Нажмите w чтобы закончить игру):.")
   
   if igra == "w":
       break
   elif igra == "q":
       pass
       
   
           