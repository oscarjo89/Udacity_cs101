#	Intro to Computer Science
#	Build a Search Engine & a Social Network
#	https://www.udacity.com/course/intro-to-computer-science--cs101
	
	
#Lesson 1	Write your first computer program
#	Sergey Brin's advice on learning to program.
#	Get started on your first Python program.
#	How to create and use variables in Python.
#Lesson 2	Write programs to do repeating work
#	Introducing procedures.
#	Sum procedure with a return statement.
#	Equality comparisons and more.
#Lesson 3	How ot manage data
#	Nested lists.
#	A list of strings.
#	Aliasing and more.
#Lesson 4	Responding to queries
#	Data structures.
#	Lookup.
#	Building the Web Index and more.
#Lesson 5	How programs run
#	Measuring speed.
#	Spin loop.
#	Index size vs. time and more.
#Lesson 6	How to have infinite power
#	Infinite power.
#	Counter.
#	Recursive definitions and more.

#####################################################
# Lesson 1	Write your first computer program

# This course will introduce you to the fundemental ideas of computing, and teach you to read and write your own programs. We are going to do this in the context of building a web search engine.

# Computer science is about how to solve problems by breaking them up into smaller pieces. And then preciely and mechanically describing a sequence of steps to execute in order to solve these pieces. And these steps can be preformed by a computer.

# Build a search engine
# - Find data (web crawler) Units- 1-3
# - Building an index (respond to search quieries) - Units 4-5
# - Rank pages (to get best result) - Units 6

# Unit 1 Getting started - extracting the first link
# Web crawler, start with one page (seed?) follow links, get many pages
# A webpage is a text, a link is a special sequence of text

print 3
print 2+3

# Bakus Naur Form, derivation: Non-terminal -> replacement
# Grace Hopper and Augusta Ada King

s = 'audacity'
print "U" + s[2:]

# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
print start_link

end_link = page.find('"', start_link+9)
print end_link

url = page[(start_link+9):end_link]
print url


###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

marker_start = line.find(marker)
marker_end = line.find(marker) + len(marker)

replaced = line[:marker_start] + replacement + line[marker_end:]
print replaced

# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###

marker_start = line.find(marker)
marker_end = line.find(marker) + len(marker)

replaced = line[:marker_start] + replacement + line[marker_end:]

print replaced
# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.


#####################################################
# Lesson 2	Write programs to do repeating work

# Procedures, like functions in R. Inputs -> Procedure -> Outputs
# Control

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
print start_link

end_link = page.find('"', start_link+9)
print end_link

url = page[(start_link+9):end_link]
print url

# Procedures



#####################################################
# Lesson 3	How ot manage data

#####################################################
# Lesson 4	Responding to queries

#####################################################
# Lesson 5	How programs run

#####################################################
# Lesson 6	How to have infinite power

