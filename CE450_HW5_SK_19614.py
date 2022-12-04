# CS450
#Assignemnt 4



empty = []
def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]


def first(s):
    assert is_link(s)# "first only applies to linked lists."
    assert s != empty# "empty linked list has no first element."
    return s[0]


def rest(s):
    assert is_link(s) # "rest only applies to linked lists."
    assert s != empty # "empty linked list has no rest."
    return s[1]
#########################################################################################

# Question 1: Write a function to check if the element exists or not in the linked list.

"""Return True if elm is in the linked list s
  cntn_link (link(1, link(2, link(3, empty))), 1)
 True
  cntn_link (link(1, link(2, link(3, empty))), 4)
 False
 """

def cntn_link(s, elm):
    assert is_link(s)
    while s!= []:
        if s == elm:
            return True, cntn_link(rest(s), elm)
        else:
            return False

ls = link(12, link(99, link(37, [] )))
print(ls)
print("Question 1: ", cntn_link (link(1, link(2, link(3, empty))), 1))
print("Question 1.1: ", cntn_link (link(1, link(2, link(3, empty))), 4))

##########################################################################################

# Question 2: Create a function to print linked list:
#new_lnk = []
def prnt_link(s):
    """Return a string of all elements in s."""
    if  s == empty:
      return " "
    elif  rest(s) == empty:
      return str(first(s))
    else:
      return str(first(s)) +" , "+ prnt_link(rest(s))

lst = link(12, link(99, link(37, [] )))
lst2 = link(1, link(2, link(3, link(4, empty))))
print("Question 2: ", prnt_link(lst))
print("Question 2: ", prnt_link(lst2))

##########################################################################################

# Question 3: Implement a function to create a new linked list in the reverse order:

def rvrs_lnk(s):
    temp = None
    if s == empty:
        return s
    else:
        temp = s[0]
        s[1] = s[0]
        s[1] = temp
        return s



rev = [1,[2,[3,[4,[]]]]]
print(rev)
print(rvrs_lnk(rev))

##########################################################################################

# Question 4: Write a function srt (lnk) function, which returns True if the linked list lnk
# is sorted ascendingly from the left to right.
# If two adjacent elements are equal, the linked list can still be considered sorted.
'''def prnt_link(s):
    """Return a string of all elements in s."""
    if  s == empty:
      return " "
    elif  rest(s) == empty:
      return str(first(s))
    else:
      return str(first(s)) +" , "+ prnt_link(rest(s))
'''
def srt(lnk):
    sort = []



lnk1 = link(1, link(2, link(3, link(4,empty))))
print(srt(lnk1))

#############################################################################################

# Question 5: Write a function with arguments a linked list lnk and a function g,
# which is applied to each number in lnk and returns the sum.
# If the linked list is empty, the sum is 0.

sqr = lambda x: x * x
dbl = lambda y: 2 * y

def sum_lnk(lnk,g):
    if lnk == empty:# if the list is empty we don't ahve to add anything
        return 0
    elif rest(lnk) == empty: #if the any part of the remaining list is empty
        return g(first(lnk))    # go back to the first one, implement the function
    else:
        return g(first(lnk)) + sum_lnk(rest(lnk), g)# using recursive, add all the list elem

lst = link(1, link(2, link(3, link(4, empty))))
lst2 = link(3, link(5, link(4, link(6, empty))))
print("Question 5: ", sum_lnk(lst, sqr))
print("Question 5: ", sum_lnk(lst2, dbl))

#####################################################################################################

# Question 6:Define a function with input parameters a linked list, lnk, and two elements, u & v. The
# function returns linked list but with all elements of u substituted with v.
'''
>> > l = link(1, link(2, link(3, empty)))
>> > n = change(l, 3, 1)
>> > n
[1, [2, [1, []]]]
'''

'''def change(lnk, u, v):
    assert is_link(lnk)
    while lnk != empty:
        for i in range(len(lnk)):
            if lnk[i] == u:
                lnk[i] = v
                return change(rest(lnk), u, v)
            else:
                return lnk'''
def change(s, u, v):
    assert is_link(s)
    if s == empty:
       return s
    for i in range(len(s)):
        if s[i] == u:
            s[i] = v
            return s
        else:
            return change(rest(s), u, v)

l = link(1, link(2, link(3, empty)))


n = change(l, 3, 1)
m = change(n, 1, 2)
o = change(m, 5, 1)
print("Question 6: ", n)
print("Question 6: ", m)
#print("Question 6: ", o)

####################################################################################################

# Question 7: Generate a function to append element to the end of linked list.
####################################################################################################

