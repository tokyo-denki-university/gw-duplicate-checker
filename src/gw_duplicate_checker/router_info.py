router = {
    "2c:d0:2d:f7:15:c0": "G1 GW",
    "2c:5a:0f:b9:8b:93": "G1 A",
    "b4:de:31:38:ae:33": "G1 B",
    "e4:aa:5d:d3:2b:40": "G2 GW",
    "50:0f:80:3c:16:53": "G2 A",
    "38:0e:4d:b6:09:13": "G2 B",
    "70:db:98:e8:4e:a0": "G3 GW",
    "70:7d:b9:54:6c:13": "G3 A",
    "00:fd:22:e2:11:f3": "G3 B",
    "00:fd:22:e2:18:80": "G4 GW",
    "00:62:ec:d7:b9:13": "G4 A",
    "70:70:8b:4a:8c:f3": "G4 B",
    "ff:ff:ff:ff:ff:00": "G5 GW",  # 不明
    "2c:d0:2d:f7:11:d3": "G5 A",
    "70:db:98:e8:a0:53": "G5 B",
    "00:81:c4:01:54:c0": "G6 GW",
    "00:f6:63:76:80:f3": "G6 A",
    "00:81:c4:01:49:53": "G6 B",
    "f8:0f:6f:b6:72:80": "G7 GW",
    "70:db:98:e8:52:d3": "G7 A",
    "50:0f:80:3c:1b:f3": "G7 B",
    "50:0f:80:3c:10:40": "G8 GW",
    "2c:5a:0f:f2:81:33": "G8 A",
    "84:3d:c6:4f:89:33": "G8 B",
    "ff:ff:ff:ff:ff:01": "G9 GW",  # 不明
    "70:db:98:e8:9f:d3": "G9 A",
    "2c:5a:0f:f3:70:f3": "G9 B",
}


def get_router_name(mac_address):
    return router.get(mac_address, "Unknown")
