import js
ctx = js.globals.Module._isl_ctx_alloc()
class Set:
  def __init__(self, ptr):
    self.ptr = ptr
  @staticmethod
  def from_str(string):
    retType = 'number'
    argTypes = ['number', 'string']
    args = [ctx, string]
    ptr = js.globals.Module.ccall('isl_set_read_from_str', retType, argTypes, args)
    return Set(ptr)
  def __repr__(self):
    p = js.globals.Module._isl_printer_to_str(ctx)
    p = js.globals.Module._isl_printer_print_set(p, self.ptr)
    string = js.globals.Module.ccall('isl_printer_get_str', 'string', ['number'], [p])
    return str(string)
  def intersect(self, set2):
     ptr1 = js.globals.Module._isl_set_copy(self.ptr)
     ptr2 = js.globals.Module._isl_set_copy(set2.ptr)
     ptr = js.globals.Module._isl_set_intersect(ptr1, ptr2)
     return Set(ptr)
  def union(self, set2):
     ptr1 = js.globals.Module._isl_set_copy(self.ptr)
     ptr2 = js.globals.Module._isl_set_copy(set2.ptr)
     ptr = js.globals.Module._isl_set_union(ptr1, ptr2)
     return Set(ptr)

