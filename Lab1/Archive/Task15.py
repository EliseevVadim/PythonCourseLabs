def pre_process(a = 0.97):
    def _decorator(function):
        def _wrapper(s):
            for i in range(len(s)):
                s[i] = s[i] - a*s[i-1]
            function(s)
        return _wrapper
    return _decorator
@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)
s=[1, 2, 3, 4, 5]
plot_signal(s)
input("Press Enter to continue...")    