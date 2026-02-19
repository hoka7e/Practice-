import json

with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<22} {'Speed':<8} {'MTU'}")
print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")

for item in data['imdata']:
    attrs = item['l1PhysIf']['attributes']
    dn = attrs['dn']
    descr = attrs['descr']
    speed = attrs['speed']
    mtu = attrs['mtu']
    print(f"{dn:<50} {descr:<22} {speed:<8} {mtu}")