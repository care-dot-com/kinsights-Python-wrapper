import urllib
import urllib2
import json
import ssl


class Lymbix:

    API_BASE = 'http://api.lymbix.com/'
    TONALIZE_MULTIPLE = 'tonalize_multiple'
    TONALIZE_DETAILED = 'tonalize_detailed'
    TONALIZE = 'tonalize'
    FLAG_RESPONSE = 'flag_response'

    def __init__(self, authentication_key, verify_ssl=True):
        '''
        Args:
                -authentication_key: your Lymbix authentication key
        '''
        if not authentication_key:
            raise Exception('You must include your authentication key')

        self.authentication_key = authentication_key
        self.verify_ssl = verify_ssl

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

    def _call(self, url, data, returns_json=False):
        headers = self._get_headers()
        request = urllib2.Request(url, data, headers)
        if not self.verify_ssl and hasattr(ssl, '_create_unverified_context'):
            context = ssl._create_unverified_context()
            response = urllib2.urlopen(request, context=context)
        else:
            response = urllib2.urlopen(request)
        if returns_json:
            return json.loads(response.read())
        return response.read()

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
        if not articles:
            raise Exception('You must include articles to tonalize')

        url = self.API_BASE + self.TONALIZE_MULTIPLE
        data = {'articles': articles}
        data = self._prep_data(data, options)

        return self._call(url, data, returns_json=True)

    def tonalize_detailed(self, article, options=None):
        '''
        tonalize an article

        Args:
                -article: article to tonalize
                -options: additional parameters (reference_id and return_fields)

        Returns:
                -see the api documentation for the format of this object
        '''
        if not article:
            raise Exception('You must include an article to tonalize')

        url = self.API_BASE + self.TONALIZE_DETAILED

        data = {'article': article}
        data = self._prep_data(data, options)

        return self._call(url, data, returns_json=True)

    def tonalize(self, article, options=None):
        '''
        tonalize an article

        Args:
                -article: article to tonalize
                -options: additional parameters (reference_id and return_fields)

        Returns:
                -see the api documentation for the format of this object
        '''
        if not article:
            raise Exception('You must include an article to tonalize')

        url = self.API_BASE + self.TONALIZE
        data = {'article': article}
        data = self._prep_data(data, options)

        return self._call(url, data, returns_json=True)

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
        if not phrase:
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

        return self._call(url, data)
