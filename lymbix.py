import urllib
import urllib2
import json


class Lymbix:

    API_BASE = 'https://gyrus.lymbix.com/'
    TONALIZE_MULTIPLE = 'tonalize_multiple'
    TONALIZE_DETAILED = 'tonalize_detailed'
    TONALIZE = 'tonalize'
    FLAG_RESPONSE = 'flag_response'

    def __init__(self, authentication_key):
        '''
        Args:
                -authentication_key: your Lymbix authentication key
        '''
        if authentication_key is None or len(authentication_key) == 0:
            raise Exception('You must include your authentication key')

        self.authentication_key = authentication_key

    ''' utility functions '''

    def _get_headers(self):
        headers = {
            'Authentication': self.authentication_key,
            'Accept': 'application/json',
            'Version': '2.2'}
        return headers

    def _prep_data(self, data, options):
        if options:
            data.update(options)
        for key, value in data.iteritems():
            data[key] = json.dumps(value)
        return urllib.urlencode(data)

    ''' api methods '''

    def tonalize_multiple(self, articles, options=None):
        '''
        tonalize multiple articles

        Args:
                -articles: articles to tonalize
                -options: additional parameters (reference_ids and return_fields)

        Returns:
                -see the api documentation for the format of this object
        '''
        if articles is None or len(articles) == 0:
            raise Exception('You must include articles to tonalize')

        url = self.API_BASE + self.TONALIZE_MULTIPLE
        data = {'articles': articles}
        data = self._prep_data(data, options)

        headers = self._get_headers()
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        return json.loads(response.read())

    def tonalize_detailed(self, article, options=None):
        '''
        tonalize an article

        Args:
                -article: article to tonalize
                -options: additional parameters (reference_id and return_fields)

        Returns:
                -see the api documentation for the format of this object
        '''
        if article is None or len(article) == 0:
            raise Exception('You must include an article to tonalize')

        url = self.API_BASE + self.TONALIZE_DETAILED

        data = {'article': article}
        data = self._prep_data(data, options)

        headers = self._get_headers()
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        return json.loads(response.read())

    def tonalize(self, article, options=None):
        '''
        tonalize an article

        Args:
                -article: article to tonalize
                -options: additional parameters (reference_id and return_fields)

        Returns:
                -see the api documentation for the format of this object
        '''
        if article is None or len(article) == 0:
            raise Exception('You must include an article to tonalize')

        url = self.API_BASE + self.TONALIZE
        data = {'article': article}
        data = self._prep_data(data, options)

        headers = self._get_headers()
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        return json.loads(response.read())

    def flag_response(self, phrase, api_method=None, api_version='2.2', callback_url=None, options=None):
        '''
        flag a response as inaccurate

        Args:
                -phrase: the phrase that returns an inaccurate response
                -api_method: the method that returns an inaccurate response
                -api_version: the version that returns an inaccurate response
                -callback_url: a url to call when the phrase has been re-rated
                -options: additional parameters (reference_id)

        Returns:
                -see the api documentation for the format of this object
        '''
        if phrase is None or len(phrase) == 0:
            raise Exception('You must include a phrase to flag')

        url = self.API_BASE + self.FLAG_RESPONSE

        data = {'phrase': phrase}
        if (api_method is not None):
            data['apiMethod'] = api_method
        if (api_version is not None):
            data['apiVersion'] = api_version
        if (callback_url is not None):
            data['callbackUrl'] = callback_url
        data = self._prep_data(data, options)

        headers = self._get_headers()
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        return response.read()
