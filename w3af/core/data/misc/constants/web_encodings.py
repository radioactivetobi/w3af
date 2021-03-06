from collections import OrderedDict

URL_HEX_FORMAT = u'%%%s'

HEX_FORMAT = u'&#x%s;'
DEC_FORMAT = u'&#%s;'
DEC_PADDED_FORMAT = u'&#%03d;'

#
# The number of encodings a developer can use is huge, and the frameworks
# don't help either, since some will (for example) write &#034; and other
# will write &#34;
#
# We want to make a real effort to cleanup all the bodies, so we are compiling
# A list with all the ways a special character can be written
#
# This table is just a reminder of how things can be encoded, it is not used
# much in the code
#
ENCODING_REMINDER = OrderedDict([
    (u'#',  [u'#',                                                  u'%23', u'%2523']),
    (u'&',  [u'&', u'&amp;',  u'&#x26;', u'&#38;', u'&#038;',       u'%26', u'%2526']),
    (u'%',  [u'%',                                                  u'%25', u'%2525']),
    (u'"',  [u'"', u'&quot;', u'&#x22;', u'&#34;', u'&#034;',       u'%22', u'%2522', u'\\u0022', u'\\"']),
    (u"'",  [u"'", u'&apos;', u'&#x27;', u'&#39;', u'&#039;',       u'%27', u'%2527', u'\\u0027', u"\\'"]),
    (u'>',  [u'>', u'&gt;',   u'&#x3e;', u'&#62;', u'&#062;',       u'%3e', u'%253e']),
    (u'=',  [u'=', u'&eq;',   u'&#x3d;', u'&#61;', u'&#061;',       u'%3d', u'%253d']),
    (u' ',  [u' ', u'&nbsp;', u'&#x20;', u'&#32;', u'&#032;', u'+', u'%20', u'%2520']),
    (u'<',  [u'<', u'&lt;',   u'&#x3c;', u'&#60;', u'&#060;',       u'%3c', u'%253c']),
    (u';',  [u';',                                                  u'%3b', u'%253b']),
    (u'/',  [u'/',                                                  u'%2f', u'%252f']),
    (u':',  [u':',                                                  u'%3a', u'%253a']),
    (u'@',  [u'@',                                                  u'%40', u'%2540']),
    (u'$',  [u'$',                                                  u'%24', u'%2524']),
    (u',',  [u',',                                                  u'%2c', u'%252c']),
    (u'?',  [u'?',                                                  u'%3f', u'%253f']),
    (u'\r', [u'\r',                                                 u'%0d', u'%250d']),
    (u'\n', [u'\n',                                                 u'%0a', u'%250a']),
])

SPECIAL_CHARS = {u'#',
                 u'&',
                 u'%',
                 u'"',
                 u"'",
                 u'>',
                 u'=',
                 u' ',
                 u'<',
                 u';',
                 u'/',
                 u':',
                 u'@',
                 u'$',
                 u',',
                 u'?',
                 u'\r',
                 u'\n'}


HTML_ENCODE_NAMES = {
    u'&': u'&amp;',
    u'"': u'&quot',
    u"'": u'&apos;',
    u'>': u'&gt;',
    u'=': u'&eq;',
    u' ': u'&nbsp;',
    u'<': u'&lt;',
}


