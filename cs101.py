#################################################
# UDACITY cs101 Intro to Computer Science
#################################################
# 1 Write your first program
# 2 Write Programs to do Repeating Work
# 3 How to Manage Data
# 4 Responding to Queries
# 5 How Programs Run
# 6 How to Have Infinite Power
#################################################

# 1 Write your first program
# Insert code from job PC
# Udacity_Intro_Computer_Science

age = 27
days_in_year = 365.25

days_lived = age * days_in_year

# Find string in string
x = "super"
statement = "This course is super, I mean really super!"

statement.find(x)

print statement.find(x,16)


# Find first link in webpage

page = '"<!DOCTYPE html> <ul> <li><li><a href="http://what-if.xkcd.com">What If?</a></li>"'
start_link = page.find("<a href=")
print start_link
start_quote = page.find('"', start_link)
print start_quote
end_quote = page.find('"', start_quote + 1)
print end_quote

url = page[(start_quote + 1):end_quote]
print url

# Rounding numbers
# str(<number>) # turns into string

x = 27.6
x = x + 0.5
x = str(x)
nearest = x[:x.find('.')]

print nearest


#################################################

# 2 Write Programs to do Repeating Work

page = 'blablabla <a href="http://visiticeland.com">English</a></li>'
## Contents of some webpage
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1:end_quote]
print url
# page = page[end_quote:]


# Procedures. Inputs -> Procedure -> Outputs

# def get_next_target (s)
# 	start_link = s.find('<a href=')
# 	start_quote = s.find('"', start_link)
# 	end_quote = s.find('"', start_quote + 1)
# 	url = s[start_quote + 1:end_quote]
# 	return url, end_quote


def rest_of_string(s): 
	return s[1:]
print rest_of_string("audacity")


def inc(n):
	return n+1
print inc(5)


def sum(a,b):
	a=a+b
	return a		## Changes value of a inside procedure, but not value of a in rest of program/script.
print sum(2,123)

s = "Hello "
t = "Dave!"
print sum(s,t)
print s  ## s is still "Hello" not "Hello Dave!"

def square(s):
	d = s**2
	return d
	
def square(n):
	return n*n
print square(4)
print square(-5)


def sum3 (a,b,c):
	return a + b + c
print sum3(1,2,3)

def abbaize(a,b):
	return a+b+b+a
print abbaize("a","b")



# Could call text for search and word for target. Depends on what is most intuitive. 
# We want the inputs to be easy to understand
def find_second(text, word):
	first = text.find(word)
	second = text.find(word, first + 1)
	return second

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')


def absolute(x):
	if x < 0:
		x = -x
	return x
print absolute(-88)

def bigger(x,y):
	if x > y:
		return x
	else:
	    return y
print bigger(2,7)


def is_friend(name):
    return name[0]=="D" or name[0]=="N" 
print is_friend('Diane')
print is_friend('Fred')
print is_friend('Niane')

# The "or" operator does not evaluate the second part if the first part is true. This can be useful.

def biggest(a,b,c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    else:
        return c
print biggest(3, 6, 9)

######## While loops
i = 0
while i < 10:
	print i
	i = i +1 


i = 0
while i != 10:
	i = i +1 
	print i

def print_numbers(n):
    i = 1
    while i<=n:
        print i
        i = i + 1
print_numbers(5)
print_numbers(0)


def factorial(n):
	result = 1
	while n >= 1:
		result = result * n
		n = n -1
	return result
print factorial(4)


def udacify(string):
    return "U" + string
print udacify('dacians')
print udacify('turn')


def median(a,b,c):
    if a >= b and a <= c:
        return a
    if a <= b and a >= c:
        return a
    if b >= a and b <= c:
        return b
    if b <= a and b >= c:
        return b
    else:
        return c
print(median(1,2,3))
print(median(13,233,43))
print(median(1444,52,5553))

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)
print(median(1,2,3))

def countdown(n):
    while n > 0:
    	print n
        n = n - 1
    print "Blastoff!"
countdown(3)



def find_last(search, target):
    i = 0
    while i >= 0:
        last = search.find(target, i)
        end = search.find(target, i+1)
        if end == -1:
            break    
        i = i +1
    return last
print find_last('aaaa', 'a')

def find_last(s,t):
	last_pos = -1
	while True:
		pos = s.find(t, last_pos + 1)
		if pos == -1:
			return last_pos
		last_pos = pos
print find_last('aaaa', 'a')



def stamps(value):
    five_p = value/5
    if type(five_p) == "float":
        five_p = five_p[:five_p.find(".")]
    value = value - 5*five_p
    two_p = value/2
    if type( two_p) == "float":
         two_p =  two_p[:two_p.find(".")]
    value = value - 2*two_p
    one_p = value
    return (five_p, two_p, one_p)
print stamps(8)



def set_range(a,b,c):
    return max(a,b,c)-min(a,b,c)




###################   
# 
# def get_page(url):
# 	try:
# 	    import urllib
# 	    return urllib.urlopen(url).read()
# 
# 	except:
# 	    return "error"
# 
# words = get_page('http://anthonyfleming.net')
# print words
# 
# 
# 
# 
# def get_next_target (page):
# 	start_link = page.find('<a href=')
# 	if start_link == -1:
# 		return None, 0
# 	start_quote = page.find('"', start_link)
# 	end_quote = page.find('"', start_quote + 1)
# 	url = page[start_quote + 1:end_quote]
# 	return url, end_quote
# 
# url, endpos = get_next_target('blablabla <a href="http://visiticeland.com">English</a></li>')
# print url
# 
# def print_all_links(page):
# 	while True:
# 		url, endpos = get_next_target(page)
# 		if url:
# 			print url
# 			page = page[endpos:]
# 		else:
# 			break
# 
# print_all_links(get_page('http://xkcd.com/830)/'))
# 

#################################################



# 3 How to Manage Data
# 4 Responding to Queries
# 5 How Programs Run
# 6 How to Have Infinite Power