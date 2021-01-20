import numpy as np

#initialization
#one-dim
a = np.array([2,3,4])
a = np.array([2,3,4], dtype=np.float64)
#multi-dim
a = np.array([ [1, 2, 3],
			[4, 5, 6] ])
#conversion
a = np.array([1,2,3,4,5,6]).reshape((2,3))
a = a.reshape((1,6))
a = a.flatten()

#by shape
a = np.zeros( (3,4) )
a = np.ones( (3,4), dtype=np.int32 )
a = np.empty( (3,4) )

#arange
a = np.arange(10,-10,-1)
a = np.arange(12).reshape( (3,4) )

#linspace
a = np.linspace(1, 10, 10, endpoint=False)

#random
a = np.random.random( (3,4) )
a = np.random.rand(3,4)
a = np.random.randn(3)

#computing method
a = np.array([1,1,1,1])
b = np.ones( (4,1) )
c = a+b
c = 10*np.sin(a)
c = a>3
c = a==3

#Transpose
a = np.array([1,1,1,1])
a_T = np.transpose(a)
a_T = a.T
b = (a.T).dot(a)
#one dim(default a.T.shape == a.shape)
#method1
a_T = a.reshape(-1,1)
#method2
#new axis
a_T = (a[np.newaxis, :]).T 
c = np.array([1 ,1 ,1])[:, np.newaxis]
c_T = c.T



#multiply
c = a*b
c_dot = np.dot(a,b)
c_dot2 = a.dot(b)

#sum  np.sum(a) == a.sum()
a = np.arange(12).reshape( (3,4) )
b = np.sum(a)
b = np.sum(a, axis=0)  #0-column 1-row

#max-min  
b = np.min(a)
b = np.max(a, axis=0)
b = np.argmin(a)
b = np.argmax(a, axis=1)

#average
b = np.mean(a)
b = np.mean(a, axis=1)
b = np.average(a, axis=1)
b = np.median(a)

#index of non-zeros
b = np.nonzero(a)

#sort
b = np.sort(a, axis=1)

#others
b = np.clip(a, 5, 9)
b = np.cumsum(a)
b = np.diff(a)


#index
a = np.arange(1,7)
a[0]
a = a.reshape( (2,3) )
a[1][1]
a[1, 1]
a[1,:]

#iteration
for row in a:
	row**2
for column in a.T:
	column**2
for item in a.flat:
	item**2

#merge
a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
c = np.vstack( (a,b) ) #vertical stack
d = np.hstack( (a,b) ) #horizantal stack
#multiple
c = np.concatenate((a,b,b,a), axis=0)

#split
a = np.arange(12).reshape( (3,4) )
c,d = np.split(a, 2, axis=1)
c,d,e, = np.split(a, 3, axis=0)
c,d = np.hsplit(a, 2)
c,d,e, = np.vsplit(a, 3)
#unequal
c,d,e = np.array_split(a, 3, axis=1)

#copy b is a
a = np.arange(4)
b = a
#deep copy
b = a.copy()