# -*- coding: utf-8 -*-

"""
:copyright: (c) 2012 by Luis Pallares, for Aquehorajuega.co.
:license: Apache2, see LICENSE for more details.

TasteKit is a recommendation engine API. No need to implement complex algorithms or manage your own recommendations.
To get started, sign up for an API key.

Items and Users are the core models of the API.

Items are the objects in your database that a User likes or dislikes.
When referencing an Item, you simply pass in a unique identifier as an item parameter for each request.
There is no need to dump your entire set of items into the database to begin with, nor is there a create
endpoint for items. This is explained below.

Users are users in your database, referenced by a unique identifier you pass in as the parameter user.

More documentation here: https://tastekit.api-docs.io/v1/
"""

import os
import requests

BASE_URL = "http://www.taste-kit.com/api/v1"
API_KEY = os.environ.get("TASTEKIT_API_KEY", "1aacec95ef775e81")

PARAMS = {
    "token": API_KEY
}
LIKES = "like"
DISLIKES = "dislike"


def likes(user_id, item_id, action=LIKES):
    """
    Like POST /api/v1/likes/like
    When a user "likes" an item.
    :param user_id:
    :param item_id:
    :param action:
    :return:
    """

    url = "{0}/likes/{1}".format(BASE_URL, action)

    data = {
        "user": str(user_id),
        "item": str(item_id)
    }
    res = requests.post(url, params=PARAMS, json=data)

    if not res.ok:
        raise Exception('Http {0}: {1}'.format(res.status_code, res.text))

    return True


def dislikes(user_id, item_id):
    """
    Dislike POST /api/v1/likes/dislike
    When a user "dislikes" an item.
    :param user_id:
    :param item_id:
    :return:
    """
    return likes(user_id, item_id, action=DISLIKES)


def recommendations(user_id):
    """
    Recommendations GET /api/v1/recommendations
    Retrieves the recommendations for a given user.
    This returns an array of identifiers for items, limit 10.

    Recommendations work based on the likes and dislikes of other users,
    no need to dump your entire set of items into the database. For example,
    say you're using a movie app that recommends you movies: you like Toy Story and Finding Nemo.
    Another user likes Toy Story, Finding Nemo, and Finding Dory. Since you have similar tastes,
    Finding Dory will be recommended to you.
    :param user_id:
    :return:
    """
    url = "{0}/recommendations".format(BASE_URL)

    data = {
        "user": str(user_id)
    }
    res = requests.get(url, params=PARAMS, json=data)

    if not res.ok:
        raise Exception('Http {0}: {1}'.format(res.status_code, res.text))

    print res.json()


def delete_item(item_id):
    """
    Delete Item DELETE /api/v1/items
    Deletes an item that any user has liked or disliked before.
    :param item_id:
    :return:
    """
    url = "{0}/items".format(BASE_URL)
    data = {
        "item": str(item_id)
    }
    res = requests.delete(url, params=PARAMS, json=data)

    if not res.ok and not res.status_code == 404:
        raise Exception('Http {0}: {1}'.format(res.status_code, res.text))

    return True


def delete_user(user_id):
    """
    Delete User DELETE /api/v1/items
    Deletes a user that has liked or disliked an item before.
    :param user_id:
    :return:
    """
    url = "{0}/users".format(BASE_URL)
    data = {
        "user": str(user_id)
    }
    res = requests.delete(url, params=PARAMS, json=data)

    if not res.ok and not res.status_code == 404:
        raise Exception('Http {0}: {1}'.format(res.status_code, res.text))

    return True
