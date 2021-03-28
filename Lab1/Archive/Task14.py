def non_empty(function):
    def _wrapper():
        res = [i for i in function() if (not i=='' and i is not None)]
        return res
    return _wrapper
@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']
print(get_pages())
input("Press Enter to continue...")