# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class ReadWriteSerializerMixin(object):
    """This mixin returns proper serializer depending on HTTP method"""

    list_serializer = None
    retrieve_serializer = None
    write_serializer = None

    def get_serializer_class(self):
        if not (self.list_serializer):
            raise NotImplementedError(
                'You must define at least "list_serializer"'
            )

        if self.action == 'retrieve' and self.retrieve_serializer is not None:
            return self.retrieve_serializer
        elif self.request.method in ('POST', 'PUT', 'PATCH') and\
                self.write_serializer is not None:
            return self.write_serializer
        else:
            return self.list_serializer
