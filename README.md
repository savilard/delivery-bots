# Delivery bots

### Latest Changes

* :robot: Add order reminder. PR [#23](https://github.com/savilard/delivery-bots/pull/23) by [@savilard](https://github.com/savilard).
* :robot: Add role filter. PR [#22](https://github.com/savilard/delivery-bots/pull/22) by [@savilard](https://github.com/savilard).
* :robot: Add choice of delivery method for customer. PR [#21](https://github.com/savilard/delivery-bots/pull/21) by [@savilard](https://github.com/savilard).
* :robot: Add customer account creation to Moltin. PR [#20](https://github.com/savilard/delivery-bots/pull/20) by [@savilard](https://github.com/savilard).
* :memo: Add latest changes to README.md. PR [#19](https://github.com/savilard/delivery-bots/pull/19) by [@savilard](https://github.com/savilard).


## Installation

* Install [Poetry](https://python-poetry.org/), make and [Direnv](https://direnv.net/);
* Clone github repository:
```bash
git clone https://github.com/savilard/delivery-bots.git
```
* Go to folder with project:
```bash
cd delivery-bots
```
* Install dependencies:
```bash
make install
```
* Create a bot in Telegram via [BotFather](https://t.me/BotFather), and get it API token;
* Create redis account in [Redislabs](https://redislabs.com/), and after that create [cloud database](https://docs.redislabs.com/latest/rc/quick-setup-redis-cloud/) (you can choose free plan).
Get your endpoint database url and port;
* Register at [Elasticpath](https://www.elasticpath.com/). Create new store and save CLIENT_ID and CLIENT_SECRET;
* Create a .envrc file with the following content ([example](https://github.com/savilard/dvmn-fish-shop-bot/blob/2ae18b4d7f62c857934bc2fbee8a181e72fd9cf0/envrc.example)):
```.env
export ELASTICPATH_CLIENT_ID='elasticpath_client_id key'
export ELASTICPATH_CLIENT_SECRET='elasticpath_client_secret key'
export TELEGRAM_TOKEN='telegram token'
export DATABASE_PASSWORD='db_password'
export DATABASE_HOST='db_host'
export DATABASE_PORT=db_port
```


## How to run

```bash
make run
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/savilard/delivery-bots/blob/main/LICENSE) file for details.
