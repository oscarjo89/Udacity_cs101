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