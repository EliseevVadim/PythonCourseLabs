class StringFormatter(object):
    def __init__(self, line, splitter=' '):
        self.__line=line
        self.__splitter=splitter
    def delete_short_words(self, minsize):
        s=' '
        s=s.join([x for x in self.__line.split(' ') if len(x)>minsize])
        self.__line=s
        return self.__line
    def replace_digits_by_stars(self):
        newline=self.__splitter
        for letter in self.__line:
           if letter.isdigit():
               letter='*'
           newline+=letter 
        self.__line=newline
        return self.__line
    def insert_spaces(self):
        mas=self.__line.split(self.__splitter)
        self.__line=''
        for word in mas:
            for letter in word:
                self.__line+=letter+' '
        return self.__line     
    def sort_by_size(self):
        s=self.__line.split(self.__splitter)
        s.sort(key=len)
        self.__line=' '.join(s)
        return self.__line
    def sort_in_lexis_order(self):
        s=self.__line.split(self.__splitter)
        s.sort(key=str.lower)
        self.__line=' '.join(s)
        return self.__line
    @property
    def line(self):
        return self.__line