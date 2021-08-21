#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  This file is part of the `pypath` python module
#
#  Copyright
#  2014-2021
#  EMBL, EMBL-EBI, Uniklinik RWTH Aachen, Heidelberg University
#
#  File author(s): Dénes Türei (turei.denes@gmail.com)
#                  Nicolàs Palacio
#                  Olga Ivanova
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: http://pypath.omnipathdb.org/
#

import itertools
import collections

import pypath.resources.urls as urls
import pypath.share.curl as curl


def mir2disease_interactions():

    Mir2diseaseInteraction = collections.namedtuple(
        'Mir2diseaseInteraction',
        (
            'mirna',
            'target_genesymbol',
            'year',
            'sentence',
        ),
    )

    url = urls.urls['mir2dis']['url_rescued']
    c = curl.Curl(url, silent = True, large = True, encoding = 'iso-8859-1')

    return [
        Mir2diseaseInteraction(
            *l.strip('\r\n\t "').split('\t')
        )
        for l in itertools.islice(c.result, 3, None)
        if l
    ]
