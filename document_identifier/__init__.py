import sys

__all__ = ["Identify"]


def Identify(scope=None, return_single=False, **kwargs):
    valid_formats = []
    
    if not scope: 
        raise ValueError('Invalid scope keyword')
        
    if hasattr(scope, '__iter__'):
        search_set = scope
    else:
        search_set = [getattr(sys.modules[scope.__name__], cls_name) for cls_name in scope.__all__]

    for LicenceClass in search_set:
        try:
            valid_formats.append(LicenceClass(**kwargs))
            if return_single:
                break
        except ValueError as e:
            pass
            #print "{0.__name__} raised {1}".format(LicenceClass, e)
            
    if len(valid_formats) <= 0:
        raise ValueError('Unknown Licence Type.')
        
    if return_single:
        return valid_formats[0]
    else:
        return valid_formats


class DocumentBase(object):
    Format = {}
    
    def __init__(self, **kwargs):
        regex_groups = {}
        for key in self.Format:
            if key not in kwargs:
                raise ValueError("Missing argument '{0}'".format(key))
        
            match_obj = self.Format[key].match(kwargs.get(key, ''))
            if match_obj:
                regex_groups.update(match_obj.groupdict())
            else:
                raise ValueError("Format['{0}'] did not match '{1}'".format(key, kwargs.get(key)))

        self.__dict__.update(**regex_groups)

    def __str__(self):
        return "{0.__class__.__name__} #{0.number}".format(self)
