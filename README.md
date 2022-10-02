## Installation
Using [pip](https://pypi.org/project/discloudapi/)

```bash
pip install discloudapi
```

## Usage

```python
import discloudapi

discloudclient = discloudapi.Client(api_token="YOUR API TOKEN HERE")

userstats = discloudclient.user()
print(userstats)
```
Example of return:
```bash
> {'status': 'ok', 'message': 'User data were successfully charged', 'user': {'userID': '281495880266416139', 'totalRamMb': 2048, 'ramUsedMb': 1512, 'subdomains': ['subdomain123'], 'customdomains': [], 'apps': ['980526863850033253', '1017178094257307770', '1017275217401352222', '1017276776973619201', '1018207339251257384', 'subdomain123'], 'plan': 'Platinum', 'locale': 'pt-BR', 'lastDataLeft': {'days': 46, 'hours': 0, 'minutes': 26, 'seconds': 43}, 'planDataEnd': '2022-11-17T01:38:35.547Z'}, 'rateLimit': '200', 'rateLimitRemaining': '199', 'rateLimitReset': '60'}
```
See all functions [here](https://github.com/GenerosoDEV/discloudapi/blob/main/src/discloudapi/discloudapi.py).
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
