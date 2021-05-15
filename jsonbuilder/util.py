import re

from dateutil.relativedelta import relativedelta
import pandas


def translate(obj, t_dict):
    if isinstance(obj, pandas.Series):
        def _translate(value):
            return t_dict.get(value, value)
        return obj.map(_translate)
    else:
        return t_dict.get(obj, obj)

def date(obj, **kwargs):
    return pandas.to_datetime(obj, **kwargs)

def delta(obj):
    if isinstance(obj, (pandas.Timedelta, relativedelta)):
        return obj
    elif isinstance(obj, str):
        obj = obj.lower()

        if obj in ('o/n', 'on'):
            return relativedelta(days=1)
        if obj in ('t/n', 'tn'):
            return relativedelta(days=2)

        units = dict(d=0,w=0,m=0,y=0)
        nodes = re.findall(r'[A-Za-z]+|[-+]?[0-9]*\.?[0-9]+', obj)
        try:
            while nodes:
                value = int(float(nodes.pop(0)))
                unit = nodes.pop(0)
                units[unit] += value
            return relativedelta(days=units['d'], weeks=units['w'], months=units['m'], years=units['y'])
        except Exception:
            raise Exception('Invalid delta-string: {}'.format(obj))
    else:
        raise Exception('Invalid delta-object: {}'.format(obj))
