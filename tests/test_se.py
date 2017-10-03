# -*- coding: utf-8 -*-
from unittest import TestCase

from num2words import num2words

class Num2WordsSETest(TestCase):
    def test_and_join_199(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/8
        self.assertEqual(num2words(199,lang='se'), "ett hundra och nittio-nio")

    def test_cardinal_for_float_number(self):
        # issue 24
        self.assertEqual(num2words(12.50,lang='se'), "tolv komma fem noll")
        self.assertEqual(num2words(12.51,lang='se'), "tolv komma fem ett")

    def test_zero_to_one_hundred(self):
        self.assertEqual(num2words(1,lang='se'), "ett")
        self.assertEqual(num2words(2,lang='se'), "två")
        self.assertEqual(num2words(3,lang='se'), "tre")
        self.assertEqual(num2words(4,lang='se'), "fyra")
        self.assertEqual(num2words(5,lang='se'), "fem")
        self.assertEqual(num2words(6,lang='se'), "sex")
        self.assertEqual(num2words(7,lang='se'), "sju")
        self.assertEqual(num2words(8,lang='se'), "åtta")
        self.assertEqual(num2words(9,lang='se'), "nio")
        self.assertEqual(num2words(10,lang='se'), "tio")
        self.assertEqual(num2words(11,lang='se'), "elva")
        self.assertEqual(num2words(12,lang='se'), "tolv")
        self.assertEqual(num2words(13,lang='se'), "tretton")
        self.assertEqual(num2words(14,lang='se'), "fjorton")
        self.assertEqual(num2words(15,lang='se'), "femton")
        self.assertEqual(num2words(16,lang='se'), "sexton")
        self.assertEqual(num2words(17,lang='se'), "sjutton")
        self.assertEqual(num2words(18,lang='se'), "arton")
        self.assertEqual(num2words(19,lang='se'), "nitton")
        self.assertEqual(num2words(20,lang='se'), "tjugo")
        self.assertEqual(num2words(21,lang='se'), "tjugo-ett")
        self.assertEqual(num2words(22,lang='se'), "tjugo-två")
        self.assertEqual(num2words(23,lang='se'), "tjugo-tre")
        self.assertEqual(num2words(24,lang='se'), "tjugo-fyra")
        self.assertEqual(num2words(25,lang='se'), "tjugo-fem")
        self.assertEqual(num2words(26,lang='se'), "tjugo-sex")
        self.assertEqual(num2words(27,lang='se'), "tjugo-sju")
        self.assertEqual(num2words(28,lang='se'), "tjugo-åtta")
        self.assertEqual(num2words(29,lang='se'), "tjugo-nio")
        self.assertEqual(num2words(30,lang='se'), "trettio")
        self.assertEqual(num2words(31,lang='se'), "trettio-ett")
        self.assertEqual(num2words(32,lang='se'), "trettio-två")
        self.assertEqual(num2words(33,lang='se'), "trettio-tre")
        self.assertEqual(num2words(34,lang='se'), "trettio-fyra")
        self.assertEqual(num2words(35,lang='se'), "trettio-fem")
        self.assertEqual(num2words(36,lang='se'), "trettio-sex")
        self.assertEqual(num2words(37,lang='se'), "trettio-sju")
        self.assertEqual(num2words(38,lang='se'), "trettio-åtta")
        self.assertEqual(num2words(39,lang='se'), "trettio-nio")
        self.assertEqual(num2words(40,lang='se'), "fyrtio")
        self.assertEqual(num2words(41,lang='se'), "fyrtio-ett")
