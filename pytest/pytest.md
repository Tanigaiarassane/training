# Pytest is an automation framework that can be used for unit and functionL tests
- Can execution test cases optionally
- can setup pre-requisite and post execution scripts
- can add assertions
- Can generate reports

# Installing pytest
- pip install pytest

# Pre-requisite
- Automation tool like requests or selenium or appiam
- Write automation code and use pytest to sequence or control the execution of the automation scripts

# Naming convention in pytest
- Test case name should start with test
- Test Case method name should start with test

#skip test case - Execute test case on condition
- Executing the test cases from command line
- Writing multiple test cases in a file
- skip test cases
    import pytest
    @pytest.mark.skip ("Dont want to execute on current version")
        def test_first()
        assert 1 ==1 
- pytest -v
# conditionally skip execution
    import pytest
    a = 10
    @pytest.mark.skipif (a > 100, reason="Dont want to execute on current version")
    def test_first()
        assert 1 ==1 
# execute any specific test case
    pytest  -k test_one
    pytest -k customer // Executes all test case with customer as substring
    
# Grouping test cases
   - @pytest.mark<name>
    - @pytest.mark.sanity
    
    pytest -m sanity
    pytest -m "not sanity" # Execute all test cases other than with mark sanity
    
#Fixture
  - Execute some code before your test code
  - Execute some code after the test case
  - Execute only once
  
  @pytest.fixture
  def setup(): // def setup(context="module") - executing once per module
      global driver
      driver = webdriver.chrome()
      yield 
      driver.close()
  
  def test_one(setup):
  
  def test_two(setup):
  
  