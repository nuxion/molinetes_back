from molinetes.models import Credencial

def test_credencial(test_client, init_db):
    assert len(Credencial.query.all()) == 2
