class People:
    country='China'
    def __init__(self,name):
        self.name=name

    def people_info(self):
        print('%s is xxx' %(self.name))

obj=People('aaa')

print(hasattr(People,'country'))
#返回值：True
print('country' in People.__dict__)
#返回值：True
print(hasattr(obj,'people_info'))
#返回值：True
print(People.__dict__)

class Foo:
    def run(self):
        while True:
            cmd=input('cmd>>: ').strip()
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func()

    def download(self):
        print('download....')

    def upload(self):
        print('upload...')

obj=Foo()
obj.run()