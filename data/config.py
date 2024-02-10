import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ABIS_DIR = os.path.join(ROOT_DIR, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
WOOFI_ABI = os.path.join(ABIS_DIR, 'woofi.json')
TAIKO_ABI = os.path.join(ABIS_DIR, 'taiko.json')
HOLESKY_ABI = os.path.join(ABIS_DIR, 'holesky.json')
HORSE_ABI = os.path.join(ABIS_DIR, 'horse.json')
BRIDGE_ABI = os.path.join(ABIS_DIR, 'bridge.json')

private_key = '687afc9f61ebd4ec5fd1d07b16842e83faf77e971151de9e7d650c56d6994778'
# seed = 'shallow scare snack olympic connect defy trigger balcony riot drink lift swamp'
eth_rpc = 'https://mainnet.infura.io/v3/'
arb_rpc = 'https://rpc.ankr.com/arbitrum/'
taiko_rpc = 'https://taiko-katla.blockpi.network/v1/rpc/public/'
holesky_rpc = 'https://ethereum-holesky.publicnode.com'


