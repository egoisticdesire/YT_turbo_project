class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, some_str: str):
        if isinstance(some_str, str):
            return some_str.upper()
        return some_str.title.upper()
