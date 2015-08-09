# This is an ugly hack that helped me dump secret keys from wallet.dat, for importing into Electrum 1.9.7.
# - ivucica, 2015
import os
import pywallet


print "IF SOMETHING BREAKS:"
print " DATADIR=path-to-datadir WALLET=wallet-new.dat PASS=passphrasehere sudo -E python secret_keys.py"

json_db = {}
try:
    wdir = os.environ['DATADIR']
except:
    wdir = '%s/.bitcoin' % os.environ['HOME']

try:
    wallet = os.environ['WALLET']
except:
    wallet = 'wallet.dat'
try:
    pywallet.passphrase = os.environ['PASS']
except:
    pass

dbb_env = pywallet.create_env(wdir)
walletinfo = pywallet.read_wallet(json_db, dbb_env, wallet, True, True, "", None)

for key in json_db['keys']:
    if not key['reserve']:
        print '%s: %s' % (key['label'], key['sec'])
