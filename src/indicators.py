"""TLP:WHITE indicators used by check-your-pulse."""

# TLP white indicators from CISA
maliciousstrings = [
    "dana/html5acc/guacamole/../../",
    "../etc/passwd?",
    "../../data/runtime/lmdb-backup/data0/data.mdb?",
    "/data/runtime/mtmp/lmdb/dataa/data.mdb",
    "/dana-admin/diag/diag.cgi",
    "/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/",
    "/../../data/runtime/lmdb-backup",
]

malicioususeragents = [
    r"Mozilla\/5.0 \(Windows NT 6.1\; rv:60.0\) Gecko\/20100101 Firefox\/60.0",
    r"Mozilla\/5.0 \(Windows NT 10.0\; rv:68.0\) Gecko\/20100101 Firefox\/68.0",
    r"Mozilla\/5.0 \(Windows NT 6.1\; WOW64\) AppleWebKit\/537.36 \(KHTML, like Gecko\) Chrome\/55\[.\]0.2883.87 Safari\/537.36",
]


maliciousIPs = [
    "51.255.45.144",
    "54.39.22.213",
    "62.102.148.68",
    "62.210.37.15",
    "77.247.181.162",
    "77.247.181.165",
    "87.120.254.98",
    "89.31.57.5",
    "94.102.51.78",
    "95.128.43.164",
    "95.211.230.211",
    "103.208.220.123",
    "104.244.72.115",
    "104.244.76.189",
    "104.244.76.245",
    "109.70.100.20",
    "109.70.100.23",
    "109.70.100.25",
    "130.149.80.199",
    "158.174.122.199",
    "162.247.74.202",
    "162.247.74.204",
    "162.247.74.216",
    "162.247.74.7",
    "162.247.74.74",
    "169.197.97.34",
    "176.10.104.240",
    "178.165.72.177",
    "178.20.55.18",
    "185.107.47.171",
    "185.220.100.247",
    "185.220.101.1",
    "185.220.101.15",
    "185.220.101.24",
    "185.220.101.26",
    "185.220.101.28",
    "185.220.101.32",
    "185.220.101.62",
    "185.220.101.70",
    "185.220.101.71",
    "185.220.101.72",
    "185.220.101.77",
    "185.220.102.8",
    "185.4.135.135",
    "192.160.102.165",
    "192.42.116.18",
    "193.110.157.151",
    "195.176.3.20",
    "199.249.230.104",
    "204.17.56.42",
    "209.141.32.33",
    "212.83.166.62",
    "223.167.32.74",
    "23.129.64.180",
    "23.129.64.194",
    "23.129.64.214",
    "45.125.65.45",
    "45.14.148.96",
    "46.165.245.154",
    "46.182.106.190",
    "5.199.135.107",
]
