import abc
class Taggable:
    __metaclass__=abc.ABCMeta()
    




class Book(object):
    #__slots__=['__name', '__author', '__code']
    def __init__(self, author, name):
        if name is None or author is None or name=='' or author=='':
            raise ValueError
        self.__author=author
        self.__name=name        
        self.__code=0
    def __str__(self):
        return('[{}] {} \'{}\''.format(self.__code, self.__author, self.__name))
        
        
        
        
        
        
        
        
        
        
        
        
class Library(object):
    Books_code=0
    def __init__(self, code, address):
        self.__code=code
        self.__address=address
        self.__books=[]
    def append(self, Book):
        self.__class__.Books_code+=1
        Book.__code=self.__class__.Books_code
        self.__books.append(Book)
        print('added')
        return self
    def __iadd__(self, Book):
        self.__class__.Books_code+=1
        Book.__code=self.__class__.Books_code
        self.__books.append(Book)
        print('added')
        return self
    def __iter__(self):
        pass
