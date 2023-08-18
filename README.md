# Microsoft Dynamics 365 Business Central Python SDK

Python SDK for accessing Microsoft Dynamics 365 Business Central APIs.

## Installation

The project is under active development, so contracts can change.

This project requires [Python 3+](https://www.python.org/downloads/) and [Requests](https://pypi.org/project/requests/) library (pip install requests).

1. Download this project and use it (copy it in your project, etc).
2. Install it from [pip](https://pypi.org).
        
        $ pip install ms-dynamics-business-central-sdk

## Usage

To use this SDK you'll need these Dynamics credentials

This SDK is very easy to use.
1. First you'll need to create a connection using the main class Dynamics.
```python
dynamics = Dynamics(
    client_id='<secret>',
    client_secret='<secret>',
    environment='sandbox',
    refresh_token='<refresh_token>'
)

company_id = dynamics.companies.get_all()[0]['id']

dynamics = Dynamics(
    client_id='<secret>',
    client_secret='<secret>',
    environment='sandbox',
    refresh_token='<refresh_token>',
    company_id=company_id
)

vendors = connection.vendors.get_all()
```


See more details about the usage into the wiki pages of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details