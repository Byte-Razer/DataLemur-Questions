def weakest_strong_link(strength):
  rowsno=len(strength)
  colno=len(strength[0])
  min_rows=[]
  max_col=[]
  for i in range(rowsno):
    smallest=min(strength[i])
    min_rows.append(smallest)
  for j in range(colno):
    largest=0
    for i in range(rowsno):
      if strength[i][j]>largest:
        largest=strength[i][j]
    max_col.append(largest)
  length1=len(min_rows)
  length2=len(max_col)
  check=False
  for i in range(0,length1):
    for j in range(0,length2):
      if min_rows[i]==max_col[j]:
        inter=min_rows[i]
        check=True
  if check==False:
    return -1
  else:
    return inter
strength = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#Test case
#[[1], [2], [3], [4]] Expected 4
#[[9, 8, 10],[6, 15, 4]] Expected -1
#[[1]] Expected 1
#[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]  Expected 12
#[[3,6],[7,1],[5,2],[4,8]] Expected -1
#[[1, 2, 3],[4, 5, 6],[7, 8, 9]] Expected 7
print(weakest_strong_link(strength))