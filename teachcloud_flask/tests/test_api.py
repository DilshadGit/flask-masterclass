def test_health_endpoint(client):
    res = client.get('/api/v1/health')
    assert res.status_code == 200
    assert res.json['status'] == 'healthy'

def test_user_registration(client):
    res = client.post('/auth/register', json={
        'username': 'flaskdev',
        'email': 'flaskdev@teachcloud.io',
        'password': 'SecurePassword123!'
    })
    assert res.status_code == 201
    assert 'user_id' in res.json
