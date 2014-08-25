def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

print "frange(0.6, 0.7, 0.1)"
for i in frange(0.6, 0.7, 0.1):
    print(i)
print ""

# Expected output for this is:
# 0.5
# 0.6
# 0.7
# We do NOT get the expected output when executed, instead we get:
# 0.5
# 0.6
# 0.7
# 0.8
print "frange(0.5, 0.8, 0.1)"
for i in frange(0.5, 0.8, 0.1):
    print(i)
print ""

# Expected output for this is:
# 0.5
# 0.6
# We get the expected output when executed.
print "frange(0.5, 0.7, 0.1)"
for i in frange(0.5, 0.7, 0.1):
    print(i)
print ""

