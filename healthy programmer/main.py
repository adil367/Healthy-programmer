import time
from pygame import mixer
no_glass=18
no_eyes_ex=12
no_phy_ex=8
eye_extime=time.time()
water_time=time.time()
phy_extime=time.time()
def drink_water():
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.play()
    time.sleep(10)
def eyes_ex():
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.play()
    time.sleep(10)
def phy_ex():
    mixer.init()
    mixer.music.load("physical.mp3")
    mixer.music.play()
    time.sleep(10)
if no_glass>0:
    if time.time()-water_time == 2100:
        print("it is time to drink water\n")
        while true:
            drink_water()
            confirm=input("did you drink water?(y/n)")
            if confirm=="y"or "Y":
                no_glass-+1
                water_time=time.time()
                with open("water log.txt","a") as w:
                    w.writelines("drank water at",time.strftime("%H:%M:%S"),"\n")
                break
if time.time() - phy_extime == 3600:
    print("it is time to do physical excercise\n")
    while true:
        phy_ex()
        confirm = input("did you do your physical excercise?(y/n)")
        if confirm == "y" or "Y":
            phy_extime = time.time()
            with open("physical ex.txt", "a") as w:
                w.writelines("physical excercise done at", time.strftime("%H:%M:%S"), "\n")
                break
if time.time() - eye_extime == 2400:
    print("it is time to do eyes excercise\n")
    while true:
        eyes_ex()
        confirm = input("did you do your eyes excercise?(y/n)")
        if confirm == "y" or "Y":
            eye_extime = time.time()
            with open("eye_ex log.txt", "a") as w:
                w.writelines("eyes exercise done at", time.strftime("%H:%M:%S"), "\n")
                break
