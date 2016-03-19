'''
This module define Filter class and the subclass of that.
'''

from abc import ABCMeta, abstractmethod
import yaml

class Filter(metaclass=ABCMeta):
    '''
    This is abstract class for feed fitering.
    '''
    def __init__(self, filterd_feed):
        '''
        :param filterd_feed: object of filter
        :type filterd_feed: Filter
        '''
        self._filterd_feed = filterd_feed

    def filtering(self):
        '''
        this method
        '''
        return self.__class__.filtering_rule(self._filterd_feed.filtering())

    @classmethod
    @abstractmethod
    def filtering_rule(cls, feed):
        '''
        This method define fintering_rule
        :rtype: dict
        '''
        ...


class UserNameBlackListFilter(Filter):
    '''
    This is Filter subclass to remove user registerd in blackliste.
    '''
    @classmethod
    def filtering_rule(cls, feed):
        '''
        :param dict feed: api_feed_dict
        :rtype: dict
        :return: filtered dict
        '''
        config = yaml.load(open('config.yml'))
        blacklist = config['filter_rule']['user_name']
        return [post for post in feed if post['user']['url_name'] not in blacklist]
