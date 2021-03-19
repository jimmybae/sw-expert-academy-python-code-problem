a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
b = 'aeiou'
re = [c for c in a if b.find(c) == -1]
print(''.join(re))