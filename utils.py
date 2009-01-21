#some useful methods we need ...

def get_next_month_year(year,month):
    """
    Method gets the next month and year
    """
    if month == 12 :
        return {
                'year':year+1,
                'month':1
                }
    else:
        return {
                'year':year,
                'month':month+1
                }

def get_prev_month_year(year,month):
    """
    Method gets the previous month and year
    """
    if month == 1 :
        return {
                'year':year-1,
                'month':12
                }
    else:
        return {'year':year,
                'month':month-1
                }

