import time
import random
rround=0
againall = True
playerscore=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weapon=['A HAMMER','A SWORD','A PEN','A SPOON','A KNIFE','A PISTOL','AN iPHONE','A LAPTOP','A CHAIR','A BANANA']
rank=['A COLD KILLER','A NOBLE KNIGHT','A NINJA','A HOT-HEADED POTATO','A GIRL ON HER PERIOD','A RAGING GANGSTER','A KUNGFU MASTER','AN ASSASSSIN','A GOD','A MAD DOG']
status=['IS SMART','IS STRONG','MET A KUNGFU MASTER','GOT JEALOUS WITH THE PREVIOUS CHAMPION','USED A SECRET DRUG','REALIZED THE REVOLUTION IDEA OF MARX-LENIN','GOT TIRED OF LIVING IN POVERTY']
reason=['YOU GOT POISONED','YOU FORGOT YOUR WEAPON','YOU SLIPPED HEAD-FIRST ON THE FLOOR','YOU FELL OFF THE BUILDING','YOU GOT IN A LETHAL CAR ACCIDENT','YOU GOT ASSASSINATED','YOU WERE WEAK','YOU WERE NOOB','YOU GOT BITEN BY DOGS','YOU DIED IN THE RESTROOM']
i=abs(int(input('Enter the number of players: ')))
start=abs(int(input('Enter start range: ')))
stop=abs(int(input('Enter stop range: ')))
pointtowin=abs(int(input('Enter the number of point(s) to win the game: ')))
while againall:
   rround=rround+1
   print('--------------ROUND ',format(rround),'-----------------')
   print('-----------------START---------------------')

   n=0
   total=0
   best=0
   player=['','#1: Player 1','#2: Player 2','','','','#6: Player 6','#7: Player 7','','#9: Player 9','#10: Player 10','','#12: Player 12','#13: Player 13','','','','','#18: Player 18','#19: Player 19','#30 Player 30']

   while n<i:
      n=n+1
      if player[n]!='':
            
         number=random.randint(start,stop)
         reroll=0
         total=0
         again=True
         while again==True:
             reroll=reroll+1
             if reroll>1:
                  
                  number=random.randint(-1,1)
                  
                  if number==1:
                     print('------------------------------------------------------------')
                     print(player[n],'started a fight with ',player[winner])
                     print('[',player[n],']====||::::> VS <::::||====[',player[winner],']')
                     time.sleep(3)
                     quote=random.randint(0,9)
                           
                     print('Result: Congrats!!!,',player[n],', You have WON the fight using',weapon[quote])
                     print(player[n],', you are now the NEW champion with the score of ',format(total))
                     best=total  
                     winner=n
                     time.sleep(3)
                     print('------------------------------------------------------------')
                  elif number==-1: 
                     print('------------------------------------------------------------')
                     print(player[n],'started a fight with ',player[winner])
                     print('[',player[n],']====||::::> VS <::::||====[',player[winner],']')
                     time.sleep(3)
                     quote=random.randint(0,9)
                     print('Result: Sorry!!,',player[n],'you have LOST the fight because',reason[quote])
                     print('------------------------------------------------------------')
                     time.sleep(3)
                  elif number==0:
                     print('------------------------------------------------------------') 
                     print(player[n],'started a fight with ',player[winner])
                     print('[',player[n],']====||::::> VS <::::||====[',player[winner],']')
                     time.sleep(3)
                     print('Result: CANNOT DETERMINE THE WINNER, REMATCH IN')
                     time.sleep(1)
                     print('3')
                     time.sleep(1)
                     print('2')                  
                     time.sleep(1)
                     print('1')
                     print('------------------------------------------------------------')
                     
                  if number!=0:
                        again=False   


             else:
                   print(player[n],' - Your power numbers are',end="\r")
                   for x in range (0,5):  
                        
                        number=random.randint(start,stop)
                        print(' ',number, end="\r")
                        total=total+number
                   if best!=total:
                        
                        again=False   

                  
                   print(' = ',format(total), end="\r")
                   print('')
                   print('------------------------------------------------------------')
                   if best<total:
                        if n>2:
                           quote=random.randint(0,6)
                           print(player[n],status[quote])
                           quote=random.randint(0,9)
                           print(player[n],'HAS SLAIN ',player[winner],' WITH',weapon[quote])
                           quote=random.randint(0,9)
                           print('---------------------LIKE',rank[quote],'---------------------')
                           time.sleep(2)
                        best=total  
                        winner=n
                        
                     
            
                   if again==True:
                        print('~~~~~~~~~~~~~~~~~~~~CONFLICTED RESULT~~~~~~~~~~~~~~~~~~~~~~~')
              

         print() 
         time.sleep(1)
         

   print('------------------------------------')
   print('The Winner of ROUND #',format(rround),'is ',player[winner], 'with the score of ',format(best))
   playerscore[winner]=playerscore[winner]+1
   print('OVERALL SCORE: ')
   k=0
   for k in range(0,i+1):
      if player[k]!='':
         print(player[k],':',format(playerscore[k]))
#      print(player[1],':',format(playerscore[1]),',',player[2],':',format(playerscore[2]),',',player[3],':',format(playerscore[6]),',',player[7],':',format(playerscore[7]),',',player[9],':',format(playerscore[9]),',',player[10],':',format(playerscore[10]),',',player[12],':',format(playerscore[12]),',',player[13],':',format(playerscore[13]),',',player[18],':',format(playerscore[18]),',',player[19],':',format(playerscore[19]),',',player[20],':',format(playerscore[20])) 
   print('------------------------------------')
   if playerscore[winner]==pointtowin:
      print('$$$$$$$$$$$$$$$$$$~~~~WINNER FOUND~~~~$$$$$$$$$$$$$$$$$$$')
      print('The Winner of THIS GIVEAWAY IS ',player[winner])
      print('CONGRATULATION',player[winner])
      print('PLEASE CONTACT DUY ANH via FACEBOOK TO GET YOUR PRIZE')
      print('\n')
      print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
      print('THANK YOU ALL FOR PLAYING')
      print('CREATED by eNovA.RS')
      print('Email: leonken56@gmail.com')
      print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
      rround=0
      againall= False
   else:
      time.sleep(5)
      print('NEXT ROUND START IN')
      time.sleep(1)
      print('3')
      time.sleep(1)
      print('2')                  
      time.sleep(1)
      print('1')
      print('------------------------------------')
      restart=0
    
#   else:
#      while restart!="y" and restart!="n":
#            restart = input("Start the next round, Y or N ")
#            restart = restart.lower()
#            if restart=="n":
#                     againall= False
#            elif restart=="y":
#                     againall= True
#            else: print("Y or N")
         
