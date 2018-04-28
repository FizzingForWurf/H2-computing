moreEighty = 0
passed = 0
score = 0
counter = 1

ans = input("Enter first score or enter to stop: ")
if ans != "":
    score = score + float(ans)

while(ans != ""):
    counter = counter + 1
    if counter == 1:
        ans = input("Enter first score or enter to stop: ")
        while(not ans.isdigit() and ans != ""):
            ans = input("Enter first score or enter to stop: ")
        if ans != "":
            while(float(ans) < 0 or float(ans) > 100):
                ans = input("Enter first score or enter to stop: ")
            score = score + float(ans)
            
    if counter == 2:
        ans = input("Enter second score: ")
        while(not ans.isdigit()):
            ans = input("Enter second score: ")
        while(float(ans) < 0 or float(ans) > 100):
            ans = input("Enter second score: ")
        score = score + float(ans)
        
    if counter == 3:
        ans = input("Enter third score: ")
        while(not ans.isdigit()):
            ans = input("Enter third score: ")
        while(float(ans) < 0 or float(ans) > 100):
            ans = input("Enter third score: ")
        score = score + float(ans)
        
    if counter == 4:
        ave = score/3
        if ave >= 60:
            print("Average: %0.1f" % float(ave), "(PASSED)")
            passed = passed + 1
        else:
            print("Average: %0.1f" % float(ave), "(FAILED)")
            
        if ave >= 80:
            moreEighty = moreEighty + 1
        print()
        counter = 0
        score = 0

print(passed, "students passed the test and", moreEighty, "students scored higher than 80.")
        
