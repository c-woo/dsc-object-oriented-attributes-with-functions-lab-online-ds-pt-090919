class School:
  def __init__(self, name=None, roster= {}):
    self.name = name
    self.roster = roster
  
  def add_student(self, name=None, grade=None):
    if not grade in self.roster:
      self.roster[grade] = [name]
    else:
      self.roster[grade].append(name)
      
  def grade(self, grade=None):
    return self.roster[grade]
    
  def sort_roster(self):
    for grade in self.roster:
      self.roster[grade].sort()
    return self.roster

