# -*- coding: utf-8 -*-
from hashlib import sha1

import xmltodict


def parse_xml(text):
    xml_dict = xmltodict.parse(text)["xml"]
    xml_dict["raw"] = text
    return xml_dict