HEX_MAP = {
 u'\x00': u'00',
 u'\x01': u'01',
 u'\x02': u'02',
 u'\x03': u'03',
 u'\x04': u'04',
 u'\x05': u'05',
 u'\x06': u'06',
 u'\x07': u'07',
 u'\x08': u'08',
 u'\t': u'09',
 u'\n': u'0a',
 u'\x0b': u'0b',
 u'\x0c': u'0c',
 u'\r': u'0d',
 u'\x0e': u'0e',
 u'\x0f': u'0f',
 u'\x10': u'10',
 u'\x11': u'11',
 u'\x12': u'12',
 u'\x13': u'13',
 u'\x14': u'14',
 u'\x15': u'15',
 u'\x16': u'16',
 u'\x17': u'17',
 u'\x18': u'18',
 u'\x19': u'19',
 u'\x1a': u'1a',
 u'\x1b': u'1b',
 u'\x1c': u'1c',
 u'\x1d': u'1d',
 u'\x1e': u'1e',
 u'\x1f': u'1f',
 u' ': u'20',
 u'!': u'21',
 u'"': u'22',
 u'#': u'23',
 u'$': u'24',
 u'%': u'25',
 u'&': u'26',
 u"'": u'27',
 u'(': u'28',
 u')': u'29',
 u'*': u'2a',
 u'+': u'2b',
 u',': u'2c',
 u'-': u'2d',
 u'.': u'2e',
 u'/': u'2f',
 u'0': u'30',
 u'1': u'31',
 u'2': u'32',
 u'3': u'33',
 u'4': u'34',
 u'5': u'35',
 u'6': u'36',
 u'7': u'37',
 u'8': u'38',
 u'9': u'39',
 u':': u'3a',
 u';': u'3b',
 u'<': u'3c',
 u'=': u'3d',
 u'>': u'3e',
 u'?': u'3f',
 u'@': u'40',
 u'A': u'41',
 u'B': u'42',
 u'C': u'43',
 u'D': u'44',
 u'E': u'45',
 u'F': u'46',
 u'G': u'47',
 u'H': u'48',
 u'I': u'49',
 u'J': u'4a',
 u'K': u'4b',
 u'L': u'4c',
 u'M': u'4d',
 u'N': u'4e',
 u'O': u'4f',
 u'P': u'50',
 u'Q': u'51',
 u'R': u'52',
 u'S': u'53',
 u'T': u'54',
 u'U': u'55',
 u'V': u'56',
 u'W': u'57',
 u'X': u'58',
 u'Y': u'59',
 u'Z': u'5a',
 u'[': u'5b',
 u'\\': u'5c',
 u']': u'5d',
 u'^': u'5e',
 u'_': u'5f',
 u'`': u'60',
 u'a': u'61',
 u'b': u'62',
 u'c': u'63',
 u'd': u'64',
 u'e': u'65',
 u'f': u'66',
 u'g': u'67',
 u'h': u'68',
 u'i': u'69',
 u'j': u'6a',
 u'k': u'6b',
 u'l': u'6c',
 u'm': u'6d',
 u'n': u'6e',
 u'o': u'6f',
 u'p': u'70',
 u'q': u'71',
 u'r': u'72',
 u's': u'73',
 u't': u'74',
 u'u': u'75',
 u'v': u'76',
 u'w': u'77',
 u'x': u'78',
 u'y': u'79',
 u'z': u'7a',
 u'{': u'7b',
 u'|': u'7c',
 u'}': u'7d',
 u'~': u'7e',
 u'\x7f': u'7f',
 u'\x80': u'80',
 u'\x81': u'81',
 u'\x82': u'82',
 u'\x83': u'83',
 u'\x84': u'84',
 u'\x85': u'85',
 u'\x86': u'86',
 u'\x87': u'87',
 u'\x88': u'88',
 u'\x89': u'89',
 u'\x8a': u'8a',
 u'\x8b': u'8b',
 u'\x8c': u'8c',
 u'\x8d': u'8d',
 u'\x8e': u'8e',
 u'\x8f': u'8f',
 u'\x90': u'90',
 u'\x91': u'91',
 u'\x92': u'92',
 u'\x93': u'93',
 u'\x94': u'94',
 u'\x95': u'95',
 u'\x96': u'96',
 u'\x97': u'97',
 u'\x98': u'98',
 u'\x99': u'99',
 u'\x9a': u'9a',
 u'\x9b': u'9b',
 u'\x9c': u'9c',
 u'\x9d': u'9d',
 u'\x9e': u'9e',
 u'\x9f': u'9f',
 u'\xa0': u'a0',
 u'\xa1': u'a1',
 u'\xa2': u'a2',
 u'\xa3': u'a3',
 u'\xa4': u'a4',
 u'\xa5': u'a5',
 u'\xa6': u'a6',
 u'\xa7': u'a7',
 u'\xa8': u'a8',
 u'\xa9': u'a9',
 u'\xaa': u'aa',
 u'\xab': u'ab',
 u'\xac': u'ac',
 u'\xad': u'ad',
 u'\xae': u'ae',
 u'\xaf': u'af',
 u'\xb0': u'b0',
 u'\xb1': u'b1',
 u'\xb2': u'b2',
 u'\xb3': u'b3',
 u'\xb4': u'b4',
 u'\xb5': u'b5',
 u'\xb6': u'b6',
 u'\xb7': u'b7',
 u'\xb8': u'b8',
 u'\xb9': u'b9',
 u'\xba': u'ba',
 u'\xbb': u'bb',
 u'\xbc': u'bc',
 u'\xbd': u'bd',
 u'\xbe': u'be',
 u'\xbf': u'bf',
 u'\xc0': u'c0',
 u'\xc1': u'c1',
 u'\xc2': u'c2',
 u'\xc3': u'c3',
 u'\xc4': u'c4',
 u'\xc5': u'c5',
 u'\xc6': u'c6',
 u'\xc7': u'c7',
 u'\xc8': u'c8',
 u'\xc9': u'c9',
 u'\xca': u'ca',
 u'\xcb': u'cb',
 u'\xcc': u'cc',
 u'\xcd': u'cd',
 u'\xce': u'ce',
 u'\xcf': u'cf',
 u'\xd0': u'd0',
 u'\xd1': u'd1',
 u'\xd2': u'd2',
 u'\xd3': u'd3',
 u'\xd4': u'd4',
 u'\xd5': u'd5',
 u'\xd6': u'd6',
 u'\xd7': u'd7',
 u'\xd8': u'd8',
 u'\xd9': u'd9',
 u'\xda': u'da',
 u'\xdb': u'db',
 u'\xdc': u'dc',
 u'\xdd': u'dd',
 u'\xde': u'de',
 u'\xdf': u'df',
 u'\xe0': u'e0',
 u'\xe1': u'e1',
 u'\xe2': u'e2',
 u'\xe3': u'e3',
 u'\xe4': u'e4',
 u'\xe5': u'e5',
 u'\xe6': u'e6',
 u'\xe7': u'e7',
 u'\xe8': u'e8',
 u'\xe9': u'e9',
 u'\xea': u'ea',
 u'\xeb': u'eb',
 u'\xec': u'ec',
 u'\xed': u'ed',
 u'\xee': u'ee',
 u'\xef': u'ef',
 u'\xf0': u'f0',
 u'\xf1': u'f1',
 u'\xf2': u'f2',
 u'\xf3': u'f3',
 u'\xf4': u'f4',
 u'\xf5': u'f5',
 u'\xf6': u'f6',
 u'\xf7': u'f7',
 u'\xf8': u'f8',
 u'\xf9': u'f9',
 u'\xfa': u'fa',
 u'\xfb': u'fb',
 u'\xfc': u'fc',
 u'\xfd': u'fd',
 u'\xfe': u'fe',
 u'\xff': u'ff'}
