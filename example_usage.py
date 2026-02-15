# Example Usage of Fortnite Account Puller System

This script demonstrates how to use the Fortnite account puller system to retrieve inventory and cosmetics data using example usernames and account IDs.

## Requirements
- Python 3.7+
- Required libraries: requests

## Example Code

```python
import requests

def retrieve_fortnite_data(username, account_id):
    url = f'https://api.fortnite.com/account/{account_id}/inventory'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f'Inventory data for {username}:')
        print(data)
    else:
        print(f'Failed to retrieve data for {username}. Status code: {response.status_code}')

if __name__ == '__main__':
    example_usernames = ['ExampleUser1', 'ExampleUser2']
    example_account_ids = ['12345', '67890']
    
    for username, account_id in zip(example_usernames, example_account_ids):
        retrieve_fortnite_data(username, account_id)