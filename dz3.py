class Url:

    def __init__(self, scheme: str, authority: str, path: list = None, query: dict = None, fragment: str = None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        return self.__str__() == other

    def __str__(self):

        def path():
            pth = '/'
            for i in self.path:
                if self.path.index(i) == 0:
                    pth += i
                else:
                    pth += '/' + i
            return pth

        def query():
            qry = '?'
            for i in range(len(self.query)):
                if i < len(self.query) - 1:
                    qry += f'{list(self.query.keys())[i]}={list(self.query.values())[i]}&'
                else:
                    qry += f'{list(self.query.keys())[i]}={list(self.query.values())[i]}'
            return qry

        return (f"{self.scheme}://{self.authority}{path() if self.path else ''}"
                f"{query() if self.query else ''}{'#' + self.fragment if self.fragment else ''}")


class HttpsUrl(Url):

    def __init__(self, authority, path=None, query=None, fragment=None):
        scheme = 'https'
        super().__init__(scheme, authority, path, query, fragment)


class HttpUrl(Url):

    def __init__(self, authority, path=None, query=None, fragment=None):
        scheme = 'http'
        super().__init__(scheme, authority, path, query, fragment)


class GoogleUrl(HttpsUrl):

    def __init__(self, path=None, query=None, fragment=None):
        authority = 'google.com'
        super().__init__(authority, path, query, fragment)


class WikiUrl(HttpsUrl):

    def __init__(self, path=None, query=None, fragment=None):
        authority = 'wikipedia.org'
        super().__init__(authority, path, query, fragment)


# reqres = HttpsUrl(authority='reqres.in')
# google = GoogleUrl(query={'q': 'python', 'result': 'json'})
# wiki = WikiUrl(path=['wiki', 'python'], fragment='Computing')
# print(reqres.scheme)
# print(google)
# print(wiki)


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'


class UrlCreator:

    def __init__(self, scheme, authority):
        self.scheme = scheme
        self.authority = authority
        self.path = None
        self.query = None
        self.fragment = None

    __eq__ = Url.__eq__

    __str__ = Url.__str__

    def __getattr__(self, item):
        if not self.path:
            self.path = []
            self.path.append(item)
        else:
            self.path.append(item)
        return self

    def __call__(self, *args, **kwargs):
        if args:
            self.path = list(args)
        if kwargs:
            self.query = kwargs
        if not args and not kwargs:
            self.path = None
            self.query = None
        return self

    def _create(self):
        return Url(scheme=self.scheme, authority=self.authority, path=self.path, query=self.query, fragment=self.fragment)


url_creator = UrlCreator(scheme='https', authority='docs.python.org')
assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
assert url_creator('api', 'v1', 'list') == 'https://docs.python.org/api/v1/list'
assert url_creator('api', 'v1', 'list', q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'
assert (url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create() ==
        'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default')
