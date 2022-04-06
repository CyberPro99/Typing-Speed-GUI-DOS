import time
String = 'Hallow world welcome to gaza  '
wordcount = len(String.split())
print(String)
while True:
    t0 = time.time()
    inputtext=str(input('Enter the Sentence:'))
    t1= time.time()
    accuracy = len(set(inputtext.split() and set(String.split())))
    accuracy = accuracy/wordcount
    timetaken=t1-t0
    wpm = wordcount/timetaken
    print("WPM",wpm,"Accuracy",accuracy,"Timetaken",timetaken)
    print("----------------------------------------------------")
    result = input('Continue...(Yes/No): ')
    if result == "Yes":
        continue
    else:
         quit()
     