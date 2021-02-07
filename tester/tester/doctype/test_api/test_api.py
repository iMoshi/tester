# -*- coding: utf-8 -*-
# Copyright (c) 2021, Manduul and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import requests
import json
from frappe.utils import now, cint, get_datetime
from frappe import _


class TestAPI(Document):
    pass


@frappe.whitelist(allow_guest=True)
def add_api_based():
    responce = "https://jsonplaceholder.typicode.com/posts/"
    data = requests.get(responce)
    r = data.json()

    for post in r:
        d = frappe.db.exists({
            'doctype': 'Test API',
            'post_id': post["id"]
        })
        if d:
            continue

        doc = frappe.get_doc({
            "doctype": "Test API",
            "post_id": post["id"],
            "post_user": post["userId"],
            "post_title": post["title"],
            "post_body": post["body"]
        })
        doc.save()
