from html.parser import HTMLParser


class BoldParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.elements = []
        self.allowed_tags = ['strong']

    def handle_starttag(self, tag, attrs):
        if tag in self.allowed_tags:
            self.elements.append("<{0}>".format(tag))

    def handle_endtag(self, tag):
        if tag in self.allowed_tags:
            self.elements.append("</{0}>".format(tag))
        if tag == 'p':
            self.elements.append("\n")

    def handle_data(self, data):
        if data:
            self.elements.append(data.strip())

    def get_data(self):
        return ''.join(self.elements)

    def normalize(self, data):
        self.elements.clear()
        self.feed(data)
        return self.get_data()
