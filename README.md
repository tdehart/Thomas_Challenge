# Thomas_Challenge

## Infrastructure Challenge

### Setup

1. Launch new EC2 Instance (using Ubuntu LTS 22) while allowing port 22, 80 and 443 and creating a private key pair
2. Update `inventory.ini` to use your instance's public IP address, private key, and domain
3. Run the following commands to launch and serve the app with nginx:

```
ansible-playbook -i inventory.ini main_playbook.yml
ansible-playbook -i inventory.ini secure_server.yml
```

4. Use the following command to test if app is running and accessible through http and https:

```
ansible-playbook -i inventory.ini test_server.yml
```

### Demo

A demo of this app can be accessed at https://54.226.36.59/

## Coding Challenge

### Usage

`python3 credit_card_validator.py`

1. Enter an integer N representing number of credit card numbers
2. Enter N number of credit card numbers

Alternatively, you can run a small test suite:

`python3 test_credit_card_validator.py`
