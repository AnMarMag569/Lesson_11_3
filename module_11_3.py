from pprint import pprint
def introspection_info(obj):

  info = {}
  info['Тип объекта:'] = type(obj)
  info['Список атрибутов :'] = dir(obj)
  info['Список методов:'] = [method for method in dir(obj) if callable(getattr(obj, method))]
  info['Модуль, к которому принадлежит объект :'] = obj.__module__ if hasattr(obj, '__module__') else 'У объекта нет модуля'
  info['Документация:'] = obj.__doc__ if obj.__doc__ else 'Документации нет (('

  return info

rezult = introspection_info([1,2,3])
pprint(rezult)
print()
rezult = rezult = introspection_info(introspection_info)
pprint(rezult)