class LeakzException(Exception):
    pass


class LeakzNotLeaked(LeakzException):
    pass


class LeakzRequestException(LeakzException):
    pass


class LeakzJSONDecodeException(LeakzException):
    pass
