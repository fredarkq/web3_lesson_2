from web3.middleware import geth_poa_middleware

from client import Client
from data.config import private_key
from models import Arbitrum, Avalanche, Optimism, Polygon, HoleskyNetwork, TaikoNetwork
from tasks.holesky import Holesky
from tasks.taiko import Taiko
from models import TokenAmount

clientHolesky = Client(private_key=private_key, network=HoleskyNetwork)
clientHolesky.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
holesky = Holesky(client=clientHolesky)

clientTaiko = Client(private_key=private_key, network=TaikoNetwork)
clientTaiko.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
taiko = Taiko(client=clientTaiko)

# block = client.w3.eth.get_block('latest')
# print(client.w3.eth.max_priority_fee)
# res = Client.get_max_priority_fee_per_gas(w3=client.w3, block=block)
# woofi = WooFi(client=client)
# amount = TokenAmount(amount=0.001)
# tx = woofi.swap_eth_to_usdc(amount=amount)
# print(res)
holesky.mint()
approve = holesky.bridge()
# send = holesky.bridge_horse()

sendEth = holesky.bridge_eth()

# print( "holesky aprove =>", aprove)

# send = taiko.bridge_horse()
# res = taiko.client.verif_tx(tx_hash=send)


print( "holesky aprove =>", sendEth)

# print(res)
