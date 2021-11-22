#! python3

import task1

def test1():
  st1 = task1.student("Anita Bath","91334",11)
  st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
  st1.getGrades( [91, 94, 87, 99, 82, 100, 73])
  assert st1.name == "Anita Bath"
  assert round(st1.average(),1) == 89.4
  assert st1.getHonorRoll() == True 
