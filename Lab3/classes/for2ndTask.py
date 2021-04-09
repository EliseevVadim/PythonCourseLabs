import abc
class Taggable:
    __metaclass__=abc.ABCMeta
    
    @abc.abstractmethod
    def tag(self):
        raise NotImplementedError


class Book(Taggable):
    def __init__(self, author, name):
        if name is None or author is None or name=='' or author=='':
            raise ValueError
        self.__author=author
        self.__name=name        
        self.__code=0
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code):
        self.__code=code
    def __str__(self):
        return('[{}] {} \'{}\''.format(self.__code, self.__author, self.__name))
    def tag(self):
        return [word for word in self.__name.split(' ') if word.istitle()]

        
class Library(object):
    Books_code=0
    def __init__(self, code, address):
        self.__code=code
        self.__address=address
        self.__books=[]
        self.__idx=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__idx<len(self.__books):            
            self.__idx+=1
            return self.__books[self.__idx-1]
        else:
            raise StopIteration
    def __iadd__(self, other:Book):
        self.Books_code+=1
        other.code=self.Books_code
        self.__books.append(other)
        return self