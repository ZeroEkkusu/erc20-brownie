# About
Just a ERC20 token with [Solmate's ERC20 implementation](https://github.com/Rari-Capital/solmate/blob/main/src/tokens/ERC20.sol).
# Setup
### Clone
```bash
git clone this
```
### Prerequisites
- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
### Requirements
```bash
pip install -r requirements.txt
```
### Other files
Set up your `.env` file using the provided [`.env.example`](./.env.example)
# Usage
### Compile
```bash
brownie compile
```
### Deploy
```bash
brownie run scripts/deploy_token.py
```