from rho_pollard import algorithm
def test_algorithm():
    assert algorithm() == 28, "Should be 28"
if __name__ == "__main__":
    test_algorithm()
    print("Completed successfully")