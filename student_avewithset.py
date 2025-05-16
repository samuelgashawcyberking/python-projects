# info of students with set
info_st=[


{
  
  "Name":'samuel ',
  "grade" : "10",
  "subject":[70,80 ,90,85,95]
},
{
  "Name":'yonas ',
  "grade" : "10",
  "subject":[76,88 ,100,85,90]

    
},
{
  "Name":'yordanos ',
  "grade" : "10",
  "subject":[80,84 ,70,85,75]
},
{
  "Name":'samuel ',
  "grade" : "10",
  "subject":[74,99 ,60,85,85]

    
}
]


 
#my own function to calculate average
def Ave(a,b):
  cal_ave=sum(a)/len(a)
  return cal_ave
# using loop
for st in info_st:
  name=st["Name"]
  sub=st["subject"]
  if sub:
    ave_subject=Ave(sub,sub)
    print(f"Average  for  student {name}: {ave_subject}")
    passing_score = 60.0
    if ave_subject>=passing_score:
        print(f'student {name}: passed')
    else:
        print(f'student {name}: failed')
#for ave_subject in ave_subject.items():
  
 