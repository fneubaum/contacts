import json
import falcon


class ContactResource(object):
    def on_get_list(self, req, resp):
        cl = {
            'name': 'A contact list',
            'contacts': []
        }

        resp.body = json.dumps(cl)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200

    def on_post_list(self, req, resp):
        cl = {
            'name': 'A contact list',
            'contacts': []
        }

        resp.body = json.dumps(cl)
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200
