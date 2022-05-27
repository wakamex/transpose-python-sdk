from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        records = api.ENS.records_by_owner('0x6666666b0b46056247e7d6cbdb78287f4d12574d')
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 1
        assert records['count'] == len(records['results'])
    except Exception:
        assert False