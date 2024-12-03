from pprint import pprint
def introspection_info(obj):
  info = {
    'Тип объекта': type(obj).__name__,
    'Список атрибутов': [],
    'Список методов': [],
    'Модуль, к которому принадлежит объект': obj.__module__ if hasattr(obj, '__module__') else 'Бесхозный обЪект',
    'Документация': obj.__doc__ if obj.__doc__ else 'Документации нет (('
  }

  for attr in dir(obj):
    if callable(getattr(obj, attr)):
      info['Список методов'].append(attr)
    else:
      info['Список атрибутов'].append(attr)
  return info

rezult = introspection_info([1,2,3])
pprint(rezult)
print()
rezult = introspection_info(introspection_info)
pprint(rezult)