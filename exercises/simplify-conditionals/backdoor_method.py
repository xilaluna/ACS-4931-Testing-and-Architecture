# by Kami Bigdely
# Remove control flag
# Reference: https://searchcode.com/file/92870153/frameworkconsole/framework.py/

def backdoor_srcmethod():
    while True:
        print("Puts the Android Agent inside an Android App APK. The application runs normally, with extra functionality.")
        inputfile = input('APK to Backdoor: ').strip()
        if inputfile == '':
            break
        else:
            print('doing other stuff.')


backdoor_srcmethod()
