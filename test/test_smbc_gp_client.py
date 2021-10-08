import sys
# sys.path.append("..")
# from smbc_gp_client.smbc_gp_client import SmbcGpClient
import requests
from smbc_gp_client.smbc_gp_client import SmbcGpClient

client = SmbcGpClient()
r = client.create_transaction(
    shopId="tshop00002314", shopPass="h26utrr3", orderId="order003", 
    jobCd="AUTH", itemCode="0000990", 
    amount=10, tax=1, tdFlag=0, 
    tdTenantName="123", tds2Type=1, tdRequired=0
    )
print(r.text)
