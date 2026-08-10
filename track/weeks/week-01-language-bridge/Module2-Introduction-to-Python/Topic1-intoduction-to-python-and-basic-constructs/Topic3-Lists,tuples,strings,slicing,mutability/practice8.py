original_scores=[]
for i in range(3):
    original_scores.append(int(input("enter the score:")))

alias_scores=original_scores
replacement_score=int(input("enter replacement score:"))
additional_score=int(input("enter additional score:"))

alias_scores[0]=replacement_score
alias_scores.append(additional_score)

print("original score:",original_scores)
print("Alias score:",alias_scores)
print("shared object:",alias_scores is original_scores)