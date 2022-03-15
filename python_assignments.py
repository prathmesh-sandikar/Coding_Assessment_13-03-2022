# WAP to test whether an input is integer or not.
input = input("Enter the input ")
print(input.isnumeric())


# WAP to display unique words from the string.
a = 'Hi this is prathmesh here prathmesh is'
b = []

for x in a.split():
    if x not in b:
        b.append(x)

print(b)


# WAP to accept a string and replace all spaces by # symbol.
string=input("Enter string:")
string=string.replace(' ','#')
print("Updated string:")
print(string)


# WAP to accept a string and count the frequency of each vowel.


vowels = 'aeiou'

ip_str = 'How Are You?'

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


# WAP to display the smallest and largest word from the string
text = input("Enter the String: ")
text = text.split()
bigWordLen = 0

for wrd in text:
  wrdLen = len(wrd)
  if wrdLen>bigWordLen:
    bigWordLen = wrdLen

print("\nLargest Word: ")
for wrd in text:
  wrdLen = len(wrd)
  if wrdLen==bigWordLen:
    print(wrd)



# WAP to sort a list in ascending and descending order.
My_list = [1,56,25,78,65,37]

My_list.sort()
print("Ascending Ordered List is:",My_list)
My_list.sort(reverse=True)
print("Descending Ordered List is:",My_list)



# WAP to add a key to a Dictionary.
d = {'1:25','2:45'}
print(d)
d.update({'name:bob'})
print(d)



# WAP to remove duplicates from a list.
My_list = [25,45,65,45,25]
print(list(set(My_list)))




# WAP to display the largest word from the String.
sentence = input("Enter sentence: ")
longest = max(sentence.split())
print("Largest word is: ", longest)


# write
# a
# function
# to
# compute
# the
# frequency
# of
# the
# words
# from the input.The
# output
# should
# output
# after
# sorting
# the
# key
# alphanumerically.
# example: input is
# "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
# Then, the
# output
# should
# be:
# 2: 2
# 3.: 1
# 3?:1
# New: 1
# Python: 5
# Read: 1
# and:1
# between: 1
# choosing: 1
# or:2
# to: 1




def frequency(input):
    freq = {}
    for word in input.split():
        freq[word] = freq.get(word, 0) + 1
    words = list(freq.keys())
    words.sort()
    for w in words:
        print(f'{w}:{freq[w]}')


str = input('enter string: ')
frequency(str)



# Write
# a
# Python
# program
# to
# calculate
# the
# length
# of
# a
# string

string1 = input('Enter the String :')
count = 0
for i in string1:
    count += 1
print(count)



# Write
# a
# Python
# function
# that
# checks
# whether
# a
# passed
# string is palindrome or not.


string = input().lower()
if string == string[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")





