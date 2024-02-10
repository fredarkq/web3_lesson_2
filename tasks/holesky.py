from web3 import Web3
from typing import Optional
import time

from client import Client
from data.config import HOLESKY_ABI, TAIKO_ABI, BRIDGE_ABI
from utils import read_json
from models import TokenAmount


class Holesky:
    horse_address = Web3.to_checksum_address('0x0469760d321D08AB4fce75E2E799902C9f55dA59')
    eth_address = Web3.to_checksum_address('0xf458747c6d6db57970dE80Da6474C0A3dfE94BF1')
    main_eth_address = Web3.to_checksum_address('0x1670080000000000000000000000000000000001')
    horse_from_address = Web3.to_checksum_address('0x0000000000000000000000000000000000000000')

    router_address =  Web3.to_checksum_address('0x095DDce4fd8818aD159D778E6a9898A2474933ca')
    router_abi = read_json(HOLESKY_ABI)
    bridge_abi = read_json(BRIDGE_ABI)
    taiko_abi = read_json(TAIKO_ABI)
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

    def bridge_horse(self, amount: Optional[TokenAmount] = None, slippage: float = 1):
        contract = self.client.w3.eth.contract(
            abi=Holesky.taiko_abi,
            address=Holesky.horse_address
        )
        if not amount:
            amount = self.client.balance_of(contract_address=Holesky.horse_address)

        data = '0x755fc20c00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000028c6000000000000000000000000026648d7d21d575d8488b0816a00d58629849d1650000000000000000000000000469760d321d08ab4fce75e2e799902c9f55da590000000000000000000000000000000000000000000000001bc16d674ec8000000000000000000000000000000000000000000000000000000000000000222e00000000000000000000000000000000000000000000000000005dcaa8ff1e8e000000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000'
        # data = '0x33bcd0cc00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cfbde4f939a268986e1a427b0c74d994adbc9e3200000000000000000000000000000000000000000000000000000000000042680000000000000000000000000000000000000000000000000000000000028c60000000000000000000000000cfbde4f939a268986e1a427b0c74d994adbc9e32000000000000000000000000cfbde4f939a268986e1a427b0c74d994adbc9e32000000000000000000000000cfbde4f939a268986e1a427b0c74d994adbc9e32000000000000000000000000000000000000000000000000005e27bac7a323900000000000000000000000000000000000000000000000000004cbd15e801ba000000000000000000000000000000000000000000000000000000000000222e0000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000001a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

        decoded_data = contract.decode_function_input(data)

        print('DECODEED', decoded_data)

        # amount = self.client.send_token()
#         amount = self.client.balance_of(contract_address=Taiko.horse_address)
#         print('!!!!!!!!!!!!11111111111111111!!!!!!!!!!!!!!!', amount )
#         contract = self.client.w3.eth.contract(
#             abi=Taiko.router_abi,
#             address=Taiko.router_address
#         )

        eth_price = self.client.get_eth_price(token='ETH')

        print("GO", TokenAmount(amount.Ether / 2).Wei)


        abi_data = {
                'destChainId': 167008,
                'to':  self.client.address,
                'token': Holesky.horse_address,
                'amount': TokenAmount(amount.Ether / 2).Wei,
                'gasLimit': 140000,
                'fee': 1650000001100000,
                'refundTo': self.client.address,
                'memo': ''
        }



        payload = contract.encodeABI('sendToken', {'op': abi_data}, )

        eth_price = self.client.get_eth_price(token='ETH')
        min_to_amount = TokenAmount(
            amount=float(amount.Ether) / eth_price * (1 - slippage / 100),
        )
        print("GO", amount.Ether)
#         return self.client.send_transaction( to=Holesky.router_address, value=amount.Wei)
        return self.client.send_transaction(
                    to=Holesky.router_address,
                    data=payload,
                    value=min_to_amount.Wei
        )


    def bridge_eth(self, amount: Optional[TokenAmount] = None, slippage: float = 1):
        contract = self.client.w3.eth.contract(
            abi=Holesky.bridge_abi,
            address=Holesky.eth_address
        )
        if not amount:
            # amount = self.client.balance_of(contract_address=Holesky.eth_address)
            amount = self.client.balance_of(contract_address=Holesky.horse_address)


        data = '0x33bcd0cc0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000000000000000000000000000000000000000042680000000000000000000000000000000000000000000000000000000000028c6000000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000026648d7d21d575d8488b0816a00d58629849d165000000000000000000000000000000000000000000000000002386f26fc100000000000000000000000000000000000000000000000000000004cbd15e801ba000000000000000000000000000000000000000000000000000000000000222e0000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000001a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        # data2 = '0x33bcd0cc0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000000000000000000000000000000000000000042680000000000000000000000000000000000000000000000000000000000028c6000000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000026648d7d21d575d8488b0816a00d58629849d165000000000000000000000000000000000000000000000000002386f26fc100000000000000000000000000000000000000000000000000000004cbd15e801ba000000000000000000000000000000000000000000000000000000000000222e0000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000001a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        #
        decoded_data = contract.decode_function_input(data)
        # decoded_dataTrans = contract.decode_function_input(data2)

        print('DECODEED', decoded_data)
        # print('DECODEED decoded_dataTrans', decoded_dataTrans)
        print('amount', amount)


        abi_data = {
            'id': 0,
            'from': self.client.address,
            'srcChainId': 17000,
            'destChainId': 167008,
            'owner': self.client.address,
            'to': self.client.address,
            'refundTo': self.client.address,
            'value': 10000000000000000,
            'fee': 1350000000900000,
            'gasLimit': 140000,
            'data': b'',
            'memo': ''
        }



        payload = contract.encodeABI('sendMessage', {'message': abi_data})
        # payload = "0x33bcd0cc0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000000000000000000000000000000000000000042680000000000000000000000000000000000000000000000000000000000028c6000000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000026648d7d21d575d8488b0816a00d58629849d16500000000000000000000000026648d7d21d575d8488b0816a00d58629849d165000000000000000000000000000000000000000000000000002386f26fc100000000000000000000000000000000000000000000000000000004cbd15e801ba000000000000000000000000000000000000000000000000000000000000222e0000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000001a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"


        decoded_data2 = contract.decode_function_input(payload)


        # print("!!!!!!!!!!!!!!!!!!!!!!!", decoded_data2)

        # eth_price = self.client.get_eth_price(token='ETH')
        # min_to_amount = TokenAmount(
        #     amount=float(amount.Ether) / eth_price * (1 - slippage / 100),
        # )
        # print("GO", amount.Ether)

        return self.client.send_transaction(
                    to=Holesky.eth_address,
                    data=payload,
                    value= TokenAmount(0.0113500000009).Wei,
        )


