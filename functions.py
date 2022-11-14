import datetime
import time
import redditcleaner
import re
import pandas as pd
from psaw import PushshiftAPI


def time_stamp(date_str):
    """
    Create UNIX timestamp from %d/%m/%Y format string.
    eg: 26/06/2022
    """
    return int(time.mktime(datetime.datetime.strptime(date_str, "%d/%m/%Y").timetuple()))


def clean_text_arr(text_arr):
    """
    Removes all non alphabetical characters from string.
    Keeps numbers.
    """
    text_arr = text_arr.map(redditcleaner.clean)
    text_arr = text_arr.apply(lambda x: re.sub('\W+', ' ', x))

    return text_arr


def retrieve_data_submissions(subreddit, start_date, end_date, limit):
    """
    Retrieves data from Pushshift reddit api.
    This function is not as complete as search_submissions().
    Only afew parameters are used.

    Returns a pandas DataFrame object.

    ==========
    Arguments:

    subreddit : str
        Non case sensitive string of a Reddit subreddit

    start_date : str
        String representation of a date in %d/%m/%Y

    end_date : str
        String representation of a date in %d/%m/%Y

    limit : int
        The maximum amount of submission to appear in the DataFrame
    """
    api = PushshiftAPI()
    s = time_stamp(start_date)
    e = time_stamp(end_date)

    submissions = api.search_submissions(subreddit=subreddit, limit=limit, after=s, before=e)
    df = pd.DataFrame([row.d_ for row in submissions])

    return df


def retrieve_data_comments(subreddit, start_date, end_date, limit):
    """
    Retrieves data from Pushshift reddit api.
    This function is not as complete as search_comments().
    Only afew parameters are used.

    Returns a pandas DataFrame object.

    ==========
    Arguments:

    subreddit : str
        Non case sensitive string of a Reddit subreddit

    start_date : str
        String representation of a date in %d/%m/%Y

    end_date : str
        String representation of a date in %d/%m/%Y

    limit : int
        The maximum amount of submission to appear in the DataFrame
    """ 
    api = PushshiftAPI()
    s = time_stamp(start_date)
    e = time_stamp(end_date)

    comments = api.search_comments(subreddit=subreddit, limit=limit, after=s, before=e)
    df = pd.DataFrame([row.d_ for row in comments])

    return df