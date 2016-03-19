'''
This module define Feed class.
'''

class Feed():
    '''
    This class is container about api feed.
    It is used by Filter Class.
    '''
    def __init__(self, feed):
        self._feed = feed

    def filtering(self):
        '''
        :rtype: dict
        '''
        return self._feed
