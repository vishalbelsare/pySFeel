from sys import float_repr_style
from sly.yacc import ERROR_COUNT
import datetime
import pySFeel

parser = pySFeel.SFeelParser()

class TestClass:
    def test_and1(self):
        SFeel = 'true and true'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_or1(self):
        SFeel = 'true or true'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_and2(self):
        SFeel = 'true and false'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_or2(self):
        SFeel = 'true or false'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_and3(self):
        SFeel = 'true and 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None
    
    def test_or3(self):
        SFeel = 'true or 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_and4(self):
        SFeel = 'false and true'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_or4(self):
        SFeel = 'false or true'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_and5(self):
        SFeel = 'false and false'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_or5(self):
        SFeel = 'false or false'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_and6(self):
        SFeel = 'false and 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_and7(self):
        SFeel = '1 and true'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None
    
    def test_or7(self):
        SFeel = '1 or true'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_and8(self):
        SFeel = '1 and false'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_or8(self):
        SFeel = '1 or false'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None
    
    def test_and9(self):
        SFeel = '1 and 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None
    
    def test_or9(self):
        SFeel = '1 or 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None
    
    def test_comparisonTest1a(self):
        SFeel = '1 = 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest1b(self):
        SFeel = '[1, 2, 3] = [1, 2, 3]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest1c(self):
        SFeel = '[1, 2, 3] = [1, 2]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest1d(self):
        SFeel = '{a:1, b:2, c:3} = {a:1, b:2, c:3}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest1e(self):
        SFeel = '{a:1, b:2, c:3} = {a:1, b:2, c:4}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest1f(self):
        SFeel = '{a:1, b:2, c:3} = {a:1, b:2, d:3}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest1g(self):
        SFeel = '{a:1, b:2, c:3} = {a:1, b:2}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest1h(self):
        SFeel = '[1..3] = [1..3]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest1i(self):
        SFeel = '[1..3] = (1..3]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest1j(self):
        SFeel = '[1..3] = [1..4]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest1k(self):
        SFeel = '[1..3] = ["a".."c"]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest2a(self):
        SFeel = '1 != 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest2b(self):
        SFeel = '[1, 2, 3] != [1, 2, 3]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest2c(self):
        SFeel = '[1, 2, 3] != [1, 2]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest2d(self):
        SFeel = '{a:1, b:2, c:3} != {a:1, b:2, c:3}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest2e(self):
        SFeel = '{a:1, b:2, c:3} != {a:1, b:2, c:4}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest2f(self):
        SFeel = '{a:1, b:2, c:3} != {a:1, b:2, d:3}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest2g(self):
        SFeel = '{a:1, b:2, c:3} != {a:1, b:2}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest2h(self):
        SFeel = '[1..3] != [1..3]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
    
    def test_comparisonTest2i(self):
        SFeel = '[1..3] != (1..3]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest2j(self):
        SFeel = '[1..3] != [1..4]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest2k(self):
        SFeel = '[1..3] != ["a".."c"]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
    
    def test_comparisonTest3(self):
        SFeel = '1 < 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_comparisonTest4(self):
        SFeel = '1 <= 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_comparisonTest5(self):
        SFeel = '1 > 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False
        
    def test_comparisonTest6(self):
        SFeel = '1 >= 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_in1(self):
        SFeel = '3 in [2,3,4]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_in2(self):
        SFeel = '3 in [(0..2),[3..4)]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_in3(self):
        SFeel = '3 in [3..4]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_add(self):
        SFeel = '1 + 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2
    
    def test_subtract(self):
        SFeel = '1 - 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 0
      
    def test_multiply(self):
        SFeel = '2 * 2'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 4
            
    def test_divide(self):
        SFeel = '2 / 2'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 1
         
    def test_exponentiation(self):
        SFeel = '2 ** 3'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 8

    def test_negation(self):
        SFeel = '- 1'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == -1
    
    def test_interval1(self):
        SFeel = '(3 .. 5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == ('(', 3, 5, ')')

    def test_interval2(self):
        SFeel = ']3 .. 5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == (']', 3, 5, ')')

    def test_interval3(self):
        SFeel = '[3 .. 5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == ('[', 3, 5, ')')

    def test_interval4(self):
        SFeel = '(3 .. 5['
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == ('(', 3, 5, '[')

    def test_interval5(self):
        SFeel = ']3 .. 5]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == (']', 3, 5, ']')

    def test_time(self):
        SFeel = '13:15:17'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.time(hour=13, minute=15, second=17)

    def test_datetime(self):
        SFeel = '2012-12-31T13:15:17'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.datetime(year=2012, month=12, day=31, hour=13, minute=15, second=17)

    def test_date1(self):
        SFeel = '2012-12-31'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.date(year=2012, month=12, day=31)

    def test_date2(self):
        SFeel = 'date("2012-12-31")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.date(year=2012, month=12, day=31)

    def test_date3(self):
        SFeel = 'date(date and time("2012-12-31T11:00:00Z"))'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.date(year=2012, month=12, day=31)

    def test_date4(self):
        SFeel = 'date(2012, 12,31)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.date(year=2012, month=12, day=31)

    def test_dateandtime1(self):
        SFeel = 'date and time(date("2012-12-31"), time("11:00:00Z"))'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.datetime(year=2012, month=12, day=31, hour=11, minute=0, second=0)

    def test_dateandtime2(self):
        SFeel = 'date and time("2012-12-31T11:00:00Z")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.datetime(year=2012, month=12, day=31, hour=11, minute=0, second=0, tzinfo=datetime.timezone.utc)

    def test_time1(self):
        SFeel = 'time("23:59:00Z") + duration("PT2M")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.time(hour=0, minute=1, second=0)

    def test_time2(self):
        SFeel = 'time(date and time("2012-12-31T11:00:00Z"))'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.time(hour=11, minute=0, second=0)

    def test_number1(self):
        SFeel = 'number("1,000.0", ",", ".")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 1000

    def test_number2(self):
        SFeel = 'number(null, ",", ".")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_range1(self):
        SFeel = '5 in ( <= 5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_range2(self):
        SFeel = '5 in ( (5 ..10])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_duration1(self):
        SFeel = 'P1DT1H1M5.5S'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.timedelta(days=1, seconds=61*60 + 5, milliseconds=500)

    def test_duration2(self):
        SFeel = '-P1DT1H1M5.5S'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == -datetime.timedelta(days=1, seconds=61*60 + 5, milliseconds=500)

    def test_duration3(self):
        SFeel = 'PT1H1M5.5S'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == datetime.timedelta(days=0, seconds=61*60 + 5, milliseconds=500)

    def test_duration4(self):
        SFeel = '-PT1H1M5.5S'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == -datetime.timedelta(days=0, seconds=61*60 + 5, milliseconds=500)

    def test_null(self):
        SFeel = 'null'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_true(self):
        SFeel = 'true'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True
        
    def test_false(self):
        SFeel = 'false'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_between(self):
        SFeel = '5 between 3 and 7'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_not1(self):
        SFeel = 'not(true)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_not2(self):
        SFeel = 'not(false)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_not3(self):
        SFeel = 'not(1)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_not4(self):
        SFeel = 'not(null)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_substring1(self):
        SFeel = 'substring("foobar", 3)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 'obar'

    def test_substring2(self):
        SFeel = 'substring("foobar", 3, 3)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 'oba'

    def test_substring3(self):
        SFeel = 'substring("foobar", -2, 1)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 'a'

    def test_uppercase(self):
        SFeel = 'upper case("aBc4")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 'ABC4'

    def test_lowercase(self):
        SFeel = 'lower case("aBc4")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 'abc4'

    def test_substringbefore1(self):
        SFeel = 'substring before("foobar", "bar")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 'foo'

    def test_substringbefore2(self):
        SFeel = 'substring before("foobar", "xyz")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == ''

    def test_substringafter1(self):
        SFeel = 'substring after("foobar", "ob")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 'ar'

    def test_substringafter2(self):
        SFeel = 'substring after("", "a")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == ''

    def test_replace(self):
        SFeel = 'replace("abcd", "(ab)|(a)", "[1=$1][2=$2]")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == '[1=ab][2=]cd'

    def test_contains1(self):
        SFeel = 'contains("foobar", "of")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_contains2(self):
        SFeel = 'contains("foobar", "ob")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_startswith1(self):
        SFeel = 'starts with("foobar", "fo")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_startswith2(self):
        SFeel = 'starts with("foobar", "of")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_endswith1(self):
        SFeel = 'ends with("foobar", "r")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_endswith2(self):
        SFeel = 'ends with("foobar", "or")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_matches1(self):
        SFeel = 'matches("foobar", "^fo*b")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_matches2(self):
        SFeel = 'matches("foobar", "fob")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_split1(self):
        SFeel = 'split("John Doe", "\\s")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == ['John', 'Doe']

    def test_split2(self):
        SFeel = 'split("a;b;c;;", ";")'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == ['a', 'b', 'c', '', '']

    def test_listcontains1(self):
        SFeel = 'list contains([1, 2, 3], 2)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_listcontains2(self):
        SFeel = 'list contains([1, 2, 3], 4)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_count1(self):
        SFeel = 'count([1, 2, 3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 3

    def test_count2(self):
        SFeel = 'count([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 0

    def test_count3(self):
        SFeel = 'count([1, [2, 3]])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2

    def test_min1(self):
        SFeel = 'min([1, 2, 3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 1

    def test_min2(self):
        SFeel = 'min(1, 2, 3)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 1

    def test_min3(self):
        SFeel = 'min([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_max1(self):
        SFeel = 'max([1, 2, 3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 3

    def test_max2(self):
        SFeel = 'max(1, 2, 3)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 3

    def test_max3(self):
        SFeel = 'max([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_sum1(self):
        SFeel = 'sum([1, 2, 3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 6

    def test_sum2(self):
        SFeel = 'sum(1, 2, 3)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 6

    def test_sum3(self):
        SFeel = 'sum([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_mean1(self):
        SFeel = 'mean([1, 2, 3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2

    def test_mean2(self):
        SFeel = 'mean(1, 2, 3)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2

    def test_mean3(self):
        SFeel = 'mean([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_all1(self):
        SFeel = 'all([true, true])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_all2(self):
        SFeel = 'all([true, false])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_all3(self):
        SFeel = 'all(true, true)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_all4(self):
        SFeel = 'all(true, false)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_all5(self):
        SFeel = 'all(true, null, false)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_all6(self):
        SFeel = 'all(0)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_any1(self):
        SFeel = 'any([false, null, true])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_any2(self):
        SFeel = 'any([true])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_any3(self):
        SFeel = 'any(true)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_any4(self):
        SFeel = 'any([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_any5(self):
        SFeel = 'any(0)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_sublist(self):
        SFeel = 'sublist([4, 5, 6], 1, 2)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [4, 5]

    def test_append(self):
        SFeel = 'append([1], 2, 3)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1, 2, 3]

    def test_concatenate(self):
        SFeel = 'concatenate([1, 2], [3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1, 2, 3]

    def test_insertbefore(self):
        SFeel = 'insert before([1, 3], 1, 2)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [2, 1, 3]

    def test_remove(self):
        SFeel = 'remove([1, 2, 3], 2)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1, 3]

    def test_reverse(self):
        SFeel = 'reverse([1, 2, 3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [3, 2, 1]

    def test_indexof(self):
        SFeel = 'index of([1, 2, 3, 2], 2)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [2, 4]

    def test_union(self):
        SFeel = 'union([1, 2], [2, 3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1, 2, 3]

    def test_distinctvalues(self):
        SFeel = 'distinct values([1, 2, 3, 2, 1])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1, 2, 3]

    def test_flatten(self):
        SFeel = 'flatten([[1, 2], [[3]], 4])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1, 2, 3, 4]

    def test_product1(self):
        SFeel = 'product([2, 3, 4])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 24

    def test_product2(self):
        SFeel = 'product(2, 3, 4)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 24

    def test_median1(self):
        SFeel = 'median(8, 2, 5, 3, 4)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 4

    def test_median2(self):
        SFeel = 'median([6, 1, 2, 3])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2.5

    def test_median3(self):
        SFeel = 'median([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_stddev1(self):
        SFeel = 'stddev(2, 4, 7, 5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2.0816659994661326

    def test_stddev2(self):
        SFeel = 'stddev([47])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_stddev3(self):
        SFeel = 'stddev(47)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_stddev4(self):
        SFeel = 'stddev([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == None

    def test_mode1(self):
        SFeel = 'mode(6, 3, 9, 6, 6)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 6

    def test_mode2(self):
        SFeel = 'mode([6, 1, 9, 6, 1])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1, 6]

    def test_mode3(self):
        SFeel = 'mode([])'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == []

    def test_decimal1(self):
        SFeel = 'decimal(1/3, 2)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == .33

    def test_decimal2(self):
        SFeel = 'decimal(1.5, 0)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2

    def test_decimal3(self):
        SFeel = 'decimal(2.5, 0)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2

    def test_floor1(self):
        SFeel = 'floor(1.5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 1

    def test_floor2(self):
        SFeel = 'floor(-1.5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == -2

    def test_ceiling1(self):
        SFeel = 'ceiling(1.5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2

    def test_ceiling2(self):
        SFeel = 'ceiling(-1.5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == -1

    def test_abs1(self):
        SFeel = 'abs(10)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 10

    def test_abs2(self):
        SFeel = 'abs(-10)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 10

    def test_modulo1(self):
        SFeel = 'modulo(12, 5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 2

    def test_modulo2(self):
        SFeel = 'modulo(-12, 5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 3

    def test_modulo3(self):
        SFeel = 'modulo(12, -5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == -3

    def test_modulo4(self):
        SFeel = 'modulo(-12, -5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == -2

    def test_modulo5(self):
        SFeel = 'modulo(10.1, 4.5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert round(retval, 1) == 1.1

    def test_modulo6(self):
        SFeel = 'modulo(-10.1, 4.5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert round(retval, 1) == 3.4

    def test_modulo7(self):
        SFeel = 'modulo(10.1, -4.5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert round(retval, 1) == -3.4

    def test_modulo8(self):
        SFeel = 'modulo(-10.1, -4.5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert round(retval, 1) == -1.1

    def test_sqrt(self):
        SFeel = 'sqrt(16)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == 4

    def test_log(self):
        SFeel = 'log(10)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert round(retval, 11) == 2.30258509299

    def test_exp(self):
        SFeel = 'exp(5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert round(retval, 12) == 148.413159102577

    def test_odd1(self):
        SFeel = 'odd(5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_odd2(self):
        SFeel = 'odd(2)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_even1(self):
        SFeel = 'even(5)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == False

    def test_even2(self):
        SFeel = 'even(2)'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == True

    def test_list1(self):
        SFeel = '[1, 2, ["c"]]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1, 2, ['c']]

    def test_list2(self):
        SFeel = '[[1, 2], [3, 4]]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [[1, 2], [3, 4]]

    def test_listitem1(self):
        SFeel = '[1, 2, 3, 4][item > 2]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [3, 4]

    def test_listitem2(self):
        SFeel = '[{x:1, y:2}, {x:2, y:3}][item x=1]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [{'x':1, 'y':2}]

    def test_listitem3(self):
        SFeel = '[{x:1, y:2}, {x:null, y:3}][item x<2]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [{'x':1, 'y':2}]

    def test_listitem4(self):
        SFeel = '[{x:1, y:2}, {x:null, y:3}].y'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [2, 3]

    def test_listitem5(self):
        SFeel = '[1, 2, 3, 4][item > 1]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [2, 3, 4]

    def test_listitem6(self):
        SFeel = '[1, 2, 3, 4][item = 1]'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == [1]

    def test_context1(self):
        SFeel = '{a:1, b:2}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == {'a':1, 'b':2}

    def test_context2(self):
        SFeel = '{a:[1, 2], b:2, c:{d:3, e:"e"}}'
        (status, retval) = parser.sFeelParse(SFeel)
        assert 'errors' not in status
        assert retval == {'a':[1, 2], 'b':2, 'c':{'d':3, 'e':'e'}}
