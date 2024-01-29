from web3 import Web3
from typing import Optional
import time

from client import Client
from data.config import HOLESKY_ABI
from utils import read_json
from models import TokenAmount


class Holesky:
    horse_address = Web3.to_checksum_address('0x0469760d321D08AB4fce75E2E799902C9f55dA59')
    horse_from_address = Web3.to_checksum_address('0x0000000000000000000000000000000000000000')

    router_address =  Web3.to_checksum_address('0x095DDce4fd8818aD159D778E6a9898A2474933ca')
    router_abi = read_json(HOLESKY_ABI)
    spender_horse_address = Web3.to_checksum_address('0x095DDce4fd8818aD159D778E6a9898A2474933ca')


    def __init__(self, client: Client):
        self.client = client


    def mint(self, slippage: float = 1):
        contract = self.client.w3.eth.contract(
            abi=Holesky.router_abi,
            address=Holesky.horse_address
        )

        return self.client.send_transaction(
            to=Holesky.horse_address,
            data=contract.encodeABI('mint',
                                    args=(
                                        self.client.address,
                                    ))
        )
    def bridge(self, amount: Optional[TokenAmount] = None, slippage: float = 1):
        contract = self.client.w3.eth.contract(
            abi=Holesky.router_abi,
            address=Holesky.horse_address
        )

        if not amount:
            amount = self.client.balance_of(contract_address=Holesky.horse_address)


        res = self.client.approve_interface(
            token_address=Holesky.horse_address,
            spender=Holesky.spender_horse_address,
            amount=amount
        )
        if not res:
            return False
        time.sleep(5)

        return res

    def bridge_horse(self, slippage: float = 1):
        
        contract = self.client.w3.eth.contract(
            abi=Holesky.router_abi,
            address=Holesky.horse_address
        )
        

        # data = '0x755fc20c00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000028c600000000000000000000000005599bee23f5bee6b5dbb742ad557a9eff3feaa950000000000000000000000000469760d321d08ab4fce75e2e799902c9f55da590000000000000000000000000000000000000000000000008ac7230489e8000000000000000000000000000000000000000000000000000000000000000222e00000000000000000000000000000000000000000000000000005dcaa8ff1e8e00000000000000000000000005599bee23f5bee6b5dbb742ad557a9eff3feaa9500000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000'

        # decoded_data = contract.decode_function_input(data)

        # print('DECODEED', decoded_data)

        # amount = self.client.send_token()

#         amount = self.client.balance_of(contract_address=Taiko.horse_address)

#         print('!!!!!!!!!!!!11111111111111111!!!!!!!!!!!!!!!', amount )

#         contract = self.client.w3.eth.contract(
#             abi=Taiko.router_abi,
#             address=Taiko.router_address
#         )
#

        print("GO")
        return self.client.send_token( to=Holesky.router_address)



