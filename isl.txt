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

class isl:
    def __init__(self):
	self.foo = True

class union_pw_multi_aff:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_multi_aff_read_from_str(self.ctx, args[0])
            return
        if len(args) == 1 and args[0].__class__ is union_pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_multi_aff_from_union_pw_aff(isl.isl_union_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is pw_multi_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_multi_aff_from_pw_multi_aff(isl.isl_pw_multi_aff_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_pw_multi_aff_free(self.ptr)
    def __str__(self):
        return str(isl.isl_union_pw_multi_aff_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_pw_multi_aff("""%s""")' % s
        else:
            return 'isl.union_pw_multi_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_multi_aff:
                arg0 = union_pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_multi_aff:
                arg1 = union_pw_multi_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_pw_multi_aff_add(isl.isl_union_pw_multi_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
        return union_pw_multi_aff(ctx=ctx, ptr=res)
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_multi_aff:
                arg0 = union_pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_multi_aff:
                arg1 = union_pw_multi_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_pw_multi_aff_flat_range_product(isl.isl_union_pw_multi_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
        return union_pw_multi_aff(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_union_pw_multi_aff_pullback_union_pw_multi_aff(isl.isl_union_pw_multi_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            return union_pw_multi_aff(ctx=arg0.ctx, ptr=res)
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_multi_aff:
                arg0 = union_pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_multi_aff:
                arg1 = union_pw_multi_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_pw_multi_aff_union_add(isl.isl_union_pw_multi_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
        return union_pw_multi_aff(ctx=ctx, ptr=res)

@staticmethod
def isl_union_pw_multi_aff_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_read_from_str', retType, argTypes, args)
isl.isl_union_pw_multi_aff_read_from_str = isl_union_pw_multi_aff_read_from_str
@staticmethod
def isl_union_pw_multi_aff_from_union_pw_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_from_union_pw_aff', retType, argTypes, args)
isl.isl_union_pw_multi_aff_from_union_pw_aff = isl_union_pw_multi_aff_from_union_pw_aff
@staticmethod
def isl_union_pw_multi_aff_from_pw_multi_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_from_pw_multi_aff', retType, argTypes, args)
isl.isl_union_pw_multi_aff_from_pw_multi_aff = isl_union_pw_multi_aff_from_pw_multi_aff
@staticmethod
def isl_union_pw_multi_aff_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_add', retType, argTypes, args)
isl.isl_union_pw_multi_aff_add = isl_union_pw_multi_aff_add
@staticmethod
def isl_union_pw_multi_aff_flat_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_flat_range_product', retType, argTypes, args)
isl.isl_union_pw_multi_aff_flat_range_product = isl_union_pw_multi_aff_flat_range_product
@staticmethod
def isl_union_pw_multi_aff_pullback_union_pw_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_pullback_union_pw_multi_aff', retType, argTypes, args)
isl.isl_union_pw_multi_aff_pullback_union_pw_multi_aff = isl_union_pw_multi_aff_pullback_union_pw_multi_aff
@staticmethod
def isl_union_pw_multi_aff_union_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_union_add', retType, argTypes, args)
isl.isl_union_pw_multi_aff_union_add = isl_union_pw_multi_aff_union_add
@staticmethod
def isl_union_pw_multi_aff_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_union_pw_multi_aff_free', retType, argTypes, args)
isl.isl_union_pw_multi_aff_free = isl_union_pw_multi_aff_free
@staticmethod
def isl_union_pw_multi_aff_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_to_str', retType, argTypes, args)
isl.isl_union_pw_multi_aff_to_str = isl_union_pw_multi_aff_to_str
@staticmethod
def isl_union_pw_multi_aff_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_pw_multi_aff_copy', retType, argTypes, args)
isl.isl_union_pw_multi_aff_copy = isl_union_pw_multi_aff_copy

class multi_union_pw_aff:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is union_pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_union_pw_aff_from_union_pw_aff(isl.isl_union_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is multi_pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_union_pw_aff_from_multi_pw_aff(isl.isl_multi_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_union_pw_aff_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_multi_union_pw_aff_free(self.ptr)
    def __str__(self):
        return str(isl.isl_multi_union_pw_aff_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.multi_union_pw_aff("""%s""")' % s
        else:
            return 'isl.multi_union_pw_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_union_pw_aff_add(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        return multi_union_pw_aff(ctx=ctx, ptr=res)
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_union_pw_aff_flat_range_product(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        return multi_union_pw_aff(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_multi_union_pw_aff_pullback_union_pw_multi_aff(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            return multi_union_pw_aff(ctx=arg0.ctx, ptr=res)
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_union_pw_aff_range_product(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        return multi_union_pw_aff(ctx=ctx, ptr=res)
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_union_pw_aff:
                arg0 = multi_union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_union_pw_aff:
                arg1 = multi_union_pw_aff(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_union_pw_aff_union_add(isl.isl_multi_union_pw_aff_copy(arg0.ptr), isl.isl_multi_union_pw_aff_copy(arg1.ptr))
        return multi_union_pw_aff(ctx=ctx, ptr=res)

@staticmethod
def isl_multi_union_pw_aff_from_union_pw_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_from_union_pw_aff', retType, argTypes, args)
isl.isl_multi_union_pw_aff_from_union_pw_aff = isl_multi_union_pw_aff_from_union_pw_aff
@staticmethod
def isl_multi_union_pw_aff_from_multi_pw_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_from_multi_pw_aff', retType, argTypes, args)
isl.isl_multi_union_pw_aff_from_multi_pw_aff = isl_multi_union_pw_aff_from_multi_pw_aff
@staticmethod
def isl_multi_union_pw_aff_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_read_from_str', retType, argTypes, args)
isl.isl_multi_union_pw_aff_read_from_str = isl_multi_union_pw_aff_read_from_str
@staticmethod
def isl_multi_union_pw_aff_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_add', retType, argTypes, args)
isl.isl_multi_union_pw_aff_add = isl_multi_union_pw_aff_add
@staticmethod
def isl_multi_union_pw_aff_flat_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_flat_range_product', retType, argTypes, args)
isl.isl_multi_union_pw_aff_flat_range_product = isl_multi_union_pw_aff_flat_range_product
@staticmethod
def isl_multi_union_pw_aff_pullback_union_pw_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_pullback_union_pw_multi_aff', retType, argTypes, args)
isl.isl_multi_union_pw_aff_pullback_union_pw_multi_aff = isl_multi_union_pw_aff_pullback_union_pw_multi_aff
@staticmethod
def isl_multi_union_pw_aff_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_range_product', retType, argTypes, args)
isl.isl_multi_union_pw_aff_range_product = isl_multi_union_pw_aff_range_product
@staticmethod
def isl_multi_union_pw_aff_union_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_union_add', retType, argTypes, args)
isl.isl_multi_union_pw_aff_union_add = isl_multi_union_pw_aff_union_add
@staticmethod
def isl_multi_union_pw_aff_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_multi_union_pw_aff_free', retType, argTypes, args)
isl.isl_multi_union_pw_aff_free = isl_multi_union_pw_aff_free
@staticmethod
def isl_multi_union_pw_aff_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_to_str', retType, argTypes, args)
isl.isl_multi_union_pw_aff_to_str = isl_multi_union_pw_aff_to_str
@staticmethod
def isl_multi_union_pw_aff_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_union_pw_aff_copy', retType, argTypes, args)
isl.isl_multi_union_pw_aff_copy = isl_multi_union_pw_aff_copy

class union_pw_aff(union_pw_multi_aff, multi_union_pw_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_aff_from_pw_aff(isl.isl_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_pw_aff_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_pw_aff_free(self.ptr)
    def __str__(self):
        return str(isl.isl_union_pw_aff_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_pw_aff("""%s""")' % s
        else:
            return 'isl.union_pw_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_aff:
                arg0 = union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_aff:
                arg1 = union_pw_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_union_pw_aff_add(isl.isl_union_pw_aff_copy(arg0.ptr), isl.isl_union_pw_aff_copy(arg1.ptr))
        return union_pw_aff(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_union_pw_aff_pullback_union_pw_multi_aff(isl.isl_union_pw_aff_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            return union_pw_aff(ctx=arg0.ctx, ptr=res)
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is union_pw_aff:
                arg0 = union_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_pw_aff:
                arg1 = union_pw_aff(arg1)
        except:
            return union_pw_multi_aff(arg0).union_add(arg1)
        ctx = arg0.ctx
        res = isl.isl_union_pw_aff_union_add(isl.isl_union_pw_aff_copy(arg0.ptr), isl.isl_union_pw_aff_copy(arg1.ptr))
        return union_pw_aff(ctx=ctx, ptr=res)

@staticmethod
def isl_union_pw_aff_from_pw_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_pw_aff_from_pw_aff', retType, argTypes, args)
isl.isl_union_pw_aff_from_pw_aff = isl_union_pw_aff_from_pw_aff
@staticmethod
def isl_union_pw_aff_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_union_pw_aff_read_from_str', retType, argTypes, args)
isl.isl_union_pw_aff_read_from_str = isl_union_pw_aff_read_from_str
@staticmethod
def isl_union_pw_aff_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_pw_aff_add', retType, argTypes, args)
isl.isl_union_pw_aff_add = isl_union_pw_aff_add
@staticmethod
def isl_union_pw_aff_pullback_union_pw_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_pw_aff_pullback_union_pw_multi_aff', retType, argTypes, args)
isl.isl_union_pw_aff_pullback_union_pw_multi_aff = isl_union_pw_aff_pullback_union_pw_multi_aff
@staticmethod
def isl_union_pw_aff_union_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_pw_aff_union_add', retType, argTypes, args)
isl.isl_union_pw_aff_union_add = isl_union_pw_aff_union_add
@staticmethod
def isl_union_pw_aff_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_union_pw_aff_free', retType, argTypes, args)
isl.isl_union_pw_aff_free = isl_union_pw_aff_free
@staticmethod
def isl_union_pw_aff_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_pw_aff_to_str', retType, argTypes, args)
isl.isl_union_pw_aff_to_str = isl_union_pw_aff_to_str
@staticmethod
def isl_union_pw_aff_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_pw_aff_copy', retType, argTypes, args)
isl.isl_union_pw_aff_copy = isl_union_pw_aff_copy

class multi_pw_aff(multi_union_pw_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is multi_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_pw_aff_from_multi_aff(isl.isl_multi_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_pw_aff_from_pw_aff(isl.isl_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is pw_multi_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_pw_aff_from_pw_multi_aff(isl.isl_pw_multi_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_pw_aff_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_multi_pw_aff_free(self.ptr)
    def __str__(self):
        return str(isl.isl_multi_pw_aff_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.multi_pw_aff("""%s""")' % s
        else:
            return 'isl.multi_pw_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_pw_aff:
                arg1 = multi_pw_aff(arg1)
        except:
            return multi_union_pw_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_pw_aff_add(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
        return multi_pw_aff(ctx=ctx, ptr=res)
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_pw_aff:
                arg1 = multi_pw_aff(arg1)
        except:
            return multi_union_pw_aff(arg0).flat_range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_pw_aff_flat_range_product(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
        return multi_pw_aff(ctx=ctx, ptr=res)
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_pw_aff:
                arg1 = multi_pw_aff(arg1)
        except:
            return multi_union_pw_aff(arg0).product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_pw_aff_product(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
        return multi_pw_aff(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_multi_pw_aff_pullback_multi_aff(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            return multi_pw_aff(ctx=arg0.ctx, ptr=res)
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_multi_pw_aff_pullback_pw_multi_aff(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
            return multi_pw_aff(ctx=arg0.ctx, ptr=res)
        if arg1.__class__ is multi_pw_aff:
            res = isl.isl_multi_pw_aff_pullback_multi_pw_aff(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
            return multi_pw_aff(ctx=arg0.ctx, ptr=res)
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_pw_aff:
                arg0 = multi_pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_pw_aff:
                arg1 = multi_pw_aff(arg1)
        except:
            return multi_union_pw_aff(arg0).range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_pw_aff_range_product(isl.isl_multi_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
        return multi_pw_aff(ctx=ctx, ptr=res)

@staticmethod
def isl_multi_pw_aff_from_multi_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_pw_aff_from_multi_aff', retType, argTypes, args)
isl.isl_multi_pw_aff_from_multi_aff = isl_multi_pw_aff_from_multi_aff
@staticmethod
def isl_multi_pw_aff_from_pw_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_pw_aff_from_pw_aff', retType, argTypes, args)
isl.isl_multi_pw_aff_from_pw_aff = isl_multi_pw_aff_from_pw_aff
@staticmethod
def isl_multi_pw_aff_from_pw_multi_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_pw_aff_from_pw_multi_aff', retType, argTypes, args)
isl.isl_multi_pw_aff_from_pw_multi_aff = isl_multi_pw_aff_from_pw_multi_aff
@staticmethod
def isl_multi_pw_aff_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_multi_pw_aff_read_from_str', retType, argTypes, args)
isl.isl_multi_pw_aff_read_from_str = isl_multi_pw_aff_read_from_str
@staticmethod
def isl_multi_pw_aff_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_pw_aff_add', retType, argTypes, args)
isl.isl_multi_pw_aff_add = isl_multi_pw_aff_add
@staticmethod
def isl_multi_pw_aff_flat_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_pw_aff_flat_range_product', retType, argTypes, args)
isl.isl_multi_pw_aff_flat_range_product = isl_multi_pw_aff_flat_range_product
@staticmethod
def isl_multi_pw_aff_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_pw_aff_product', retType, argTypes, args)
isl.isl_multi_pw_aff_product = isl_multi_pw_aff_product
@staticmethod
def isl_multi_pw_aff_pullback_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_pw_aff_pullback_multi_aff', retType, argTypes, args)
isl.isl_multi_pw_aff_pullback_multi_aff = isl_multi_pw_aff_pullback_multi_aff
@staticmethod
def isl_multi_pw_aff_pullback_pw_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_pw_aff_pullback_pw_multi_aff', retType, argTypes, args)
isl.isl_multi_pw_aff_pullback_pw_multi_aff = isl_multi_pw_aff_pullback_pw_multi_aff
@staticmethod
def isl_multi_pw_aff_pullback_multi_pw_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_pw_aff_pullback_multi_pw_aff', retType, argTypes, args)
isl.isl_multi_pw_aff_pullback_multi_pw_aff = isl_multi_pw_aff_pullback_multi_pw_aff
@staticmethod
def isl_multi_pw_aff_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_pw_aff_range_product', retType, argTypes, args)
isl.isl_multi_pw_aff_range_product = isl_multi_pw_aff_range_product
@staticmethod
def isl_multi_pw_aff_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_multi_pw_aff_free', retType, argTypes, args)
isl.isl_multi_pw_aff_free = isl_multi_pw_aff_free
@staticmethod
def isl_multi_pw_aff_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_pw_aff_to_str', retType, argTypes, args)
isl.isl_multi_pw_aff_to_str = isl_multi_pw_aff_to_str
@staticmethod
def isl_multi_pw_aff_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_pw_aff_copy', retType, argTypes, args)
isl.isl_multi_pw_aff_copy = isl_multi_pw_aff_copy

class pw_multi_aff(multi_pw_aff, union_pw_multi_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is multi_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_multi_aff_from_multi_aff(isl.isl_multi_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is pw_aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_multi_aff_from_pw_aff(isl.isl_pw_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_multi_aff_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_pw_multi_aff_free(self.ptr)
    def __str__(self):
        return str(isl.isl_pw_multi_aff_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.pw_multi_aff("""%s""")' % s
        else:
            return 'isl.pw_multi_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_add(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        return pw_multi_aff(ctx=ctx, ptr=res)
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).flat_range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_flat_range_product(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        return pw_multi_aff(ctx=ctx, ptr=res)
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).product(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_product(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        return pw_multi_aff(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_pw_multi_aff_pullback_multi_aff(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            return pw_multi_aff(ctx=arg0.ctx, ptr=res)
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_pw_multi_aff_pullback_pw_multi_aff(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
            return pw_multi_aff(ctx=arg0.ctx, ptr=res)
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_range_product(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        return pw_multi_aff(ctx=ctx, ptr=res)
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is pw_multi_aff:
                arg0 = pw_multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_multi_aff:
                arg1 = pw_multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).union_add(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_multi_aff_union_add(isl.isl_pw_multi_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
        return pw_multi_aff(ctx=ctx, ptr=res)

@staticmethod
def isl_pw_multi_aff_from_multi_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_pw_multi_aff_from_multi_aff', retType, argTypes, args)
isl.isl_pw_multi_aff_from_multi_aff = isl_pw_multi_aff_from_multi_aff
@staticmethod
def isl_pw_multi_aff_from_pw_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_pw_multi_aff_from_pw_aff', retType, argTypes, args)
isl.isl_pw_multi_aff_from_pw_aff = isl_pw_multi_aff_from_pw_aff
@staticmethod
def isl_pw_multi_aff_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_pw_multi_aff_read_from_str', retType, argTypes, args)
isl.isl_pw_multi_aff_read_from_str = isl_pw_multi_aff_read_from_str
@staticmethod
def isl_pw_multi_aff_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_multi_aff_add', retType, argTypes, args)
isl.isl_pw_multi_aff_add = isl_pw_multi_aff_add
@staticmethod
def isl_pw_multi_aff_flat_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_multi_aff_flat_range_product', retType, argTypes, args)
isl.isl_pw_multi_aff_flat_range_product = isl_pw_multi_aff_flat_range_product
@staticmethod
def isl_pw_multi_aff_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_multi_aff_product', retType, argTypes, args)
isl.isl_pw_multi_aff_product = isl_pw_multi_aff_product
@staticmethod
def isl_pw_multi_aff_pullback_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_multi_aff_pullback_multi_aff', retType, argTypes, args)
isl.isl_pw_multi_aff_pullback_multi_aff = isl_pw_multi_aff_pullback_multi_aff
@staticmethod
def isl_pw_multi_aff_pullback_pw_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_multi_aff_pullback_pw_multi_aff', retType, argTypes, args)
isl.isl_pw_multi_aff_pullback_pw_multi_aff = isl_pw_multi_aff_pullback_pw_multi_aff
@staticmethod
def isl_pw_multi_aff_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_multi_aff_range_product', retType, argTypes, args)
isl.isl_pw_multi_aff_range_product = isl_pw_multi_aff_range_product
@staticmethod
def isl_pw_multi_aff_union_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_multi_aff_union_add', retType, argTypes, args)
isl.isl_pw_multi_aff_union_add = isl_pw_multi_aff_union_add
@staticmethod
def isl_pw_multi_aff_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_pw_multi_aff_free', retType, argTypes, args)
isl.isl_pw_multi_aff_free = isl_pw_multi_aff_free
@staticmethod
def isl_pw_multi_aff_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_pw_multi_aff_to_str', retType, argTypes, args)
isl.isl_pw_multi_aff_to_str = isl_pw_multi_aff_to_str
@staticmethod
def isl_pw_multi_aff_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_pw_multi_aff_copy', retType, argTypes, args)
isl.isl_pw_multi_aff_copy = isl_pw_multi_aff_copy

class pw_aff(union_pw_aff, multi_pw_aff, pw_multi_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_aff_from_aff(isl.isl_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_pw_aff_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_pw_aff_free(self.ptr)
    def __str__(self):
        return str(isl.isl_pw_aff_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.pw_aff("""%s""")' % s
        else:
            return 'isl.pw_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_add(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        return pw_aff(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_pw_aff_pullback_multi_aff(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            return pw_aff(ctx=arg0.ctx, ptr=res)
        if arg1.__class__ is pw_multi_aff:
            res = isl.isl_pw_aff_pullback_pw_multi_aff(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_multi_aff_copy(arg1.ptr))
            return pw_aff(ctx=arg0.ctx, ptr=res)
        if arg1.__class__ is multi_pw_aff:
            res = isl.isl_pw_aff_pullback_multi_pw_aff(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_multi_pw_aff_copy(arg1.ptr))
            return pw_aff(ctx=arg0.ctx, ptr=res)
    def union_add(arg0, arg1):
        try:
            if not arg0.__class__ is pw_aff:
                arg0 = pw_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is pw_aff:
                arg1 = pw_aff(arg1)
        except:
            return union_pw_aff(arg0).union_add(arg1)
        ctx = arg0.ctx
        res = isl.isl_pw_aff_union_add(isl.isl_pw_aff_copy(arg0.ptr), isl.isl_pw_aff_copy(arg1.ptr))
        return pw_aff(ctx=ctx, ptr=res)

@staticmethod
def isl_pw_aff_from_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_pw_aff_from_aff', retType, argTypes, args)
isl.isl_pw_aff_from_aff = isl_pw_aff_from_aff
@staticmethod
def isl_pw_aff_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_pw_aff_read_from_str', retType, argTypes, args)
isl.isl_pw_aff_read_from_str = isl_pw_aff_read_from_str
@staticmethod
def isl_pw_aff_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_aff_add', retType, argTypes, args)
isl.isl_pw_aff_add = isl_pw_aff_add
@staticmethod
def isl_pw_aff_pullback_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_aff_pullback_multi_aff', retType, argTypes, args)
isl.isl_pw_aff_pullback_multi_aff = isl_pw_aff_pullback_multi_aff
@staticmethod
def isl_pw_aff_pullback_pw_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_aff_pullback_pw_multi_aff', retType, argTypes, args)
isl.isl_pw_aff_pullback_pw_multi_aff = isl_pw_aff_pullback_pw_multi_aff
@staticmethod
def isl_pw_aff_pullback_multi_pw_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_aff_pullback_multi_pw_aff', retType, argTypes, args)
isl.isl_pw_aff_pullback_multi_pw_aff = isl_pw_aff_pullback_multi_pw_aff
@staticmethod
def isl_pw_aff_union_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_pw_aff_union_add', retType, argTypes, args)
isl.isl_pw_aff_union_add = isl_pw_aff_union_add
@staticmethod
def isl_pw_aff_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_pw_aff_free', retType, argTypes, args)
isl.isl_pw_aff_free = isl_pw_aff_free
@staticmethod
def isl_pw_aff_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_pw_aff_to_str', retType, argTypes, args)
isl.isl_pw_aff_to_str = isl_pw_aff_to_str
@staticmethod
def isl_pw_aff_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_pw_aff_copy', retType, argTypes, args)
isl.isl_pw_aff_copy = isl_pw_aff_copy

class multi_aff(multi_pw_aff, pw_multi_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is aff:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_aff_from_aff(isl.isl_aff_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_multi_aff_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_multi_aff_free(self.ptr)
    def __str__(self):
        return str(isl.isl_multi_aff_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.multi_aff("""%s""")' % s
        else:
            return 'isl.multi_aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_aff:
                arg1 = multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_aff_add(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
        return multi_aff(ctx=ctx, ptr=res)
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_aff:
                arg1 = multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).flat_range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_aff_flat_range_product(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
        return multi_aff(ctx=ctx, ptr=res)
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_aff:
                arg1 = multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_aff_product(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
        return multi_aff(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_multi_aff_pullback_multi_aff(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            return multi_aff(ctx=arg0.ctx, ptr=res)
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_aff:
                arg0 = multi_aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_aff:
                arg1 = multi_aff(arg1)
        except:
            return multi_pw_aff(arg0).range_product(arg1)
        ctx = arg0.ctx
        res = isl.isl_multi_aff_range_product(isl.isl_multi_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
        return multi_aff(ctx=ctx, ptr=res)

@staticmethod
def isl_multi_aff_from_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_aff_from_aff', retType, argTypes, args)
isl.isl_multi_aff_from_aff = isl_multi_aff_from_aff
@staticmethod
def isl_multi_aff_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_multi_aff_read_from_str', retType, argTypes, args)
isl.isl_multi_aff_read_from_str = isl_multi_aff_read_from_str
@staticmethod
def isl_multi_aff_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_aff_add', retType, argTypes, args)
isl.isl_multi_aff_add = isl_multi_aff_add
@staticmethod
def isl_multi_aff_flat_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_aff_flat_range_product', retType, argTypes, args)
isl.isl_multi_aff_flat_range_product = isl_multi_aff_flat_range_product
@staticmethod
def isl_multi_aff_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_aff_product', retType, argTypes, args)
isl.isl_multi_aff_product = isl_multi_aff_product
@staticmethod
def isl_multi_aff_pullback_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_aff_pullback_multi_aff', retType, argTypes, args)
isl.isl_multi_aff_pullback_multi_aff = isl_multi_aff_pullback_multi_aff
@staticmethod
def isl_multi_aff_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_aff_range_product', retType, argTypes, args)
isl.isl_multi_aff_range_product = isl_multi_aff_range_product
@staticmethod
def isl_multi_aff_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_multi_aff_free', retType, argTypes, args)
isl.isl_multi_aff_free = isl_multi_aff_free
@staticmethod
def isl_multi_aff_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_aff_to_str', retType, argTypes, args)
isl.isl_multi_aff_to_str = isl_multi_aff_to_str
@staticmethod
def isl_multi_aff_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_aff_copy', retType, argTypes, args)
isl.isl_multi_aff_copy = isl_multi_aff_copy

class aff(pw_aff, multi_aff):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_aff_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_aff_free(self.ptr)
    def __str__(self):
        return str(isl.isl_aff_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.aff("""%s""")' % s
        else:
            return 'isl.aff("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is aff:
                arg0 = aff(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return pw_aff(arg0).add(arg1)
        ctx = arg0.ctx
        res = isl.isl_aff_add(isl.isl_aff_copy(arg0.ptr), isl.isl_aff_copy(arg1.ptr))
        return aff(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is multi_aff:
            res = isl.isl_aff_pullback_multi_aff(isl.isl_aff_copy(arg0.ptr), isl.isl_multi_aff_copy(arg1.ptr))
            return aff(ctx=arg0.ctx, ptr=res)

@staticmethod
def isl_aff_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_aff_read_from_str', retType, argTypes, args)
isl.isl_aff_read_from_str = isl_aff_read_from_str
@staticmethod
def isl_aff_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_aff_add', retType, argTypes, args)
isl.isl_aff_add = isl_aff_add
@staticmethod
def isl_aff_pullback_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_aff_pullback_multi_aff', retType, argTypes, args)
isl.isl_aff_pullback_multi_aff = isl_aff_pullback_multi_aff
@staticmethod
def isl_aff_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_aff_free', retType, argTypes, args)
isl.isl_aff_free = isl_aff_free
@staticmethod
def isl_aff_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_aff_to_str', retType, argTypes, args)
isl.isl_aff_to_str = isl_aff_to_str
@staticmethod
def isl_aff_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_aff_copy', retType, argTypes, args)
isl.isl_aff_copy = isl_aff_copy

class union_map:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is basic_map:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_map_from_basic_map(isl.isl_basic_map_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is map:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_map_from_map(isl.isl_map_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_map_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_map_free(self.ptr)
    def __str__(self):
        return str(isl.isl_union_map_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_map("""%s""")' % s
        else:
            return 'isl.union_map("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_affine_hull(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def apply_domain(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_apply_domain(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def apply_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_apply_range(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def coalesce(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_coalesce(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def compute_divs(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_compute_divs(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def deltas(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_deltas(isl.isl_union_map_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_detect_equalities(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def domain(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain(isl.isl_union_map_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def domain_factor_domain(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_factor_domain(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def domain_factor_range(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_factor_range(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def domain_map(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_map(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def domain_map_union_pw_multi_aff(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_map_union_pw_multi_aff(isl.isl_union_map_copy(arg0.ptr))
        return union_pw_multi_aff(ctx=ctx, ptr=res)
    def domain_product(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_domain_product(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def factor_domain(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_factor_domain(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def factor_range(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_factor_range(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def fixed_power(arg0, arg1):
        if arg1.__class__ is val:
            res = isl.isl_union_map_fixed_power_val(isl.isl_union_map_copy(arg0.ptr), isl.isl_val_copy(arg1.ptr))
            return union_map(ctx=arg0.ctx, ptr=res)
    def foreach_map(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = map(ctx=arg0.ctx, ptr=cb_arg0)
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_map_foreach_map(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise exc_info[0][0], exc_info[0][1], exc_info[0][2]
        return res
    @staticmethod
    def convert_from(arg0):
        if arg0.__class__ is union_pw_multi_aff:
            res = isl.isl_union_map_from_union_pw_multi_aff(isl.isl_union_pw_multi_aff_copy(arg0.ptr))
            return union_map(ctx=arg0.ctx, ptr=res)
        if arg0.__class__ is multi_union_pw_aff:
            res = isl.isl_union_map_from_multi_union_pw_aff(isl.isl_multi_union_pw_aff_copy(arg0.ptr))
            return union_map(ctx=arg0.ctx, ptr=res)
    @staticmethod
    def from_domain_and_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_from_domain_and_range(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_gist(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def gist_domain(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_gist_domain(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def gist_params(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_gist_params(isl.isl_union_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def gist_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_gist_range(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_intersect(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def intersect_domain(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_intersect_domain(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_intersect_params(isl.isl_union_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def intersect_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_intersect_range(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def is_bijective(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_bijective(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_injective(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_injective(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_single_valued(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_single_valued(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_strict_subset(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_strict_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_lexmax(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def lexmin(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_lexmin(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def polyhedral_hull(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_polyhedral_hull(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_product(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def range(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range(isl.isl_union_map_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def range_factor_domain(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range_factor_domain(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def range_factor_range(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range_factor_range(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def range_map(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range_map(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_range_product(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def reverse(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_reverse(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def subtract(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_subtract(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def subtract_domain(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_subtract_domain(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def subtract_range(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_subtract_range(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_union(isl.isl_union_map_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_map(ctx=ctx, ptr=res)
    def wrap(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_wrap(isl.isl_union_map_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def zip(arg0):
        try:
            if not arg0.__class__ is union_map:
                arg0 = union_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_map_zip(isl.isl_union_map_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)

@staticmethod
def isl_union_map_from_basic_map(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_from_basic_map', retType, argTypes, args)
isl.isl_union_map_from_basic_map = isl_union_map_from_basic_map
@staticmethod
def isl_union_map_from_map(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_from_map', retType, argTypes, args)
isl.isl_union_map_from_map = isl_union_map_from_map
@staticmethod
def isl_union_map_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_union_map_read_from_str', retType, argTypes, args)
isl.isl_union_map_read_from_str = isl_union_map_read_from_str
@staticmethod
def isl_union_map_affine_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_affine_hull', retType, argTypes, args)
isl.isl_union_map_affine_hull = isl_union_map_affine_hull
@staticmethod
def isl_union_map_apply_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_apply_domain', retType, argTypes, args)
isl.isl_union_map_apply_domain = isl_union_map_apply_domain
@staticmethod
def isl_union_map_apply_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_apply_range', retType, argTypes, args)
isl.isl_union_map_apply_range = isl_union_map_apply_range
@staticmethod
def isl_union_map_coalesce(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_coalesce', retType, argTypes, args)
isl.isl_union_map_coalesce = isl_union_map_coalesce
@staticmethod
def isl_union_map_compute_divs(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_compute_divs', retType, argTypes, args)
isl.isl_union_map_compute_divs = isl_union_map_compute_divs
@staticmethod
def isl_union_map_deltas(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_deltas', retType, argTypes, args)
isl.isl_union_map_deltas = isl_union_map_deltas
@staticmethod
def isl_union_map_detect_equalities(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_detect_equalities', retType, argTypes, args)
isl.isl_union_map_detect_equalities = isl_union_map_detect_equalities
@staticmethod
def isl_union_map_domain(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_domain', retType, argTypes, args)
isl.isl_union_map_domain = isl_union_map_domain
@staticmethod
def isl_union_map_domain_factor_domain(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_domain_factor_domain', retType, argTypes, args)
isl.isl_union_map_domain_factor_domain = isl_union_map_domain_factor_domain
@staticmethod
def isl_union_map_domain_factor_range(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_domain_factor_range', retType, argTypes, args)
isl.isl_union_map_domain_factor_range = isl_union_map_domain_factor_range
@staticmethod
def isl_union_map_domain_map(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_domain_map', retType, argTypes, args)
isl.isl_union_map_domain_map = isl_union_map_domain_map
@staticmethod
def isl_union_map_domain_map_union_pw_multi_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_domain_map_union_pw_multi_aff', retType, argTypes, args)
isl.isl_union_map_domain_map_union_pw_multi_aff = isl_union_map_domain_map_union_pw_multi_aff
@staticmethod
def isl_union_map_domain_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_domain_product', retType, argTypes, args)
isl.isl_union_map_domain_product = isl_union_map_domain_product
@staticmethod
def isl_union_map_factor_domain(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_factor_domain', retType, argTypes, args)
isl.isl_union_map_factor_domain = isl_union_map_factor_domain
@staticmethod
def isl_union_map_factor_range(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_factor_range', retType, argTypes, args)
isl.isl_union_map_factor_range = isl_union_map_factor_range
@staticmethod
def isl_union_map_fixed_power_val(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_fixed_power_val', retType, argTypes, args)
isl.isl_union_map_fixed_power_val = isl_union_map_fixed_power_val
@staticmethod
def isl_union_map_foreach_map(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_foreach_map', retType, argTypes, args)
isl.isl_union_map_foreach_map = isl_union_map_foreach_map
@staticmethod
def isl_union_map_from_union_pw_multi_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_from_union_pw_multi_aff', retType, argTypes, args)
isl.isl_union_map_from_union_pw_multi_aff = isl_union_map_from_union_pw_multi_aff
@staticmethod
def isl_union_map_from_multi_union_pw_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_from_multi_union_pw_aff', retType, argTypes, args)
isl.isl_union_map_from_multi_union_pw_aff = isl_union_map_from_multi_union_pw_aff
@staticmethod
def isl_union_map_from_domain_and_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_from_domain_and_range', retType, argTypes, args)
isl.isl_union_map_from_domain_and_range = isl_union_map_from_domain_and_range
@staticmethod
def isl_union_map_gist(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_gist', retType, argTypes, args)
isl.isl_union_map_gist = isl_union_map_gist
@staticmethod
def isl_union_map_gist_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_gist_domain', retType, argTypes, args)
isl.isl_union_map_gist_domain = isl_union_map_gist_domain
@staticmethod
def isl_union_map_gist_params(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_gist_params', retType, argTypes, args)
isl.isl_union_map_gist_params = isl_union_map_gist_params
@staticmethod
def isl_union_map_gist_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_gist_range', retType, argTypes, args)
isl.isl_union_map_gist_range = isl_union_map_gist_range
@staticmethod
def isl_union_map_intersect(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_intersect', retType, argTypes, args)
isl.isl_union_map_intersect = isl_union_map_intersect
@staticmethod
def isl_union_map_intersect_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_intersect_domain', retType, argTypes, args)
isl.isl_union_map_intersect_domain = isl_union_map_intersect_domain
@staticmethod
def isl_union_map_intersect_params(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_intersect_params', retType, argTypes, args)
isl.isl_union_map_intersect_params = isl_union_map_intersect_params
@staticmethod
def isl_union_map_intersect_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_intersect_range', retType, argTypes, args)
isl.isl_union_map_intersect_range = isl_union_map_intersect_range
@staticmethod
def isl_union_map_is_bijective(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_is_bijective', retType, argTypes, args)
isl.isl_union_map_is_bijective = isl_union_map_is_bijective
@staticmethod
def isl_union_map_is_empty(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_is_empty', retType, argTypes, args)
isl.isl_union_map_is_empty = isl_union_map_is_empty
@staticmethod
def isl_union_map_is_equal(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_is_equal', retType, argTypes, args)
isl.isl_union_map_is_equal = isl_union_map_is_equal
@staticmethod
def isl_union_map_is_injective(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_is_injective', retType, argTypes, args)
isl.isl_union_map_is_injective = isl_union_map_is_injective
@staticmethod
def isl_union_map_is_single_valued(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_is_single_valued', retType, argTypes, args)
isl.isl_union_map_is_single_valued = isl_union_map_is_single_valued
@staticmethod
def isl_union_map_is_strict_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_is_strict_subset', retType, argTypes, args)
isl.isl_union_map_is_strict_subset = isl_union_map_is_strict_subset
@staticmethod
def isl_union_map_is_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_is_subset', retType, argTypes, args)
isl.isl_union_map_is_subset = isl_union_map_is_subset
@staticmethod
def isl_union_map_lexmax(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_lexmax', retType, argTypes, args)
isl.isl_union_map_lexmax = isl_union_map_lexmax
@staticmethod
def isl_union_map_lexmin(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_lexmin', retType, argTypes, args)
isl.isl_union_map_lexmin = isl_union_map_lexmin
@staticmethod
def isl_union_map_polyhedral_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_polyhedral_hull', retType, argTypes, args)
isl.isl_union_map_polyhedral_hull = isl_union_map_polyhedral_hull
@staticmethod
def isl_union_map_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_product', retType, argTypes, args)
isl.isl_union_map_product = isl_union_map_product
@staticmethod
def isl_union_map_range(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_range', retType, argTypes, args)
isl.isl_union_map_range = isl_union_map_range
@staticmethod
def isl_union_map_range_factor_domain(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_range_factor_domain', retType, argTypes, args)
isl.isl_union_map_range_factor_domain = isl_union_map_range_factor_domain
@staticmethod
def isl_union_map_range_factor_range(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_range_factor_range', retType, argTypes, args)
isl.isl_union_map_range_factor_range = isl_union_map_range_factor_range
@staticmethod
def isl_union_map_range_map(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_range_map', retType, argTypes, args)
isl.isl_union_map_range_map = isl_union_map_range_map
@staticmethod
def isl_union_map_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_range_product', retType, argTypes, args)
isl.isl_union_map_range_product = isl_union_map_range_product
@staticmethod
def isl_union_map_reverse(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_reverse', retType, argTypes, args)
isl.isl_union_map_reverse = isl_union_map_reverse
@staticmethod
def isl_union_map_subtract(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_subtract', retType, argTypes, args)
isl.isl_union_map_subtract = isl_union_map_subtract
@staticmethod
def isl_union_map_subtract_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_subtract_domain', retType, argTypes, args)
isl.isl_union_map_subtract_domain = isl_union_map_subtract_domain
@staticmethod
def isl_union_map_subtract_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_subtract_range', retType, argTypes, args)
isl.isl_union_map_subtract_range = isl_union_map_subtract_range
@staticmethod
def isl_union_map_union(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_map_union', retType, argTypes, args)
isl.isl_union_map_union = isl_union_map_union
@staticmethod
def isl_union_map_wrap(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_wrap', retType, argTypes, args)
isl.isl_union_map_wrap = isl_union_map_wrap
@staticmethod
def isl_union_map_zip(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_zip', retType, argTypes, args)
isl.isl_union_map_zip = isl_union_map_zip
@staticmethod
def isl_union_map_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_union_map_free', retType, argTypes, args)
isl.isl_union_map_free = isl_union_map_free
@staticmethod
def isl_union_map_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_to_str', retType, argTypes, args)
isl.isl_union_map_to_str = isl_union_map_to_str
@staticmethod
def isl_union_map_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_map_copy', retType, argTypes, args)
isl.isl_union_map_copy = isl_union_map_copy

class map(union_map):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_map_read_from_str(self.ctx, args[0])
            return
        if len(args) == 1 and args[0].__class__ is basic_map:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_map_from_basic_map(isl.isl_basic_map_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_map_free(self.ptr)
    def __str__(self):
        return str(isl.isl_map_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.map("""%s""")' % s
        else:
            return 'isl.map("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_affine_hull(isl.isl_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def apply_domain(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).apply_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_apply_domain(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def apply_range(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).apply_range(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_apply_range(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def coalesce(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_coalesce(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def complement(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_complement(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def deltas(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_deltas(isl.isl_map_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_detect_equalities(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def flatten(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_flatten(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def flatten_domain(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_flatten_domain(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def flatten_range(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_flatten_range(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def foreach_basic_map(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = basic_map(ctx=arg0.ctx, ptr=cb_arg0)
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_map_foreach_basic_map(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise exc_info[0][0], exc_info[0][1], exc_info[0][2]
        return res
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).gist(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_gist(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def gist_domain(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_map(arg0).gist_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_gist_domain(isl.isl_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).intersect(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_intersect(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def intersect_domain(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_map(arg0).intersect_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_intersect_domain(isl.isl_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_map(arg0).intersect_params(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_intersect_params(isl.isl_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def intersect_range(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_map(arg0).intersect_range(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_intersect_range(isl.isl_map_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def is_bijective(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_is_bijective(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_disjoint(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).is_disjoint(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_is_disjoint(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).is_equal(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_injective(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_is_injective(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_single_valued(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_is_single_valued(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_strict_subset(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).is_strict_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_is_strict_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).is_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_lexmax(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def lexmin(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_lexmin(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def polyhedral_hull(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_polyhedral_hull(isl.isl_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def reverse(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_reverse(isl.isl_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def sample(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_sample(isl.isl_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def subtract(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).subtract(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_subtract(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_map(arg0).union(arg1)
        ctx = arg0.ctx
        res = isl.isl_map_union(isl.isl_map_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)
    def unshifted_simple_hull(arg0):
        try:
            if not arg0.__class__ is map:
                arg0 = map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_map_unshifted_simple_hull(isl.isl_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)

@staticmethod
def isl_map_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_map_read_from_str', retType, argTypes, args)
isl.isl_map_read_from_str = isl_map_read_from_str
@staticmethod
def isl_map_from_basic_map(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_from_basic_map', retType, argTypes, args)
isl.isl_map_from_basic_map = isl_map_from_basic_map
@staticmethod
def isl_map_affine_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_affine_hull', retType, argTypes, args)
isl.isl_map_affine_hull = isl_map_affine_hull
@staticmethod
def isl_map_apply_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_apply_domain', retType, argTypes, args)
isl.isl_map_apply_domain = isl_map_apply_domain
@staticmethod
def isl_map_apply_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_apply_range', retType, argTypes, args)
isl.isl_map_apply_range = isl_map_apply_range
@staticmethod
def isl_map_coalesce(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_coalesce', retType, argTypes, args)
isl.isl_map_coalesce = isl_map_coalesce
@staticmethod
def isl_map_complement(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_complement', retType, argTypes, args)
isl.isl_map_complement = isl_map_complement
@staticmethod
def isl_map_deltas(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_deltas', retType, argTypes, args)
isl.isl_map_deltas = isl_map_deltas
@staticmethod
def isl_map_detect_equalities(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_detect_equalities', retType, argTypes, args)
isl.isl_map_detect_equalities = isl_map_detect_equalities
@staticmethod
def isl_map_flatten(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_flatten', retType, argTypes, args)
isl.isl_map_flatten = isl_map_flatten
@staticmethod
def isl_map_flatten_domain(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_flatten_domain', retType, argTypes, args)
isl.isl_map_flatten_domain = isl_map_flatten_domain
@staticmethod
def isl_map_flatten_range(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_flatten_range', retType, argTypes, args)
isl.isl_map_flatten_range = isl_map_flatten_range
@staticmethod
def isl_map_foreach_basic_map(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_foreach_basic_map', retType, argTypes, args)
isl.isl_map_foreach_basic_map = isl_map_foreach_basic_map
@staticmethod
def isl_map_gist(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_gist', retType, argTypes, args)
isl.isl_map_gist = isl_map_gist
@staticmethod
def isl_map_gist_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_gist_domain', retType, argTypes, args)
isl.isl_map_gist_domain = isl_map_gist_domain
@staticmethod
def isl_map_intersect(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_intersect', retType, argTypes, args)
isl.isl_map_intersect = isl_map_intersect
@staticmethod
def isl_map_intersect_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_intersect_domain', retType, argTypes, args)
isl.isl_map_intersect_domain = isl_map_intersect_domain
@staticmethod
def isl_map_intersect_params(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_intersect_params', retType, argTypes, args)
isl.isl_map_intersect_params = isl_map_intersect_params
@staticmethod
def isl_map_intersect_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_intersect_range', retType, argTypes, args)
isl.isl_map_intersect_range = isl_map_intersect_range
@staticmethod
def isl_map_is_bijective(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_is_bijective', retType, argTypes, args)
isl.isl_map_is_bijective = isl_map_is_bijective
@staticmethod
def isl_map_is_disjoint(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_is_disjoint', retType, argTypes, args)
isl.isl_map_is_disjoint = isl_map_is_disjoint
@staticmethod
def isl_map_is_empty(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_is_empty', retType, argTypes, args)
isl.isl_map_is_empty = isl_map_is_empty
@staticmethod
def isl_map_is_equal(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_is_equal', retType, argTypes, args)
isl.isl_map_is_equal = isl_map_is_equal
@staticmethod
def isl_map_is_injective(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_is_injective', retType, argTypes, args)
isl.isl_map_is_injective = isl_map_is_injective
@staticmethod
def isl_map_is_single_valued(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_is_single_valued', retType, argTypes, args)
isl.isl_map_is_single_valued = isl_map_is_single_valued
@staticmethod
def isl_map_is_strict_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_is_strict_subset', retType, argTypes, args)
isl.isl_map_is_strict_subset = isl_map_is_strict_subset
@staticmethod
def isl_map_is_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_is_subset', retType, argTypes, args)
isl.isl_map_is_subset = isl_map_is_subset
@staticmethod
def isl_map_lexmax(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_lexmax', retType, argTypes, args)
isl.isl_map_lexmax = isl_map_lexmax
@staticmethod
def isl_map_lexmin(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_lexmin', retType, argTypes, args)
isl.isl_map_lexmin = isl_map_lexmin
@staticmethod
def isl_map_polyhedral_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_polyhedral_hull', retType, argTypes, args)
isl.isl_map_polyhedral_hull = isl_map_polyhedral_hull
@staticmethod
def isl_map_reverse(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_reverse', retType, argTypes, args)
isl.isl_map_reverse = isl_map_reverse
@staticmethod
def isl_map_sample(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_sample', retType, argTypes, args)
isl.isl_map_sample = isl_map_sample
@staticmethod
def isl_map_subtract(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_subtract', retType, argTypes, args)
isl.isl_map_subtract = isl_map_subtract
@staticmethod
def isl_map_union(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_map_union', retType, argTypes, args)
isl.isl_map_union = isl_map_union
@staticmethod
def isl_map_unshifted_simple_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_unshifted_simple_hull', retType, argTypes, args)
isl.isl_map_unshifted_simple_hull = isl_map_unshifted_simple_hull
@staticmethod
def isl_map_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_map_free', retType, argTypes, args)
isl.isl_map_free = isl_map_free
@staticmethod
def isl_map_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_to_str', retType, argTypes, args)
isl.isl_map_to_str = isl_map_to_str
@staticmethod
def isl_map_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_map_copy', retType, argTypes, args)
isl.isl_map_copy = isl_map_copy

class basic_map(map):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_basic_map_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_basic_map_free(self.ptr)
    def __str__(self):
        return str(isl.isl_basic_map_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.basic_map("""%s""")' % s
        else:
            return 'isl.basic_map("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_affine_hull(isl.isl_basic_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def apply_domain(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).apply_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_apply_domain(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def apply_range(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).apply_range(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_apply_range(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def deltas(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_deltas(isl.isl_basic_map_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_detect_equalities(isl.isl_basic_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def flatten(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_flatten(isl.isl_basic_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def flatten_domain(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_flatten_domain(isl.isl_basic_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def flatten_range(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_flatten_range(isl.isl_basic_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).gist(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_gist(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).intersect(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_intersect(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def intersect_domain(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return map(arg0).intersect_domain(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_intersect_domain(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def intersect_range(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return map(arg0).intersect_range(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_intersect_range(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).is_equal(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).is_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_lexmax(isl.isl_basic_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def lexmin(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_lexmin(isl.isl_basic_map_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def reverse(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_reverse(isl.isl_basic_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def sample(arg0):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_map_sample(isl.isl_basic_map_copy(arg0.ptr))
        return basic_map(ctx=ctx, ptr=res)
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is basic_map:
                arg0 = basic_map(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return map(arg0).union(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_map_union(isl.isl_basic_map_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        return map(ctx=ctx, ptr=res)

@staticmethod
def isl_basic_map_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_basic_map_read_from_str', retType, argTypes, args)
isl.isl_basic_map_read_from_str = isl_basic_map_read_from_str
@staticmethod
def isl_basic_map_affine_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_affine_hull', retType, argTypes, args)
isl.isl_basic_map_affine_hull = isl_basic_map_affine_hull
@staticmethod
def isl_basic_map_apply_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_apply_domain', retType, argTypes, args)
isl.isl_basic_map_apply_domain = isl_basic_map_apply_domain
@staticmethod
def isl_basic_map_apply_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_apply_range', retType, argTypes, args)
isl.isl_basic_map_apply_range = isl_basic_map_apply_range
@staticmethod
def isl_basic_map_deltas(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_deltas', retType, argTypes, args)
isl.isl_basic_map_deltas = isl_basic_map_deltas
@staticmethod
def isl_basic_map_detect_equalities(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_detect_equalities', retType, argTypes, args)
isl.isl_basic_map_detect_equalities = isl_basic_map_detect_equalities
@staticmethod
def isl_basic_map_flatten(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_flatten', retType, argTypes, args)
isl.isl_basic_map_flatten = isl_basic_map_flatten
@staticmethod
def isl_basic_map_flatten_domain(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_flatten_domain', retType, argTypes, args)
isl.isl_basic_map_flatten_domain = isl_basic_map_flatten_domain
@staticmethod
def isl_basic_map_flatten_range(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_flatten_range', retType, argTypes, args)
isl.isl_basic_map_flatten_range = isl_basic_map_flatten_range
@staticmethod
def isl_basic_map_gist(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_gist', retType, argTypes, args)
isl.isl_basic_map_gist = isl_basic_map_gist
@staticmethod
def isl_basic_map_intersect(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_intersect', retType, argTypes, args)
isl.isl_basic_map_intersect = isl_basic_map_intersect
@staticmethod
def isl_basic_map_intersect_domain(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_intersect_domain', retType, argTypes, args)
isl.isl_basic_map_intersect_domain = isl_basic_map_intersect_domain
@staticmethod
def isl_basic_map_intersect_range(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_intersect_range', retType, argTypes, args)
isl.isl_basic_map_intersect_range = isl_basic_map_intersect_range
@staticmethod
def isl_basic_map_is_empty(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_is_empty', retType, argTypes, args)
isl.isl_basic_map_is_empty = isl_basic_map_is_empty
@staticmethod
def isl_basic_map_is_equal(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_is_equal', retType, argTypes, args)
isl.isl_basic_map_is_equal = isl_basic_map_is_equal
@staticmethod
def isl_basic_map_is_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_is_subset', retType, argTypes, args)
isl.isl_basic_map_is_subset = isl_basic_map_is_subset
@staticmethod
def isl_basic_map_lexmax(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_lexmax', retType, argTypes, args)
isl.isl_basic_map_lexmax = isl_basic_map_lexmax
@staticmethod
def isl_basic_map_lexmin(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_lexmin', retType, argTypes, args)
isl.isl_basic_map_lexmin = isl_basic_map_lexmin
@staticmethod
def isl_basic_map_reverse(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_reverse', retType, argTypes, args)
isl.isl_basic_map_reverse = isl_basic_map_reverse
@staticmethod
def isl_basic_map_sample(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_sample', retType, argTypes, args)
isl.isl_basic_map_sample = isl_basic_map_sample
@staticmethod
def isl_basic_map_union(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_map_union', retType, argTypes, args)
isl.isl_basic_map_union = isl_basic_map_union
@staticmethod
def isl_basic_map_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_basic_map_free', retType, argTypes, args)
isl.isl_basic_map_free = isl_basic_map_free
@staticmethod
def isl_basic_map_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_to_str', retType, argTypes, args)
isl.isl_basic_map_to_str = isl_basic_map_to_str
@staticmethod
def isl_basic_map_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_map_copy', retType, argTypes, args)
isl.isl_basic_map_copy = isl_basic_map_copy

class union_set:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is basic_set:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_from_basic_set(isl.isl_basic_set_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is set:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_from_set(isl.isl_set_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is point:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_from_point(isl.isl_point_copy(args[0].ptr))
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_set_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_set_free(self.ptr)
    def __str__(self):
        return str(isl.isl_union_set_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_set("""%s""")' % s
        else:
            return 'isl.union_set("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_affine_hull(isl.isl_union_set_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def apply(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_apply(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_set(ctx=ctx, ptr=res)
    def coalesce(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_coalesce(isl.isl_union_set_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def compute_divs(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_compute_divs(isl.isl_union_set_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_detect_equalities(isl.isl_union_set_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def foreach_point(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = point(ctx=arg0.ctx, ptr=cb_arg0)
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_set_foreach_point(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise exc_info[0][0], exc_info[0][1], exc_info[0][2]
        return res
    def foreach_set(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = set(ctx=arg0.ctx, ptr=cb_arg0)
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_union_set_foreach_set(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise exc_info[0][0], exc_info[0][1], exc_info[0][2]
        return res
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_gist(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_set(ctx=ctx, ptr=res)
    def gist_params(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_gist_params(isl.isl_union_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return union_set(ctx=ctx, ptr=res)
    def identity(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_identity(isl.isl_union_set_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_intersect(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_set(ctx=ctx, ptr=res)
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_intersect_params(isl.isl_union_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return union_set(ctx=ctx, ptr=res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_strict_subset(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_is_strict_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_lexmax(isl.isl_union_set_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def lexmin(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_lexmin(isl.isl_union_set_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def polyhedral_hull(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_polyhedral_hull(isl.isl_union_set_copy(arg0.ptr))
        return union_set(ctx=ctx, ptr=res)
    def sample_point(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_sample_point(isl.isl_union_set_copy(arg0.ptr))
        return point(ctx=ctx, ptr=res)
    def subtract(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_subtract(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_set(ctx=ctx, ptr=res)
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_set:
                arg1 = union_set(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_union(isl.isl_union_set_copy(arg0.ptr), isl.isl_union_set_copy(arg1.ptr))
        return union_set(ctx=ctx, ptr=res)
    def unwrap(arg0):
        try:
            if not arg0.__class__ is union_set:
                arg0 = union_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_set_unwrap(isl.isl_union_set_copy(arg0.ptr))
        return union_map(ctx=ctx, ptr=res)

@staticmethod
def isl_union_set_from_basic_set(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_from_basic_set', retType, argTypes, args)
isl.isl_union_set_from_basic_set = isl_union_set_from_basic_set
@staticmethod
def isl_union_set_from_set(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_from_set', retType, argTypes, args)
isl.isl_union_set_from_set = isl_union_set_from_set
@staticmethod
def isl_union_set_from_point(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_from_point', retType, argTypes, args)
isl.isl_union_set_from_point = isl_union_set_from_point
@staticmethod
def isl_union_set_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_union_set_read_from_str', retType, argTypes, args)
isl.isl_union_set_read_from_str = isl_union_set_read_from_str
@staticmethod
def isl_union_set_affine_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_affine_hull', retType, argTypes, args)
isl.isl_union_set_affine_hull = isl_union_set_affine_hull
@staticmethod
def isl_union_set_apply(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_apply', retType, argTypes, args)
isl.isl_union_set_apply = isl_union_set_apply
@staticmethod
def isl_union_set_coalesce(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_coalesce', retType, argTypes, args)
isl.isl_union_set_coalesce = isl_union_set_coalesce
@staticmethod
def isl_union_set_compute_divs(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_compute_divs', retType, argTypes, args)
isl.isl_union_set_compute_divs = isl_union_set_compute_divs
@staticmethod
def isl_union_set_detect_equalities(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_detect_equalities', retType, argTypes, args)
isl.isl_union_set_detect_equalities = isl_union_set_detect_equalities
@staticmethod
def isl_union_set_foreach_point(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_foreach_point', retType, argTypes, args)
isl.isl_union_set_foreach_point = isl_union_set_foreach_point
@staticmethod
def isl_union_set_foreach_set(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_foreach_set', retType, argTypes, args)
isl.isl_union_set_foreach_set = isl_union_set_foreach_set
@staticmethod
def isl_union_set_gist(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_gist', retType, argTypes, args)
isl.isl_union_set_gist = isl_union_set_gist
@staticmethod
def isl_union_set_gist_params(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_gist_params', retType, argTypes, args)
isl.isl_union_set_gist_params = isl_union_set_gist_params
@staticmethod
def isl_union_set_identity(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_identity', retType, argTypes, args)
isl.isl_union_set_identity = isl_union_set_identity
@staticmethod
def isl_union_set_intersect(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_intersect', retType, argTypes, args)
isl.isl_union_set_intersect = isl_union_set_intersect
@staticmethod
def isl_union_set_intersect_params(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_intersect_params', retType, argTypes, args)
isl.isl_union_set_intersect_params = isl_union_set_intersect_params
@staticmethod
def isl_union_set_is_empty(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_is_empty', retType, argTypes, args)
isl.isl_union_set_is_empty = isl_union_set_is_empty
@staticmethod
def isl_union_set_is_equal(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_is_equal', retType, argTypes, args)
isl.isl_union_set_is_equal = isl_union_set_is_equal
@staticmethod
def isl_union_set_is_strict_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_is_strict_subset', retType, argTypes, args)
isl.isl_union_set_is_strict_subset = isl_union_set_is_strict_subset
@staticmethod
def isl_union_set_is_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_is_subset', retType, argTypes, args)
isl.isl_union_set_is_subset = isl_union_set_is_subset
@staticmethod
def isl_union_set_lexmax(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_lexmax', retType, argTypes, args)
isl.isl_union_set_lexmax = isl_union_set_lexmax
@staticmethod
def isl_union_set_lexmin(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_lexmin', retType, argTypes, args)
isl.isl_union_set_lexmin = isl_union_set_lexmin
@staticmethod
def isl_union_set_polyhedral_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_polyhedral_hull', retType, argTypes, args)
isl.isl_union_set_polyhedral_hull = isl_union_set_polyhedral_hull
@staticmethod
def isl_union_set_sample_point(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_sample_point', retType, argTypes, args)
isl.isl_union_set_sample_point = isl_union_set_sample_point
@staticmethod
def isl_union_set_subtract(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_subtract', retType, argTypes, args)
isl.isl_union_set_subtract = isl_union_set_subtract
@staticmethod
def isl_union_set_union(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_set_union', retType, argTypes, args)
isl.isl_union_set_union = isl_union_set_union
@staticmethod
def isl_union_set_unwrap(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_unwrap', retType, argTypes, args)
isl.isl_union_set_unwrap = isl_union_set_unwrap
@staticmethod
def isl_union_set_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_union_set_free', retType, argTypes, args)
isl.isl_union_set_free = isl_union_set_free
@staticmethod
def isl_union_set_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_to_str', retType, argTypes, args)
isl.isl_union_set_to_str = isl_union_set_to_str
@staticmethod
def isl_union_set_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_set_copy', retType, argTypes, args)
isl.isl_union_set_copy = isl_union_set_copy

class set(union_set):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_set_read_from_str(self.ctx, args[0])
            return
        if len(args) == 1 and args[0].__class__ is basic_set:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_set_from_basic_set(isl.isl_basic_set_copy(args[0].ptr))
            return
        if len(args) == 1 and args[0].__class__ is point:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_set_from_point(isl.isl_point_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_set_free(self.ptr)
    def __str__(self):
        return str(isl.isl_set_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.set("""%s""")' % s
        else:
            return 'isl.set("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_affine_hull(isl.isl_set_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def apply(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is map:
                arg1 = map(arg1)
        except:
            return union_set(arg0).apply(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_apply(isl.isl_set_copy(arg0.ptr), isl.isl_map_copy(arg1.ptr))
        return set(ctx=ctx, ptr=res)
    def coalesce(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_coalesce(isl.isl_set_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def complement(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_complement(isl.isl_set_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_detect_equalities(isl.isl_set_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def flatten(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_flatten(isl.isl_set_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def foreach_basic_set(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        exc_info = [None]
        fn = CFUNCTYPE(c_int, c_void_p, c_void_p)
        def cb_func(cb_arg0, cb_arg1):
            cb_arg0 = basic_set(ctx=arg0.ctx, ptr=cb_arg0)
            try:
                arg1(cb_arg0)
            except:
                import sys
                exc_info[0] = sys.exc_info()
                return -1
            return 0
        cb = fn(cb_func)
        ctx = arg0.ctx
        res = isl.isl_set_foreach_basic_set(arg0.ptr, cb, None)
        if exc_info[0] != None:
            raise exc_info[0][0], exc_info[0][1], exc_info[0][2]
        return res
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).gist(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_gist(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return set(ctx=ctx, ptr=res)
    def identity(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_identity(isl.isl_set_copy(arg0.ptr))
        return map(ctx=ctx, ptr=res)
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).intersect(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_intersect(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return set(ctx=ctx, ptr=res)
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).intersect_params(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_intersect_params(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return set(ctx=ctx, ptr=res)
    def is_disjoint(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).is_disjoint(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_is_disjoint(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).is_equal(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_strict_subset(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).is_strict_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_is_strict_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).is_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_wrapping(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_is_wrapping(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_lexmax(isl.isl_set_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def lexmin(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_lexmin(isl.isl_set_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def max_val(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return union_set(arg0).max_val(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_max_val(arg0.ptr, arg1.ptr)
        return val(ctx=ctx, ptr=res)
    def min_val(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is aff:
                arg1 = aff(arg1)
        except:
            return union_set(arg0).min_val(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_min_val(arg0.ptr, arg1.ptr)
        return val(ctx=ctx, ptr=res)
    def polyhedral_hull(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_polyhedral_hull(isl.isl_set_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def sample(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_sample(isl.isl_set_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def subtract(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).subtract(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_subtract(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return set(ctx=ctx, ptr=res)
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is set:
                arg1 = set(arg1)
        except:
            return union_set(arg0).union(arg1)
        ctx = arg0.ctx
        res = isl.isl_set_union(isl.isl_set_copy(arg0.ptr), isl.isl_set_copy(arg1.ptr))
        return set(ctx=ctx, ptr=res)
    def unshifted_simple_hull(arg0):
        try:
            if not arg0.__class__ is set:
                arg0 = set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_set_unshifted_simple_hull(isl.isl_set_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)

@staticmethod
def isl_set_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_set_read_from_str', retType, argTypes, args)
isl.isl_set_read_from_str = isl_set_read_from_str
@staticmethod
def isl_set_from_basic_set(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_from_basic_set', retType, argTypes, args)
isl.isl_set_from_basic_set = isl_set_from_basic_set
@staticmethod
def isl_set_from_point(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_from_point', retType, argTypes, args)
isl.isl_set_from_point = isl_set_from_point
@staticmethod
def isl_set_affine_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_affine_hull', retType, argTypes, args)
isl.isl_set_affine_hull = isl_set_affine_hull
@staticmethod
def isl_set_apply(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_apply', retType, argTypes, args)
isl.isl_set_apply = isl_set_apply
@staticmethod
def isl_set_coalesce(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_coalesce', retType, argTypes, args)
isl.isl_set_coalesce = isl_set_coalesce
@staticmethod
def isl_set_complement(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_complement', retType, argTypes, args)
isl.isl_set_complement = isl_set_complement
@staticmethod
def isl_set_detect_equalities(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_detect_equalities', retType, argTypes, args)
isl.isl_set_detect_equalities = isl_set_detect_equalities
@staticmethod
def isl_set_flatten(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_flatten', retType, argTypes, args)
isl.isl_set_flatten = isl_set_flatten
@staticmethod
def isl_set_foreach_basic_set(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_foreach_basic_set', retType, argTypes, args)
isl.isl_set_foreach_basic_set = isl_set_foreach_basic_set
@staticmethod
def isl_set_gist(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_gist', retType, argTypes, args)
isl.isl_set_gist = isl_set_gist
@staticmethod
def isl_set_identity(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_identity', retType, argTypes, args)
isl.isl_set_identity = isl_set_identity
@staticmethod
def isl_set_intersect(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_intersect', retType, argTypes, args)
isl.isl_set_intersect = isl_set_intersect
@staticmethod
def isl_set_intersect_params(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_intersect_params', retType, argTypes, args)
isl.isl_set_intersect_params = isl_set_intersect_params
@staticmethod
def isl_set_is_disjoint(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_is_disjoint', retType, argTypes, args)
isl.isl_set_is_disjoint = isl_set_is_disjoint
@staticmethod
def isl_set_is_empty(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_is_empty', retType, argTypes, args)
isl.isl_set_is_empty = isl_set_is_empty
@staticmethod
def isl_set_is_equal(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_is_equal', retType, argTypes, args)
isl.isl_set_is_equal = isl_set_is_equal
@staticmethod
def isl_set_is_strict_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_is_strict_subset', retType, argTypes, args)
isl.isl_set_is_strict_subset = isl_set_is_strict_subset
@staticmethod
def isl_set_is_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_is_subset', retType, argTypes, args)
isl.isl_set_is_subset = isl_set_is_subset
@staticmethod
def isl_set_is_wrapping(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_is_wrapping', retType, argTypes, args)
isl.isl_set_is_wrapping = isl_set_is_wrapping
@staticmethod
def isl_set_lexmax(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_lexmax', retType, argTypes, args)
isl.isl_set_lexmax = isl_set_lexmax
@staticmethod
def isl_set_lexmin(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_lexmin', retType, argTypes, args)
isl.isl_set_lexmin = isl_set_lexmin
@staticmethod
def isl_set_max_val(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_max_val', retType, argTypes, args)
isl.isl_set_max_val = isl_set_max_val
@staticmethod
def isl_set_min_val(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_min_val', retType, argTypes, args)
isl.isl_set_min_val = isl_set_min_val
@staticmethod
def isl_set_polyhedral_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_polyhedral_hull', retType, argTypes, args)
isl.isl_set_polyhedral_hull = isl_set_polyhedral_hull
@staticmethod
def isl_set_sample(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_sample', retType, argTypes, args)
isl.isl_set_sample = isl_set_sample
@staticmethod
def isl_set_subtract(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_subtract', retType, argTypes, args)
isl.isl_set_subtract = isl_set_subtract
@staticmethod
def isl_set_union(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_set_union', retType, argTypes, args)
isl.isl_set_union = isl_set_union
@staticmethod
def isl_set_unshifted_simple_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_unshifted_simple_hull', retType, argTypes, args)
isl.isl_set_unshifted_simple_hull = isl_set_unshifted_simple_hull
@staticmethod
def isl_set_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_set_free', retType, argTypes, args)
isl.isl_set_free = isl_set_free
@staticmethod
def isl_set_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_to_str', retType, argTypes, args)
isl.isl_set_to_str = isl_set_to_str
@staticmethod
def isl_set_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_set_copy', retType, argTypes, args)
isl.isl_set_copy = isl_set_copy

class basic_set(set):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_basic_set_read_from_str(self.ctx, args[0])
            return
        if len(args) == 1 and args[0].__class__ is point:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_basic_set_from_point(isl.isl_point_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_basic_set_free(self.ptr)
    def __str__(self):
        return str(isl.isl_basic_set_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.basic_set("""%s""")' % s
        else:
            return 'isl.basic_set("%s")' % s
    def affine_hull(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_affine_hull(isl.isl_basic_set_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def apply(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_map:
                arg1 = basic_map(arg1)
        except:
            return set(arg0).apply(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_apply(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_map_copy(arg1.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def detect_equalities(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_detect_equalities(isl.isl_basic_set_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def flatten(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_flatten(isl.isl_basic_set_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def gist(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).gist(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_gist(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def intersect(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).intersect(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_intersect(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def intersect_params(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).intersect_params(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_intersect_params(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def is_empty(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_is_empty(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_equal(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).is_equal(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_is_equal(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_subset(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).is_subset(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_is_subset(arg0.ptr, arg1.ptr)
        if res < 0:
            raise
        return bool(res)
    def is_wrapping(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_is_wrapping(arg0.ptr)
        if res < 0:
            raise
        return bool(res)
    def lexmax(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_lexmax(isl.isl_basic_set_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def lexmin(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_lexmin(isl.isl_basic_set_copy(arg0.ptr))
        return set(ctx=ctx, ptr=res)
    def sample(arg0):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_basic_set_sample(isl.isl_basic_set_copy(arg0.ptr))
        return basic_set(ctx=ctx, ptr=res)
    def union(arg0, arg1):
        try:
            if not arg0.__class__ is basic_set:
                arg0 = basic_set(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is basic_set:
                arg1 = basic_set(arg1)
        except:
            return set(arg0).union(arg1)
        ctx = arg0.ctx
        res = isl.isl_basic_set_union(isl.isl_basic_set_copy(arg0.ptr), isl.isl_basic_set_copy(arg1.ptr))
        return set(ctx=ctx, ptr=res)

@staticmethod
def isl_basic_set_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_basic_set_read_from_str', retType, argTypes, args)
isl.isl_basic_set_read_from_str = isl_basic_set_read_from_str
@staticmethod
def isl_basic_set_from_point(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_from_point', retType, argTypes, args)
isl.isl_basic_set_from_point = isl_basic_set_from_point
@staticmethod
def isl_basic_set_affine_hull(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_affine_hull', retType, argTypes, args)
isl.isl_basic_set_affine_hull = isl_basic_set_affine_hull
@staticmethod
def isl_basic_set_apply(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_set_apply', retType, argTypes, args)
isl.isl_basic_set_apply = isl_basic_set_apply
@staticmethod
def isl_basic_set_detect_equalities(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_detect_equalities', retType, argTypes, args)
isl.isl_basic_set_detect_equalities = isl_basic_set_detect_equalities
@staticmethod
def isl_basic_set_flatten(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_flatten', retType, argTypes, args)
isl.isl_basic_set_flatten = isl_basic_set_flatten
@staticmethod
def isl_basic_set_gist(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_set_gist', retType, argTypes, args)
isl.isl_basic_set_gist = isl_basic_set_gist
@staticmethod
def isl_basic_set_intersect(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_set_intersect', retType, argTypes, args)
isl.isl_basic_set_intersect = isl_basic_set_intersect
@staticmethod
def isl_basic_set_intersect_params(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_set_intersect_params', retType, argTypes, args)
isl.isl_basic_set_intersect_params = isl_basic_set_intersect_params
@staticmethod
def isl_basic_set_is_empty(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_is_empty', retType, argTypes, args)
isl.isl_basic_set_is_empty = isl_basic_set_is_empty
@staticmethod
def isl_basic_set_is_equal(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_set_is_equal', retType, argTypes, args)
isl.isl_basic_set_is_equal = isl_basic_set_is_equal
@staticmethod
def isl_basic_set_is_subset(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_set_is_subset', retType, argTypes, args)
isl.isl_basic_set_is_subset = isl_basic_set_is_subset
@staticmethod
def isl_basic_set_is_wrapping(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_is_wrapping', retType, argTypes, args)
isl.isl_basic_set_is_wrapping = isl_basic_set_is_wrapping
@staticmethod
def isl_basic_set_lexmax(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_lexmax', retType, argTypes, args)
isl.isl_basic_set_lexmax = isl_basic_set_lexmax
@staticmethod
def isl_basic_set_lexmin(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_lexmin', retType, argTypes, args)
isl.isl_basic_set_lexmin = isl_basic_set_lexmin
@staticmethod
def isl_basic_set_sample(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_sample', retType, argTypes, args)
isl.isl_basic_set_sample = isl_basic_set_sample
@staticmethod
def isl_basic_set_union(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_basic_set_union', retType, argTypes, args)
isl.isl_basic_set_union = isl_basic_set_union
@staticmethod
def isl_basic_set_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_basic_set_free', retType, argTypes, args)
isl.isl_basic_set_free = isl_basic_set_free
@staticmethod
def isl_basic_set_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_to_str', retType, argTypes, args)
isl.isl_basic_set_to_str = isl_basic_set_to_str
@staticmethod
def isl_basic_set_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_basic_set_copy', retType, argTypes, args)
isl.isl_basic_set_copy = isl_basic_set_copy

class multi_val:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_multi_val_free(self.ptr)
    def __str__(self):
        return str(isl.isl_multi_val_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.multi_val("""%s""")' % s
        else:
            return 'isl.multi_val("%s")' % s
    def add(arg0, arg1):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_val_add(isl.isl_multi_val_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        return multi_val(ctx=ctx, ptr=res)
    def flat_range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_val_flat_range_product(isl.isl_multi_val_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        return multi_val(ctx=ctx, ptr=res)
    def product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_val_product(isl.isl_multi_val_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        return multi_val(ctx=ctx, ptr=res)
    def range_product(arg0, arg1):
        try:
            if not arg0.__class__ is multi_val:
                arg0 = multi_val(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is multi_val:
                arg1 = multi_val(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_multi_val_range_product(isl.isl_multi_val_copy(arg0.ptr), isl.isl_multi_val_copy(arg1.ptr))
        return multi_val(ctx=ctx, ptr=res)

@staticmethod
def isl_multi_val_add(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_val_add', retType, argTypes, args)
isl.isl_multi_val_add = isl_multi_val_add
@staticmethod
def isl_multi_val_flat_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_val_flat_range_product', retType, argTypes, args)
isl.isl_multi_val_flat_range_product = isl_multi_val_flat_range_product
@staticmethod
def isl_multi_val_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_val_product', retType, argTypes, args)
isl.isl_multi_val_product = isl_multi_val_product
@staticmethod
def isl_multi_val_range_product(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_multi_val_range_product', retType, argTypes, args)
isl.isl_multi_val_range_product = isl_multi_val_range_product
@staticmethod
def isl_multi_val_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_multi_val_free', retType, argTypes, args)
isl.isl_multi_val_free = isl_multi_val_free
@staticmethod
def isl_multi_val_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_val_to_str', retType, argTypes, args)
isl.isl_multi_val_to_str = isl_multi_val_to_str
@staticmethod
def isl_multi_val_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_multi_val_copy', retType, argTypes, args)
isl.isl_multi_val_copy = isl_multi_val_copy

class point(basic_set):
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_point_free(self.ptr)
    def __str__(self):
        return str(isl.isl_point_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.point("""%s""")' % s
        else:
            return 'isl.point("%s")' % s

@staticmethod
def isl_point_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_point_free', retType, argTypes, args)
isl.isl_point_free = isl_point_free
@staticmethod
def isl_point_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_point_to_str', retType, argTypes, args)
isl.isl_point_to_str = isl_point_to_str
@staticmethod
def isl_point_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_point_copy', retType, argTypes, args)
isl.isl_point_copy = isl_point_copy

class schedule:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_schedule_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_free(self.ptr)
    def __str__(self):
        return str(isl.isl_schedule_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule("""%s""")' % s
        else:
            return 'isl.schedule("%s")' % s
    def get_map(arg0):
        try:
            if not arg0.__class__ is schedule:
                arg0 = schedule(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_get_map(arg0.ptr)
        return union_map(ctx=ctx, ptr=res)
    def get_root(arg0):
        try:
            if not arg0.__class__ is schedule:
                arg0 = schedule(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_get_root(arg0.ptr)
        return schedule_node(ctx=ctx, ptr=res)
    def pullback(arg0, arg1):
        if arg1.__class__ is union_pw_multi_aff:
            res = isl.isl_schedule_pullback_union_pw_multi_aff(isl.isl_schedule_copy(arg0.ptr), isl.isl_union_pw_multi_aff_copy(arg1.ptr))
            return schedule(ctx=arg0.ctx, ptr=res)

@staticmethod
def isl_schedule_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_schedule_read_from_str', retType, argTypes, args)
isl.isl_schedule_read_from_str = isl_schedule_read_from_str
@staticmethod
def isl_schedule_get_map(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_get_map', retType, argTypes, args)
isl.isl_schedule_get_map = isl_schedule_get_map
@staticmethod
def isl_schedule_get_root(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_get_root', retType, argTypes, args)
isl.isl_schedule_get_root = isl_schedule_get_root
@staticmethod
def isl_schedule_pullback_union_pw_multi_aff(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_schedule_pullback_union_pw_multi_aff', retType, argTypes, args)
isl.isl_schedule_pullback_union_pw_multi_aff = isl_schedule_pullback_union_pw_multi_aff
@staticmethod
def isl_schedule_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_schedule_free', retType, argTypes, args)
isl.isl_schedule_free = isl_schedule_free
@staticmethod
def isl_schedule_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_to_str', retType, argTypes, args)
isl.isl_schedule_to_str = isl_schedule_to_str
@staticmethod
def isl_schedule_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_copy', retType, argTypes, args)
isl.isl_schedule_copy = isl_schedule_copy

class schedule_node:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_schedule_node_free(self.ptr)
    def __str__(self):
        return str(isl.isl_schedule_node_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.schedule_node("""%s""")' % s
        else:
            return 'isl.schedule_node("%s")' % s
    def band_member_get_coincident(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_member_get_coincident(arg0.ptr, arg1)
        if res < 0:
            raise
        return bool(res)
    def band_member_set_coincident(arg0, arg1, arg2):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_band_member_set_coincident(isl.isl_schedule_node_copy(arg0.ptr), arg1, arg2)
        return schedule_node(ctx=ctx, ptr=res)
    def child(arg0, arg1):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_child(isl.isl_schedule_node_copy(arg0.ptr), arg1)
        return schedule_node(ctx=ctx, ptr=res)
    def get_prefix_schedule_multi_union_pw_aff(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_prefix_schedule_multi_union_pw_aff(arg0.ptr)
        return multi_union_pw_aff(ctx=ctx, ptr=res)
    def get_prefix_schedule_union_map(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_prefix_schedule_union_map(arg0.ptr)
        return union_map(ctx=ctx, ptr=res)
    def get_prefix_schedule_union_pw_multi_aff(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_prefix_schedule_union_pw_multi_aff(arg0.ptr)
        return union_pw_multi_aff(ctx=ctx, ptr=res)
    def get_schedule(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_get_schedule(arg0.ptr)
        return schedule(ctx=ctx, ptr=res)
    def parent(arg0):
        try:
            if not arg0.__class__ is schedule_node:
                arg0 = schedule_node(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_schedule_node_parent(isl.isl_schedule_node_copy(arg0.ptr))
        return schedule_node(ctx=ctx, ptr=res)

@staticmethod
def isl_schedule_node_band_member_get_coincident(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_schedule_node_band_member_get_coincident', retType, argTypes, args)
isl.isl_schedule_node_band_member_get_coincident = isl_schedule_node_band_member_get_coincident
@staticmethod
def isl_schedule_node_band_member_set_coincident(a_0, a_1, a_2):
  retType = 'number'
  argTypes = ['number', 'number', 'number']
  args = [a_0, a_1, a_2]
  return js.globals.Module.ccall('isl_schedule_node_band_member_set_coincident', retType, argTypes, args)
isl.isl_schedule_node_band_member_set_coincident = isl_schedule_node_band_member_set_coincident
@staticmethod
def isl_schedule_node_child(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_schedule_node_child', retType, argTypes, args)
isl.isl_schedule_node_child = isl_schedule_node_child
@staticmethod
def isl_schedule_node_get_prefix_schedule_multi_union_pw_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_node_get_prefix_schedule_multi_union_pw_aff', retType, argTypes, args)
isl.isl_schedule_node_get_prefix_schedule_multi_union_pw_aff = isl_schedule_node_get_prefix_schedule_multi_union_pw_aff
@staticmethod
def isl_schedule_node_get_prefix_schedule_union_map(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_node_get_prefix_schedule_union_map', retType, argTypes, args)
isl.isl_schedule_node_get_prefix_schedule_union_map = isl_schedule_node_get_prefix_schedule_union_map
@staticmethod
def isl_schedule_node_get_prefix_schedule_union_pw_multi_aff(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_node_get_prefix_schedule_union_pw_multi_aff', retType, argTypes, args)
isl.isl_schedule_node_get_prefix_schedule_union_pw_multi_aff = isl_schedule_node_get_prefix_schedule_union_pw_multi_aff
@staticmethod
def isl_schedule_node_get_schedule(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_node_get_schedule', retType, argTypes, args)
isl.isl_schedule_node_get_schedule = isl_schedule_node_get_schedule
@staticmethod
def isl_schedule_node_parent(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_node_parent', retType, argTypes, args)
isl.isl_schedule_node_parent = isl_schedule_node_parent
@staticmethod
def isl_schedule_node_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_schedule_node_free', retType, argTypes, args)
isl.isl_schedule_node_free = isl_schedule_node_free
@staticmethod
def isl_schedule_node_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_node_to_str', retType, argTypes, args)
isl.isl_schedule_node_to_str = isl_schedule_node_to_str
@staticmethod
def isl_schedule_node_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_schedule_node_copy', retType, argTypes, args)
isl.isl_schedule_node_copy = isl_schedule_node_copy

class union_access_info:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and args[0].__class__ is union_map:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_union_access_info_from_sink(isl.isl_union_map_copy(args[0].ptr))
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_access_info_free(self.ptr)
    def __str__(self):
        return str(isl.isl_union_access_info_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_access_info("""%s""")' % s
        else:
            return 'isl.union_access_info("%s")' % s
    def compute_flow(arg0):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_compute_flow(isl.isl_union_access_info_copy(arg0.ptr))
        return union_flow(ctx=ctx, ptr=res)
    def set_may_source(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_may_source(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_access_info(ctx=ctx, ptr=res)
    def set_must_source(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_must_source(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_access_info(ctx=ctx, ptr=res)
    def set_schedule(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is schedule:
                arg1 = schedule(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_schedule(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_schedule_copy(arg1.ptr))
        return union_access_info(ctx=ctx, ptr=res)
    def set_schedule_map(arg0, arg1):
        try:
            if not arg0.__class__ is union_access_info:
                arg0 = union_access_info(arg0)
        except:
            raise
        try:
            if not arg1.__class__ is union_map:
                arg1 = union_map(arg1)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_access_info_set_schedule_map(isl.isl_union_access_info_copy(arg0.ptr), isl.isl_union_map_copy(arg1.ptr))
        return union_access_info(ctx=ctx, ptr=res)

@staticmethod
def isl_union_access_info_from_sink(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_access_info_from_sink', retType, argTypes, args)
isl.isl_union_access_info_from_sink = isl_union_access_info_from_sink
@staticmethod
def isl_union_access_info_compute_flow(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_access_info_compute_flow', retType, argTypes, args)
isl.isl_union_access_info_compute_flow = isl_union_access_info_compute_flow
@staticmethod
def isl_union_access_info_set_may_source(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_access_info_set_may_source', retType, argTypes, args)
isl.isl_union_access_info_set_may_source = isl_union_access_info_set_may_source
@staticmethod
def isl_union_access_info_set_must_source(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_access_info_set_must_source', retType, argTypes, args)
isl.isl_union_access_info_set_must_source = isl_union_access_info_set_must_source
@staticmethod
def isl_union_access_info_set_schedule(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_access_info_set_schedule', retType, argTypes, args)
isl.isl_union_access_info_set_schedule = isl_union_access_info_set_schedule
@staticmethod
def isl_union_access_info_set_schedule_map(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0, a_1]
  return js.globals.Module.ccall('isl_union_access_info_set_schedule_map', retType, argTypes, args)
isl.isl_union_access_info_set_schedule_map = isl_union_access_info_set_schedule_map
@staticmethod
def isl_union_access_info_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_union_access_info_free', retType, argTypes, args)
isl.isl_union_access_info_free = isl_union_access_info_free
@staticmethod
def isl_union_access_info_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_access_info_to_str', retType, argTypes, args)
isl.isl_union_access_info_to_str = isl_union_access_info_to_str
@staticmethod
def isl_union_access_info_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_access_info_copy', retType, argTypes, args)
isl.isl_union_access_info_copy = isl_union_access_info_copy

class union_flow:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_union_flow_free(self.ptr)
    def __str__(self):
        return str(isl.isl_union_flow_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.union_flow("""%s""")' % s
        else:
            return 'isl.union_flow("%s")' % s
    def get_full_may_dependence(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_full_may_dependence(arg0.ptr)
        return union_map(ctx=ctx, ptr=res)
    def get_full_must_dependence(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_full_must_dependence(arg0.ptr)
        return union_map(ctx=ctx, ptr=res)
    def get_may_dependence(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_may_dependence(arg0.ptr)
        return union_map(ctx=ctx, ptr=res)
    def get_may_no_source(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_may_no_source(arg0.ptr)
        return union_map(ctx=ctx, ptr=res)
    def get_must_dependence(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_must_dependence(arg0.ptr)
        return union_map(ctx=ctx, ptr=res)
    def get_must_no_source(arg0):
        try:
            if not arg0.__class__ is union_flow:
                arg0 = union_flow(arg0)
        except:
            raise
        ctx = arg0.ctx
        res = isl.isl_union_flow_get_must_no_source(arg0.ptr)
        return union_map(ctx=ctx, ptr=res)

@staticmethod
def isl_union_flow_get_full_may_dependence(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_flow_get_full_may_dependence', retType, argTypes, args)
isl.isl_union_flow_get_full_may_dependence = isl_union_flow_get_full_may_dependence
@staticmethod
def isl_union_flow_get_full_must_dependence(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_flow_get_full_must_dependence', retType, argTypes, args)
isl.isl_union_flow_get_full_must_dependence = isl_union_flow_get_full_must_dependence
@staticmethod
def isl_union_flow_get_may_dependence(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_flow_get_may_dependence', retType, argTypes, args)
isl.isl_union_flow_get_may_dependence = isl_union_flow_get_may_dependence
@staticmethod
def isl_union_flow_get_may_no_source(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_flow_get_may_no_source', retType, argTypes, args)
isl.isl_union_flow_get_may_no_source = isl_union_flow_get_may_no_source
@staticmethod
def isl_union_flow_get_must_dependence(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_flow_get_must_dependence', retType, argTypes, args)
isl.isl_union_flow_get_must_dependence = isl_union_flow_get_must_dependence
@staticmethod
def isl_union_flow_get_must_no_source(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_flow_get_must_no_source', retType, argTypes, args)
isl.isl_union_flow_get_must_no_source = isl_union_flow_get_must_no_source
@staticmethod
def isl_union_flow_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_union_flow_free', retType, argTypes, args)
isl.isl_union_flow_free = isl_union_flow_free
@staticmethod
def isl_union_flow_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_flow_to_str', retType, argTypes, args)
isl.isl_union_flow_to_str = isl_union_flow_to_str
@staticmethod
def isl_union_flow_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_union_flow_copy', retType, argTypes, args)
isl.isl_union_flow_copy = isl_union_flow_copy

class val:
    def __init__(self, *args, **keywords):
        if "ptr" in keywords:
            self.ctx = keywords["ctx"]
            self.ptr = keywords["ptr"]
            return
        if len(args) == 1 and type(args[0]) == int:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_val_int_from_si(self.ctx, args[0])
            return
        if len(args) == 1 and type(args[0]) == str:
            self.ctx = Context.getDefaultInstance()
            self.ptr = isl.isl_val_read_from_str(self.ctx, args[0])
            return
        raise Error
    def __del__(self):
        if hasattr(self, 'ptr'):
            isl.isl_val_free(self.ptr)
    def __str__(self):
        return str(isl.isl_val_to_str(self.ptr))
    def __repr__(self):
        s = str(self)
        if '"' in s:
            return 'isl.val("""%s""")' % s
        else:
            return 'isl.val("%s")' % s
    @staticmethod
    def infty():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_infty(ctx)
        return val(ctx=ctx, ptr=res)
    @staticmethod
    def nan():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_nan(ctx)
        return val(ctx=ctx, ptr=res)
    @staticmethod
    def neginfty():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_neginfty(ctx)
        return val(ctx=ctx, ptr=res)
    @staticmethod
    def negone():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_negone(ctx)
        return val(ctx=ctx, ptr=res)
    @staticmethod
    def one():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_one(ctx)
        return val(ctx=ctx, ptr=res)
    @staticmethod
    def zero():
        ctx = Context.getDefaultInstance()
        res = isl.isl_val_zero(ctx)
        return val(ctx=ctx, ptr=res)

@staticmethod
def isl_val_int_from_si(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'number']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_val_int_from_si', retType, argTypes, args)
isl.isl_val_int_from_si = isl_val_int_from_si
@staticmethod
def isl_val_read_from_str(a_0, a_1):
  retType = 'number'
  argTypes = ['number', 'string']
  args = [a_0.ptr, a_1]
  return js.globals.Module.ccall('isl_val_read_from_str', retType, argTypes, args)
isl.isl_val_read_from_str = isl_val_read_from_str
@staticmethod
def isl_val_infty(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0.ptr]
  return js.globals.Module.ccall('isl_val_infty', retType, argTypes, args)
isl.isl_val_infty = isl_val_infty
@staticmethod
def isl_val_nan(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0.ptr]
  return js.globals.Module.ccall('isl_val_nan', retType, argTypes, args)
isl.isl_val_nan = isl_val_nan
@staticmethod
def isl_val_neginfty(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0.ptr]
  return js.globals.Module.ccall('isl_val_neginfty', retType, argTypes, args)
isl.isl_val_neginfty = isl_val_neginfty
@staticmethod
def isl_val_negone(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0.ptr]
  return js.globals.Module.ccall('isl_val_negone', retType, argTypes, args)
isl.isl_val_negone = isl_val_negone
@staticmethod
def isl_val_one(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0.ptr]
  return js.globals.Module.ccall('isl_val_one', retType, argTypes, args)
isl.isl_val_one = isl_val_one
@staticmethod
def isl_val_zero(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0.ptr]
  return js.globals.Module.ccall('isl_val_zero', retType, argTypes, args)
isl.isl_val_zero = isl_val_zero
@staticmethod
def isl_val_free(a_0):
  retType = None
  argTypes = ['number']
  args = [a_0.ptr]
  js.globals.Module.ccall('isl_val_free', retType, argTypes, args)
isl.isl_val_free = isl_val_free
@staticmethod
def isl_val_to_str(a_0):
  retType = 'string'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_val_to_str', retType, argTypes, args)
isl.isl_val_to_str = isl_val_to_str
@staticmethod
def isl_val_copy(a_0):
  retType = 'number'
  argTypes = ['number']
  args = [a_0]
  return js.globals.Module.ccall('isl_val_copy', retType, argTypes, args)
isl.isl_val_copy = isl_val_copy
