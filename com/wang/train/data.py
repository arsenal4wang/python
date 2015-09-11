import sys;
#coding=utf-8

x = "foo";
y = 100;
x1=x[1:3];

print(x1);
print(y);


small_list = [123, 'john']
list = ['abcd', 786 , 2.23, 'john', 70.2, small_list]

print(list)
print(list[1])
print(list)


tuple = ('abcd', 786, 2.23, 'john', 70.2);
tinytuple = (123, 'john');

print(tuple)



dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict[2])
print(tinydict.keys())