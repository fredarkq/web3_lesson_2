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


private_key = '1a2587aa73d5e1e92ed71bdc85fffc543f93f14016d542661c31319e5c5960cf'
# seed = 'shallow scare snack olympic connect defy trigger balcony riot drink lift swamp'
eth_rpc = 'https://mainnet.infura.io/v3/'
arb_rpc = 'https://rpc.ankr.com/arbitrum/'
taiko_rpc = 'https://taiko-katla.blockpi.network/v1/rpc/public/'
holesky_rpc = 'https://ethereum-holesky.publicnode.com'
