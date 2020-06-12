from functions import create_accel_lst
from functions import calibration_for_xy
from functions import calibration_for_z
from functions import integration_for_distance
from functions import Navigator

def test_calib():
    a=(create_accel_lst())
    b=calibration_for_xy(a)
    for i in range(0,len(a)):
        assert  b[i]<=100 and b[i]>=0
def test_integration():
    assert isinstance(integration_for_distance(create_accel_lst()),float)