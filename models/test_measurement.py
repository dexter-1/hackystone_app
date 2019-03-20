import measurement
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def test_readcsv():
    mock_data1_file = os.path.join(dir_path, '../data/mock_data1/tagdata.csv')
    measurements = measurement.Measurement.readcsv(mock_data1_file)
    # based on manual inspection
    assert(measurements[-1].tagId == "1")
    assert(measurements[-1].anchorId == "4")
    assert(measurements[-1].rssi == "-90.375")
    assert(measurements[-1].timestamp == "60")
    assert(len(measurements) == 240)

def run():
    test_readcsv()

if __name__ == "__main__":
    run()    
