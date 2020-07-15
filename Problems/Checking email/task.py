def check_email(_string):
    if ' ' not in _string and '@' in _string:
        if _string.rfind('.') > _string.find('@') and not _string.rfind('.') == _string.find('@')+1:
            return True
        return False
    return False

