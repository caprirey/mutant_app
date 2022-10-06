from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

def test_data_ok_mutant():
    response = client.post(
        "/api/v1/mutant/",
        json={"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]},
    )
    assert response.status_code == 200
    assert response.json() == { "result": "you have gene x" }


def test_data_ok_mutant_same_axis():
    response = client.post(
        "/api/v1/mutant/",
        json={"dna":["AAAAGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]},
    )
    assert response.status_code == 200
    assert response.json() == { "result": "you have gene x" }

def test_data_ok_mutant_diag():
    response = client.post(
        "/api/v1/mutant/",
        json={"dna":["ATGCGA","CCGTAC","TTAAGT","AGAAGG","CCCCTA","TCACTG"]},
    )
    assert response.status_code == 200
    assert response.json() == { "result": "you have gene x" }

def test_data_ok_no_mutant():
    response = client.post(
        "/api/v1/mutant/",
        json={"dna":["ATGCGA","CAGTGC","TTATTT","AGACGG","GCGTCA","TCACTG"]},
    )
    assert response.status_code == 403
    assert response.json() == { "detail": "You are not mutant" }

def test_data_invalid_one():
    response = client.post(
        "/api/v1/mutant/",
        json={"dna":["ATGCGAX","CAGTGC","TTATTT","AGACGG","GCGTCA","TCACTG"]},
    )
    assert response.status_code == 400
    assert response.json() == { "detail": "Invalid data" }


def test_data_invalid_two():
    response = client.post(
        "/api/v1/mutant/",
        json={"dna":["AXGCGA","CAGXGC","XXAXXX","AGACGG","GCGXCA","XCACXG"]},
    )
    assert response.status_code == 400
    assert response.json() == { "detail": "Invalid data" }

def test_data_invalid_three():
    response = client.post(
        "/api/v1/mutant/",
        json={"dna":["ATGCGA","CAGTGC","TTATTT","AGACGG","GCGTCA"]},
    )
    assert response.status_code == 400
    assert response.json() == { "detail": "Invalid data" }


def test_data_trafic_10():
    start_time = datetime.now()
    for x in range(10):
        response = client.post(
        "/api/v1/mutant/",
        json={"dna":["ATGCGA","CAGTGC","TTATTT","AGACGG","GCGTCA","TCACTG"]},)
        assert response.status_code == 403
        assert response.json() == { "detail": "You are not mutant" }
    diff_time = (datetime.now() - start_time).seconds
    print(diff_time) 
    assert diff_time  <= 10

def test_data_stats():
    response = client.get(
        "/api/v1/stats",
    )
    assert response.status_code == 200  
    assert response.json()["count_mutant_dna"] > 0
    assert response.json()["count_human_dna"] > 0