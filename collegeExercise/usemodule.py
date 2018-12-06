#using module example
#import mymodule as mx
import importlib.util
spec = importlib.util.spec_from_file_location("exe10_Operators", "C:\\Users\\Admin\\Documents\\exe10_Operators.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


#foo.MyClass()

#mx.greeting()

