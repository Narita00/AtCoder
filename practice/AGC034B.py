s = str(input())

count = 0

while s.count("ABC") != 0:
    count += s.count("ABC")
    s = s.replace("ABC", "BCA")
print(count)