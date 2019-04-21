import re
url = '''515. A force of 5 N, making an angle \(\theta \) with the horizontal, acting on an
object displaces it by \(0.4m\) along the horizontal direction. If the object
gains kinetic energy of 1J, the horizontal component of the force is

\(\textbf{[EAMCET(Engg.) 2000]}\)
\(\textbf{[MP PMT 2002; CBSE PMT 2003; UPSEAT 2004]}\)

'''

url = re.sub('\(\\textbf.+\d{4}.+', 'DELETED', url)
url = re.sub('\\\\DELETED', '', url)
url = url.replace('\n', '').replace('\r', '')
# print(url)


url = '''515. A force of 5 N, making an angle \(\theta \) with the horizontal, acting on an
object displaces it by \(0.4m\) along the horizontal direction. If the object
gains kinetic energy of 1J, the horizontal component of the force is

\(\textbf{[EAMCET(Engg.) 2000]}\)
\(\textbf{[MP PMT 2002; CBSE PMT 2003; UPSEAT 2004]}\)

Read the assertion and reason carefully to mark the correct option out of the
options given below:

(a)If both assertion and reason are true and the reason is the correct
explanation of the assertion.

(b)If both assertion and reason are true but reason is not the correct
explanation of the assertion.

(c)If assertion is true but reason is false.

(d)If the assertion and reason both are false.

'''


sep = 'Read the assertion'
rest = url.split(sep, 1)[0]
print('printing rest')
print(rest)
