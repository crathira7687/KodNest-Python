n=int(input("enter score count:"))
scores=[]

for i in range(n):
    score=int(input("enter the score:"))
    scores.append(score)
search_for=int(input("enter a number:"))


print("Highest Score:",max(scores))
print("Lowest Score:",min(scores))
print("Total Score:",sum(scores))
if search_for in scores:
    print("Search Result:Found")
else:
    print("Search Result:Not Found")