def make_readable(seconds):
    secs = seconds % 60
    minutes = (seconds - secs) % 3600
    hours = (seconds - minutes) // 3600
    return f"{hours:02d}:{minutes//60:02d}:{secs:02d}"


test1 = 5
test2 = 60
test3 = 86399
test4 = 359999
data = make_readable(test3)
print(data)