from blockfrost import BlockFrostApi, ApiError, ApiUrls

api = BlockFrostApi(
    project_id='testnetGUOhfUBi4nP8Ac3HyLkFL9aw8DTTvFVJ',  # or export environment variable BLOCKFROST_PROJECT_ID
    # optional: pass base_url or export BLOCKFROST_API_URL to use testnet, defaults to ApiUrls.mainnet.value
    base_url=ApiUrls.testnet.value,
)
try:
    health = api.health()
    print(health)  # prints object:    HealthResponse(is_healthy=True)
    health = api.health(return_type='json')  # Can be useful if python wrapper is behind api version
    print(health)  # prints json:      {"is_healthy":True}
    health = api.health(return_type='pandas')
    print(health)  # prints Dataframe:         is_healthy
    #                       0         True

    account_rewards = api.account_rewards(
        stake_address='stake_test1ur37k5awfzjt6q6w5f2w9vsqfhl52zqrhss8uev7z2zf6sqwdrun0',
        count=20,
    )
    print(account_rewards)  # prints 221
    print(len(account_rewards))  # prints 20

    account_rewards = api.account_rewards(
        stake_address='stake_test1ur37k5awfzjt6q6w5f2w9vsqfhl52zqrhss8uev7z2zf6sqwdrun0',
        count=20,
        gather_pages=True,  # will collect all pages
    )
    print(account_rewards)  # prints 221
    print(len(account_rewards))  # prints 57
except ApiError as e:
    print(e)

def get_ada_in_wallet():
    try:
        address = api.address(
            address='addr_test1qrkwu77nu83jd49rhrmxp9d4fafs53rccvd04nu304gqdtlradf6uj9yh5p5agj5u2eqqn0lg5yq80pq0ejeuy5yn4qqammtf4')
        print(address.type)  # prints 'shelley'
        for amount in address.amount:
            print(amount.quantity)  # prints 'lovelace'
        return amount.quantity
    except ApiError as e:
        print(e)
