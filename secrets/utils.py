class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
        if "default_attr_value" in kwargs:
            self.default_attr_value = kwargs["default_attr_value"]

    # This is to avoid exception, little hacky
    def __getattribute__(self, attr):
        if "default_attr_value" not in self:
            return super(AttrDict, self).__getattribute__(attr)
        if attr not in self:
            return None
        return dict.get(self, attr)

    def set_default_attr_value(self, set_default=False):
        self.default_attr_value = set_default
