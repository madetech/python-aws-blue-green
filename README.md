# AWS Blue/Green Deploy Scrips

A collection of script to flip a Route53 domain between two A records.

## Prerequisites

In order to keep configuration out of the scripts all variables are configured via ENV.
Each tools requirements may require additional variables, however you will always need to set:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `BLUE_DEPLOY_DOMAIN` - the domain for "blue" platform.
- `GREEN_DEPLOY_DOMAIN` - the domain for "green" platform.
- `TARGET_DEPLOY_DOMAIN` - the domain you wish switch the DNS on.

We strongly advise creating a new IAM user just for Route53 just in case.

## Tools

### Retrieving currently live domain
```
env PYTHONPATH=. /bin/current_live_environment
```
Returns the current live environment

### Flipping currently live domain
```
env PYTHONPATH=. /bin/flip_dns_record
```
Points `TARGET_DEPLOY_DOMAIN` at the alternate blue/green record

### Rollback
```
env PYTHONPATH=. /bin/rollback
```
Returns the current live environment
