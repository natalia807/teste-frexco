from frexco.apps.core.renderers import FrexcoJSONRenderer


class UserJSONRenderer(FrexcoJSONRenderer):
    object_label = 'user'
    pagination_object_label = 'users'
    pagination_count_label = 'usersCount'