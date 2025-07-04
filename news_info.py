class news_info:

    def __init__(self, title, source, description, link, image, publish_date):
        self.title = title
        self.source = source
        self.description = description
        self.link = link
        self.image = image
        self.summarization = ''
        self.publish_date = publish_date

    def valid_fields(self):
        fields = [
            self.title,
            self.source,
            self.description,
            self.link,
            self.image,
            self.publish_date
        ]
        return all(field is not None and field != '' for field in fields)