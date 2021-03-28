def string_proc(lines):
    for i in lines:
        if i.startswith('www'):
            i = 'http://' + i
            if not i.endswith('.com'):
                i+='.com'
            yield i
lines = ['nothing', 'wwwfgdfd', 'WWWghjd.com', 'http://www.normline.com', 'www.tx.com']
out = [i for i in string_proc(lines)]
print(out)
input("Press Enter to continue...")