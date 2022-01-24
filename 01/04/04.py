# Set 
# 


name = { 'h','f','QA12', 'as12', 'wq12' }

print(type(name))

name.add('df45')
print(name)
print(len(name))


new_set = {'a', 'b','c','d','e','f','g','h','i'}

print(new_set.union(name))

new_set.update(name)
print(new_set)


a = [12, 12, 13,14]

n = set(a)
print(n)


r = {12,14,45,67,89}
e = list(r)
print(e)




d = {1,2,3,4,5,6}

m = {4,5,6,7,8,9}

v = d.difference(m)
print(v)



p = {1,2,3,4,5,6}

p.pop()
print(p)


h= {1,3,4,5,6,7,8,9}

q = {1,2,3,4,5}


print(q.issubset(h))
