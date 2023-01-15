import numpy as np 

dt = np.dtype(np.int32)
print(dt)


aa = np.dtype('i1')
at = np.dtype('i2')
ab = np.dtype('i4')
ac = np.dtype('i8')


print(ac)
print(aa)
print(ab)
print(at)

da = np.dtype([('age', np.int8)])
db = np.array([(10,),(20,),(30)], dtype=da)
print(db)
print(db['age'])

student = np.dtype([('name', 'S20'),('age','i1'),('marks','f4')])
test = np.array([('abc',30,50),('xyz',18,75.0)],dtype=student)
print(test)


print(student)




