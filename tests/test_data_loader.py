
import pandas as pd
import pytest

from finguard.data_loader import load_transactions


@pytest.fixture
def sample_transactions(tmp_path):
    """Create a small, valid PaySim dataset for testing."""
    df = pd.DataFrame({
        "step": [1, 2],
        "type": ["TRANSFER", "CASH_OUT"],
        "amount": [100.0, 250.0],
        "nameOrig": ["C1", "C2"],
        "oldbalanceOrg": [500.0, 300.0],
        "newbalanceOrig": [400.0, 50.0],
        "nameDest": ["C3", "C4"],
        "oldbalanceDest": [0.0, 100.0],
        "newbalanceDest": [100.0, 350.0],
        "isFraud": [0, 1],
        "isFlaggedFraud": [0, 0],
    })

    file_path = tmp_path / "sample_paysim.csv"
    df.to_csv(file_path, index=False)

    return file_path


def test_load_valid_dataset(sample_transactions):
    """A valid dataset should load successfully."""
    df = load_transactions(sample_transactions)

    assert df.shape == (2, 11)
    assert df["isFraud"].tolist() == [0, 1]


def test_load_missing_file(tmp_path):
    """A missing file should raise FileNotFoundError."""
    missing_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_transactions(missing_path)


def test_load_missing_columns(sample_transactions):
    """Missing required columns should raise ValueError."""
    df = pd.read_csv(sample_transactions)
    df = df.drop(columns=["amount"])

    df.to_csv(sample_transactions, index=False)

    with pytest.raises(ValueError, match="Missing required columns"):
        load_transactions(sample_transactions)
