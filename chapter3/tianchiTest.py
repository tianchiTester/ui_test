import wqrfnium

wqrfnium

class _const:
    class ConstError(TypeError):pass
    def __setattr__(this,name,value):
        if name in this.__dict__:
            raise this.ConstError("Can't rebind const (%s)" %name)
        self.__dict__[name]=value

    def a(self,s:str):

        for s in ['1','2']:
            print(s)



