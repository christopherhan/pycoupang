import re

class BaseAPI:
    @staticmethod
    def _to_camel_case(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    @classmethod
    def _process_kwargs(cls, **kwargs):
        return {cls._to_camel_case(k): v for k, v in kwargs.items() if v is not None}