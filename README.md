# Microsoft Dynamics 365 Business Central Python SDK

Python SDK for accessing Microsoft Dynamics 365 Business Central APIs.

## Installation

This project requires [Python 3+](https://www.python.org/downloads/) and [Requests](https://pypi.org/project/requests/) library (pip install requests).

1. Download this project and use it (copy it in your project, etc).
2. Install it from [pip](https://pypi.org).
        
        $ pip install ms-dynamics-business-central-sdk

## Usage

To use this SDK you'll need these Dynamics credentials

This SDK is very easy to use.
1. First you'll need to create a connection using the main class Dynamics.
```python
from dynamics import Dynamics

connection = Dynamics(
    user_name='USER NAME',
    web_api_key='WEB API KEY',
    tenant_domain='example.com',
    environment='sandbox / production',
    company_id='company id'
)
```


See more details about the usage into the wiki pages of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details