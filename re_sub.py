import re

text = '''
 answer_content : Answer = (b)Aniline reacts with benzaldehyde and forms Schiff's base (benzal aniline)or anils.\({C_6}{H_5} - N{H_2} + O = CH{C_6}{H_5} {C_6}{H_5}N= CH{C_6}{H_5}\)Benzylidine aniline}
 answer :
 is_eligible : 1
  Question : Nitroso amines \(({R_2}N - N = O)\) are soluble in water. On heating themwith concentrated \({H_2}S{O_4}\) they give secondary amines. The reaction iscalled
 a : (a)Perkin's reaction
 b : (b)Fittig's reaction
 c : (c)Sandmeyer's reaction
 d : (d)Liebermann's nitroso reaction

 answer_content : Answer =  (d)Liebermann's Nitroso reaction.
 answer : 4
 is_eligible : 1
'''

text = text.replace('\\', '\\\\')

sql = 'INSERT INTO `question`(`section`, `question_content`, `a`, `b`, `c`, `d`, `ans`, `sub_section`, `level`, `date_posted`) VALUES (\'[value-1]\',\'[value-2]\',\'[value-3]\',\'[value-4]\',\'[value-5]\',\'[value-6]\',\'[value-7]\',\'[value-8]\',\'[value-9]\',CURRENT_TIMESTAMP)'
sql = sql.replace('[value-1]', 'sunil')
print(sql)
