# system apell atm 
# developer : Amirmahdi heydari/ telefon : 09196792984
# python prigramming
# naim : shbyh saz sastem amel atm 



# deyta 
tapell_g= 0
deytamany = 999
deyta_uzer =  ['amirmahdi heydari ', 1388,4333, 00]  
deyta_pasword2 = [4413,4455,6644,7799,2244,5588,8844,9966,6677,2456,227]
deyta_tayps = ['not1','not2','not3','not4','not5','not6','not7','not8']
g = 1 
# deleete s
def delete() :
  deyta_uzer[1:3] = 'not'
  deyta_pasword2 [0:10] = 'not '
  deytamany = 'not '
  tapell_g  = 'not'
  g = 'not'
  deyta_tayps = 'not'
  print ('all deytas delete !')
 
 
import random 




while tapell_g<= 3 : # tacrar hlgeh 
    print ('ABERANK')
    print ('==========================================================')
    print ('hi ! welcome you in aber bank ')
    print ('inter pasword for worod  ')
    print ('===========================================================')
    print ('developer :amirmahdi heydari ')
    print ('===========================================================')
    tapell = int(input('inter pasword :')) #worody
    if tapell == deyta_uzer[1] :
        print ('welcome to aber banke  ')
        print ('==================================================')
        print ('1- cart to cart ')
        print ('2-pardagt gabz  ')
        print ('3-mojody')
        print ('4-gtyde shaarg')
        print ('5-bardasht many  ')
        print ('==================================================')
        print ('9921 --hesab banke   ')
        print ('deyta 9933')
        print ('9922-exit')
        print ('==================================================')
        tapell1 = int(input('inter gozineh :'))
        if tapell1 == 1 :
          print ('carmozd :10')
          tapell2 = int (input ('enter shamareh cart :'))
          tapell3 = int (input('inter mablag :')) 
          if tapell3 < deytamany and tapell3 < 900   :
            deyta_tayps[1] = 'inter uzer cart to cart :' , tapell1
            deytamany = deytamany - tapell3 
            deytamany = deytamany - 10
            print ('amalyat movafag :)')
            tapell15 = input ('aryou ok for print resid ? : ok/no')
            if tapell15 == 'ok' :
             print ('=========================================')
             print ('amalait movafag :)')
             print ('mablag ' , tapell3)
             print ('shoomareh  cart : ' , tapell2)
             print ('mogody :' , deytamany)
             print ('==========================================')
             print ('lotfa cart god ra dardarid !')
             input ('you for exit enter :')
             continue
            elif tapell15 == 'no' :
              print ('lotfa cart god ra bardarid ')
              continue 
          else :
            print ('==========================================')
            print ('you cant cart to cart  ! ')
            print ('mogody nacafy or mahdodiat 900m raiat nshodeh ast  !')
            print ('===========================================')
            print ('latfa cart god ra bar daryd ')
            input ('you for exit enter :')
            continue
        elif tapell1 == 2   :
          print ('===================================')
          print ('1-gbztelefon ')
          print ('2- gabz brg')
          print ('3-gbz gaz ')
          print ('4-gabz ab ')
          print ('===================================')
          print ('antegab conyd ')
          tapell20 = int (input('enter gozinneh :'))
          if (tapell20 == 1 or tapell20 == 2 or tapell20 == 3 or tapell20 == 4  ) and g == 1  :
            deyta_tayps[2] = 'inter uzer pardagt gabz :' , tapell1
            tapell4 = int (input ('inter shenaseh gabz :'))
            tapell2 = int (input ('inter shmareh cart :'))
            if tapell4 == deyta_uzer[2] and deytamany > 50  : 
             deytamany = deytamany - 50
             g = g - 1 
             print ('amalyat movafag :)')
             tapell16 = input ('aya maeyel beh print resyd hastyd : ok/no')
             if tapell16 == 'ok' :
              print ('==============================================')
              print ('amalait movafag :)')
              print ('mablag :50')
              print ('shoomaseh cart ' , tapell2)
              print ('cart : amirmahdi heydari ')
              print ('===============================================')
              print ('lotfa cart god ra dardarid !')
              input('you for exit enrer :')
              continue
             elif tapell16 == 'no' :
              print ('lotfa cart god ra bardarid ')
              continue
            else :
              print ('===============================')
              print ('mojody na cafa ro shmarehjbz na morabar !')
              print ('================================')
              print ('latfa cart god ra bardarid ')
              input ('you for exit enter :')
              continue 
          else :
            print ('=======================================')
            print ('gozineh na motabar   ')
            print (' or shooma pardagt cardeh ed !')
            print ('========================================')
            print ('lootfa cart god ra bar daryd ')
            input ('for you exit enter :')
            continue
        elif tapell1 == 3 :
           if deytamany> 0 :
             deyta_tayps[3] = 'inter uzer mojody :', tapell1
             print ('ammalait mogody ')
             print ('print resyd ba pishfarz  angam shod  ')
             print ('=================================================')
             print ('amalait movafag ')
             print  (deytamany)
             print (' cart : ')
             print ('==================================================')
             print ('lotfa cart god ra dardarid !')
             input  ('you for exit enter :')
             continue
           else :
            print ('============================================')
            print ('you not mony  ')
            print ('mogody : 0')
            print('==============================================')
            print ('latfa cart god ra bardaryd ')
            input ('for you exit enter :')
            continue
        elif tapell1 == 4 :
          print ('==========================================')
          print ('shaarg intgab  : ')
          print ('1-hamrah aval ' , '2-eransel ')
          print ('===========================================')
          tapell5 = int (input ('enter operator :'))
          if tapell5 == 1 or 2 :
            tapell6 = int (input ('inter shamareh cart :'))
            tapell7 = int (input ('enter shmareh telefon :'))
            tapell22 = int (input('enter ramz dodom :'))
            tapell8 = int (input ('enter mabalg :'))
            if tapell8 < deytamany and tapell22 == deyta_uzer[3] : 
              deyta_tayps[4] = 'inter uzer paardgt shaarg : ' , tapell1
              deytamany = deytamany - tapell8
              print ('amalyat movafg :)')
              tapell17 = input ('aya mayel bbeh print resid hastid : ok/no')
              if tapell17 == 'ok' : 
               print ('================================================')
               print ('amalait mmovafag :)')
               print ('shrg angam shod ') 
               print ('mablag :' , tapell8)
               print ('shomareh shend : ' , tapell7)
               print ('=================================================')
               print ('lotfa cart god ra bardaryd ')
               input('for you exit enter :') 
               continue
              elif tapell17 == 'no' :
                print ('lotfa cart god ra dardaryd ')
                continue
            else :
             print ('=========================================')
             print ('mogody na cafy !')
             print ('or ramz dovom na matabar ')
             print ('==========================================')
             print ('lataafa cart god ra bardartd ')
             input  ('for you exit enter :')
             continue
          else :
            print ('========================================')
            print ('gozineh na motabar !')
            print ('=========================================')
            print ('lataafa cart god ra bardaryd ')
            input ('you for exit ennter :')
            continue 
        elif tapell1 == 5 :
          tapell9 = int(input('inter mablag ra bray bardasht vared conyd :'))
          if tapell9 < deytamany and tapell9 >10 :
            deyta_tayps[5] = 'inter uzer bardashvagehha :' , tapell1
            deytamany = deytamany - 10
            deytamany = deytamany - tapell9 
            print ('amalyat movafag :)')
            tapell18 = input ('enter are you ok for print resid : ok/no')
            if tapell18 == 'ok'  :
             print ('============================================')
             print ('amalait movafag :)')
             print ('mablag bardasht :', tapell9)
             print ('bardasht :  carmazd : 10')
             print ('=============================================')
             print ('lotfa cart got ra brdarid ')
             input ('you for exit enter :')
             continue
            elif tapell18 == 'no' :
              print ('lotfa cart god ra baardarid ')
              continue
          else :
            print ('======================================')
            print ('mogody nacafy !')
            print ('or mablag kamtar 10 ')
            print ('=======================================')
            print ('latfa cart god ra dardaryd ')
            input ('you for exit enter :')
            continue
        elif tapell1 == 9921:
          deyta_tayps[6] = 'inter uzer 9921 :', tapell1
          print ('modyriat cart banke ')
          print ('=====================================================')
          print ('1-amalait ramz ')
          print  ('2-masdod cardan cart ')
          print ('3-amaalyat ramz dovom ')
          print ('=====================================================')
          tapell10 = int (input ('enter gozyneh'))
          if tapell10 == 1 :
            tapell11 = int (input ('emter ramz fely :'))
            tapell12 = int (input('enter ramz gadyd :'))
            if tapell11 == deyta_uzer[1] and tapell11 !=tapell12:
              deyta_uzer[1] = tapell12
              print ('==================================')
              print ('amalait movafag ')
              print ('amalait ramz ramz gadyd : ' , tapell12)
              print ('ramz gadym :', tapell11)
              print ('===================================')
              print ('lotfa  cart god ra bardaryd ')
              input ('you for exit enter :')
              continue
            else :
              print ('===================================')
              print ('eror')
              print ('ramz na motabar !')
              print ('or ramz fely da ramz gadyd yeli ast ')
              print ('====================================')
              print ('latfa cart god ra bardaryd :')
              input ('you for exit enetr :')
              continue 
          elif tapell10 == 2 :
            tapell13 = int (input ('enter ramz cart :'))
            if tapell13 == deyta_uzer[1] :
              print ('===================================')
              del deyta_uzer[1]
              print (' cart shma masdod shod :)')
              print ('====================================')
              print ('litfa cart god ra bardaryd ')
              input ('you for exit enter :')
              continue 
            else :
              print ('================================')
              print ('ramz na motabaer') 
              print ('=================================')
          elif tapell10 == 3 :
            tapell21 = int (input ('enter ramz aval cart :'))
            print ('shrayet faal sazi ramz dovom ')
            print ('==================================')
            print ('The terms of using the second code are applicable for internet purchases and transactions outside the card reader and bank teller. The use of the second code has conditions that you must always comply with. There is no other and only for your own video card')
            print ('===================================')
            input ('enter  for admeh :')
            if tapell21 == deyta_uzer[1] :
             deyta_uzer[3] = random.choice(deyta_pasword2)
             print ('====================================')
             print ('amalyat ramz dovom ')
             print (deyta_uzer[3])
             print ('======================================')
             print ('latfa cart god ra bardaryd :')
             input ('you for exit enter :')
            else :
              print ('==================================')
              print ('eror do not in paaswor ')
              print ('===================================')
              print ('lotfa cart god rabardaryd :')
              input ('you for exit enter :')
        elif tapell1 == 9922 :
          deyta_tayps[7] = 'inter uzer 9922 :', tapell1
          tapell14 = input ('are you ok for exit ok/no ?')
          if tapell14 == 'ok' :
           print ('goode by uzer :)') 
           print ('developer : amirmahdi heydari')
           break
          elif tapell14 == 'no' :
            print ('welcome ;)')
            continue
          else :
            print ('dastorna motabar  !')
            continue
        elif tapell1 == 9933 :
          print ('==========================================')
          print (deyta_tayps)
          print ('===========================================')
          print ('atalaat taytpes ')
        elif tapell1 == 99222 :
          deyta_tayps[8] = 'inter uzer 99222', tapell1
          print ('pangareh magfy shaarg hesab ')
          print ('===================================')
          print (' 1-shaarg hesab')
          print ('2- dlete all deyta !')
          print ('====================================')
          tapell19 = int (input ('enter you :'))
          if tapell19 == 1 :
            tapell23 = int (input ('enter mablag :'))
            deytamany = deytamany + tapell23 
            print ('========================================')
            print ('amalyat ba movafrgit angam shood :)')
            print ('=========================================')
            print ('lotfa cart god ra bardaryd ')
            input ('you for exit enter :')
            continue
          elif tapell19 == 2 :
            print ('=================================')
            print ('all deytas delete ! ')
            print ('==================================')
            delete ()
            continue 
          else :
            print ('==============================')
            print ('gizineh na motabar ')
            print ('===============================')
            print ('latfa cart god ra bardaryd ')
            input ('yoou for exit enter :')
            continue
        else :
          print ('===================================')
          print ('dastor namotabr')
          print ('====================================')
          continue
    elif tapell != (deyta_uzer[1]):  # eror do not pasword 
      print ('===============================================')
      print ('Eror not in pasword  !')
      print ('================================================')
      tapell_g = tapell_g + 1
else :  # eror masdodiat 
 print ('============================================')
 print ('oh ! you can not inter pasword !')
 print ('cort shoma masdod shod !')
 print ('blook cart !')
 print ('============================================')  
 input ('you for exit enter :')




# app payabn 
#developer : amirmahdi heydari 
# تمامی حقوق برای امیرمهدی  حیدری محفوظ است  اسکی حرام 
# شبیه ساز دستگاه atm
#  مرداد ماه تابستان 1402 