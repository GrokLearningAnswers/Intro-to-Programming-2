translation = [
  ('tion', 'shun'),
  ('an', 'un'),
  ('th', 'z'),
  ('v', 'f'),
  ('w', 'v'),
  ('c', 'k'),
  ('o', 'oo'),
  ('i', 'ee')]

def eng2chef(s):
  for i, j in translation:
    s = s.replace(i,j)
  if s[-1] == '!':
    s = s[:-1] + '. bork bork bork!!'
  return s.lower().strip()