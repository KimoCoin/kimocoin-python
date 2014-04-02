# coding=utf-8
'''
Test script
*WARNING* Don't run this on a production kimocoin server! *WARNING*
Only on the test network.
'''
import argparse
import sys
sys.path.append('../src')

import kimocoinrpc
from kimocoinrpc.exceptions import BitcoinException, InsufficientFunds


from decimal import Decimal

parser = argparse.ArgumentParser()
parser.add_argument('--config', help="Specify configuration file")
parser.add_argument('--nolocal', help="Don't use connect_to_local",
                    action='store_true')
parser.add_argument('--noremote', help="Don't use connect_to_remote",
                    action='store_true')
args = parser.parse_args()

if __name__ == "__main__":

    if args.config:
        from kimocoinrpc.config import read_config_file
        cfg = read_config_file(args.config)
    else:
        from kimocoinrpc.config import read_default_config
        cfg = read_default_config(None)
    port = int(cfg.get('rpcport', '11988' if cfg.get('testnet') else '1988'))
    rpcuser = cfg.get('rpcuser', '')

    connections = []
    if not args.nolocal:
        local_conn = kimocoinrpc.connect_to_local()  # will use read_default_config
        connections.append(local_conn)

    for conn in connections:

        assert(type(conn.getconnectioncount()) is int)
        assert(type(conn.getdifficulty()) is Decimal)
        assert(type(conn.getgenerate()) is bool)
        conn.setgenerate(True)
        conn.setgenerate(True, 2)
        conn.setgenerate(False)
        #conn.backupwallet(destination)
        account = 'test'
        bitcoinaddress = conn.getnewaddress(account)
        conn.setaccount(bitcoinaddress, account)
        x = conn.validateaddress("invalid")
        assert(x.isvalid == False)
        messages = ('Hello, world!', u'かたな')
        for message in messages:
            signature = conn.signmessage(bitcoinaddress, message)
            assert(conn.verifymessage(bitcoinaddress, signature, message) is True)

        assert(type(conn.listunspent()) is list)  # needs better testing


    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty

    m_info = conn.getmininginfo()
    print ("Pooled Transactions: {pooledtx}\n"
           "Testnet: {testnet}\n".format(pooledtx=m_info.pooledtx,
                                        testnet=m_info.testnet,
                                        ))
