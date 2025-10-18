import random #เป็นการเรียกใช้ฟังชันในโมดูลrandom
import pyfiglet #เป็นการเรียกใช้ฟังก์ชันจากpyfigletเพื่อสร้างรูปภาพแบบascii
from colorama import init, Fore, Style #เป็นการเรียกใช้ฟังก์ชันfore,styleจากcolorama
init(autoreset=True,convert=True)

flower = ['Rose', 'Daisy', 'Sunflower', 'Cherry-Blossom','Jasmine']
animal = ['Dog', 'Cat', 'Rabbit', 'Panda', 'Penguin']
place = ['Paris', 'Maldives', 'Tokyo', 'Rome', 'Barcelona']

QF=['This is a flower that we mostly in Valentines(answer choice:Rose,Daisy,Sunflower,Cherry-Blossom,Jasmine)',
    'This is a small flower with white petals around yellow center,its name means a new beginning(answer choice:Rose,Daisy,Sunflower,Cherry-Blossom,Jasmine)',
    'This flower is always looking at the sun.Its colour is yellow with brown center(answer choice:Rose,Daisy,Sunflower,Cherry-Blossom,Jasmine)',
    'This is a famous flower in Japan.It is a tiny pink flower(answer choice:Rose,Daisy,Sunflower,Cherry-Blossom,Jasmine)',
    'This flower is usually used in Mothers Day in Thiland with white petals(answer choice:Rose,Daisy,Sunflower,Cherry-Blossom,Jasmine)']

QA=['This animal is kept for guarding the house or as pets, such as the Golden Retriever(answer choice:Dog,Cat,Rabbit,Panda,Penguin)',
    'This animal is has a strong sence of smell and excellent night vision,such as Scottish Fold(answer choice:Dog,Cat,Rabbit,Panda,Penguin)',
    'This animal has long ears,short fluffy tails and continuously growing teeth,such as Holland Lop(answer choice:Dog,Cat,Rabbit,Panda,Penguin)',
    'This is a famous animal from China,it is white and black,it likes to eat bamboo(answer choice:Dog,Cat,Rabbit,Panda,Penguin)',
    'This animal lives in the Southern Hemisphere,its exceptional swimming and diving abilities in cold water(answer choice:Dog,Cat,Rabbit,Panda,Penguin)']

QP=['There are many famous tourist attractions here, such as the Eiffel Tower and the Palace of Versailles(answer choice:Paris,Maldives,Tokyo,Rome,Barcelona)',
    'This is an island nation in the Indian Ocean, widely regarded as a quintessential tropical paradise(answer choice:Paris,Maldives,Tokyo,Rome,Barcelona)',
    'This is the dazzling,high-tech capital of Japan(answer choice:Paris,Maldives,Tokyo,Rome,Barcelona)',
    'This is a city in Italy that has famous places,such as the Colosseum(answer choice:Paris,Maldives,Tokyo,Rome,Barcelona)',
    'This is a city in Spain that is famous for its tapas culture and perfectly blends beach with a metropolitan(answer choice:Paris,Maldives,Tokyo,Rome,Barcelona)']

global_round=0
global_score=0

