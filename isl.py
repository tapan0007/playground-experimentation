import js

class Error(Exception):
    pass

class Context:
    defaultInstance = None

    def __init__(self):
        retType = 'number'
        argTypes = []
        args = []
        ptr = js.globals.Module.ccall('isl_ctx_alloc', retType, argTypes, args)
        self.ptr = ptr

    def __del__(self):
        retType = None
        argTypes = [number]
        args = [self.ptr]
        ptr = js.globals.Module.ccall('isl_ctx_free', retType, argTypes, args)
        isl.isl_ctx_free(self)

    def from_param(self):
        return self.ptr

    @staticmethod
    def getDefaultInstance():
        if Context.defaultInstance == None:
            Context.defaultInstance = Context()
        return Context.defaultInstance
