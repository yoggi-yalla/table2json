from jsonbuilder.jsonbuilder import Tree
import rapidjson

test_data_folder = 'jsonbuilder/test/testdata/'

def test_1():
    with open(test_data_folder + 'format1.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'test.csv').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_1.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output

def test_2():
    with open(test_data_folder + 'format2.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'test.csv').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_2.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output

def test_3():
    with open(test_data_folder + 'format3.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'test.csv').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_3.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output

def test_3_quick():
    with open(test_data_folder + 'format3quick.json', 'r') as f:
        output_quick = Tree(rapidjson.load(f), test_data_folder + 'test.csv').build().toJson(indent=2)
    with open(test_data_folder + 'format3.json', 'r') as f:
        output_slow = Tree(rapidjson.load(f), test_data_folder + 'test.csv').build().toJson(indent=2)
    assert output_quick == output_slow

def test_crif():
    with open(test_data_folder + 'formatcrif.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'testcrif.csv').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_crif.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_txt():
    with open(test_data_folder + 'format1.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'test.txt').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_txt.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_pipe():
    with open(test_data_folder + 'format1.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'testpipe.txt').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_pipe.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_xlsx():
    with open(test_data_folder + 'format1.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'test.xlsx').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_xlsx.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_nan():
    with open(test_data_folder + 'format1.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'testnan.csv').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_nan.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_headeronly():
    with open(test_data_folder + 'format1.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'test_headeronly.csv').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_headeronly.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_empty():
    with open(test_data_folder + 'formatempty.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'test.csv').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_empty.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_utf():
    with open(test_data_folder + 'format1.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'testutf.csv').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_utf.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_full():
    with open(test_data_folder + 'formatfull.json', 'r') as f:
        output = Tree(rapidjson.load(f), test_data_folder + 'testfull.csv', date='2020-02-02').build().toJson(indent=2)
    with open(test_data_folder + 'output_test_full.json', 'r') as f:
        expected_output = f.read()
    assert output == expected_output 

def test_full_csv_excel():
    with open(test_data_folder + 'formatfull.json', 'r') as f:
        output1 = Tree(rapidjson.load(f), test_data_folder + 'testfull.csv', date='2020-02-02').build().toJson(indent=2)
    with open(test_data_folder + 'formatfull.json', 'r') as f:
        output2 = Tree(rapidjson.load(f), test_data_folder + 'testfull.xlsx', date='2020-02-02').build().toJson(indent=2)
    assert output1 == output2 
