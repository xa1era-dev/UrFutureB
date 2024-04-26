import inspect
import sys
import types
from .course import *
from .responses import * 
from .exceptions import *

def filter_schema_classes(obj):
    return inspect.isclass(obj) and issubclass(obj, BaseModel) and __name__ in obj.__module__

schema_classes_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__], filter_schema_classes)]
SCHEMA_CLASSES: types.UnionType = schema_classes_list.pop(0)
for i in range(len(schema_classes_list)):
    SCHEMA_CLASSES = SCHEMA_CLASSES.__or__(schema_classes_list.pop(0))