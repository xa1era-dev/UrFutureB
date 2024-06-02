import inspect
import sys
import types
from pydantic import BaseModel
from .course import Course
from .responses import NotFoundApiError, MissingArgumetsError, UnauthorizedApiError, NotImplementError
from .exceptions import *
from .lesson import Lesson, LessonTime
from .profession import Profession, WorkData
from .teacher import BaseTeacher
from .choices import LessonTimeChoice
from .iot import IOT, IOTTime
from .discipline import Discipline
from .half_period import HalfPeroid
from .teacher import BaseTeacher, Teacher

def filter_schema_classes(obj):
    return inspect.isclass(obj) and issubclass(obj, BaseModel) and __name__ in obj.__module__

def filter_exception_classes(obj):
    return filter_schema_classes(obj) and "Error" in obj.__name__

__all_schema_classes_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__], filter_schema_classes)]
ALL_SCHEMA_CLASSES: types.UnionType = __all_schema_classes_list.pop(0)
for i in range(len(__all_schema_classes_list)):
    ALL_SCHEMA_CLASSES = ALL_SCHEMA_CLASSES.__or__(__all_schema_classes_list.pop(0))

SCHEMA_ERRORS_LIST = [obj for name, obj in inspect.getmembers(sys.modules[__name__], filter_exception_classes)]

TUPLES_ERR_EXC: list[tuple[BaseModel, Exception]] = [(err, err._exc.default) for err in SCHEMA_ERRORS_LIST]