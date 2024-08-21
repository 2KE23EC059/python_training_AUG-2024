#accept average score from the student of his exam and print his result as follows 
#0 t0 49 is fail 
# 50 t0 74 is second class 
# 75 t0 90 distiction 
# also check for invalid score 
avg_score = int(input("enter your average score to print the result :"))

if avg_score>=0 and avg_score<=49:
    print('result is fail')
elif avg_score >= 50 and avg_score <= 74:
    print("result is second class")
elif avg_score <=75 and avg_score >=90:
    print("result  is first class")
elif avg_score >= 91 and avg_score<=100:
    print("result is distiction")
else:
    print("invalid input")