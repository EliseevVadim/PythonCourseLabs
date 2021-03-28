from classes.stringTools import StringFormatter
s=StringFormatter('your password abcdef12345 is not safe')
s.delete_short_words(5)
s.replace_digits_by_stars()
s.sort_in_lexis_order()
s.insert_spaces()
print(s.line)