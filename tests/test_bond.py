#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Bond
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestBond(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_bond(self):
        """  """
        bond = Bond(self.redis)
        self.assertNotEqual('', bond.text)

    def test_bond_features(self):
        """  """
        bond = Bond(self.redis, {
            'you': 'Jesse',
            'other': 'Will',
            'either': 'Tony',
            'partyA': 'Shaun',
            'partyB': 'Rich',
            'template': '{{params.you}} {{params.other}} {{params.either}} {{params.partyA}} {{params.partyB}}',
            'bond_when_roll': 5,
            'when': 'Bob',
            })
        self.assertEqual(bond.text, 'Bob, Jesse Will Tony Shaun Rich')