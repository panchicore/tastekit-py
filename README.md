# tastekit-py
:copyright: (c) 2012 by Luis Pallares, for Aquehorajuega.co.
:license: Apache2, see LICENSE for more details.

TasteKit is a recommendation engine API. No need to implement complex algorithms or manage your own recommendations.
To get started, sign up for an API key: http://www.taste-kit.com/

## example:

```
from tastekit import tastekit

def send_tastekit(user, model_type, object, action=None):
    """
    Send to recommendation engine if user likes or dislikes a team or competition.
    Send to tastekit something like:
    user "user_1" likes "team_1"
    user "user_1" dislikes "team_4234"
    user "user_222" likes "competition_333"
    :param user: User object
    :param model_type: name of the object: team or competition
    :param object: Object in action
    :param action: None if dislike, else likes.
    :return:
    """
    user_id = "user_{}".format(user.id)
    item_id = "{0}_{1}".format(model_type, object.id)
    if action is None:
        print '{0} dislikes {1} ({2})'.format(user_id, item_id, object)
        tastekit.dislikes(user_id, item_id)
    else:
        print '{0} likes {1} ({2})'.format(user_id, item_id, object)
        tastekit.likes(user_id, item_id)
```


