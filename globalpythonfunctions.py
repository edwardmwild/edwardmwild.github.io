def version(): return("v1.0.1, modified 2023.07.01") #§

# ============================================================================ #
#                                 functions                                    #
# ============================================================================ #
#                                                                              #
#                      note: add 31 to every line count!                       #
#                                                                              #
# ============================================================================ #
#                                                                              #
#    1 - floatformatter                                                        #
#      - formats a float to look nice (e.g. 453b or 3.8t instead of            #
#            453967305626 or 3845267490257)                                    #
#      - lines 1 --> 85                                                        #
#                                                                              #
#    2 - discordtimestamp                                                      #
#      - returns a discord timestamp for any give datetime object              #
#      - lines 87 --> 113                                                      #
#                                                                              #
#    3 - finddate_weeks                                                        #
#      - jumps backwards or forwards in x week intervals to find the next date #
#            of something that reoccurs every x weeks                          #
#      - lines 115 --> 144                                                     #
#                                                                              #
#    4 - finddate_days                                                         #
#      - jumps backwards or forwards in x day intervals to find the next date  #
#            of something that reoccurs every x days                           #
#      - lines 146 --> 175                                                     #
#                                                                              #
# ============================================================================ #

def floatformatter(value:float=None, mode:int=0, space:bool=None):
    """
    modes:
     0: string w/ number and letter (e.g. 3.6b)
     1: string w/ number and word (e.g. 3.6 billion)
     2: just the letter (e.g. b)
     3: just the word (e.g. billion)
    space:
     adds a space between number and quantity (modes 0 and 1 only).
     defaults to true for mode 1, false otherwise
    """

    if value == None: return("undefined")

    if space == None:
        if mode == 1: space = True
        else: space = False

    letter = [
        ["inf", 10**18, False],
        ["q",   10**15, True],
        ["t",   10**12, True],
        ["b",   10**9,  True],
        ["m",   10**6,  True],
        ["k",   10**3,  True]
    ]

    word = [
        ["infinity",          10**66, False],
        ["vigintillion",      10**63, True],
        ["novemdecillion",    10**60, True],
        ["octodecillion",     10**57, True],
        ["septendecillion",   10**54, True],
        ["sexdecillion",      10**51, True],
        ["quindecillion",     10**48, True],
        ["quattuordecillion", 10**45, True],
        ["tredecillion",      10**42, True],
        ["duodecillion",      10**39, True],
        ["undecillion",       10**36, True],
        ["decillion",         10**33, True],
        ["nonillion",         10**30, True],
        ["octillion",         10**27, True],
        ["septillion",        10**24, True],
        ["sextillion",        10**21, True],
        ["quintillion",       10**18, True],
        ["quadrillion",       10**15, True],
        ["trillion",          10**12, True],
        ["billion",           10**9,  True],
        ["million",           10**6,  True],
        ["thousand",          10**3,  True]
    ]

    if value < 0:
        negative = "-"
        value = abs(value)
    else: negative = ""

    found = False

    if mode == 0 or mode == 2:
        for weight in letter:
            if value > weight[1]:
                found = True
                if not weight[2]: return(weight[0])
                else:
                    if mode == 0:
                        if value > 10*weight[1]: number = str(round(value/weight[1]))
                        elif value > weight[1]: number = str(round(value/weight[1], 1))
                        
                        if space: return(negative+number+" "+weight[0])
                        else: return(negative+number+weight[0])
                    else: return(weight[0])
            if found: break
        if not found: return(str(value))

    elif mode == 1 or mode == 3:
        for weight in word:
            if value > weight[1]:
                found = True
                if not weight[2]: return(weight[0])
                else:
                    if mode == 1:
                        if value > 10*weight[1]: number = str(round(value/weight[1]))
                        elif value > weight[1]: number = str(round(value/weight[1], 1))
                        
                        if space: return(negative+number+" "+weight[0])
                        else: return(negative+number+weight[0])
                    else: return(weight[0])
            if found: break
        if not found: return(str(value))

    return("undefined")
# formats a float to look nice (e.g. 453b or 3.8t instead of 453967305626 or 3845267490257)

def discordtimestamp(datetime_object, mode:int=5):
    """
    modes:
     0: relative (e.g. 36 seconds ago)
     1: short time (e.g. 07:05)
     2: long time (e.g. 07:05:16)
     3: numbered date (e.g. 01/07/2023)
     4: short date (e.g. 1 July 2023)
     5: short date w/ time (e.g. 1 July 2023 at 07:05)
     6: long date w/ time (e.g. Saturday, 1 July 2023 at 07:05)
    """

    from time import mktime

    timeformat = [
        ":R>",
        ":t>",
        ":T>",
        ":d>",
        ":D>",
        ":f>",
        ":F>"
    ]

    try: return("<t:"+str(round(mktime(datetime_object.timetuple())))+timeformat[mode])
    except: return("`undefined`")
# returns a discord timestamp for any give datetime object

def finddate_weeks(weeks:int=4, year:int=None, month:int=None, day:int=None, hours:int=0, minutes:int=0, seconds:int=0):
    """
    inputs:
     weeks: how many weeks to jump (defaults to 4)
     year, month, day: required. these are the date you wish to work forwards/backwards from. if you don't specify these, the function will return the current time.
     hours, minutes, seconds: defaults to 0: adds a time onto the date.

    outputs:
     0: datetime object
     1: date object (no time)
     2: bool if it's today
    """

    from datetime import date, timedelta, time, datetime

    if year == None or month == None or day == None: return(date.today(), datetime.now(), True)

    inputdate = date(year=year, month=month, day=day)
    now = date.today()

    while inputdate > now: inputdate -= timedelta(weeks=weeks)
    while inputdate < now: inputdate += timedelta(weeks=weeks)
    
    if inputdate == now: today = True
    else: today = False

    outputtime = datetime.combine(date=inputdate, time=time(hours, minutes, seconds))
    
    return(inputdate, outputtime, today)
# jumps backwards or forwards in x week intervals to find the next date of something that reoccurs every x weeks

def finddate_days(days:int=7, year:int=None, month:int=None, day:int=None, hours:int=0, minutes:int=0, seconds:int=0):
    """
    inputs:
     days: how many days to jump (defaults to 7)
     year, month, day: required. these are the date you wish to work forwards/backwards from. if you don't specify these, the function will return the current time.
     hours, minutes, seconds: defaults to 0: adds a time onto the date.

    outputs:
     0: datetime object
     1: date object (no time)
     2: bool if it's today
    """

    from datetime import date, timedelta, time, datetime

    if year == None or month == None or day == None: return(date.today(), datetime.now(), True)

    inputdate = date(year=year, month=month, day=day)
    now = date.today()

    while inputdate > now: inputdate -= timedelta(days=days)
    while inputdate < now: inputdate += timedelta(days=days)
    
    if inputdate == now: today = True
    else: today = False

    outputtime = datetime.combine(date=inputdate, time=time(hours, minutes, seconds))
    
    return(inputdate, outputtime, today)
# jumps backwards or forwards in x day intervals to find the next date of something that reoccurs every x days

