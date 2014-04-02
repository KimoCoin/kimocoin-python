####kimocoin-python

kimocoin-python is a set of python libraries that allows easy access to the 
kimocoin peer-to-peer cryptocurrency client API.

codebase originally derived from <a href="https://github.com/laanwj/bitcoin-python">@laanwj/bitcoin-python</a>. additionaly some modifications made for the portability of kimocoin.

####installation

```bash
$ [sudo] pip install kimocoin-python
```
or if you like 90s:
```bash
$ [sudo] easy_install kimocoin-python
```

####running the deamon

- run `kimocoind` from the kimocoin source. (src/kimocoind) follow the instructions about rpcuser and password.

example kimocoin.conf

```bash
rpcuser=changeme
rpcpassword=changemechangemechangemechangeme
rpcallowip=*
server=1
bind = 0.0.0.0
rpcport=1988
txindex=1
```

####api
```python

import kimocoinrpc

conn = kimocoinrpc.connect_to_local()
print "Your balance is %f" % (conn.getbalance(),)

# output: Your balance is 131.589260


print conn.getinfo()

# kimocoinrpc.data.ServerInfo(
# 	connections = 4,
# 	errors = u '',
# 	blocks = 7675,
# 	paytxfee = Decimal('0E-8'),
# 	keypoololdest = 1389617961,
# 	walletversion = 60000,
# 	difficulty = Decimal('0.00008961'),
# 	testnet = False,
# 	version = 85600,
# 	proxy = u '',
# 	protocolversion = 70001,
# 	timeoffset = 0,
# 	balance = Decimal('131.58925958'),
# 	keypoolsize = 101
# )

print conn.getdifficulty()

# output: 0.00008961
```

you can explore other methods over the <a href="http://laanwj.github.io/bitcoin-python/doc/">bitcoin-python documentation.</a>
