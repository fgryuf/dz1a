__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    if(seconds == 0):
        return '00s'
    days = int(seconds // (3600*24))
    seconds = seconds % (3600*24)
    hours = int(seconds // 3600)
    seconds = seconds % 3600
    mins = int(seconds // 60)
    sec = seconds % 60
    ans = ''
    if(days != 0) :
        if(days < 10) : 
            ans = ans + '0' + str(days) + 'd'
        else :
            ans = ans + str(days) + 'd'
    if(hours != 0) :
        if(hours < 10) :
            ans = ans + '0' + str(hours) + 'h'
        else : 
            ans = ans + str(hours) + 'h'
    elif(days != 0 and hours == 0):
        ans = ans + '00' + 'h'
    if(mins != 0) :
        if(mins < 10) :
            ans = ans + '0' + str(mins) + 'm'
        else:
            ans = ans + str(mins) + 'm'
    elif((mins == 0 and hours != 0) or (mins == 0 and days != 0)):
        ans = ans + '00'  + 'm'
    if(sec != 0):
        if(sec < 10):
            ans = ans + '0' + str(sec) + 's'
        else:
            ans = ans + str(sec) + 's'
    else :
        ans = ans + '00' + 's'

    return ans