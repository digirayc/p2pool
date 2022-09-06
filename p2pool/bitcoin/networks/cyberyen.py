import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c1c1c1c1'.decode('hex')
P2P_PORT = 58383
ADDRESS_VERSION = 48
ADDRESS_P2SH_VERSION = 50
HUMAN_READABLE_PART = 'ltc'
RPC_PORT = 58382
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            'litecoin' in (yield bitcoind.rpc_help()) and # new versions have "litecoinprivkey" but no "litecoinaddress"
            (yield helper.check_block_header(bitcoind, '34458c96bb547193fa90b2f2599056684b0083d8a2996f2025943eb545031d29')) and
                          (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'LTC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Cyberyen') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Cybeyen/') if platform.system() == 'Darwin' else os.path.expanduser('~/.cyberyen'), 'cyberyen.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ltc/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ltc/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ltc/tx.dws?'
SANE_TARGET_RANGE = (2**256//1000000000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
