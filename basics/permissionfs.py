from logging import exception


def login_required(obj):
    if not obj.is_aunthenticated:
        raise exception("USER NO REGISTERED")