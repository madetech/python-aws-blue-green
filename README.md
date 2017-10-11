# AWS Blue/Green Deploy Scrips

A collection of script to flip a Route53 domain between two A records.

## Prerequisites

In order to keep configuration out of the scripts all variables are configured via ENV.
Each tools requirements may require additional variables, however you will always need to set:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

We strongly advise creating a new IAM user just for Route53 just in case.

## Tools

### Retrieving currently live domain
```
/bin/current_live_environment
```
Returns the current live environment

**Additional ENV variables**

`TARGET_DEPLOY_DOMAIN` - the domain you wish to get a DNS target from.