def process(select):
  global global_round,global_score
  if (select==1):
    number=random.randint(0,4) #เป็นการสุ่มเลขเพื่อมาใช้เป็นลำดับของคำถามที่จะถูกนำมาใช้
    kind_name="Flower"
    kind=flower
    question=QF #เป็นการกำหนดว่าคำถามที่จะใช้เป็นของหมดหมู่ดอกไม้
    print(Fore.RED + Style.BRIGHT)
    print("  \\ | /")
    print(" - * * -")
    print("  / | \\")
    print("    |")
    print("  / |")
  elif(select==2):
    number=random.randint(0,4) #เป็นการสุ่มเลขเพื่อมาใช้เป็นลำดับของคำถามที่จะถูกนำมาใช้
    kind_name="Animal"
    kind=animal
    question=QA #เป็นการกำหนดว่าคำถามที่จะใช้เป็นของหมดหมู่สัตว์
    print(Fore.YELLOW + Style.BRIGHT)
    print(" (\\_/)")
    print(" (='.')")
    print(" (\\_(")
  elif(select==3):
    number=random.randint(0,4) #เป็นการสุ่มเลขเพื่อมาใช้เป็นลำดับของคำถามที่จะถูกนำมาใช้
    kind_name="Place"
    kind=place
    question=QP #เป็นการกำหนดว่าคำถามที่จะใช้เป็นของหมดหมู่สถานที่
    print(Fore.BLUE + Style.BRIGHT)
    print("     /\\")
    print("    /  \\")
    print("   /____\\")
    print("  | o  o |")
    print("  --------")
  else:
    print(Fore.RED + Style.BRIGHT+ "!!!Please enter only 1,2 or 3!!!") #แสดงข้อความเพื่อให้ผู้เล่นพิมพ์เลือกหมวดหมู่ด้วยตัวเลขที่กำหนดเท่านั้น
    return None
  global_round +=1
  
  print()
  print(Fore.YELLOW +"="*100)
  print(Fore.BLUE+ Style.BRIGHT+ f"CATEGORY : {kind_name} | ROUND : {global_round} | SCORE : {global_score}") #แสดงชนิดคำถามที่เราจะต้องทายและจำนวนรอบและจำนวนคะแนนรวมสะสมที่เรามี
  print(Fore.YELLOW +"="*100)
  print()
  print(Fore.BLUE+ f"The question is : {question[number]}") #แสดงคำถามที่ถูกสุ่มมาให้ผู้เล่นตอบ

  ans=input(Fore.CYAN + "Enter your answer:").strip() #รับคคำตอบที่ผู้เลนตอบเข้ามาแล้วลบช่องว่างออก
  key=kind[number] #คำตอบของคำถามที่ถูกสุ่มมา

  if(ans.lower()==key.lower()): #เปรียบเทียบคำตอบของผู้เล่นกับเฉลยโดยเปรียบเทียบโดยการทำให้เป็นตัวพิมพ์เล็กทั้งคู่
    print(Fore.GREEN+ Style.BRIGHT+'!!!Your answer is CORRECT!!!')
    global_score+=1
    return True

  else:
    print(Fore.RED+ Style.BRIGHT +'!!!Your answer is INCORRECT!!!')
    print(Fore.YELLOW +f"The correct answer is : {key}")
    return False

def intro():
    print()
    print(Fore.WHITE+"="*100)
    print(Fore.WHITE+"="*100)
    text1="Welcome To"
    ascii_art1= pyfiglet.figlet_format(text1,font='smslant') #กำหนดว่าจะวาดรูปข้อความออกมาเป็นคำว่าอะไรและใช้ฟ้อนต์อะไร
    print(Fore.WHITE + Style.BRIGHT + ascii_art1) #แสดงข้อความasciiที่สร้างออกมาทางหน้าจอ
    print(Fore.WHITE+"="*100)
    print(Fore.GREEN+"="*100)
    text2="Word Wizard"
    ascii_art2= pyfiglet.figlet_format(text2,font='slant')
    print(Fore.GREEN + Style.BRIGHT + ascii_art2)
    print(Fore.GREEN+"="*100)
    print(Fore.GREEN+"="*100)
    print()
    

intro()

while True:
  print(Fore.CYAN+ Style.BRIGHT +f"-----SCORE: {global_score} | ROUND: {global_round}-----") #แสดงคะแนนก่อนเล่นตานี้และจำนวนรอบที่เล่นมาแล้ว
  print(Fore.BLUE+ """
Frist you have to select kind of word BY enter order of the kind in the following
  1.Flower
  2.Animal
  3.Place""")
  select_input=input(Fore.CYAN+ "Choose the order:")

  if select_input.isdigit(): #เงื่อนไขว่าถ้าค่าที่รับมาเป็นตัวเลข
    select = int(select_input) #แปลงข้อความที่รับมาเป็นตัวเลข
    process(select)
  else:
    print(Fore.RED + Style.BRIGHT+ "!!!Please enter only 1,2 or 3!!!")
    continue

  print(Fore.CYAN+Style.BRIGHT+ f"Undapted Score: {global_score}") #แสดงคะแนนหลังจากที่ตอบคำถามแล้วว่าคะแนนตอนนี้เป็นเท่าไหร่

  print()
  print(Fore.YELLOW+'='*100)
  next=input(Fore.MAGENTA+ "Do you want to play it again(Yes/No):").strip() #ถามว่ายังจะเล่นเกมต่อไหมและให้ผู้เล่นตอบ
  print(Fore.YELLOW+'='*100)
  print()

  if (next.lower() =='yes'):
    continue
  else:
    text3="Game Over"
    ascii_art3=pyfiglet.figlet_format(text3,font='smslant')
    print(Fore.RED + Style.BRIGHT + ascii_art3)
    print(Fore.YELLOW+Style.BRIGHT+ f"Thank you for joining our game! Your final score is {global_score} out of {global_round} questions.") #แสดงคะแนนสุดท้ายที่ไก้และจำนวนรอบที่เล่นไปทั้งหมด
    print(Fore.LIGHTRED_EX+"-"*100)
    break




