# telegram-username-checker
Simple telegram username availability checker using [fragment](https://fragment.com/)

## Usage

```py
tg = Telegram()

username = 'gaklmgaw'

status = tg.get_user(username)
print(f'The username {username} is {status}')

# Expected output: "The username gaklmgaw is Available"

```
