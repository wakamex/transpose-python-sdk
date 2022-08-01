
ENS_API_ENDPOINTS = {

    # ENS Record Endpoints
    'records_by_owner':                       'https://api.transpose.io/ens/ens-records-by-owner',
    'records_by_account':                     'https://api.transpose.io/ens/ens-records-by-account',
    'records_by_ens_name':                    'https://api.transpose.io/ens/ens-records-by-name',
    'records_by_ens_token_id':                'https://api.transpose.io/ens/ens-records-by-token-id',
    'records_by_date':                        'https://api.transpose.io/ens/ens-records-by-date',

    # ENS Transfer Endpoints
    'transfers_by_ens_name':                  'https://api.transpose.io/ens/ens-transfers-by-name',
    'transfers_by_ens_token_id':              'https://api.transpose.io/ens/ens-transfers-by-token-id',
}

BLOCK_API_ENDPOINTS = {

    # Account Endpoints
    'accounts_by_address':                    'https://api.transpose.io/block/accounts-by-address',
    'accounts_by_date_created':               'https://api.transpose.io/block/accounts-by-date-created',
    'contracts_by_creator':                   'https://api.transpose.io/block/contracts-by-creator',
    
    # Block Endpoints
    'blocks_by_number':                       'https://api.transpose.io/block/blocks-by-number',
    'blocks_by_date':                         'https://api.transpose.io/block/blocks-by-date',
    
    # Transaction Endpoints
    'transactions_by_hash':                   'https://api.transpose.io/block/transactions-by-hash',
    'transactions_by_block':                  'https://api.transpose.io/block/transactions-by-block',
    'transactions_by_date':                   'https://api.transpose.io/block/transactions-by-date',
    'transactions_by_account':                'https://api.transpose.io/block/transactions-by-account',
    
    # Log Endpoints
    'logs_by_transaction':                    'https://api.transpose.io/block/logs-by-transaction',
    'logs_by_block':                          'https://api.transpose.io/block/logs-by-block',
    'logs_by_date':                           'https://api.transpose.io/block/logs-by-date',
}

NFT_API_ENDPOINTS = {
    
    # Collection Endpoints
    'collections_by_date_created':            'https://api.transpose.io/nft/collections-by-date-created',
    'collections_by_contract_address':        'https://api.transpose.io/nft/collections-by-contract-address',
    'collections_by_name':                    'https://api.transpose.io/nft/collections-by-name',
    'collections_by_symbol':                  'https://api.transpose.io/nft/collections-by-symbol',
    
    # NFT Endpoints
    'nfts_by_date_minted':                    'https://api.transpose.io/nft/nfts-by-date-minted',
    'nfts_by_contract_address':               'https://api.transpose.io/nft/nfts-by-contract-address',
    'nfts_by_token_id':                       'https://api.transpose.io/nft/nfts-by-token-id',
    'nfts_by_name':                           'https://api.transpose.io/nft/nfts-by-name',
    'nfts_by_owner':                          'https://api.transpose.io/nft/nfts-by-owner',
    'nfts_by_approved_account':               'https://api.transpose.io/nft/nfts-by-approved-account',
    
    # Owner Endpoints
    'owners_by_contract_address':             'https://api.transpose.io/nft/owners-by-contract-address',
    'owners_by_token_id':                     'https://api.transpose.io/nft/owners-by-token-id',
   
    # Transfer Endpoints
    'transfers':                              'https://api.transpose.io/nft/transfers',
    'transfers_by_contract_address':          'https://api.transpose.io/nft/transfers-by-contract-address',
    'transfers_by_token_id':                  'https://api.transpose.io/nft/transfers-by-token-id',
    'transfers_by_account':                   'https://api.transpose.io/nft/transfers-by-account',

    # Sale Endpoints
    'sales':                                  'https://api.transpose.io/nft/sales',
    'sales_by_contract_address':              'https://api.transpose.io/nft/sales-by-contract-address',
    'sales_by_token_id':                      'https://api.transpose.io/nft/sales-by-token-id',
    'sales_by_account':                       'https://api.transpose.io/nft/sales-by-account',
}

TOKEN_API_ENDPOINTS = {
    
    # Token Endpoints
    'tokens_by_date_created':                 'https://api.transpose.io/token/tokens-by-date-created',
    'tokens_by_contract_address':             'https://api.transpose.io/token/tokens-by-contract-address',
    'tokens_by_name':                         'https://api.transpose.io/token/tokens-by-name',
    'tokens_by_symbol':                       'https://api.transpose.io/token/tokens-by-symbol',
    'tokens_by_owner':                        'https://api.transpose.io/token/tokens-by-owner',
    
    # Owner Endpoints
    'owners_by_contract_address':             'https://api.transpose.io/token/owners-by-contract-address',
    
    # Transfer Endpoints
    'transfers':                              'https://api.transpose.io/token/transfers',
    'transfers_by_contract_address':          'https://api.transpose.io/token/transfers-by-contract-address',
    'transfers_by_account':                   'https://api.transpose.io/token/transfers-by-account',
    
    # Native Token Endpoints
    'native_token_transfers':                 'https://api.transpose.io/token/native-token-transfers',
    'native_token_transfers_by_account':      'https://api.transpose.io/token/native-token-transfers-by-account',
    'native_token_balances_by_account':       'https://api.transpose.io/token/native-token-balances-by-account',
    
    # Swap Endpoints
    'swaps':                                  'https://api.transpose.io/token/swaps',
    'swaps_by_account':                       'https://api.transpose.io/token/swaps-by-account',
    'swaps_by_token':                         'https://api.transpose.io/token/swaps-by-token',
    'swaps_by_pair':                          'https://api.transpose.io/token/swaps-by-pair',
}