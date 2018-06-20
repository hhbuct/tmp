import base64

link = 'ssr://NjQuMTM3LjI0Ni42MToxNTQ4OmF1dGhfc2hhMV92NDpjaGFjaGEyMDp0bHMxLjJfdGlja2V0X2F1dGg6Wkc5MVlpNXBieTl6YzNwb1puZ3ZLakUxTkRnLz9yZW1hcmtzPTVweXM1WVdONkxTNTZMU201WS0zNXAybDZJZXFPbVJ2ZFdJdWFXOHZjM042YUdaNEx3'

with open('tmp.txt', 'w') as f:
    f.write(base64.b64encode(link))
