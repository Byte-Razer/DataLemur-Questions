def min_attendees(answers):
  length=len(answers)
  total=0
  j=0
  for i in range(length):
    if answers[j]==0:
      total=total+1
      answers.remove(answers[j])
    else:
      j=j+1
    
  #return sorted(answers)
  newanswers=list(set(answers)) 
  newanswers=sorted(newanswers)
  #maximum=max(newanswers)
  length=len(answers)
  for i in range(0,len(newanswers)):
    value=newanswers[i] 
    no1 = answers.count(value)
    if no1%2==0:
      if value+1==no1:
          total=total+no1
      else:
          for k in range(no1): 
              total=total+value
    else:
      no1=no1-1
      if value+1==no1:
        total=total+no1
      else:
        for l in range(no1): 
          total=total+value
      # add 2
      total=total+value+1

  return total
  